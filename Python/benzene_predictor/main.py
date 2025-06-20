import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("dataset.csv", sep=";", decimal=",", na_values=-200)

df.drop(columns=["Unnamed: 15", "Unnamed: 16"], inplace=True)

df['Time'] = df['Time'].str.replace('.', ':')

df["Datetime"] = pd.to_datetime(df["Date"] + ' ' + df["Time"], dayfirst=True, errors="coerce")

df.drop(columns=["Date", "Time"], inplace=True)
df.set_index("Datetime", inplace=True)

features = ["PT08.S1(CO)", "PT08.S2(NMHC)", "PT08.S3(NOx)", "PT08.S4(NO2)", "PT08.S5(O3)", "T", "RH", "AH"]

model_df = df[features + ["C6H6(GT)"]].dropna()

X = model_df[features]
y = model_df["C6H6(GT)"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(max_depth=5, random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42)
}

max_distribution = 0
# max_residual = 0

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    counts_actual, _ = np.histogram(y_test, bins=50)
    counts_pred, _ = np.histogram(y_pred, bins=50)
    max_distribution = max(max_distribution, counts_actual.max(), counts_pred.max())

    # residuals = y_test - y_pred
    # max_residual = max(max_residual, abs(residuals).max())

fig, axs = plt.subplots(3, 4, figsize=(20, 12))

for i, (name, model) in enumerate(models.items()):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    residuals = y_test - y_pred
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    axs[0, i].scatter(y_test, y_pred, alpha=0.5)
    axs[0, i].plot([y.min(), y.max()], [y.min(), y.max()], "r--", label="Ideal Prediction")
    axs[0, i].set_title(f"{name}\nMSE={mse:.2f}, R²={r2:.2f}")
    axs[0, i].set_xlabel("Actual Benzene")
    axs[0, i].set_ylabel("Predicted Benzene")
    axs[0, i].legend()
    axs[0, i].grid(True)

    axs[1, i].scatter(y_test, residuals, alpha=0.5)
    axs[1, i].axhline(0, color="r", linestyle="--")
    # axs[1, i].set_ylim(-max_residual * 1.1, max_residual * 1.1)
    axs[1, i].set_title("Residuals")
    axs[1, i].set_xlabel("Actual")
    axs[1, i].set_ylabel("Error")
    axs[1, i].grid(True)

    axs[2, i].hist(y_test, bins=50, alpha=0.6, label="Actual")
    axs[2, i].hist(y_pred, bins=50, alpha=0.6, label="Predicted")
    axs[2, i].set_ylim(0, max_distribution + 5)
    axs[2, i].set_title("Distribution")
    axs[2, i].set_xlabel("Benzene")
    axs[2, i].set_ylabel("Count")
    axs[2, i].legend()

plt.tight_layout()
plt.show()
