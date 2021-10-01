import django_tables2 as tables
from django.utils.safestring import mark_safe

from .models import Customer, EmailStatus


class CustomerTable(tables.Table):

    Email_Status = tables.Column()

    class Meta: 
        model = Customer
        template_name = "django_tables2/bootstrap4.html"
        fields = ("first_name",
                  "last_name",
                  "city",
                  "state",
                  "email_address",
                  "phone_number",
                  "Email_Status",
                  "date_created",
                  "date_updated",
                  )
    
    def render_data_from_emailstatus(self, value, record):
        return mark_safe("</br>".join(EmailStatus.objects.filter().values_list("status", flat=True)))
