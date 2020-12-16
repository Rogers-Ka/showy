from django.forms import ModelForm
from django import forms
from .models import Upload


class FileUpload(ModelForm):
    class Meta:
        model = Upload
        fields = ('Username', 'Phone', 'Country', 'State', 'Parish', 'Media', 'item', 'price', 'description', 'image',)
        widgets = {
            'Username': forms.TextInput(attrs={"placeholder": "Username", 'class': "form-control form-control   w-75 form-control-danger", "id": "Search"}),
            'Phone': forms.TextInput(attrs={'class': "form-control form-control  w-75 form-control-danger", "placeholder": "Phone-Number", "id": "Search"}),
            'Country': forms.TextInput(attrs={"placeholder": "Country", 'class': "form-control form-control  w-75 form-control-danger", "id": "Search"}),
            'State': forms.TextInput(attrs={'class': "form-control form-control w-75 form-control-danger", 'placeholder': "State/ District", "id": "Search"}),
            'Parish': forms.TextInput(attrs={"placeholder": "Town", 'class': "form-control form-control  w-75 form-control-danger", "id": "Search"}),
            'Media': forms.TextInput(attrs={"placeholder": "exp. BuckBuck.facebook, 041417251.whatsapp", 'class': "form-control form-control  ml-3 w-75 form-control-danger", "id": "Search"}),
            'item': forms.TextInput(attrs={"placeholder": "item", 'class': "form-control form-control  w-75 form-control-danger", "id": "Search"}),
            'price': forms.TextInput(attrs={"placeholder": "amount", 'class': "form-control form-control  w-75 form-control-danger", "id": "Search"}),
            'description': forms.Textarea(attrs={"placeholder": "Exp; This item is new, second hand.Durable....Iphone 11, 12", 'class': "form-control  mt-3 mb-3", "style": "height:80px; width:100%;", "id": "Search"}),
            'image': forms.FileInput(attrs={"style": "width: 100%;", 'class': "text-black np-form-element np-shadow-inverse np-hover-inverse mt-3 mb-3"}),
        }

