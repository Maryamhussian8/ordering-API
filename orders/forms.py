from django import forms
from .models import Order, OrderItem
from meals.models import Meals

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []

class OrderItemForm(forms.ModelForm):
    meal = forms.ModelChoiceField(queryset=Meals.objects.all())
    class Meta:
        model = OrderItem
        fields = ['meal', 'quantity']
