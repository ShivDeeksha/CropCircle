# models.py
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator
from twilio.rest import Client
import time
from geopy.geocoders import Nominatim

class User(models.Model):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('farmer', 'Farmer'),
        ('merchant', 'Merchant'),
        ('driver', 'Driver'),
        ('cropbankowner', 'Crop Bank Owner'),
        ('cropexpert', 'Crop Expert'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50, verbose_name='Confirm Password')
    is_verified = models.BooleanField(default=False)
    adharcard = models.ImageField(upload_to='documents/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    document = models.ImageField(upload_to='documents/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    merchant_license = models.ImageField(upload_to='documents/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    driving_license = models.ImageField(upload_to='documents/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
   
    def save(self, *args, **kwargs):
        # Check if the user has been verified and the number is provided
        if self.is_verified and self.whatsapp_number:
            # Remove any non-numeric characters from the phone number
            cleaned_whatsapp_number = ''.join(filter(str.isdigit, str(self.whatsapp_number)))

            # Your Twilio account SID and authentication token
            account_sid = 'AC79298178fe2b6db7d741d6eb03476349'
            auth_token = 'b78f699787b2c9769167f0f1d5eca84c'


            # Create a Twilio client
            client = Client(account_sid, auth_token)

            # Compose the WhatsApp message
            message = client.messages.create(
                body="Your account has been verified!",
                from_='whatsapp:+14155238886',  # Twilio sandbox number
                to=f'whatsapp:+91{cleaned_whatsapp_number}'
            )

            # You can handle the message creation success or failure as needed
            print(f"WhatsApp message sent with SID: {message.sid}")

        super().save(*args, **kwargs)
        
class CropBank(models.Model):
    bank_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    capacity = models.IntegerField()
    review = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    bank_image = models.ImageField(upload_to='crop_bank_images/', null=True, blank=True)
    
    # New fields for latitude and longitude
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.bank_name

class BankImage(models.Model):
    crop_bank = models.ForeignKey(CropBank, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='crop_bank_images/')

class BankCommodity(models.Model):
    crop_bank = models.ForeignKey(CropBank, on_delete=models.CASCADE, related_name='commodities')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Signal to calculate latitude and longitude before saving CropBank
@receiver(pre_save, sender=CropBank)
def calculate_latitude_longitude(sender, instance, **kwargs):
    if instance.location:
        geolocator = Nominatim(user_agent="bank")  # Replace 'your_app_name' with a unique identifier
        location = geolocator.geocode(instance.location)

        if location:
            instance.latitude = location.latitude
            instance.longitude = location.longitude
