from django import forms
from django.db import models

ready = False


def animals():
    if not ready:
        raise RuntimeError("Not ready to load animals")

    return [
        (1, "Aardvark"),
        (2, "Banana"),
    ]


class User(models.Model):
    spirit_animal = models.IntegerField(choices=animals)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["spirit_animal"]


ready = True
