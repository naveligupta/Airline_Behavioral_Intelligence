import pandas as pd
import os

# ---------------------------------------
# Base Path
# ---------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")


# ---------------------------------------
# KPI SUMMARY
# ---------------------------------------

def load_kpi():

    return pd.read_csv(
        os.path.join(DATA_DIR, "kpi_summary.csv")
    )


# ---------------------------------------
# CUSTOMER SEGMENTS
# ---------------------------------------

def load_customer_segments():

    return pd.read_csv(
        os.path.join(DATA_DIR, "customer_segments.csv")
    )


# ---------------------------------------
# CLUSTER SUMMARY
# ---------------------------------------

def load_cluster_summary():

    return pd.read_csv(
        os.path.join(DATA_DIR, "cluster_summary.csv")
    )


# ---------------------------------------
# FEATURE IMPORTANCE
# ---------------------------------------

def load_feature_importance():

    return pd.read_csv(
        os.path.join(DATA_DIR, "feature_importance.csv")
    )


# ---------------------------------------
# MODEL COMPARISON
# ---------------------------------------

def load_model_comparison():

    return pd.read_csv(
        os.path.join(DATA_DIR, "model_comparison.csv")
    )