from django.shortcuts import render, get_object_or_404,redirect
from .models import CropBank, User
from django.db.models import Value
from .forms import UserRegistrationForm, LoginForm
from django.db.models.functions import ACos, Cos, Radians, Sin
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from geopy.distance import geodesic
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def index(request):
    users=User.objects.all()
    context={'users':users}
    return render(request,'index.html',context)


@require_POST
def check_username_availability(request):
    username = request.POST.get('username', '')
    data = {'available': not User.objects.filter(username=username).exists()}

    if not data['available']:
        data['error'] = 'This username is already taken.'

    return JsonResponse(data)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            # Perform additional logic to determine verification status
            if user.user_type in ['customer', 'cropexpert', 'cropbankowner']:
                user.is_verified = True
            else:
                user.is_verified = False

            user.save()

            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def farmer(request):
    return render(request,'farmer.html')

def customer(request):
    return render(request,'customer.html')

def merchant(request):
    return render(request,'merchant.html')

def driver(request):
    return render(request,'driver.html')

def expert(request):
    return render(request,'expert.html')

def bankowner(request):
    return render(request, 'bankowner.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username, password=password)
                if user.is_verified:
                    if user.user_type == 'customer':
                        return redirect('customer')
                    elif user.user_type == 'farmer':
                        return redirect('farmer')
                    elif user.user_type == 'merchant':
                        return redirect('merchant')
                    elif user.user_type == 'cropbankowner':
                        # Pass user details to the bankowner.html template
                        return render(request, 'bankowner.html', {'user': user})
                    elif user.user_type == 'driver':
                        return redirect('driver')
                    # Add similar conditions for other user types

                else:
                    messages.error(request, 'Account not verified yet.')

            except User.DoesNotExist:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
def banks(request):
    banks = CropBank.objects.all()

    context = {'banks': banks}
    return render(request,'allbanks.html', context)

def cropBank(request):
    # Retrieve all Crop Banks from the database
    banks = CropBank.objects.all()

    # Pass the retrieved data to the template
    context = {'banks': banks}
    return render(request, 'cropBank.html', context) 
   
def product_details(request, bank_id):

    bank = get_object_or_404(CropBank, pk=bank_id)

    # Calculate radius in kilometers
    radius_km = 60.0

    # Calculate related banks within the specified radius
    related_banks = CropBank.objects.annotate(
        distance=ACos(
            Sin(Radians(Value(bank.latitude))) * Sin(Radians('latitude')) +
            Cos(Radians(Value(bank.latitude))) * Cos(Radians('latitude')) *
            Cos(Radians('longitude') - Radians(Value(bank.longitude)))
        ) * 6371  # Earth's radius in kilometers
    ).filter(distance__lte=radius_km).exclude(id=bank.id)  # type: ignore

    context = {'bank': bank, 'related_banks': related_banks}
    print("Related Banks:", related_banks)
    print("Bank Latitude:", bank.latitude)
    print("Bank Longitude:", bank.longitude)



    return render(request, 'bank-details.html', context)

# All the pages for About in the Index.html !!Only UI Donot use elsewhere!!!
def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def aboutBank(request):
    return render(request,'aboutBank.html')

def veggieShop(request):
    return render(request,'ecom.html')

def bidZone(request):
    return render(request,'bidzone.html')

def aboutCropGuide(request):
    return render(request,'cropGuide.html')

def aboutCropHealth(request):
    return render(request,'crophealth.html')

def aboutTransport(request):
    return render(request,'transport.html')

def contact(request):
    return render(request,'contact.html')