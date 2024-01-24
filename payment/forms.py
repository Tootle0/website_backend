from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('card_number', 'name', 'month', 'year', 'code')
    # number = forms.CharField(max_length=16)
    # name = forms.CharField(max_length=255)
    # month = forms.CharField(max_length=2)
    # year = forms.CharField(max_length=2)
    # code = forms.CharField(max_length=3)
    # payment_type = forms.CharField(max_length=255)

