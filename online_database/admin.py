from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CreateEmailTemplateForm, CustomerRequestsForm
from .models import (Client, Customer, CustomerRequests, EmailStatus,
                     EmailTemplate)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('business_name','city','state','phone_number','email_address')
    fields = ['business_name',('city','state'),('phone_number','email_address')]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','city','state','phone_number','email_address')
    fields = ['first_name','last_name',('city','state'),('phone_number','email_address')]

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin): 
    form = CreateEmailTemplateForm

@admin.register(EmailStatus)
class EmailStatusAdmin(admin.ModelAdmin):
    list_filter = ('status', 'create_status')

    fieldsets = (
        (None, {
            'fields': ('email', 'sent_email_id')
        }),
        ('Edit', {
            'fields': ('status', 'create_status')
        }),
    )

@admin.register(CustomerRequests)
class CustomerRequestsAdmin(admin.ModelAdmin): 
    form = CustomerRequestsForm
