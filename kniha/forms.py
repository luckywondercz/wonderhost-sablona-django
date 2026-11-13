from django import forms

from .models import Vzkaz


class VzkazForm(forms.ModelForm):
    class Meta:
        model = Vzkaz
        fields = ["jmeno", "text"]
        widgets = {"text": forms.Textarea(attrs={"rows": 4})}
