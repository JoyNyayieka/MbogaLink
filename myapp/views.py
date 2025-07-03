import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests import request
from requests.auth import HTTPBasicAuth

from myapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from myapp.models import Contact, Subscriber, Member, VendorMember, Product


# Create your views here.
def index(request):
    # Handle login logic
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
            ).exists():
                return render(request, 'index.html')  # Successful login
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})  # Login failed

        # Handle subscription logic
        elif 'email' in request.POST:
            mysubscriber = Subscriber(
                email=request.POST['email']
            )
            mysubscriber.save()
            return redirect('/index')  # Redirect back to index after subscribing

    # Default: Render login page if no POST request
    return render(request, 'login.html')

def about(request):
    return render(request,'about-us.html')

def contact(request):
    if request.method == 'POST':
        mycontact=Contact(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact-us.html')

def typography(request):
    return render(request,'typography.html')

def starter(request):
    return render(request,'starter-page.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def testimonials(request):
    return render(request,'testimonials.html')

def register(request):
    if request.method == 'POST':
        members=Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def vendorlogin(request):
    return render(request, 'vendor-login.html')

def vendorregistration(request):
    if request.method == 'POST':
        vendormembers = VendorMember(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        vendormembers.save()
        return redirect('/vendorlogin')
    else:
        return render(request, 'vendor-registration.html')

def uploadimg(request):
    if request.method == 'POST':
        # Debugging: Print contents of request.FILES and request.POST
        print("FILES keys:", request.FILES.keys())
        print("POST keys:", request.POST.keys())

        try:
            product = Product(
                image=request.FILES['image'],  # Access directly
                produce_name=request.POST['produce_name'],
                price=request.POST['price'],
            )
            product.save()
            return redirect('shop')
        except KeyError as e:
            print(f"KeyError: {e}")
            return render(request, 'uploadimg.html', {'error': f'Missing {e}'})
    else:
        return render(request, 'uploadimg.html')

#def imagedelete(request, id):
    #image = Product.objects.get(id=id)
    #image.delete()
    #return redirect('/showimage')

def token(request):
    consumer_key = 'yAKxzGusBGuapzV57mpFhHwi2xAXkm0FgqJ3EY1aECTex0JW'
    consumer_secret = 'IbGLwoJpVVGBhsvAeGRk7Oh3XKGSq0Sap44M5sSahbJruijLhoxOt6EWzbs0As1h'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')


def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Groceries",
            "TransactionDesc": "MbogaLink payment"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Payment made successfully!")


