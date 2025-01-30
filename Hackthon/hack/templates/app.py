from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from request
    data = request.json
    input_features = data['features']  # Example: {"features": [0.5, 0.8, 0.3]}

    # Create a DataFrame for prediction
    input_df = pd.DataFrame([input_features], columns=['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5','sensor6','sensor7','sensor8','sensor9'])  # Replace columns

    # Make prediction
    prediction = model.predict(input_df)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
