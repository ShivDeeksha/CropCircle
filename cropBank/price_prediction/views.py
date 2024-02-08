from django.shortcuts import render

# crops/views.py
from django.shortcuts import render
from django.http import JsonResponse
import joblib

def predict_price(request):
    # Assuming you receive input data from the user
    input_data = request.GET.get('input_data', '')
    input_data = float(input_data)

    # Load the trained price prediction model
    price_model = joblib.load('price_model.pkl')

    # Make a prediction
    prediction = price_model.predict([[input_data]])

    # Return the prediction as JSON
    return JsonResponse({'prediction': prediction[0]})

def analyze_production(request):
    # Assuming you receive input data from the user
    input_data = request.GET.get('input_data', '')
    input_data = float(input_data)

    # Load the trained production analysis model
    production_model = joblib.load('production_model.pkl')

    # Make a prediction
    prediction = production_model.predict([[input_data]])

    # Return the prediction as JSON
    return JsonResponse({'prediction': prediction[0]})
