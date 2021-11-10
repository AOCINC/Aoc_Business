from django.contrib import admin
from JobsApp.models import Job_Upload


class Jobs_UploadAdmin(admin.ModelAdmin):
    list_display = [
            'Designation',
            'Location',
            'Client_Name',
            'Functional_Area',
            'Industry',
            'Experience',
            'Job_Description',
            'Rate_Card',
            'Salary_LPA',
            'Notice_Period',
            'Posted_On'

    ]
admin.site.register(Job_Upload, Jobs_UploadAdmin)