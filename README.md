# Medical Disease Prediction Web Application

A Flask-based machine learning web application that predicts three major diseases: **Diabetes**, **Heart Disease**, and **Parkinson's Disease**. The application is successfully deployed on Render and provides an intuitive interface for users to input medical parameters and receive predictions.

## 🚀 Live Demo

**Deployed Application**: [https://vaidyai-1.onrender.com]

## 📋 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Models Integrated](#models-integrated)
- [Installation](#installation)
- [Usage](#usage)

- [Deployment](#deployment)

## 🧠 Models Integrated

- **Multi-Disease Prediction**: Supports prediction for three different diseases
- **User-Friendly Interface**: Clean and responsive web interface
- **Real-time Predictions**: Instant results based on user input
- **Input Validation**: Comprehensive form validation for medical parameters
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Cloud Deployment**: Successfully deployed on Render platform

## 🛠 Technologies Used

### Backend
- **Flask** - Python web framework
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **pickle** - Model serialization

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling and responsive design
- **JavaScript** - Client-side interactivity
- **Bootstrap** (optional) - UI framework

### Deployment
- **Render** - Cloud platform for deployment
- **Git** - Version control
- **requirements.txt** - Python dependencies management

## 🧠 Models Integrated

### 1. Diabetes Prediction Model
- **Algorithm**: Support Vector Machine (SVM)
- **Features**: Glucose level, BMI, Age, Blood Pressure, etc.
- **Accuracy**: 84%

### 2. Heart Disease Prediction Model
- **Algorithm**: K-Nearest Neighbors (KNN)
- **Features**: Chest pain type, cholesterol, maximum heart rate, etc.
- **Accuracy**: 86%

### 3. Parkinson's Disease Prediction Model
- **Algorithm**: Linear Regression
- **Features**: Voice measurements, tremor indicators, etc.
- **Accuracy**: 82%

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/medical-prediction-app.git
   cd medical-prediction-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 💻 Usage

### Web Interface
1. Navigate to the home page
2. Select the disease prediction you want to perform
3. Fill in the required medical parameters
4. Click "Predict" to get the result
5. View the prediction result with confidence score

### Input Parameters

#### Diabetes Prediction
- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI
- Diabetes Pedigree Function
- Age

#### Heart Disease Prediction
- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope
- Number of Major Vessels
- Thalassemia

#### Parkinson's Disease Prediction
- Voice frequency measurements
- Jitter and shimmer values
- Noise-to-harmonics ratio
- Other voice-related parameters



## 🚀 Deployment

### Render Deployment Steps

1. **Prepare your repository**
   - Ensure all files are committed to Git
   - Create `requirements.txt` with all dependencies
   - Create `render.yaml` (optional) for build configuration

2. **Create Render account**
   - Sign up at [render.com](https://render.com)
   - Connect your GitHub repository

3. **Deploy application**
   - Create new Web Service
   - Connect your repository
   - Set build and start commands:
     ```
     Build Command: pip install -r requirements.txt
     Start Command: python app.py
     ```

4. **Environment variables** (if needed)
   - Set any required environment variables in Render dashboard

5. **Access deployed app**
   - Your app will be available at `https://vaidyai-1.onrender.com`

### Required Files for Deployment

- `requirements.txt` - Python dependencies
- `app.py` - Main Flask application
- `Procfile` (optional) - Process file for deployment
- Model files (`.pkl` files)
- Templates and static files



## 🧪 Model Training

The models were trained using the following datasets:
- **Diabetes**: Pima Indians Diabetes Database
- **Heart Disease**: Cleveland Heart Disease Dataset
- **Parkinson's**: Parkinson's Disease Dataset

### Model Performance
| Model | Algorithm | Accuracy |
|-------|-----------|----------|
| Diabetes | SVM | 84% |
| Heart Disease | KNN | 86% |
| Parkinson's | Knn | 82% |



---

⭐ **If you found this project helpful, please give it a star!** ⭐
