from flask import Flask, render_template

from services.data_loader import (
    load_kpi,
    load_cluster_summary,
    load_customer_segments,
    load_feature_importance,
    load_model_comparison,
)

from services.chart_service import (
    customer_segment_chart,
    avg_flights_chart,
    tenure_chart,
    churn_rate_chart
)

from flask import request
from services.prediction_service import predict_churn

from services.strategy_service import feature_importance_chart

app = Flask(__name__)

# ---------------------------------------
# HOME PAGE
# ---------------------------------------


@app.route("/")
def home():
    return render_template("home.html")


# ---------------------------------------
# FLIGHT DECK
# ---------------------------------------
@app.route("/flight-deck")
def flight_deck():

    kpi = load_kpi()
    metrics = dict(zip(kpi["Metric"], kpi["Value"]))

    customer_df = load_customer_segments()

    flights_chart = avg_flights_chart(customer_df)
    tenure_chart_html = tenure_chart(customer_df)
    churn_chart = churn_rate_chart(customer_df)

    return render_template(
        "flight_deck.html",
        metrics=metrics,
        flights_chart=flights_chart,
        tenure_chart=tenure_chart_html,
        churn_chart=churn_chart
    )
        

# ---------------------------------------
# PASSENGER INSIGHTS
# ---------------------------------------


@app.route("/passenger-insights")
def passenger_insights():

    customer_df = load_customer_segments()

    segment_chart = customer_segment_chart(customer_df)

    return render_template("passenger_insights.html", segment_chart=segment_chart)


# ---------------------------------------
# RETENTION CENTER
# ---------------------------------------

# ---------------------------------------
# RETENTION CENTER
# ---------------------------------------

@app.route("/retention-center", methods=["GET", "POST"])
def retention_center():

    prediction = None
    probability = None
    recommendation = None

    if request.method == "POST":

        customer = {

            "Total Flights": float(request.form["total_flights"]),

            "Total Distance": float(request.form["total_distance"]),

            "Total Points Redeemed": float(request.form["points_redeemed"]),

            "Active Months": float(request.form["active_months"]),

            "Avg Flights per Active Month": float(request.form["avg_flights"]),

            "Redemption Ratio": float(request.form["redemption_ratio"]),

            "Avg Distance per Flight": float(request.form["avg_distance"]),

            "Loyalty Tenure (Months)": float(request.form["loyalty_tenure"]),

            "Months Since Last Flight": float(request.form["months_since_last_flight"])

        }

        result, prob = predict_churn(customer)

        probability = f"{prob*100:.2f}%"

        if prob >= 0.70:
            prediction = "🔴 High Churn Risk"
            recommendation = "Immediate retention campaign. Offer bonus miles, premium upgrade and personalized discounts."

        elif prob >= 0.30:
            prediction = "🟡 Medium Churn Risk"
            recommendation = "Customer engagement is declining. Send targeted offers and reward incentives."

        else:
            prediction = "🟢 Low Churn Risk"
            recommendation = "Customer is likely to remain loyal. Continue engagement through rewards and exclusive offers."

    return render_template(

        "retention_center.html",

        prediction=prediction,

        probability=probability,

        recommendation=recommendation

    )


# ---------------------------------------
# STRATEGY HUB
# ---------------------------------------

# ---------------------------------------
# STRATEGY HUB
# ---------------------------------------

@app.route("/strategy-hub")
def strategy_hub():

    chart = feature_importance_chart()

    metrics = {
        "Accuracy": "98.15%",
        "Precision": "95%",
        "Recall": "79%",
        "F1 Score": "86%"
    }

    return render_template(
        "strategy_hub.html",
        chart=chart,
        metrics=metrics
    )

# ---------------------------------------
# RUN APPLICATION
# ---------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
