from django import forms

from .models import CV

EMPTY_FIELD_ERROR = "You must fill in this field."

class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('title', 'name',)
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter your name'
            })
        }
        error_messages = {
            'name': {'required': EMPTY_FIELD_ERROR}
        }