
from cmath import log
from email import message
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django import forms
from .forms import Invoice_Search, Invoice_form,InvoiceUpdateForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
##for generating pdf 
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image

# Create your views here.

def home(request):
    return render(request , 'index.html')

@login_required
def AddInvoice(request):
    Invoiceform = Invoice_form()
    if request.method == "POST":
        Invoiceform = Invoice_form(request.POST)
        if Invoiceform.is_valid():
            Invoiceform.save()
            messages.success(request, "Successfully Created")
            return redirect('addinvoice')

    else:
        Invoiceform = Invoice_form()

    context={
        'form': Invoiceform
    }
    return render(request , 'add_invoice.html' , context)

@login_required
def Items(request):
    items=Customer_Invoice.objects.all()
    search_form=Invoice_Search()
    total_invoice=Customer_Invoice.objects.count()
    show=Customer_Invoice.objects.order_by('-Invoice_Date')[:3]


    context={
        'item_list': items,
        'search_items': search_form,
        'total_invoice': total_invoice,
        'show': show
    

    }
    if request.method == "POST":
        search_form=Invoice_Search(request.POST)
        items=Customer_Invoice.objects.filter(Invoice_Number__icontains=search_form['Invoice_Number'].value(),
        Name__icontains=search_form['Name'].value())

        context={
        'item_list': items,
        'search_items': search_form

        }

        if search_form['generate_form'].value() == True:
            instance=items
            data_file = instance
            num_of_pdf=len(items)
            message= str(num_of_pdf) + 'Invoices successfully created.'
            messages.success(request, message)


            def import_data(data_file):
                invoice_data= data_file
                for row in invoice_data:
                    Invoice_Number= row.Invoice_Number
                    Invoice_Date=row.Invoice_Date
                    Name = row.Name
                    Address= row.Address
                    Phone_Number= row.Phone_Number

                    Product_1= row.Product_1
                    P1_Quantity= row.P1_Quantity
                    P1_UnitPrice= row.P1_UnitPrice
                    P1_TotalPrice=row.P1_TotalPrice

                    Product_2= row.Product_2
                    P2_Quantity= row.P2_Quantity
                    P2_UnitPrice= row.P2_UnitPrice
                    P2_TotalPrice=row.P2_TotalPrice

                    Product_3= row.Product_3
                    P3_Quantity= row.P3_Quantity
                    P3_UnitPrice= row.P3_UnitPrice
                    P3_TotalPrice=row.P3_TotalPrice

                    Total= row.Total
                    paid=row.paid
                    InvoiceType = row.InvoiceType
               

                    pdf_file_name= str(Invoice_Number) + ' ' + str(Name) + '.pdf'

                    generate_invoice(str(Invoice_Number),str(Invoice_Date),str(Name),str(Address),str(Phone_Number),
                        str(Product_1),str(P1_Quantity),str(P1_UnitPrice),str(Product_2),str(P2_Quantity),
                        str(P2_UnitPrice),str(Product_3),str(P3_Quantity),
                        str(P3_UnitPrice),str(P1_TotalPrice),str(P2_TotalPrice),str(P3_TotalPrice),str(Total),str(paid),str(InvoiceType),str(pdf_file_name)
                    )

                    
            def generate_invoice(
                Invoice_Number,Invoice_Date, Name,Address,Phone_Number,Product_1,P1_Quantity,
                P1_UnitPrice,Product_2,P2_Quantity,
                P2_UnitPrice,Product_3,P3_Quantity,
                 P3_UnitPrice,P1_TotalPrice,P2_TotalPrice,P3_TotalPrice,Total,paid, InvoiceType,  pdf_file_name):

                c=canvas.Canvas(pdf_file_name)

                logo='bnb.png'
                c.drawImage(logo , 200 , 680 , width= 200 , height= 200)
                c.setFont('Helvetica' ,12 , leading=None)
                c.drawCentredString(100,700 , str(InvoiceType) + ':')
                invoice_num=str('ABHE' + Invoice_Number)
                c.drawCentredString(200 ,700 , invoice_num)
           
                c.drawCentredString(100, 680 , "Date : ")
                c.drawCentredString(200 ,680 , Invoice_Date)

                c.drawRightString(400, 700 , "Customer Name : ")
                c.drawCentredString(500 ,700 , Name)

                c.drawRightString(400, 680 , "Address : ")
                c.drawRightString(500 , 680, Address)

                c.drawRightString(400, 660 , "Contact Number : ")
                c.drawRightString(500 ,660 , Phone_Number)

                c.setFont('Helvetica-Bold' ,14 , leading=None)
                c.drawCentredString(250, 530 , "Particulars: ")

            

                c.drawCentredString(100,500, "Items")
                c.drawCentredString(200,500, "Quantity")
                c.drawCentredString(300,500, "Unit Total")
                c.drawCentredString(400,500, "Item Total")

                c.setFont('Helvetica' ,12 , leading=None)
                c.drawCentredString(100,470, Product_1)
                c.drawCentredString(200,470, P1_Quantity)
                c.drawCentredString(300,470, P1_UnitPrice)
                c.drawCentredString(400,470, P1_TotalPrice)

                if Product_2 != '':
                    c.drawCentredString(100,440, Product_2)
                    c.drawCentredString(200,440, P2_Quantity)
                    c.drawCentredString(300,440, P2_UnitPrice)
                    c.drawCentredString(400,440, P2_TotalPrice)

                if Product_3 != '':
                    c.drawCentredString(100,410, Product_3)
                    c.drawCentredString(200,410, P3_Quantity)
                    c.drawCentredString(300,410, P3_UnitPrice)
                    c.drawCentredString(400,410, P3_TotalPrice)

                c.setFont('Helvetica-Bold' ,14 , leading=None)
                c.drawCentredString(300, 380 , "Total Amount : ")
                c.drawCentredString(400, 380 , Total )


                c.showPage()
                c.save()
  
            import_data(data_file)
    
    return render(request, 'item.html' , context)

                

    
@login_required
def Update_Invoice(request, pk):
    query= Customer_Invoice.objects.get(id=pk)
    form =InvoiceUpdateForm(instance=query)

    if request.method == "POST":
        form=InvoiceUpdateForm(request.POST , instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Updated")
            return redirect('items')

    context={
            'form': form
        }

    return render(request, 'add_invoice.html' , context)
    
    
def Delete_Invoice(request, pk):
    query= Customer_Invoice.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        messages.success(request, "Invoice Deleted")
    return render(request, 'delete.html')
    