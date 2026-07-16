import pandas as pd
import plotly.express as px
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "feature_importance.csv"
)


def feature_importance_chart():

    df = pd.read_csv(DATA_PATH)
    df = df[df["Importance"] > 0]

    fig = px.bar(
        df,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        text="Importance",
        title="Feature Importance"
    )

    fig.update_layout(
        template="plotly_white",
        height=550,
        title_x=0.5,
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    return fig.to_html(full_html=False)