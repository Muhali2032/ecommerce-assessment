from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Store, Product


class UserRegistrationForm(UserCreationForm):
    """
    Registration form for vendors and buyers.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'role')


class StoreForm(forms.ModelForm):
    """
    Form for vendors to create and update their stores.
    """

    class Meta:
        model = Store
        fields = ('name', 'description')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your store name'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your store',
                'rows': 4
            }),
        }
class ProductForm(forms.ModelForm):
    """
    Form for vendors to create and update products.
    """

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'quantity_available'
        )