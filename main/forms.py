import uuid
from django.forms import ModelForm
from main.models import Product

class ProductEntry(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "effects"]