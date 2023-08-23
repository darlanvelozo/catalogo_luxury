from django import forms
from .models import ItemCarrinho

class ItemCarrinhoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrinho
        fields = ['quantidade']