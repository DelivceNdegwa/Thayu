from django.db import models

# Create your models here.
class Amenities(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='amenities', null=True, blank=True)
    
    class Meta:
        verbose_name_plural="Amenities"
    
    def __str__(self):
        return self.name

class HouseType(models.Model):
    RENTAL=1
    MORTGAGE=2
    
    TYPE_CHOICES = (
        (RENTAL, "Rental"),
        (MORTGAGE, "Mortgage")
    )
    
    name= models.CharField(max_length=100)
    image=models.ImageField(upload_to='house_types')
    choices = models.IntegerField(choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name
    

class Location(models.Model):
    COUNTY_CHOICES =(
        (1, "Mombasa"),
        (2, "Kwale"),
        (3, "Kilifi"),
        (4, "Tana River"),
        (11, "Isiolo"),
        (12, "Meru"),
        (14, "Embu"),
        (16, "Machakos"),
        (19, "Nyeri"),
        (20, "Kirinyaga"),
        (22, "Kiambu"),
        (32, "Nakuru"),
        (36, "Bomet"),
        (37, "Kakamega"),
        (42, "Kisumu"),
        (47, "Nairobi")
    
    )
    county=models.IntegerField(choices=COUNTY_CHOICES)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id_front = models.ImageField(upload_to='id_front')
    national_id_back = models.ImageField(upload_to='id_back')
    phone = models.IntegerField()
    email = models.EmailField()
    profile_img = models.ImageField(upload_to='profile_photos')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class House(models.Model):
    AVAILABLE = 1
    UNAVAILABLE =2
    STATUS_CHOICES = (
        (AVAILABLE, "Available"),
        (UNAVAILABLE, "Unavailable")
    )
    
    name=models.CharField(max_length=100)
    price=models.DecimalField(decimal_places=2, max_digits=15)
    location=models.ForeignKey(Location, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='houses')
    house_type = models.ForeignKey(HouseType, on_delete=models.PROTECT)
    number_of_rooms=models.IntegerField()
    status=models.IntegerField(choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.name
    
class HouseAmenity(models.Model):
    house=models.ForeignKey(House, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenities, null=True, blank=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name_plural='House Amenities'
    
    def __str__(self):
        return self.house.name
    

class HouseRating(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    comment = models.TextField()
    
    def __str__(self):
        return self.house.name


class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
