import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

# Load data
df = pd.read_csv("dubai_properties_validated.csv")

# Drop columns not useful for prediction
drop_cols = ["address", "rent_category", "Price_Category", "posted_date"]
df = df.drop(columns=[col for col in drop_cols if col in df.columns])

# One-hot encode all categorical (object) columns
df = pd.get_dummies(df, drop_first=True)

# Add engineered columns if missing
if "Luxury_Score" not in df.columns:
    df["Luxury_Score"] = 5
if "affordability_index" not in df.columns:
    df["affordability_index"] = 5

# Split features and target
X = df.drop(columns=["rent_aed"])
y = df["rent_aed"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("✅ Model trained successfully!")
print("R² Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

# Save model and feature list
joblib.dump(model, "property_rent_model.pkl")
joblib.dump(X.columns.tolist(), "model_features.pkl")

print("💾 Model and features saved successfully!")
