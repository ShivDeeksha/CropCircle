from django.urls import path

from . import views
from .views import cropBank

urlpatterns = [
    path('', views.index, name='index'),
    path('cropbanks/', cropBank, name='bank'),
    path('product/<int:bank_id>/', views.product_details, name='product-details'),
    path('banks/', views.banks, name='allbanks'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='aboutus'),
    path('register/',views.register,name='register'),
    path('check-username/', views.check_username_availability, name='check_username_availability'),
    path('customer/', views.customer, name='customer'),
    path('farmer/', views.farmer, name='farmer'),
    path('merchant/', views.merchant, name='merchant'),
    path('expert/', views.expert, name='expert'),
    path('driver/', views.driver, name='driver'),
    path('bankowner/', views.bankowner, name='bankowner'),
    path('services/', views.services,name='services'),
    path('aboutbanks/',views.aboutBank,name='aboutBank'),
    path('veggieshop/',views.veggieShop,name='veggieshop'),
    path('aboutBidZone/',views.bidZone,name='BidZone'),
    path('aboutCropGuide/',views.aboutCropGuide,name='aboutCropGuide'),
    path('aboutCropHealth/',views.aboutCropHealth,name='aboutCropHealth'),
    path('aboutTransport/',views.aboutTransport,name='aboutTransport'),
    path('contact/',views.contact,name='contactUs'),




]