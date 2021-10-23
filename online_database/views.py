import json

import django_tables2
from dal import autocomplete
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic import FormView, ListView, TemplateView
from rest_framework import viewsets

from .forms import (CreateClientForm, CreateCustomerForm,
                    CreateEmailTemplateForm, CustomerRequestsForm,
                    ManageCurrentCustomerForm, SelectEmailTemplateForm,
                    SendEmailForm, UpdateBusinessDetailsForm)
from .models import (Client, Customer, CustomerRequests, EmailStatus,
                     EmailTemplate)
from .serializers import CustomerQuerySerializer
from .tables import CustomerTable


#Home Page
def home_page(request):

    """Home page database view"""
    num_customers =  Customer.objects.all().count()
    num_email_status = EmailStatus.objects.all().count()

    """Unsent Emails"""
    emails_to_be_sent = EmailStatus.objects.filter(status__exact='U').count()

    context = {
        'num_customers': num_customers,
        'num_email_status': num_email_status,
        'emails_to_be_sent': emails_to_be_sent,
    }

    return render(request, 'home_page.html', context=context)


#Customer Database
def customer_database_view(request):

    table = CustomerTable(Customer.objects.all())

    return render(request, "customer_database.html", {
        "table": table
    }) 


#Manage Customers
def manage_customers(request):
    return render(request, 'manage_customers.html')

#Manage Customers/Manage Current Customers
def manage_current_customers(request): #Search Bar to search for customers to manage 
    edit_customer_form = ManageCurrentCustomerForm

    if request.method == 'POST': 

        searched = request.POST['searched']
        customers = Customer.objects.filter(first_name__icontains=searched)

        return render(request, 'manage_customers/manage_current_customers.html',
        
                {'searched':searched ,'customers':customers, 'edit_customer_form': edit_customer_form})
    else: 
        return render(request, 'manage_customers/manage_current_customers.html')

    #Edit Customer forms are prompted after a query for a customer is made
    if edit_customer_form.is_valid(): 
        return render(request, 'manage_customers/manage_current_customers.html')

#Manage Customers/Create Customers 
def create_customers(request):
    
    #CreateClientForm for clients to input new user information.
    formset = CreateCustomerForm

    if request.method == 'POST':
        formset = CreateCustomerForm(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/online_database/customer_database/')
    else:
        formset = formset
    return render(request, 'manage_customers/create_customers.html', {'formset':formset})

#Manage Customers/Manage Email Tempalates
def manage_email_templates(request):

    #CreatEmailTemplateForm for clients to edit email templates.

    formset = CreateEmailTemplateForm

    if request.method == 'POST':
        formset = CreateEmailTemplateForm(request.POST)
        if formset.is_valid():
            formset.save()
            #return HttpResponseRedirect('/online_database/manage_customers/manage_email_templates/')
    else:
        formset = formset
    return render(request, 'manage_customers/manage_email_templates.html', {'formset':formset}) 


def send_emails(request):
    #Directory that maps out to the different functions of this feature
    return render(request, 'send_emails.html')

def send_daily_email(request):

    form = SelectEmailTemplateForm()

    #A select email drop down list to select templates to choose from, 
    #clients are able to choose from a list of templates 
    if request.method ==  "POST":
        form =  SelectEmailTemplateForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('send_emails/send_daily_email')
    errors = form.errors 
    return render(request, 'send_emails/send_daily_email.html', {'form':form, 'errors': errors})

    """
    - Render multiple forms on one page
    ç- Create empty form to populate
    - Selected template autopopulates field
    - Button to send email template to all customers. 
    """

def send_email(request):
    
    #A select email drop down list to select templates to choose from, 
    #clients are able to choose from a list of templates 

    form = SelectEmailTemplateForm()

    if request.method ==  "POST":
        form =  SelectEmailTemplateForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('send_emails/send_email.html')
    errors = form.errors 
    return render(request, 'send_emails/send_email.html', {'form':form, 'errors': errors})

#Help 
def help(request):
    return render(request, 'help.html')

#Help/Customer Support - form for customers to fill in their support requests
def customer_support(request):

    formset = CustomerRequestsForm

    if request.method == 'POST':
        formset = CustomerRequestsForm(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = formset
    
    return render(request, 'help/customer_support.html', {'formset':formset}) 

def update_business_details(request): 

    formset = UpdateBusinessDetailsForm

    if request.method == 'POST':
        formset = UpdateBusinessDetailsForm(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = formset

    return render(request, 'help/update_business_details.html', {'formset':formset})
