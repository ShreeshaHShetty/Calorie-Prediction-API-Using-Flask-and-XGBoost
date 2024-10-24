from flask import Flask, request, jsonify
import numpy as np
from xgboost import Booster  # Import Booster from XGBoost

# Initialize the Flask app
app = Flask(__name__)

# Load the XGBoost model from the JSON file
model = Booster()
model.load_model('xgboost_model.json')  # Load the model saved in JSON format

# Function to calculate Lean Body Mass (LBM)
def calculate_lbm(gender, weight, height):
    if gender == 0:  # Male
        lbm = 0.407 * weight + 0.267 * height - 19.2
    else:  # Female
        lbm = 0.252 * weight + 0.473 * height - 48.3
    return lbm

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json(force=True)

    # Parse input data
    gender = data['gender']
    age = data['age']
    height = data['height']
    weight = data['weight']
    duration = data['duration']
    heart_rate = data['heart_rate']
    body_temp = data['body_temp']  # Add Body_Temp to match your feature list

    # Calculate LBM
    lbm = calculate_lbm(gender, weight, height)

    # Create the input array (now with 8 features)
    input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp, lbm]])

    # Make the prediction using the loaded model
    prediction = model.inplace_predict(input_data)

    # Return the prediction as a JSON response
    return jsonify({'calories_burned': float(prediction[0])})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
