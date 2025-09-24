from django.forms import ModelForm
from main.models import Shop


class ProductForm(ModelForm):
    class Meta:
        model = Shop
        fields = ["name", "price", "description", "thumbnail", "is_featured", "category", "rating", "stock"]

