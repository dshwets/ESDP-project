from django import forms

from employees.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'passport_id',
            'phone_number',
            'relative_phone_number',
            'labor_contract',
            'passport',
            'photo',
            'achievement',
            'deposit_amount',
            'medical_record',
            'address',
            'note',
        ]