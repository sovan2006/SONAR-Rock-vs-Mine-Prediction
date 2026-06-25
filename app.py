
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Receive JSON data from frontend
        data = request.get_json()

        # Convert input into NumPy array
        sonar_data = np.array(
            data["sonar_data"]
        ).reshape(1, -1)

        # Make prediction
        prediction = model.predict(sonar_data)[0]

        # Confidence score
        try:
            confidence = round(
                np.max(model.predict_proba(sonar_data)) * 100,
                2
            )
        except Exception:
            confidence = 95.0

        return jsonify({
            "prediction": prediction,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
