import datetime

from dal import autocomplete
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

from .models import (Client, Customer, CustomerRequests, EmailStatus,
                     EmailTemplate)

#Authentication/Create User(Client) 
class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta: 
        model = Client
        fields = ('email',
                  'business_name',
                  'first_name',
                  'last_name',
                  'city',
                  'state',
                  'phone_number',
                )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user

#Authenticaiton/Client Login(Client)
class LoginForm(AuthenticationForm):
    class Meta: 
        model = Client 
        fields = ['username', 'email', 'password1', 'password2']

class CreateCustomerForm(ModelForm): #This form is used to create new custoemrs by clients. 
    class Meta: 
        model = Customer 
        fields = '__all__'

class ManageCurrentCustomerForm(ModelForm): #Form is used to edit current customers. 
    class Meta: 
        model = Customer 
        fields = '__all__'


#Manage Customers & Email Templates/ Create A New Email Template
class CreateEmailTemplateForm(ModelForm): #Form to create new email tempalate 
    message = forms.CharField( widget=forms.Textarea )
    class Meta: 
        model = EmailTemplate 
        fields = '__all__'

#Send Emails/ Select Email Template 
class SelectEmailTemplateForm(forms.Form):
    templates = forms.ModelChoiceField(queryset=EmailTemplate.objects.all().order_by('subject'))

class SendEmailForm(ModelForm):
    class Meta: 
        model = Customer 
        fields = ('first_name',
                  'last_name',
                  'city',
                  'state',
                  'email_address',)

#Help/Change Business Details
#Form for business to update their details 

class UpdateBusinessDetailsForm(ModelForm):
    class Meta: 
        model = Client
        exclude = ('email','email_confirmed','uniqueID',)

#Help/Support
#Form for clients to be able to submit support requests
class CustomerRequestsForm(ModelForm):
    message = forms.CharField( widget=forms.Textarea )
    class Meta: 
        model = CustomerRequests
        fields = '__all__'
    
