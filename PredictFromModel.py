# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:30:28 2020

@author: Ijaz
"""
import pickle
import numpy as np
from PreprocessInputFile import PreprocessInput

class PredictFromModel_:
    def Predict_stock_for_date(self,input_date):
        PreprocessInput_obj = PreprocessInput()
        input_days_to_predict = PreprocessInput_obj.get_user_input_date_to_predict(input_date)
        model = pickle.load(open('model.pkl','rb'))
        fc, se, conf = model.forecast(input_days_to_predict, alpha=0.05)
        return np.exp(fc[input_days_to_predict-1])
       
        
        
        