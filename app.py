from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load trained model
model = joblib.load(os.path.join("model", "cyber_threat_model.pkl"))

# Load encoders
protocol_encoder = joblib.load(os.path.join("model", "protocol_encoder.pkl"))
service_encoder = joblib.load(os.path.join("model", "service_encoder.pkl"))
flag_encoder = joblib.load(os.path.join("model", "flag_encoder.pkl"))
label_encoder = joblib.load(os.path.join("model", "label_encoder.pkl"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    protocol = request.form["protocol"]
    service = request.form["service"]
    flag = request.form["flag"]

    try:
        # Encode inputs
        protocol_encoded = protocol_encoder.transform([protocol])[0]
        service_encoded = service_encoder.transform([service])[0]
        flag_encoded = flag_encoder.transform([flag])[0]

        # Predict
        prediction = model.predict([[protocol_encoded, service_encoded, flag_encoded]])

        # Convert prediction back to attack name
        result = label_encoder.inverse_transform(prediction)[0]

        return render_template(
            "index.html",
            prediction=f"Prediction: {result}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)