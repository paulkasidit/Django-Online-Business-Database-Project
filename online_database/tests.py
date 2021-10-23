from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from online_database.models import Customer

#Authentication/Customer User Model - 
class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)

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



        
