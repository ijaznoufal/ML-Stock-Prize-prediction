# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:59:19 2020

@author: Ijaz
"""



from datetime import datetime
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from pylab import rcParams
rcParams['figure.figsize'] = 11, 7
from ReadCsvFile import ReadData
from StationarityTestFile import TestForStationarity
from ScaleDownFile import ScaleDown
from TrainTestSplitFile import TrainTest

#from ForecastFutureFile import  Predict
from PreprocessInputFile import PreprocessInput
#from RangeForcastFile import Predict

class PredictForRange:
    def Predict_stock_for_range(self,date_to_predict):
        
        read_csv = ReadData()
        test_for_stat = TestForStationarity()
        df_close = read_csv.Read_from_csv('Close','aaba.us.txt')
      
            # test for sts
        test_for_stat.test_stationarity(df_close)
        
        #scaling down
        scaling_down = ScaleDown()
        df_log = scaling_down.Scale_down(df_close)
        
        #spliting 
        split = TrainTest()
        train_data, test_data = split.TrainTestSplit(df_log)
        
        #build model
        
        PreprocessInput_obj = PreprocessInput()
        input_date_to_predict = PreprocessInput_obj.get_user_input_date_to_predict(date_to_predict)
        print("Graph:")
        #forcast
        
        model = pickle.load(open('model.pkl','rb'))
        fc, se, conf = model.forecast(input_date_to_predict, alpha=0.05)
        
        
        test_data_firstdate = datetime(2011,5,22)
        
        df_date = pd.date_range(test_data_firstdate,date_to_predict,freq='B')
      #  df_final= pd.DataFrame(fc,index=df_date,columns=['Close'])

        
        fc_series = pd.Series(fc, index=df_date)
        lower_series = pd.Series(conf[:, 0], index=df_date)
        upper_series = pd.Series(conf[:, 1], index=df_date)
        plt.figure(figsize=(12,5), dpi=100)
        plt.plot(np.exp(train_data), label='training')
        plt.plot(np.exp(test_data), color = 'blue', label='Actual Stock Price')
        plt.plot(np.exp(fc_series), color = 'orange',label='Predicted Stock Price')
        plt.fill_between(lower_series.index, lower_series, upper_series, 
             color='k', alpha=.10)
        plt.title('Altaba Inc. Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Actual Stock Price')
        #static/plot
        plt.legend(loc='upper left', fontsize=8)
        plt.savefig('static/plot.png', dpi=100)
        plt.show()