# This code is a Flask application that serves as a web interface for three different health prediction models:
# diabetes, heart disease, and Parkinson's disease. It loads pre-trained models and scalers, processes user input from forms,

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load models and scalers once on startup
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))
diabetes_scaler = pickle.load(open('diabetes_scaler.pkl', 'rb'))

heart_model = pickle.load(open('heart_model.pkl', 'rb'))
heart_scaler = pickle.load(open('heart_scaler.pkl', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.pkl', 'rb'))
parkinsons_scaler = pickle.load(open('parkinsons_scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    prediction = None
    if request.method == 'POST':
        try:
            features = [float(request.form[key]) for key in request.form]
            scaled = diabetes_scaler.transform([features])
            prediction = int(diabetes_model.predict(scaled)[0])
        except Exception as e:
            prediction = None
            # optionally: log the exception e for debugging
    return render_template('diabetes.html', prediction=prediction)


@app.route('/heart', methods=['GET', 'POST'])
def heart():
    prediction = None
    if request.method == 'POST':
        try:
            features = [float(request.form[key]) for key in request.form]
            scaled = heart_scaler.transform([features])
            prediction = int(heart_model.predict(scaled)[0])
        except Exception as e:
            prediction = None
    return render_template('heart.html', prediction=prediction)


@app.route('/parkinsons', methods=['GET', 'POST'])
def parkinsons():
    prediction = None
    if request.method == 'POST':
        try:
            features = [float(request.form[key]) for key in request.form]
            scaled = parkinsons_scaler.transform([features])
            prediction = int(parkinsons_model.predict(scaled)[0])
        except Exception as e:
            prediction = None
    return render_template('parkinsons.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
# This code is a Flask application that serves as a web interface for three different health prediction models:
# diabetes, heart disease, and Parkinson's disease. It loads pre-trained models and scalers, processes user input from forms,