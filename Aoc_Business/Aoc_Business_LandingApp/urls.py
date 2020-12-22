from django.urls import path
from Aoc_Business_LandingApp import views


urlpatterns = [
    path('', views.index_view, name = 'Home'),
    path('web-appliction-dev', views.Web_App, name = 'web_application_dev'),
    path('Projects-Info', views.projects_info, name = 'Projects_Info'),
    path('Privacy-policy', views.privacy_policy, name = 'Privacy_policy'),
    path('Terms-Conditions', views.Terms_Conditions, name = 'Terms_Conditions'),
    path('Disclaimer',views.Disclaimer, name = 'Disclaimer'),

]
