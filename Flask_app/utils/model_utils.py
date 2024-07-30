import joblib

random_forest_model = joblib.load('E:\\Hackatone Project\\NetTrafficGuard\\model\\random_forest_model.pkl')
tuned_random_forest_model = joblib.load('E:\\Hackatone Project\\NetTrafficGuard\\model\\tuned_random_forest_model.pkl')
# Ensure the model is loaded correctly and expects the right number of features
