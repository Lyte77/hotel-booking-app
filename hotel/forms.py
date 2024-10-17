from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'room','check_in_date',
                  'check_out_date','number_of_guests']