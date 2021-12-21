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
            'Freelancing',
            # NewFields Adding below..
            'Skill_Set',
            'Offer_Type',
            'Job_Skills_1',
            'Job_Skills_2',
            'Job_Skills_3',
            'Job_Skills_4',
            'About_Company_1',
            'About_Company_2',
            'About_Company_3',
            'Required_Skills_1',
            'Required_Skills_2',
            'Required_Skills_3',
            'Required_Skills_4',
            'Posted_On'

    ]
admin.site.register(Job_Upload, Jobs_UploadAdmin)