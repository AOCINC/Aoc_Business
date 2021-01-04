from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
import re
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm
from .Email_Config import EMAIL_HOST_USER




def index_view(request):
    template_name = 'Aoc_Business_LandingApp/home.html'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            phone = form.cleaned_data['Phone_Number']
            requirement = form.cleaned_data['Requirement']
             # Mail Sending to aocinc admin 
            subject = 'New Requirement By\t' + name 
            context = {
                    'name':name,
                    'email':email, 
                    'phone':phone,
                    'requirement':requirement,                

                }
        
            from_email = EMAIL_HOST_USER
            to   = [EMAIL_HOST_USER]
            message = get_template('Aoc_Business_LandingApp/contact_email.html').render(context)
            msg = EmailMessage(subject, message, to=to,from_email = from_email)
            msg.content_subtype  = 'html'
            msg.send()
            return HttpResponseRedirect(request.path_info) # redirecting the current page after updating in the form 

    else:
        form = ContactForm()
    context = {
                'form': form
             }
    return render(request, template_name,context)

# def ContactForm_View(request):
#     '''This is Contact form for getting data from user for requirements '''
#     template = 'Aoc_Business_LandingApp/contactForm.html'
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             pass # here we not saving user data but need to configure Emial to send
#     else:
#         form = ContactForm()
#     context = {
#                 'form': form
#              }
#     return render(request,template, context)





def isValid(Number): 
    # validation for mobile number...
    # 1) Begins with 0 or 91 
    # 2) Then contains 7 or 8 or 9. 
    # 3) Then contains 9 digits 
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    return Pattern.match(Number) 

def Web_App(request):
    template = 'Aoc_Business_LandingApp/Web_Application.html'
    return render(request, template)

def UX_Mobile_View(request):
    template = 'Aoc_Business_LandingApp/ux_design.html'
    return render(request, template)

def Solutions_View(request):
    template  = 'Aoc_Business_LandingApp/Solutions.html'
    return render(request,template)

def About(request):
    template  = 'Aoc_Business_LandingApp/about.html'
    return render(request, template)

def schedule_meeting(request):
    template = 'Aoc_Business_LandingApp/schedule.html'
    if request.method == 'POST':
        Name  = request.POST.get('Name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Zoom  = request.POST.get('zoom')
        Note  = request.POST.get('notes')
        if Name == '' or Name.isdigit():    #validation for name should be alphabet not empty field nor digit
            messages.error(request, 'Please Provide Name Not digits or empty Field & not Special symbols')
            return HttpResponseRedirect(request.path_info) # redirecting the current page after updating in the form 
        if Email == '' or not '@' in Email: #validation for email if @ is not included then raise error message.
            messages.error(request, 'Please Provide valid Email or Not Given Email') 
            return HttpResponseRedirect(request.path_info) # redirecting the current page after updating in the form 
        if not isValid(Phone): # validation for phone number 
            messages.error(request, 'Please Enter valid Mobile Number') 
            return HttpResponseRedirect(request.path_info) # redirecting the current page after updating in the form 
        
        subject = 'New Enquiry  By\t' + Name 
        context = {
                'Name':Name,
                'Email':Email, 
                'Phone':Phone,
                'Zoom':Zoom,  
                'Note':Note,              
            }
        from_email = EMAIL_HOST_USER
        to   = [EMAIL_HOST_USER]
        message = get_template('Aoc_Business_LandingApp/Schedule_Enquiry.html').render(context)
        msg = EmailMessage(subject, message, to=to,from_email = from_email)
        msg.content_subtype  = 'html'
        msg.send()
        return HttpResponseRedirect(request.path_info) # redirecting the current page after updating in the form 
    return render(request, template)


def projects_info(request):
    template_name = 'Aoc_Business_LandingApp/projects_info.html'
    return render(request, template_name)

def privacy_policy(request):
    template_name = 'Aoc_Business_LandingApp/Privacy_policy.html'
    return render(request, template_name)


def Terms_Conditions(request):
    template_name = 'Aoc_Business_LandingApp/Terms_Conditions.html'
    return render(request, template_name)


def Disclaimer(request):
    template_name  = 'Aoc_Business_LandingApp/Disclaimer.html'
    return render(request, template_name)