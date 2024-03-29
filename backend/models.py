from django.db import models
import random

from math import cos, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))

def closest(data, location):
    return min(data, key=lambda p: distance(location['lat'],location['lon'],p['lat'],p['lon']))

def generateunique() -> str:
    return random.randint(1000000, 9999999)


class Category(models.Model):
    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz
        
    @property
    def ImageURL(self):
        try:
            return self.image.url
        except:
            return ''


class ProductCategory(models.Model):
    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name_uz
    

class User(models.Model):
    user_id = models.CharField(max_length=20, null=True, blank=True, unique=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    lang = models.CharField(max_length=20, null=True, blank=True)
    order_type = models.CharField(max_length=25, null=True, blank=True)
    interests = models.ManyToManyField(to=Category)
    phone = models.CharField(max_length=20, null=True, blank=True)
    new_phone = models.CharField(max_length=20, null=True, blank=True)
    otp = models.CharField(max_length=20, null=True, blank=True)
    
    
    company =  models.CharField(max_length=2000, null=True, blank=True)
    product_category = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL)
    monthly = models.CharField(max_length=50, null=True)
    full = models.BooleanField(default=False)
    
    def __str__(self):
        try:
            return str(self.phone)
        except:
            return str(self.user_id)


class Region(models.Model):
    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name_uz

    
class Customs(models.Model):
    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)
    description_uz = models.TextField(max_length=5000, null=True, blank=True)
    description_en = models.TextField(max_length=5000, null=True, blank=True)
    description_ru = models.TextField(max_length=5000, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    longitude = models.CharField(max_length=500, null=True, blank=True)
    latitude = models.CharField(max_length=500, null=True, blank=True)
    contact = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name_uz


class Wearhouse(models.Model):
    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)
    name_kr = models.CharField(max_length=500, null=True, blank=True)
    place = models.CharField(max_length=10, null=True)
    description_uz = models.CharField(max_length=500, null=True, blank=True)
    description_en = models.CharField(max_length=500, null=True, blank=True)
    description_ru = models.CharField(max_length=500, null=True, blank=True)
    description_kr = models.CharField(max_length=500, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    address_en = models.TextField(max_length=5000, null=True, blank=True)
    owner = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name_uz


class LoaderService(models.Model):
    phone = models.CharField(max_length=500, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)
    persons = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.phone


class LoaderEquipment(models.Model):

    TYPE = (
        ("kara", 'Kara'),
        ("manipulyator", 'Manipulyator'),
        ("evacuator", 'Evacuator'),
        ("kran", 'kran')
    )

    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, choices=TYPE)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    description_uz = models.TextField(max_length=5000, null=True, blank=True)
    description_en = models.TextField(max_length=5000, null=True, blank=True)
    description_ru = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name_uz


class LogisticService(models.Model):
    phone = models.CharField(max_length=500, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    tonna = models.TextField(max_length=5000, null=True, blank=True)
    type = models.TextField(max_length=5000, null=True, blank=True)
    is_international = models.BooleanField(default=False)
    
    def __str__(self):
        return self.phone


class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ctagory = models.ForeignKey(Category, on_delete=models.CASCADE)
    used = models.BooleanField(default=False)
    

class TnVed(models.Model):
    kod = models.CharField(max_length=500, null=True, blank=True)
    description_uz = models.TextField(max_length=5000, null=True, blank=True)
    description_en = models.TextField(max_length=5000, null=True, blank=True)
    description_ru = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.kod


class PostService(models.Model):
    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)
    legalname_uz = models.CharField(max_length=500, null=True, blank=True)
    legalname_en = models.CharField(max_length=500, null=True, blank=True)
    legalname_ru = models.CharField(max_length=500, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    description_uz = models.TextField(max_length=5000, null=True, blank=True)
    description_en = models.TextField(max_length=5000, null=True, blank=True)
    description_ru = models.TextField(max_length=5000, null=True, blank=True)
    address_uz = models.TextField(max_length=5000, null=True, blank=True)
    address_en = models.TextField(max_length=5000, null=True, blank=True)
    address_ru = models.TextField(max_length=5000, null=True, blank=True)
    contacts = models.TextField(max_length=5000, null=True, blank=True)
    longitude = models.CharField(max_length=500, null=True, blank=True)
    latitude = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name_uz


class Sertification(models.Model):
    name_uz = models.CharField(max_length=500, null=True, blank=True)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    name_ru = models.CharField(max_length=500, null=True, blank=True)
    legalname_uz = models.CharField(max_length=500, null=True, blank=True)
    legalname_en = models.CharField(max_length=500, null=True, blank=True)
    legalname_ru = models.CharField(max_length=500, null=True, blank=True)
    address_uz = models.TextField(max_length=5000, null=True, blank=True)
    address_en = models.TextField(max_length=5000, null=True, blank=True)
    address_ru = models.TextField(max_length=5000, null=True, blank=True)
    contacts = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name_uz

