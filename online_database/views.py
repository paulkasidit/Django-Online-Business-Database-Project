import json

import django_tables2
from dal import autocomplete
from django.conf import settings
from django.core import mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic import ListView

from .forms import CreateClientForm, CreateCustomerForm, CreateEmailTemplateForm, ManageCurrentCustomerForm, SendEmailForm, SelectEmailTemplateForm
from .models import Client, Customer, EmailStatus, EmailTemplate
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
def manage_current_customers(request):

    if request.method == "POST":
        searched = request.POST['searched']

        customers = Customer.objects.filter(first_name__icontains=searched)

        return render(request, 'manage_customers/manage_current_customers.html',
         {'searched':searched ,'customers':customers})

    else: 
        return render(request, 'manage_customers/manage_current_customers.html')

def manage_current_customers_form(request):

    formset = ManageCurrentCustomerForm

    if request.method == 'POST':
        formset = ManageCurrentCustomerForm(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/online_database/customer_database/')
    else:
        formset = formset
    return render(request, 'manage_customers/manage_current_customers.html', {'formset':formset})


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

    if request.method ==  "POST":
        form =  SelectEmailTemplateForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('send_emails/send_daily_email')
    errors = form.errors 
    return render(request, 'send_emails/send_daily_email.html', {'form':form, 'errors': errors})


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

    
    """
        #Declare arguments for the send email form: 
    form = SendEmailForm 
    emails = Customer.objects.filter(id=showid).values('email_address')
    date = timezone.now()
    subject = EmailTemplate.objects.filter(id=showid).values('email_address')
    message = EmailTemplate.objects.filter(id=showid).values('email_address')

    def isSent(emails):
        subject = subject
        message = message
        recepient = emails 

        send_mail(subject, 
        message, EMAIL_HOST_USER, 
        [recepient], 
        fail_silently = False)
    
    
    if isSent: 
        return render(request, 'send_emails/send_email.html') 
    
    else: 
        isSent(emails)
        return render(request, 'send_emails/send_email.html',{'select_email_template':select_email_template,'form': SendEmailForm }) 
    """
    

#Help 
def help(request):
    return render(request, 'help.html')
