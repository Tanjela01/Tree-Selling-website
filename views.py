from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def homepage(request):
    user = Customer.objects.all()
    itm = Products.objects.all()
    ItmLst = Card.objects.all()
    WayPay = MethodToPay.objects.all()
    OrderCustomer = Reciver.objects.all()
    OrderProduct = Order.objects.all()
    Py = Payment.objects.all()

    context = {
        'Users': user,
        'Item': itm,
        'ItemList': ItmLst,
        'PaymentWay': WayPay,
        'OrderedCustomer': OrderCustomer,
        'OrderProduct': OrderProduct,
        'Pay': Py,
    }

    return render(request, 'index.html', context)

def sellerpage(request):
    if request.method == 'POST':
        sellername = request.POST.get('sname')
        AccountNum = request.POST.get('saccnum')
        PhoneNum = request.POST.get('sphnum')
        Email = request.POST.get('seml')

        Mydata = Employee()
        Mydata.SeName=sellername
        Mydata.AccountNumber=AccountNum
        Mydata.phone=PhoneNum
        Mydata.email=Email

        Mydata.save()

    return render(request, 'seller.html')

