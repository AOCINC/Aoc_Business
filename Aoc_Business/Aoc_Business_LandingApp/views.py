from django.shortcuts import render
from django.core.mail import send_mail
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






def Web_App(request):
    template = 'Aoc_Business_LandingApp/Web_Application.html'
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