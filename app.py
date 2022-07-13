import json
import pandas as pd
from flask import Flask, jsonify, request
import pickle
# import torch

# load model

# recipic_model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])
def predict():
    # get data
    data = request.get_json(force=True)
    # print(type(recipic_model))
    # print(data)
    # results = recipic_model(data, size=416)
    # print(results)
    # convert data into dataframe
    return jsonify(data)

    # # predictions
    # result = model.predict(data_df)

    # # send back to browser
    # output = {'results': int(result[0])}

    # # return data
    # return jsonify(result)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)