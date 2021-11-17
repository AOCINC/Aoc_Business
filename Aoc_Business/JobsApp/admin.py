from django.contrib import admin
from JobsApp.models import Job_Upload


class Jobs_UploadAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'Designation',
            'Education',
            'Location',
            'Client_Name',
            'Functional_Area',
            'Industry',
            'Experience',
            'Job_Description',
            'Job_Description1',
            'Job_Description2',
            'Job_Description3',
            'Rate_Card',
            'Salary_LPA',
            'Notice_Period',
            'Openings',
            'Role',
            'Posted_On'

    ]
admin.site.register(Job_Upload, Jobs_UploadAdmin)