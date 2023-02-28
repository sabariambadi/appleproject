from django import forms
from .models import Apple


class AppleForm(forms.ModelForm):
    class Meta:
        model=Apple
        fields=['name','desc','year','img']




