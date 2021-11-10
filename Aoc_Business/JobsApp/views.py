from django.shortcuts import render,redirect
from django.contrib import messages
from JobsApp.models import Job_Upload
from JobsApp.forms import JobUpload_Form
import datetime
from django.db.models import Q

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
    context  = {
        'JobList':JobList,
    }
    return render(request, template, context)

