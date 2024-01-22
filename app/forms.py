from django import forms
from .models import mobile,amazon

class mobileform(forms.ModelForm):
    class Meta:
        model=mobile
        fields='__all__'


class amazonform(forms.ModelForm):
    class Meta:
        model=amazon
        fields='__all__'