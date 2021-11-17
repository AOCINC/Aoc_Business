from django.shortcuts import render,redirect
from django.contrib import messages
from JobsApp.models import Job_Upload
from JobsApp.forms import JobUpload_Form
import datetime
from django.db.models import Q
from Aoc_Business_LandingApp.Email_Config import EMAIL_HOST_USER
from django.template.loader import get_template
from django.core.mail import EmailMessage


def Job_UploadsView(request):
    template = 'JobsApp/JobsUpload.html'
    if request.method == "POST":
        jobsForm = JobUpload_Form(request.POST)
        if jobsForm.is_valid():
            jobsForm.save()
            print('form is saving line========')
            messages.success(request, 'Jobs Uploaded Successfully')
            return redirect('Jobs_List')
    else:
        jobsForm = JobUpload_Form()
    context = {
        'jobsForm':jobsForm,
    }
    return render(request,template,context)

def JobsListView(request):
    template = 'JobsApp/All_JobsList.html'
    JobList  = Job_Upload.objects.all().order_by('-id')
    query    = request.GET.get('q',default=' ') #added default for preventing the None Error when Joblisting PAGE TRIGGERED
    if query:
        JobList = Job_Upload.objects.filter(
            Q(Designation__icontains = query.strip())
        )
    if not Job_Upload.objects.filter(Designation__icontains = query).exists():
        messages.warning(request,'Your Searhed Result Not Found..')
    if query == '':
        messages.warning(request,'Please Enter Which Job You Are Searching For...')
    today = datetime.datetime.today()
    print(today)
    context  = {
        'JobList':JobList,
        'today':today,
    }
    return render(request, template, context)



def Jobs_Details_View(request,id=None):
    """
    In This Method job detail template will be render, from there you can
    Apply action will open the Form and fetch the User DATA and 
    send Mail to Admin of PORTAL & user who applied for the position.
    
    """
    template = 'JobsApp/Jobs_Detials.html'
    JobDetail = Job_Upload.objects.get(id = id)
    if request.method == "POST":
        name        = request.POST.get('user_name')
        phone       = request.POST.get('user_phone')
        email       = request.POST.get('user_email')
        objectId    = request.POST.get('objectId')
        JobFile     = request.FILES['JobFile']
        selected_job= Job_Upload.objects.get(id = objectId)
        designation = selected_job.Designation
        print(JobFile,'=====')
        # mail sending to admin of aocinc
        subject = 'AOCINC JOB PORTAL MAIL,JOB APPLIED BY \t' + name
        context = {
            'name':name,
            'phone':phone,
            'email':email,
            'designation':designation,
        }
        from_email = EMAIL_HOST_USER
        to         = [EMAIL_HOST_USER]
        message = get_template('JobsApp/Aocinc_Jobs_Mail.html').render(context)
        msg = EmailMessage(subject, message, to=to,from_email = from_email)
        msg.attach(JobFile.name, JobFile.read(), JobFile.content_type)                    # attaching a single file from the form to send it to mail as attachement.
        msg.content_subtype  = 'html'
        msg.send()
        messages.success(request,'Job Applied Successfully..')
        # mail sending To Admin ends here.
        # mail sending To Applied User
        subject2 = "AOCINC JOB PORTAL MAIL,SUCCESSFULLY APPLIED"
        context = {
            'name':name,
            'designation':designation,
        }
        from_email = EMAIL_HOST_USER
        to         = [email]
        message = get_template('JobsApp/Aocinc_Jobs_Mail_To_User.html').render(context)
        msg = EmailMessage(subject2, message, to=to,from_email = from_email)
        msg.content_subtype  = 'html'
        msg.send()
        return redirect('Jobs_List')
        # mail sending To Applied User Ends here
    context  = {
        'JobDetail':JobDetail,
    }
    return render(request,template,context)