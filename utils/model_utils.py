# utils/model_utils.py

import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

def save_model(model, path):
    """Save a trained model to disk."""
    joblib.dump(model, path)

def load_model(path):
    """Load a trained model from disk."""
    return joblib.load(path)

def evaluate_regression(y_true, y_pred, verbose=True):
    """Print and return regression metrics."""
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    if verbose:
        print(f"RMSE: {rmse:.2f}")
        print(f"MAE: {mae:.2f}")
        print(f"R² Score: {r2:.2f}")

    return {"rmse": rmse, "mae": mae, "r2": r2}

def evaluate_classification(y_true, y_pred, average='weighted', verbose=True):
    """Print and return classification metrics."""
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average=average, zero_division=0)
    rec = recall_score(y_true, y_pred, average=average, zero_division=0)
    f1 = f1_score(y_true, y_pred, average=average, zero_division=0)

    if verbose:
        print(f"Accuracy: {acc:.2f}")
        print(f"Precision: {prec:.2f}")
        print(f"Recall: {rec:.2f}")
        print(f"F1 Score: {f1:.2f}")

    return {"accuracy": acc, "precision": prec, "recall": rec, "f1": f1}

def plot_confusion_matrix(y_true, y_pred, labels=None, title="Confusion Matrix"):
    """Plot confusion matrix."""
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap='Blues')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
