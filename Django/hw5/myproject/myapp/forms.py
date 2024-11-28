from django import forms
from .models import Product, ProductReview


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock"]


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = [
            "product_name",
            "user_email",
            "description",
            "rating",
            "review_type",
            "phone_number",
            "image",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"placeholder": "Ваш відгук..."}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Номер телефону"}),
        }
