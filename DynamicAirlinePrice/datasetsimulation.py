import numpy as np
import pandas as pd

# Number of data points
num_samples = 1000

# Generate data
np.random.seed(42)

# Days left until departure (random between 1 and 30)
days_left = np.random.randint(1, 31, num_samples)

# Demand (random float between 0 and 1, representing percentage of seats sold)
demand = np.random.uniform(0, 1, num_samples)

# Seasonality factor (0 for off-season, 1 for holiday/peak season)
seasonality = np.random.choice([0, 1], num_samples)

# Competitor pricing (slightly varied around a base value, e.g., $100 to $300)
competitor_price = np.random.uniform(100, 300, num_samples)

# Base price for the ticket (random between $100 and $500)
base_price = np.random.uniform(100, 500, num_samples)

# Add a new factor: Class type (0 for economy, 1 for business)
class_type = np.random.choice([0, 1], num_samples)

# Formula for the ticket price
ticket_price = (base_price * (1 + demand) * (1 + 0.5 * seasonality)) - (0.2 * days_left) + (0.1 * competitor_price) + (50 * class_type)

# Create a DataFrame
df = pd.DataFrame({
    'days_left': days_left,
    'demand': demand,
    'seasonality': seasonality,
    'competitor_price': competitor_price,
    'base_price': base_price,
    'class_type': class_type,
    'ticket_price': ticket_price
})

# Save the dataset to a CSV file
df.to_csv('airline_pricing_dataset.csv', index=False)

print(df.head())
