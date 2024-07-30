from flask import Blueprint, render_template, request
from ..utils.model_utils import random_forest_model

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        feature1 = request.form.get('feature1')
        feature2 = request.form.get('feature2')
        feature3 = request.form.get('feature3')

        # Validate input
        if not feature1 or not feature2 or not feature3:
            return render_template('index.html', error="Please fill in all fields.")

        try:
            # Convert input to float
            feature1 = float(feature1)
            feature2 = float(feature2)
            feature3 = float(feature3)
        except ValueError:
            return render_template('index.html', error="Please enter valid numbers.")

        # Prepare feature data
        features = [[feature1, feature2, feature3]]

        # Prediction
        try:
            model = random_forest_model
            prediction = model.predict(features)
            return render_template('results.html', prediction=prediction[0])
        except Exception as e:
            return render_template('index.html', error=f"Prediction error: {e}")

    return render_template('index.html')
