from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.test import TestCase
from django.utils import timezone

from online_database.models import Customer


#Send Emails/ Send Email Function 
class EmailTestCase(TestCase): 
    def SendEmail(self): #Plain Send Email Function 
        emails = list(Customer.objects.all().values_list('email_address', flat=True)) 
        send_mass_mail(
            'Newest Promotion', #subject
            '50% off this Tuesday', #message 
            settings.EMAIL_HOST_USER, #from email
            ['emails'], #to email (must be a list)
            fail_silently = False, #will raise SMTP Exception if false
        )



        
