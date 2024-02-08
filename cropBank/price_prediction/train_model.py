# train_models.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load your dataset (replace 'your_dataset.csv' with your actual dataset)
data = pd.read_csv('your_dataset.csv')

# Assume columns: 'price', 'production', and 'other_features'
X = data[['other_features']]
y_price = data['price']
y_production = data['production']

# Split the data into training and testing sets
X_train, X_test, y_price_train, y_price_test, y_production_train, y_production_test = train_test_split(
    X, y_price, y_production, test_size=0.2, random_state=42
)

# Train price prediction model
price_model = LinearRegression()
price_model.fit(X_train, y_price_train)
joblib.dump(price_model, 'price_model.pkl')

# Train production analysis model
production_model = LinearRegression()
production_model.fit(X_train, y_production_train)
joblib.dump(production_model, 'production_model.pkl')
