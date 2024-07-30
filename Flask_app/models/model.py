import joblib
import os

# Correct path to the models directory
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model')

def load_model(model_name):
    model_file = os.path.join(MODEL_PATH, model_name)
    return joblib.load(model_file)

# Load the models
