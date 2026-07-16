import joblib
import numpy as np
import os

# ---------------------------------------
# Load Trained Model
# ---------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "Models",
    "best_churn_model.pkl"
)

model = joblib.load(MODEL_PATH)
print("=" * 60)
print("Loaded Model:")
print(model)
print(model.get_params())
print("=" * 60)


# ---------------------------------------
# Predict Churn
# ---------------------------------------
def predict_churn(data):

    features = np.array([[
        data["Total Flights"],
        data["Total Distance"],
        data["Total Points Redeemed"],
        data["Active Months"],
        data["Avg Flights per Active Month"],
        data["Redemption Ratio"],
        data["Avg Distance per Flight"],
        data["Loyalty Tenure (Months)"],
        data["Months Since Last Flight"]
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    
    print("Features:", features)
    print("Prediction:", prediction)
    print("Probability:", probability)

    return prediction, probability