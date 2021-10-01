from ajax_select import register, LookupChannel
from .models import Client, Customer, EmailStatus

@register('customer_lookup')
class CustomerLookUp(LookupChannel): 

    pass
