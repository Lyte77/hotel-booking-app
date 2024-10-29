from django.shortcuts import render,get_object_or_404, redirect
from .models import Room, Hotel, Booking
from django.db import IntegrityError
from django.contrib import messages
from django.db.models import Q 
from .forms import BookingForm

# Create your views here.

def home_page(request):
    hotels =  Hotel.objects.all() 
    rooms =  Room.objects.all()    
    context = { 'hotels': hotels}

    return render(request, 'hotel/home.html', context)

def hotel_detail_page(request,slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    rooms = Room.objects.filter(hotel=hotels)
    
    context = {'hotels':hotels,
               'background_image':hotels.background_image,
               'rooms':rooms
                }
    return render(request, 
                  'hotel/hotel_detail_page.html',
                  context)


def is_room_available(room,check_in_date,check_out_date):
    check_in_date = check_in_date
    check_out_date = check_out_date
    bookings = Booking.objects.filter(room=room)
    for booking in bookings:
        if booking.check_in_date < check_out_date and booking.check_out_date > check_in_date:
            if check_out_date < check_in_date:
                return False
            
            return False
    return True 

    
def check_booking_date(request):
    booking = Booking.objects.all()
    if booking.check_out_date < booking.check_in_date:
         messages.add_message(request, messages.ERROR, "Invalid dates added.") 
         print("Invalid date") 
         return False
    return True     
            


    
def book_a_room(request, slug):
    print('Booking')
    room = get_object_or_404(Room, slug=slug)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            if is_room_available(room, form.cleaned_data['check_in_date'], form.cleaned_data['check_out_date']):
                
                try:
                    booking = form.save(commit=False)
                    booking.user = request.user
                    booking.room = room
                  
                    booking.save()
                    print("Booking Successful")
                    messages.add_message(request, messages.ERROR, "Room booked successfully.")  
                    return redirect('hotel:home')
                except IntegrityError:
                    print("Can't book room. Database integrity error.")
                except Exception as e:
                    print(f"Can't book room. Error: {e}")
            else:
                 messages.add_message(request, messages.ERROR, "Room not available.")
                 print("Unavailable")
    else:
        form = BookingForm()
    context = {'room': room, 'form': form}
    return render(request, 'hotel/booking_form.html', context)
       
        


def search_for_room(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Room.objects.filter(name__icontains=searched)
        return render(request, 'hotel/searched_room.html' ,{'searched':searched})
        
    else:
        return render(request, 'hotel/searched_room.html')
    

