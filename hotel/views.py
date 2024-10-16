from django.shortcuts import render,get_object_or_404
from .models import Room, Hotel

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