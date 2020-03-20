# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:14:03 2020

@author: Ijaz
"""
from statsmodels.tsa.arima_model import ARIMA

class ArimaModel:
    def ArimaModelBuild(self,train_data):
        model = ARIMA(train_data, order=(3, 1, 2))  
        fitted = model.fit(disp=-1)  
        #print(fitted.summary())
        return fitted
      