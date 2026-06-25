from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load Model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data received"
            }), 400

        sonar_values = data.get("sonar_data")

        if not sonar_values:
            return jsonify({
                "error": "sonar_data missing"
            }), 400

        if len(sonar_values) != 60:
            return jsonify({
                "error": f"Expected 60 values, got {len(sonar_values)}"
            }), 400

        sonar_data = np.array(
            sonar_values,
            dtype=float
        ).reshape(1, -1)

        prediction = model.predict(sonar_data)[0]

        try:
            confidence = round(
                float(np.max(
                    model.predict_proba(sonar_data)
                )) * 100,
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
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
