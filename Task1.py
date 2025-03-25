#  Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#  Load the dataset
df = pd.read_csv("Enhanced_Dataset_Task3.csv")  # Ensure correct file path

#  Selecting Features and Target Variable
X = df[['Restaurant_Name_Length', 'Address_Length', 'Has_Table_Booking', 'Has_Online_Delivery', 'Price range']]
y = df['Aggregate rating']

#  Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Standardizing the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#  Model Training & Evaluation
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
    # Train the model
    model.fit(X_train_scaled, y_train)
    
    # Predict on test data
    y_pred = model.predict(X_test_scaled)
    
    # Evaluate performance
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Store results
    results[name] = {"MAE": mae, "MSE": mse, "R2 Score": r2}

#  Display results
for model, metrics in results.items():
    print(f"\n {model} Performance:")
    print(f"✅ Mean Absolute Error: {metrics['MAE']:.4f}")              
    print(f"✅ Mean Squared Error: {metrics['MSE']:.4f}")
    print(f"✅ R2 Score: {metrics['R2 Score']:.4f}")

print("\n✅ Predictive Modeling Completed!")
