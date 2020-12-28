from django.urls import path
from Aoc_Business_LandingApp import views


urlpatterns = [
    path('', views.index_view, name = 'Home'),
    # path('Contact-Form', views.ContactForm_View,name = 'Contact_Form'),
    path('web-appliction-dev', views.Web_App, name = 'web_application_dev'),
    path('ux-mobile', views.UX_Mobile_View, name = 'ux_mobile'),
    path('solutions',views.Solutions_View, name = 'solutions'),
    path('Projects-Info', views.projects_info, name = 'Projects_Info'),
    path('Privacy-policy', views.privacy_policy, name = 'Privacy_policy'),
    path('Terms-Conditions', views.Terms_Conditions, name = 'Terms_Conditions'),
    path('Disclaimer',views.Disclaimer, name = 'Disclaimer'),

]
