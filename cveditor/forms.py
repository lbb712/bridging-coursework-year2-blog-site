from django import forms

from .models import CV

EMPTY_FIELD_ERROR = "You must fill in this field."

class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('title', 'name','address_line_1','address_line_2','address_line_3','town','postcode','phone','email','personal_profile','university_name','modules_studied','sixth_form_or_college_name','alevel_results','school_name','gcse_results','experience','employment','skills_and_achievements','academic_referee','academic_referee_contact_details','employment_referee','employment_referee_contact_details',)
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter your name'
            })
        }
        error_messages = {
            'name': {'required': EMPTY_FIELD_ERROR}
        }