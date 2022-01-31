from django.db import models

# Create your models here.

class Customer_Invoice(models.Model):
    Invoice_Number = models.IntegerField(null=True,blank=True)
    Invoice_Date= models.DateField(auto_now_add=True,null=True,blank=True)
    Name=models.CharField('Customer Name' ,max_length=100,null=True,blank=True)
    Address=models.TextField(null=True, blank=True)
    Phone_Number=models.IntegerField('Phone Number',null=False,blank=False)

    Product_1=models.CharField(max_length=100,null=True, blank=True)
    P1_Quantity=models.PositiveIntegerField('Quantity',default=0,null=True,blank=True)
    P1_UnitPrice=models.PositiveIntegerField('Price',default=0,null=True,blank=True)
    P1_TotalPrice=models.FloatField(editable=False,default=0)

    Product_2=models.CharField(max_length=100,null=True, blank=True)
    P2_Quantity=models.PositiveIntegerField('Quantity',default=0,null=True,blank=True)
    P2_UnitPrice=models.PositiveIntegerField('Price',default=0,null=True,blank=True)
    P2_TotalPrice=models.FloatField(editable=False,default=0)

    Product_3=models.CharField(max_length=100,null=True, blank=True)
    P3_Quantity=models.PositiveIntegerField('Quantity',default=0,null=True,blank=True)
    P3_UnitPrice=models.PositiveIntegerField('Price',default=0,null=True,blank=True)
    P3_TotalPrice=models.FloatField(editable=False,default=0)

    Total=models.FloatField(editable=False,default=0)
    paid=models.BooleanField(default=False)
    InvoiceType_Choice=(
        ('Receipt','Receipt'),
        ('Business' ,'Business')
        )
    InvoiceType=models.CharField(max_length=100,default='',null=True, blank=True,choices=InvoiceType_Choice)
   
    def save(self,*args,**kwargs):
        
        self.P1_TotalPrice = self.P1_Quantity * self.P1_UnitPrice
        self.P2_TotalPrice = self.P2_Quantity * self.P2_UnitPrice
        self.P3_TotalPrice = self.P3_Quantity * self.P3_UnitPrice
        self.Total =self.P1_TotalPrice +self.P2_TotalPrice + self.P3_TotalPrice 
        super(Customer_Invoice,self).save(*args,**kwargs)

