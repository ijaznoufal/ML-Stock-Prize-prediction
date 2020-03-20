# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:39:09 2020

@author: Ijaz
"""
import pandas as pd

class ReadData:
        def Read_from_csv(self,Target_col_name,file_path):
            dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
            data = pd.read_csv(file_path,sep=',', index_col='Date', parse_dates=['Date'], date_parser=dateparse).fillna(0)
            df_close = data[Target_col_name]
            return df_close
