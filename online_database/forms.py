import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from dal import autocomplete

from .models import Client, Customer, EmailStatus, EmailTemplate


class CreateClientForm(ModelForm): #This form is used for sign up for new clients. 
    class Meta: 
        model = Client 
        fields = ('business_name',
                  'first_name',
                  'last_name',
                  'city',
                  'state',
                  'email_address',
                  'phone_number',
                    )
                
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
