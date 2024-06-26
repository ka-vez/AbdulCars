from django import forms
from .models import Car, Brand

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'