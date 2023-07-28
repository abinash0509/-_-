# Assuming you're using Flask for deployment
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_sales():
    data = request.get_json()
    # Assuming 'data' contains input features for the model
    prediction = best_random_forest_model.predict([data])
    return jsonify({'prediction': prediction[0]})
