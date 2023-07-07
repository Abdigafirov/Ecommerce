from django.forms import ModelForm
from .models.product import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'narxi', 'category', 'rasmi']


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'narxi', 'category', 'rasmi']

