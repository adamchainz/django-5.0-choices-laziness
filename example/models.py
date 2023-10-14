from django.db import models

language = "en"


class Animals:
    def __iter__(self):
        if language == "en":
            yield from [
                (1, "Aardvark"),
                (2, "Banana"),
            ]
        elif language == "pt":
            yield from [
                (2, "Banana"),
                (1, "Porco-da-terra"),
            ]
        else:
            raise ValueError("Language not supported")


# animals = Animals()


class AnimalField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs["choices"] = Animals()
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        """
        Remove choices from deconstructed field, as this is the country list
        and not user editable.

        Not including the ``blank_label`` property, as this isn't database
        related.
        """
        name, path, args, kwargs = super().deconstruct()
        kwargs.pop("choices")
        return name, path, args, kwargs


class User(models.Model):
    spirit_animal = AnimalField()
