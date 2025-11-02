import streamlit as st
import pandas as pd
import joblib

# Load trained model and features
model = joblib.load("property_rent_model.pkl")
features = joblib.load("model_features.pkl")

st.title("UAE Property Rent Prediction App")
st.write("Enter property details below to estimate the rent:")

# City selection
city = st.selectbox("Select City", [
    'Abu Dhabi', 'Ajman', 'Al Ain', 'Dubai', 'Fujairah',
    'Ras Al Khaimah', 'Sharjah', 'Umm Al Quwain'
])

# User inputs
area_sqft = st.number_input("Area (sqft)", min_value=100, max_value=10000, value=2000)
beds = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
baths = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
rent_per_sqft = st.number_input("Rent per sqft (AED)", min_value=1, max_value=200, value=50)

# Encode city numerically for now (your previous logic)
city_mapping = {
    'Abu Dhabi': 0, 'Ajman': 1, 'Al Ain': 2,
    'Dubai': 3, 'Fujairah': 4, 'Ras Al Khaimah': 5,
    'Sharjah': 6, 'Umm Al Quwain': 7
}
city_encoded = city_mapping[city]

# Calculate additional engineered features
luxury_score = (area_sqft * 0.5 + beds * 1000 + baths * 500) / 10000
affordability_index = 1 / (rent_per_sqft + 0.001)

# Prepare input data for prediction
input_data = pd.DataFrame([{
    'area_sqft': area_sqft,
    'beds': beds,
    'baths': baths,
    'rent_per_sqft': rent_per_sqft,
    'city_encoded': city_encoded,
    'luxury_score': luxury_score,
    'affordability_index': affordability_index
}])

# Reindex to match training features (fill missing ones with 0)
input_data = input_data.reindex(columns=features, fill_value=0)

# City rent multiplier (for more realistic predictions)
city_multiplier = {
    'Dubai': 1.25,
    'Abu Dhabi': 1.15,
    'Sharjah': 0.9,
    'Ajman': 0.8,
    'Al Ain': 0.85,
    'Fujairah': 0.75,
    'Ras Al Khaimah': 0.7,
    'Umm Al Quwain': 0.65
}

# Predict rent
if st.button("Click to Predict Rent"):
    base_prediction = model.predict(input_data)[0]
    final_prediction = base_prediction * city_multiplier[city]
    st.success(f"🏠 Estimated Property Rent in {city}: AED {final_prediction:,.2f}")
