from flask import Flask, jsonify, send_from_directory
from model import model

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/predict/<int:passengers>")
def predict(passengers):
    prediction = model.predict([[passengers]])

    return jsonify({
        "passengers": passengers,
        "prediction": prediction[0]
    })

if __name__ == "__main__":
    app.run(debug=True)