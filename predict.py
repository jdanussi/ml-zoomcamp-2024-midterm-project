import pickle

from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd


model_file = 'model_rf_230_10_1.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('potability')

@app.route('/predict', methods=['POST'])
def predict():
    water_sample = request.get_json()

    X = pd.DataFrame([water_sample]) 
    y_pred = model.predict_proba(X)[0, 1]
    potability = y_pred >= 0.5

    result = {
        'potability_probability': float(y_pred),
        'potability': bool(potability)
    }
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)