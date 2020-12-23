from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField(max_length=254)
    Phone_Number = forms.CharField(max_length=12,validators = [RegexValidator(r'^\d{1,12}$')])
    Requirement = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "6", }),
        help_text='We Want to Develop a web/mobile Application')

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name        = cleaned_data.get('Name')
        email       = cleaned_data.get('Email')
        message     = cleaned_data.get('Phone_Number')
        requirement = cleaned_data.get('Requirement')
        if not name and not email and not message and not requirement:
            raise forms.ValidationError('Please Fill The Form!')
