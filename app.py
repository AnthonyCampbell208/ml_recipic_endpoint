import pandas as pd
from flask import Flask, jsonify, request
import pickle

# load model
# model = pickle.load(open('model.pkl','rb'))
filehandler = open('model.pkl', 'r') 
model = pickle.load(filehandler)

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)
    print(type(model))
    print(data)
    # convert data into dataframe
    return data['file']

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(result)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)