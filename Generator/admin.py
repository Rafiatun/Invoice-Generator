from re import search
from django.contrib import admin
from .models import *
from .forms import Invoice_form

class Customer_InvoiceAdmin(admin.ModelAdmin):
    list_display=['Name','Phone_Number','Invoice_Number','Invoice_Date','Total']
    form=Invoice_form
    list_filter=['Name']
    search_fields=['Name','Invoice_Number']

admin.site.register(Customer_Invoice,Customer_InvoiceAdmin)
# Register your models here.
