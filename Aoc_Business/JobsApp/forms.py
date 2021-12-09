from django import forms
from JobsApp.models import Job_Upload

class JobUpload_Form(forms.ModelForm):
    class Meta:
        model = Job_Upload
        fields = [
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
                    'Freelancing'
                    # 'Posted_On',    
                ]
        widgets = {
        'Job_Description': forms.Textarea(attrs={'rows':1, 'cols':15}),
        'Job_Description1': forms.Textarea(attrs={'rows':1, 'cols':15}),
        'Job_Description2': forms.Textarea(attrs={'rows':1, 'cols':15}),
        'Job_Description3': forms.Textarea(attrs={'rows':1, 'cols':15}),
        }
        