from django.db import models
from multiselectfield import MultiSelectField
from autoslug import AutoSlugField

# Create your models here.
class Room(models.Model):
    choices_for_rooms = (
        ('Wifi', 'Wifi'),
        ('Air Conditioning','Air Conditioning'),

    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    first_room_img = models.ImageField(
        upload_to="room_images",
    )
    second_room_img = models.ImageField(
        upload_to="room_images",
        null=True,
        blank=True
    )
    third_room_img = models.ImageField(
        upload_to="room_images",
        null=True,
        blank=True
    )
    # hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.IntegerField()
    room_options = MultiSelectField(choices=choices_for_rooms,blank=True, max_length=300)
    is_Booked = models.BooleanField(default=False,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(unique=True, populate_from='name',sep='-',null=True)

    def __str__(self):
        return f"{self.name} "


class Hotel(models.Model):
    feature_choices = (
        ('Dry cleaning','Dry cleaning'),
        ('Spa','Spa'),
        ('Gym','Gym'),
        ('Car park', 'Car park'),
        ('Wifi', 'Wifi'),
        ('Room service', 'Room service'),
        ('Special service', 'Special service')
    )

    name =  models.CharField(max_length=150)
    
    description = models.TextField()
    room =  models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=False)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    features = MultiSelectField(choices=feature_choices, blank=True, max_length=200)
    mobile_no = models.CharField( max_length=15)
    email = models.EmailField(max_length=50)
    slug = AutoSlugField(unique=True, populate_from='name',sep='-',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
