# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:21:11 2020

@author: Ijaz
"""
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
import numpy as np

class PerformanceReport:
    def GetPerformanceReport(self,test_data,fc):
        mse = mean_squared_error(test_data, fc)
        print('MSE: '+str(mse))
        mae = mean_absolute_error(test_data, fc)
        print('MAE: '+str(mae))
        rmse = math.sqrt(mean_squared_error(test_data, fc))
        print('RMSE: '+str(rmse))
        mape = np.mean(np.abs(fc - test_data)/np.abs(test_data))
        print('MAPE: '+str(mape))
        