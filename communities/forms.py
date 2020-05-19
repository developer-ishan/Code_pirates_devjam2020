from django import forms
from .models import community


class communityForm(forms.ModelForm):
    class Meta():
        model = community
        fields = ['name','desc','community_img','theme']
        widgets = {
            'theme': forms.HiddenInput,
        }