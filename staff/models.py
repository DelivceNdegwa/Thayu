from django.db import models

# Create your models here.
class Amenities(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/amenities', null=True, blank=True)

class HouseType(models.Model):
    RENTAL=1
    MORTGAGE=2
    
    TYPE_CHOICES = (
        (RENTAL, "Rental"),
        (MORTGAGE, "Mortgage")
    )
    
    name= models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/house_types')
    choices = models.IntegerField(choices=TYPE_CHOICES)
    

class Location(models.Model):
    COUNTY_CHOICES =(
        (1, "Mombasa"),
    )
    county=models.IntegerField(choices=COUNTY_CHOICES)
    name=models.CharField(max_length=100)
    

class House(models.Model):
    AVAILABLE = 1
    UNAVAILABLE =2
    STATUS_CHOICES = (
        (AVAILABLE, "Available"),
        (UNAVAILABLE, "Unavailable")
    )
    
    name=models.CharField(max_length=100)
    price=models.DecimalField()
    location=models.ForeignKey(Location, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/houses')
    house_type = models.ForeignKey(HouseType, on_delete=models.PROTECT)
    number_of_rooms=models.IntegerField()
    status=models.IntegerField(choices=STATUS_CHOICES)
    
class HouseAmenity(models.Model):
    house=models.ForeignKey(House, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenities, null=True, blank=True, on_delete=models.SET_NULL)