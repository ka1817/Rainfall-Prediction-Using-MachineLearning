import os
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

from preprocess import preprocess


mlflow.set_tracking_uri("http://127.0.0.1:5000") 
mlflow.set_experiment("Rainfall_Prediction_Experiment_1")


project_root = os.path.dirname(os.path.dirname(__file__))  
models_dir = os.path.join(project_root, "models")
os.makedirs(models_dir, exist_ok=True)


df = preprocess()
X = df.drop(columns=["rainfall_binary"])
y = df["rainfall_binary"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


models = {
    "RandomForestClassifier": {
        "model": RandomForestClassifier(random_state=42),
        "params": {
            "n_estimators": [50, 100],
            "max_depth": [6, 8, 10]
        }
    },
    "LogisticRegression": {
        "model": LogisticRegression(solver='liblinear'),
        "params": {
            "C": [0.01, 0.1, 1, 10]
        }
    },
    "KNeighborsClassifier": {
        "model": KNeighborsClassifier(),
        "params": {
            "n_neighbors": [3, 5, 7],
            "weights": ['uniform', 'distance']
        }
    },
    "SVC": {
        "model": SVC(probability=True),
        "params": {
            "C": [0.1, 1, 10],
            "kernel": ['linear', 'rbf']
        }
    }
}


best_score = 0
best_model = None
best_model_name = ""


for name, config in models.items():
    print(f"\n🔍 Training {name}")
    with mlflow.start_run(run_name=name):
        grid = GridSearchCV(config["model"], config["params"], cv=5, scoring='accuracy', n_jobs=-1)
        grid.fit(X_train, y_train)

        y_pred = grid.best_estimator_.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        
        mlflow.log_params(grid.best_params_)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(grid.best_estimator_, "model")

        
        report_path = os.path.join(models_dir, f"{name}_report.txt")
        with open(report_path, "w") as f:
            f.write(report)
        mlflow.log_artifact(report_path)

        
        model_path = os.path.join(models_dir, f"{name}.pkl")
        joblib.dump(grid.best_estimator_, model_path)
        print(f"✅ Saved {name} to: {model_path} | Accuracy: {acc:.4f}")

        
        if acc > best_score:
            best_score = acc
            best_model = grid.best_estimator_
            best_model_name = name


best_model_path = os.path.join(models_dir, "best_model.pkl")
joblib.dump(best_model, best_model_path)
print(f"\n🏆 Best Model: {best_model_name} with Accuracy: {best_score:.4f}")
print(f"📦 Best model saved to: {best_model_path}")
