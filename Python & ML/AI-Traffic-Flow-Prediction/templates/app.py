from flask import Flask, request, render_template, jsonify
import joblib

# Load model
model = joblib.load('traffic_model.pkl')

# Initialize Flask
app = Flask(__name__)

# Home page (form)
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['temp']),
        int(request.form['rain_1h']),
        float(request.form['lag_1']),
        float(request.form['lag_2']),
        float(request.form['rolling_mean_3']),
        float(request.form['accident_intensity'])
    ]

    prediction = model.predict([features])[0]

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
