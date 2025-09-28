from flask import Flask, request, jsonify
import joblib
import numpy as np

# بارگذاری مدل و اسکیلر
model = joblib.load("signal_loss_model.pkl")
scaler = joblib.load("scaler.pkl")

# ایجاد اپلیکیشن Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Fiber Optic Signal Loss Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # دریافت داده‌های ورودی از درخواست
        data = request.get_json(force=True)
        
        # داده‌های ورودی باید شامل ۴ ویژگی باشد
        input_data = np.array([[
            data['Input Power (dBm)'],
            data['Fiber Length (km)'],
            data['Temperature (°C)'],
            data['Number of Connectors']
        ]])

        # نرمال‌سازی داده‌ها
        scaled_data = scaler.transform(input_data)

        # پیش‌بینی با مدل
        prediction = model.predict(scaled_data)

        # ارسال نتیجه به صورت JSON
        return jsonify({'Predicted Signal Loss (dB)': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)