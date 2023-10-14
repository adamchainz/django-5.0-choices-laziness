from django import forms

from example.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["spirit_animal"]
