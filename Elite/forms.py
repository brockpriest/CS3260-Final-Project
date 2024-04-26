from django import forms
from .models import VehicleInformation, Expense


class VehicleInformationForm(forms.ModelForm):
    class Meta:
        model = VehicleInformation
        fields = '__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

class lockUnlockForm(forms.ModelForm):
    class Meta:
        model = VehicleInformation
        fields = {
            'id': forms.IntegerField(),
            'LockVehicle': forms.BooleanField(required=False)
        }
