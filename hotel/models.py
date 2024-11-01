from django.db import models
from multiselectfield import MultiSelectField
from autoslug import AutoSlugField
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from account.models import User



# Create your models here.



class Hotel(models.Model):
    feature_choices = (
        ('Dry cleaning','Dry cleaning'),
        
       
        ('Wifi', 'Wifi'),
        ('Room service', 'Room service'),
        ('Special service', 'Special service'),
        ('Waiting area', 'waiting area'),
        ('Secrete smoking area', 'Secrete smoking area'),
        ('Lift','Lift')
    )

    hotel_activities = (
        ('Spa','Spa'),
        ('Gym','Gym'),
        ('Car park', 'Car park'),
        ('Kids Play Area', 'Kids Play Area'),
    )

    hotel_payment_methods = (
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Cash', 'Cash'),
        ('Crypto', 'Crypto')
    )

    hotel_staff_languages = (
        ('English', 'English'),
        ('French', 'French'),
        ('German', 'German'),
        ('Portuguese', 'Portuguese')
    )

    name =  models.CharField(max_length=150)
    
    description = models.TextField()
    # room =  models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=False)
    address = models.CharField(max_length=250)
    image = models.ImageField(upload_to='room_images', null=True, blank=True)
    background_image = models.URLField(null=True, blank=True)
    city = models.CharField(max_length=100)
    services = MultiSelectField(choices=feature_choices, blank=True, max_length=200)
    activities = MultiSelectField(choices=hotel_activities, blank=True, max_length=200)
    payment_method = MultiSelectField(choices=hotel_payment_methods, blank=True, max_length=200)
    staff_languages = MultiSelectField(choices=hotel_staff_languages, blank=True, max_length=200)
    mobile_no = models.CharField( max_length=15)
    email = models.EmailField(max_length=50)
    slug = AutoSlugField(unique=True, populate_from='name',sep='-',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class RoomType(models.Model):
     choices_for_rooms = (
        ('Wifi', 'Wifi'),
        ('Air Conditioning','Air Conditioning'),

    )

     first_room_img = models.ImageField(
        upload_to="room_images" ),

     second_room_img = models.ImageField(
        upload_to="room_images",
        null=True,
        blank=True),
     third_room_img = models.ImageField(
        upload_to="room_images",
        null=True,
        blank=True
    )
     name = models.CharField(max_length=100)
     description = models.TextField()
     room_options = MultiSelectField(choices=choices_for_rooms,blank=True, max_length=300)
     slug = AutoSlugField(unique=True, populate_from='name',sep='-',null=True)

     def __str__(self):
         return self.name
    
class Room(models.Model):
    choices_for_rooms = (
        ('Wifi', 'Wifi'),
        ('Air Conditioning','Air Conditioning'),
        ('TV', 'TV')

    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE, null=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT, null=True)
    price = models.IntegerField()
    room_options = MultiSelectField(choices=choices_for_rooms,blank=True, max_length=300)
    is_Booked = models.BooleanField(default=False,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(unique=True, populate_from='name',sep='-',null=True)

    def __str__(self):
        return f"{self.name} "
    







class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    number_of_guests = models.IntegerField()
    booked =  models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.user.username} for {self.room}"