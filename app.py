from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsRegressor


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction',methods=['get','post'])
def prediction():
    HP = float(request.form.get('HP'))
    VOL = float(request.form.get('VOL'))
    SP = float(request.form.get('SP'))
    WT = float(request.form.get('WT'))

    model = pickle.load(open(r"C:\Users\ravin\fuel.pkl",'rb'))
    prediction = model.predict([[HP,VOL,SP,WT]])


    return render_template('home.html',prediction=prediction[0])
if __name__=='__main__':
    app.run(debug=True)