from django import forms


class BookForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=40,
        widget=forms.TextInput(
            attrs={"class": "w-35 text-black border border-black rounded-lg"}
        ),
    )
    author = forms.CharField(
        label="Autor",
        max_length=40,
        widget=forms.TextInput(
            attrs={"class": "w-35 text-black border border-black rounded-lg"}
        ),
    )
    release_date = forms.IntegerField(
        label="Año de Publicación",
        widget=forms.NumberInput(
            attrs={"class": "w-35 text-black border border-black rounded-lg"}
        ),
    )
