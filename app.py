import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify

# Load the trained model
with open('xgboost_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

# Function to calculate Lean Body Mass (LBM) based on gender, weight, and height
def calculate_lbm(gender, weight, height):
    if gender == 0:  # Male
        lbm = 0.407 * weight + 0.267 * height - 19.2
    else:  # Female
        lbm = 0.252 * weight + 0.473 * height - 48.3
    return lbm

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data from the user
        gender = int(request.form['gender'])  # 0 for male, 1 for female
        age = float(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        duration = float(request.form['duration'])  # Exercise duration
        heart_rate = float(request.form['heart_rate'])  # Heart rate
        body_temp = float(request.form['body_temp'])  # Body temperature
        
        # Calculate Lean Body Mass (LBM)
        lbm = calculate_lbm(gender, weight, height)
        
        # Prepare the input data for prediction
        input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp, lbm]])
        
        # Predict calories using the loaded model
        prediction = model.predict(input_data)
        predicted_calories = prediction[0]  # Extract single value from array
        
        return render_template('index.html', prediction_text=f'Predicted Calories: {predicted_calories:.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
