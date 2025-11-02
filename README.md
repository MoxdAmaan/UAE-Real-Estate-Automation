#   UAE Property Rent Prediction App
## AI-Powered Real Estate Intelligence for Smarter Rent Decisions
![684bb84cadc0fe1c66045e96_Dubai-real-estate](https://github.com/user-attachments/assets/930e65ad-7fc0-41ec-9afc-f21d36f94b7d)

# 🧠 UAE Property Rent Prediction App

An **AI-powered Machine Learning web app** that predicts property rents across UAE cities using real-world data and custom-built intelligent features.  
This project moves beyond dashboards — it’s built to **solve real market problems** for property owners, investors, and tenants.  

---

## 🚀 About the Project

This project predicts **real estate rent prices** across major UAE cities (Dubai, Abu Dhabi, Sharjah, etc.) using advanced data science techniques and AI modeling.  

The goal:  
> To help people make **smarter, faster, data-driven rent decisions** with the power of AI.  

---

## 🧹 1️⃣ Data Cleaning — Making Raw Data Usable

Real-world data is messy — so we:
- Removed duplicates, nulls, and irrelevant records  
- Standardized city names and data types  
- Handled outliers in rent and area  
- Added useful derived columns like `bed_bath_ratio` and `age_days`

✅ *Ensured clean, consistent data for accurate model training.*

---

## 🔍 2️⃣ Exploratory Data Analysis (EDA)

We visualized and analyzed to understand the market:
- City-wise rent trends 📊  
- Correlations between `area_sqft`, `beds`, and `rent_aed`  
- Rent distribution histograms and heatmaps  
- Outlier detection using box plots  

✅ *Helped identify key rent-influencing features.*

---

## 💰 3️⃣ Normalizing Rent Prices

Rent varies hugely between cities — normalization ensured fairness:
- Applied **log transformation** on rent data  
- Scaled features with **Min-Max normalization**  
- Added **city multipliers** to adjust model predictions  

✅ *Prevented one city’s high rent from dominating the model.*

---

## ⚙️ 4️⃣ Feature Engineering — Making the Model Smarter

Engineered custom AI features to improve prediction power:

| Feature | Description | Purpose |
|----------|--------------|----------|
| 🏗️ `Luxury_Score` | Combines area, beds & baths | Represents property quality |
| 💸 `Affordability_Index` | 1 / (rent_per_sqft + 0.001) | Measures value-for-money |
| 🏙️ `city_encoded` / one-hot | Encodes city identity | Handles categorical city data |
| 🧱 `bed_bath_ratio` | Ratio of bedrooms to bathrooms | Property proportion |
| ⏳ `age_days` | Days since posting | Recent listings perform differently |

✅ *Helped model “understand” luxury, affordability, and property context.*

---

## 🧮 5️⃣ Machine Learning Models

Tried multiple ML models to find the best performer:

| Model | Description | Notes |
|--------|--------------|-------|
| 💡 Linear Regression | Simple baseline | Fast but less flexible |
| 🌲 Random Forest Regressor | Ensemble of trees | Best performer for accuracy & robustness |
| 🚀 Gradient Boosting | Boosted trees | High accuracy, slower training |
| 🧠 XGBoost (Planned) | Advanced boosting | For next upgrade version |

### 📈 Evaluation Metrics
- **R² Score** – Model accuracy  
- **MAE** – Mean Absolute Error  
- **RMSE** – Root Mean Squared Error  

✅ *Random Forest delivered the best balance of accuracy and interpretability.*

---

## 🤖 6️⃣ AI Predictive Modeling Pipeline

How it works:

1️⃣ User enters property details (city, area, beds, baths, rent/sqft)  
2️⃣ Features are transformed and matched with training columns  
3️⃣ Random Forest model predicts base rent  
4️⃣ City multiplier adjusts final rent based on city  
5️⃣ Output → **Estimated Rent (AED)** 💰  

✅ *An end-to-end intelligent AI rent predictor.*

---

## 🌐 7️⃣ Streamlit Frontend — Making AI Interactive

The app is powered by **Streamlit** for real-time interaction:
- City dropdown selection 🏙️  
- User inputs for area, beds, and baths  
- Instant AI predictions on click 🔮  
- Beautiful, lightweight interface  

✅ *Brings AI to life with one click.*

---

## 🧰 Tech Stack

**Languages & Tools:**
- Python 🐍  
- Pandas | NumPy | Scikit-Learn  
- Matplotlib | Seaborn  
- Streamlit  
- Joblib / Pickle  

---

## 💻 Run Locally

```bash
# 1️⃣ Clone the repo
git clone https://github.com/MoxdAmaan/uae-rent-prediction.git

# 2️⃣ Navigate into the project folder
cd uae-rent-prediction

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the app
streamlit run app.py
