from django.db import models
from django.forms import ModelForm, TextInput, NumberInput


class Book(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    release_date = models.IntegerField()


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author", "release_date"]
        widgets = {
            "name": TextInput(
                attrs={"class": "w-35 text-black border border-black rounded-lg"}
            ),
            "author": TextInput(
                attrs={"class": "w-35 text-black border border-black rounded-lg"}
            ),
            "release_date": NumberInput(
                attrs={"class": "w-35 text-black border border-black rounded-lg"}
            ),
        }
