from asyncio import IncompleteReadError
from dataclasses import fields
from django import forms
from .models import *

class Invoice_form(forms.ModelForm):
    class Meta:
        model=Customer_Invoice
        fields=['Invoice_Number','Name','Address','Phone_Number','Product_1','P1_Quantity',
        'P1_UnitPrice','Product_2','P2_Quantity',
        'P2_UnitPrice','Product_3','P3_Quantity',
        'P3_UnitPrice','paid','InvoiceType']


    def clean_invoice_num(self):
        Inv_Number = self.cleaned_data.get('Invoice_Number')
        if not Inv_Number:
            raise forms.ValidationError('This field is required')
        return Inv_Number

    
    def clean_name(self):
        Na = self.cleaned_data.get('Name')
        if not Na:
            raise forms.ValidationError('This field is required')
        return Na
class Invoice_Search(forms.ModelForm):
    generate_form= forms.BooleanField(required=False )
    class Meta:
        model =Customer_Invoice
        fields=['Name','Invoice_Number','generate_form']
  
class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model=Customer_Invoice
        fields=['Invoice_Number','Name','Address','Phone_Number','Product_1','P1_Quantity',
        'P1_UnitPrice','Product_2','P2_Quantity',
        'P2_UnitPrice','Product_3','P3_Quantity',
        'P3_UnitPrice','paid','InvoiceType']