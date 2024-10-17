from django.shortcuts import render,get_object_or_404, redirect
from .models import Room, Hotel, Booking
from django.db import IntegrityError
from .forms import BookingForm

# Create your views here.

def home_page(request):
    hotels =  Hotel.objects.all()
    rooms =  Room.objects.all()
    context = {'hotels':hotels}
    return render(request, 'hotel/home.html', context)

def hotel_detail_page(request,slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    context = {'hotels':hotels}
    return render(request, 
                  'hotel/hotel_detail_page.html',
                  context)


def is_room_available(room,check_in_date,check_out_date):
    bookings =Booking.objects.filter(room=room)
    for booking in bookings:
        if booking.check_in_date < check_out_date and booking.check_out_date > check_in_date:
            print("Room is not available")
            return False

    return True
    
def book_a_room(request, slug):
    print('Booking')
    room = get_object_or_404(Room, slug=slug)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            if is_room_available(room, form.cleaned_data['check_in_date'], form.cleaned_data['check_out_date']):
                print(form.errors)
                try:
                    booking = form.save(commit=False)
                    booking.user = request.user
                    booking.room = room
                    booking.save()
                    print("Booking Successful")
                    return redirect('hotel:home')  # Make sure URL pattern accepts slug
                except IntegrityError:
                    print("Can't book room. Database integrity error.")
                except Exception as e:
                    print(f"Can't book room. Error: {e}")
            else:
                print("Room not available")
    else:
        form = BookingForm()
    context = {'room': room, 'form': form}
    return render(request, 'hotel/booking_form.html', context)