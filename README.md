#   UAE Property Rent Prediction App
## AI-Powered Real Estate Intelligence for Smarter Rent Decisions
![684bb84cadc0fe1c66045e96_Dubai-real-estate](https://github.com/user-attachments/assets/930e65ad-7fc0-41ec-9afc-f21d36f94b7d)
🚀 Overview

The UAE Property Rent Prediction App is an AI-driven web application that predicts rental prices across major UAE cities using real-world housing data.

It bridges the gap between data analytics and data science — converting insights into actionable intelligence that helps:

🏠 Owners set competitive rent prices

💼 Investors evaluate property value

👨‍👩‍👧‍👦 Tenants find affordable housing

🧠 Features

✅ Real UAE property data
✅ AI model powered by Random Forest Regressor
✅ Custom-engineered features for real-world accuracy:

Luxury Score — measures property value aesthetics

Affordability Index — reflects price fairness per sqft
✅ Interactive Streamlit UI — easy and fast predictions
✅ Instant rent estimation by city, size, and features

⚙️ Tech Stack
Category	Tools Used
Language	Python
Libraries	Pandas, Scikit-learn, Joblib, Pickle
Frontend	Streamlit
Model	Random Forest Regressor
Deployment	Streamlit Cloud / Localhost
🧩 Project Structure
uae-rent-prediction/
│
├── app.py                  # Streamlit web app
├── train_model.py          # Model training script
├── model.pkl               # Trained ML model
├── requirements.txt        # Dependencies
├── data/                   # Dataset (optional)
└── README.md               # Project documentation

🧮 How It Works

1️⃣ User selects city, area (sqft), number of beds, baths, and rent per sqft
2️⃣ Data is preprocessed and fed to the trained model
3️⃣ AI model predicts base rent
4️⃣ Prediction is fine-tuned using city-based multiplier
5️⃣ Final rent estimate is displayed with city insights

💻 Run Locally
# 1️⃣ Clone the repo
git clone https://github.com/MoxdAmaan/uae-rent-prediction.git

# 2️⃣ Navigate into the project folder
cd uae-rent-prediction

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the app
streamlit run app.py


Then open your browser at 👉 http://localhost:8501/

🧩 Example Output

💬 Input:
City: Dubai | Area: 2000 sqft | Beds: 3 | Baths: 2

💰 Predicted Rent: AED 120,000/year (approx.)

🧱 Future Improvements

🌐 Integrate live property APIs for dynamic predictions

📊 Add visual analytics dashboard

🤖 Experiment with XGBoost & Deep Learning models

🏗️ Build containerized deployment using Docker

🙌 Acknowledgements

Built with ❤️ by Mohammad Aman

Inspired by real-world data challenges and powered by AI ⚡

⭐ Support

If you like this project, consider giving it a ⭐ on GitHub — it motivates me to build more real-world AI tools!
