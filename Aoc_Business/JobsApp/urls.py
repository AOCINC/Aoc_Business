from django.urls import path
from JobsApp import views


urlpatterns = [
    path('Jobs-List',views.JobsListView, name ='Jobs_List'),
    path('Job-Upload',views.Job_UploadsView, name = 'Jobs_Upload'),
]
