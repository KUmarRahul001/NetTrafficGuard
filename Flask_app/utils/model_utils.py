import joblib
import os

# Correct path to the models directory
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'model')

def load_model(model_name):
    model_file = os.path.join(MODEL_PATH, model_name)
    return joblib.load(model_file)

#load Model

random_forest_model = load_model('E:\\Hackatone Project\\NetTrafficGuard\\model\\random_forest_model.pkl')
tuned_random_forest_model = load_model('E:\\Hackatone Project\\NetTrafficGuard\\model\\tuned_random_forest_model.pkl')
