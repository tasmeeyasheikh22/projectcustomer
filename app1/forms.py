from django import forms

from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

        widgets = {
            "delivery_date":forms.DateInput(attrs={"placeholder":"eg.12june2023","type":"date"})
        }