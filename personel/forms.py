from django import forms
from .models import Personnel

class PersonnelForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="تاریخ تولد")
    hire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="تاریخ استخدام")
    region_entry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="تاریخ ورود به منطقه")

    class Meta:
        model = Personnel
        fields = [
            'first_name', 'last_name', 'rank', 'personnel_number', 'branch', 
            'specialty', 'birth_date', 'birth_place', 'national_id', 'hire_date', 
            'region_entry_date', 'is_instructor', 'instructors_grade', 'instructors_rank'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.initial.get('is_instructor', False):
            self.fields['instructors_grade'].widget.attrs['disabled'] = 'disabled'
            self.fields['instructors_rank'].widget.attrs['disabled'] = 'disabled'

    def clean(self):
        cleaned_data = super().clean()
        is_instructor = cleaned_data.get("is_instructor")
        if not is_instructor:
            # Prevent saving any data in these fields if `is_instructor` is False
            cleaned_data['instructors_grade'] = None
            cleaned_data['instructors_rank'] = None
        return cleaned_data
