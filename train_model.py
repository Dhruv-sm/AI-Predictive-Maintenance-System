import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv("data/system_metrics.csv")
def get_risk(row):

    if row["cpu_usage"] > 90 or row["ram_usage"] > 90:
        return "HIGH"

    elif row["cpu_usage"] > 70 or row["ram_usage"] > 85:
        return "MEDIUM"

    else:
        return "LOW"


df["risk"] = df.apply(get_risk, axis=1)
print(df["risk"].value_counts())
features = [
    "cpu_usage",
    "ram_usage",
    "disk_usage",
    "cpu_frequency",
    "available_ram_gb",
    "free_disk_gb"
]

X = df[features]
y = df["risk"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
joblib.dump(model, "models/risk_model.pkl")

print("Model saved successfully")
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)
print("Total Rows:", len(df))
print(df.describe())