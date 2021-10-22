from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from . import views

app_name = 'online_database'

urlpatterns = [
    #homepage
    path('', views.home_page, name='home_page'),
    #database view
    path('customer_database/', views.customer_database_view, name='customer_database'),
    #manage customers
    path('manage_customers/', views.manage_customers, name='manage_customers'),
    path('manage_customers/create_customers', views.create_customers, name='create_customers'),
    path('manage_customers/manage_current_customers', views.manage_current_customers, name="manage_current_customers"),
    path('manage_customers/manage_email_templates', views.manage_email_templates, name='manage_email_templates'),
    #send emails 
    path('send_emails/', views.send_emails, name='send_emails'),
    path('send_emails/send_email', views.send_email, name='send_email'),
    path('send_emails/send_daily_email', views.send_daily_email, name='send_daily_email'),
    #help 
    path('help/', views.help, name='help'),
    path('help/customer_support', views.customer_support, name='customer_support'),
]
 