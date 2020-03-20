# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:42:41 2020

@author: Ijaz
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from statsmodels.tsa.stattools import adfuller     

class TestForStationarity:
    def test_stationarity(self,timeseries):
            
        adft = adfuller(timeseries,autolag='AIC')
    # output for dft will give us without defining what the values are.
    #hence we manually write what values does it explains using a for loop
        output = pd.Series(adft[0:4],index=['Test Statistics','p-value','No. of lags used','Number of observations used'])
        for key,values in adft[4].items():
            output['critical value (%s)'%key] =  values
       
        if(adft[1] > 0.05):
            result = False
        else:
           result = True
        return result
                    