# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:58:11 2020

@author: Ijaz
"""
from datetime import datetime
import pandas as pd

class PreprocessInput:
    def get_user_input_date_to_predict(self,date_to_predict):
        test_data_firstdate = datetime(2011,5,22)
        df_date = pd.date_range(test_data_firstdate,date_to_predict,freq='B')  
        return df_date.size
        