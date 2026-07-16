import plotly.express as px

# ------------------------------------------
# Customer Segment Distribution Chart
# ------------------------------------------


def customer_segment_chart(df):

    segment = df.groupby("Customer Segment").size().reset_index(name="Customers")

    fig = px.bar(
        segment,
        x="Customer Segment",
        y="Customers",
        color="Customer Segment",
        text="Customers",
        title="Customer Distribution by Segment",
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        showlegend=False,
        title_x=0.5,
        xaxis_title="Customer Segment",
        yaxis_title="Customers",
    )

    fig.update_traces(textposition="outside")

    return fig.to_html(full_html=False)


# ------------------------------------------
# Average Flights by Customer Segment
# ------------------------------------------


def avg_flights_chart(df):

    flights = df.copy()

    flights["Total Flights"] = flights["Total Flights"].fillna(0)

    flights = flights.groupby("Customer Segment", as_index=False)[
        "Total Flights"
    ].mean()

    fig = px.bar(
        flights,
        x="Customer Segment",
        y="Total Flights",
        color="Customer Segment",
        title="Average Flights by Customer Segment",
    )

    fig.update_layout(
        template="plotly_white", height=450, showlegend=False, title_x=0.5
    )

    return fig.to_html(full_html=False)


# ------------------------------------------
# Loyalty Tenure Chart
# ------------------------------------------


def tenure_chart(df):

    tenure = df.copy()

    tenure["Loyalty Tenure (Months)"] = tenure["Loyalty Tenure (Months)"].fillna(0)

    tenure = tenure.groupby("Customer Segment", as_index=False)[
        "Loyalty Tenure (Months)"
    ].mean()

    fig = px.bar(
        tenure,
        x="Customer Segment",
        y="Loyalty Tenure (Months)",
        color="Customer Segment",
        title="Average Loyalty Tenure",
    )

    fig.update_layout(
        template="plotly_white", height=450, showlegend=False, title_x=0.5
    )

    return fig.to_html(full_html=False)

# ------------------------------------------
# Churn Rate by Customer Segment
# ------------------------------------------

def churn_rate_chart(df):

    churn = (
        df.groupby("Customer Segment")["Churn"]
        .mean()
        .reset_index()
    )

    churn["Churn Rate"] = churn["Churn"] * 100

    fig = px.bar(
        churn,
        x="Customer Segment",
        y="Churn Rate",
        color="Customer Segment",
        title="Churn Rate by Customer Segment",
        text="Churn Rate"
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        showlegend=False,
        title_x=0.5,
        yaxis_title="Churn Rate (%)",
        xaxis_title=""
    )

    return fig.to_html(full_html=False)
