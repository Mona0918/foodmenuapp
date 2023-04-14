from django import forms
from .models import ItemModel

class AddItemForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields='__all__'
        
