import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def prepare_features(df):
    """Prepare features for modeling."""
    features = [
        "Age",
        "AnnualPremium",
        "Deductible",
        "NCD",
        "PastClaims",
        "CustomValueEstimate",
    ]
    categorical = ["Gender", "Province", "VehicleType"]
    df_encoded = pd.get_dummies(df[categorical], drop_first=True)
    X = pd.concat([df[features], df_encoded], axis=1)
    return X


def train_models(X_train, X_test, y_train, y_test):
    """Train multiple models and return results."""
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "XGBoost": XGBRegressor(n_estimators=100, random_state=42),
    }
    results = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        results.append({"Model": name, "RMSE": rmse, "R2": r2})
    return results
