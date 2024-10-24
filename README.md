
## **Calorie Prediction API Using Flask and XGBoost**

This repository contains a Flask-based API for predicting calories burned during exercise based on user input data such as gender, age, weight, height, heart rate, and exercise duration. The machine learning model used is an XGBoost regression model.

### **Project Overview**
This project includes:
- **Flask API**: A simple web API built using Flask to handle user input and return calorie predictions.
- **Machine Learning Model**: XGBoost model trained on exercise and calorie datasets.
- **Data**: Includes datasets (`calories.csv` and `exercise.csv`) for model training and evaluation.

### **Files in the Repository**
- `app.py`: The Flask application with the prediction logic.
- `predict`: Any additional API code or related scripts.
- `xgboost_model.json`: The saved XGBoost model used for predictions.
- `Calories_Prediction.ipynb`: Jupyter notebook for training and evaluating the model.
- `calories.csv` & `exercise.csv`: Datasets used for training the model.
- `requirements.txt`: Python package dependencies.
- `README.md`: Project documentation.

---

### **Setup and Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShreeshaHShetty/Calorie-Prediction-API-Using-Flask-and-XGBoost.git
   cd calorie-prediction-api
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install the Dependencies**:
   Install the required Python packages using `pip` and the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**:
   Start the Flask app by running:
   ```bash
   python app.py
   ```

   The app will be running locally at `http://127.0.0.1:5000/`.

---

### **Using the API**

Once the app is running, you can send POST requests to the `/predict` endpoint to get a calorie prediction.

#### **Request Format**
Send a JSON object with the following fields to the `/predict` endpoint:

```json
{
  "gender": 1,
  "age": 30,
  "height": 170,
  "weight": 70,
  "duration": 40,
  "heart_rate": 110,
  "body_temp": 37.5
}
```

- `gender`: 0 for male, 1 for female.
- `age`: Age in years.
- `height`: Height in centimeters.
- `weight`: Weight in kilograms.
- `duration`: Exercise duration in minutes.
- `heart_rate`: Heart rate during exercise in beats per minute.
- `body_temp`: Body temperature during exercise in Celsius.

#### **Example Response**
A successful request will return a JSON response with the predicted calories burned:

```json
{
  "calories_burned": 245.32
}
```

---

### **Model Training**
- The XGBoost model was trained on the `calories.csv` and `exercise.csv` datasets.
- Lean Body Mass (LBM) is calculated as an additional feature during model training and prediction.

For more details on the model training process, refer to the `Calories_Prediction.ipynb` notebook.

---

### **Dependencies**
- Flask
- XGBoost
- NumPy
- Pandas

All dependencies are listed in the `requirements.txt` file.

---

### **License**
This project is licensed under the MIT License.

---

### **Contributing**
Feel free to open issues or submit pull requests for any improvements or questions!
