# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:18:11 2020

@author: Ijaz
"""
#np.exp(fc[input_date_to_predict-1])
import numpy as np

class Predict:
    def ForcastFuture(self,fitted,input_date_to_predict):
       fc, se, conf = fitted.forecast(input_date_to_predict, alpha=0.05)
       return np.exp(fc[input_date_to_predict-1])