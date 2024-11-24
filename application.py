from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

application = Flask(__name__)  # Create an instance of the Flask class
app = application

# import ridge regressor and standard scaler pickle
ridge = pickle.load(open('models/ridge.pkl','rb'))
scaler = pickle.load(open('models/scaler.pkl','rb'))

# @app.route('/')  # Define the route for the home page
# def index():
#     return render_template('index.html')

@app.route("/",methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        data = [float(value) for value in request.form.to_dict().values()]
        new_data_scaled = scaler.transform([data])
        result = ridge.predict(new_data_scaled)
        print(result)
        return render_template('home.html',result=result[0])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")  # Start the development server
