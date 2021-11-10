from django import forms
from JobsApp.models import Job_Upload

class JobUpload_Form(forms.ModelForm):
    class Meta:
        model = Job_Upload
        fields = [
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
                    # 'Posted_On',    
                ]
        widgets = {
        'Job_Description': forms.Textarea(attrs={'rows':1, 'cols':15}),
        }
        