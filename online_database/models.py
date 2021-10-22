import uuid

from django.conf import settings
from django.core import mail
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.utils.text import slugify
from django.db import models
from django.urls import reverse
from django.utils import timezone
from localflavor.us.us_states import STATE_CHOICES


class Client(models.Model):
    business_name = models.CharField("Business Name",max_length = 30)
    first_name = models.CharField("First Name",max_length = 30)
    last_name =  models.CharField("Last Name",max_length = 30)
    city = models.CharField("City Name",max_length = 30)
    state = models.CharField("State", max_length=2, choices=STATE_CHOICES, null=True, blank=True)  
    phone_number = models.CharField("Phone Number",max_length=10)
    email_address = models.EmailField("Email Address",max_length=50)
    email_confirmed = models.BooleanField(default=False)
    uniqueID = models.UUIDField("Your Client ID", max_length=255, default = uuid.uuid1,primary_key=True)

    def __str__(self):
        return f'{self.business_name} - {self.city}, {self.state}'
        

    def get_absolute_url(self):
        return reverse('client_details', args=[str(self.id)])

class Customer(models.Model): 

    first_name  = models.CharField("First Name", max_length = 50)
    last_name = models.CharField("Last Name", max_length = 50)
    city = models.CharField("City",max_length = 30)
    state = models.CharField("State", max_length=2, choices=STATE_CHOICES, null=True, blank=True)  
    email_address = models.EmailField(max_length=50, help_text='Enter a valid email address')
    phone_number = models.CharField(max_length=10, help_text='Enter a valid ten digit phone number')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.city}, {self.state} - {self.email_address}'

class EmailTemplate(models.Model): 
    
    date_created = models.DateField(default = timezone.now)
    subject = models.CharField("Email Subject", max_length = 50)
    message =  models.CharField("Email Message", max_length = 1000)

    def __str__(self):
        return f'Created ({self.date_created}) // {self.subject}'

class EmailStatus(models.Model):

    sent_email_id = models.UUIDField(unique=True, default=uuid.uuid4)
    email = models.ForeignKey(Customer, on_delete=models.RESTRICT, null=True)
    create_status = models.DateField(default = timezone.now)

    EMAIL_STATUS = (
        ('S','Sent'),
        ('U','Unsent'),
    )

    status = models.CharField(
        max_length = 1,
        choices = EMAIL_STATUS,
        blank = False,
        default = 'U',
        help_text='Has the email already been sent?',
    )
    """
    def SendEmail(self):
        

        
    """
    class Meta: 
        ordering = ['create_status']
    
    def __str__(self):
        return f'{self.status} - {self.email}'

class CustomerRequests(models.Model): 

    business_name = models.CharField("Business Name", max_length = 30)
    date = models.DateField("Date", default = timezone.now)
    message = models.CharField("Request Message", max_length = 150) 
    email = models.EmailField("Email Address", max_length=50, help_text='Enter a valid email address')

    def __str__(self): 
        return f'{self.business_name} - {self.date} - {self.message}'
