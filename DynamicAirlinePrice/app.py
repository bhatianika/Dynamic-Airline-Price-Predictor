from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('airline_pricing_dataset.csv')
X = data[['days_left', 'demand', 'seasonality', 'competitor_price', 'base_price']]
y = data['ticket_price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
modelupd = RandomForestRegressor(n_estimators=250, random_state=42, max_depth=10,min_samples_leaf=1,min_samples_split=2)
modelupd.fit(X_train, y_train)

# Function to simulate demand based on days left and user-provided seasonality
def simulate_demand(days_left, seasonality):
    if seasonality == 1:  # Peak season
        demand = np.random.uniform(0.6, 1.0)  # Higher demand
    else:  # Off-peak season
        demand = np.random.uniform(0.1, 0.5)  # Lower demand
    
    # Reduce demand as days left increase
    demand *= (1 - days_left / 30)  # Normalize based on days left
    return round(demand, 2)

# Function to simulate competitor pricing based on base price and demand
def simulate_competitor_price(base_price, demand):
    # Competitor price varies around base price, influenced by demand
    competitor_price = base_price * (1 + (0.1 * (1 - demand)))  # Higher demand means higher competitor price
    return round(competitor_price, 2)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route


@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from user
    try:
        days_left = int(request.form['days_left'])  # Ensure days_left is being retrieved
        # Proceed with your model prediction logic here
    except KeyError:
        return "days_left value is missing", 400
    base_price = float(request.form['base_price'])
    seasonality = int(request.form['seasonality'])  # Get seasonality from user input

    # Simulate demand and competitor price
    demand = simulate_demand(days_left, seasonality)
    competitor_price = simulate_competitor_price(base_price, demand)

    # Make a prediction using the model
    prediction = modelupd.predict([[days_left, demand, seasonality, competitor_price, base_price]])
    predicted_price = round(prediction[0], 2)

    # Return the result to the user
    return render_template('index.html', predicted_price=f"{predicted_price}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
