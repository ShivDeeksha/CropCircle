# crops/urls.py
from django.urls import path
from .views import predict_price, analyze_production

urlpatterns = [
    path('predict_price/', predict_price, name='predict_price'),
    path('analyze_production/', analyze_production, name='analyze_production'),
]
