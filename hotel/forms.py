from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'room','check_in_date',
                  'check_out_date','number_of_guests']
        
    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        if check_out_date <= check_in_date:
             raise forms.ValidationError("Check-out date must be after check-in date.")
        return cleaned_data