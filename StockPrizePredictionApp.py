# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:34:56 2020

@author: Ijaz
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from PredictFromModel import PredictFromModel_
from PredictForRangeDate import PredictForRange

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [str(x) for x in request.form.values()]
    
    #prediction = model.predict(final_features)
    
    PredictFromModel_obj = PredictFromModel_()
    input_date = int_features[0]
    stock_prize = PredictFromModel_obj.Predict_stock_for_date(input_date)
  #  return render_template('input.html', name = 'new_plot', url ='foo.jpg')
    return render_template('input.html', prediction_text='Date :{0} Stock Prize: {1}'.format(input_date,stock_prize))

@app.route('/predict_range',methods=['POST'])

def predict_range():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [str(x) for x in request.form.values()]
    
   
    
    input_date = int_features[1]
    
    PredictForRange_obj = PredictForRange()
    
    PredictForRange_obj.Predict_stock_for_range(input_date)
  
    return render_template('input.html', prediction_text='Date :{0} Stock Prize: {1}'.format(int_features[0],int_features[1]))
   

if __name__ == "__main__":
    app.run(debug=False)