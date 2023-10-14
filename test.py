from example import models
from example.forms import UserForm

choices = UserForm()["spirit_animal"].field.choices
assert choices == [
    ("", "---------"),
    (1, "Aardvark"),
    (2, "Banana"),
]

models.language = "pt"
choices = UserForm()["spirit_animal"].field.choices
print(choices)
assert choices == [
    ("", "---------"),
    (2, "Banana"),
    (1, "Porco-da-terra"),
]
