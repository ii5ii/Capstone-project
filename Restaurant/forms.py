from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'number_of_guests', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
