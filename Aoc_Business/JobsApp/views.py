from django.shortcuts import render

def JobsListView(request):
    template = 'JobsApp/All_JobsList.html'
    return render(request, template)