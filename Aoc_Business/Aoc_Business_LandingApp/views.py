from django.shortcuts import render


def index_view(request):
    template_name = 'Aoc_Business_LandingApp/home.html'
    return render(request, template_name)



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