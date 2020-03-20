# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:09:20 2020

@author: Ijaz
"""


class TrainTest:
    def TrainTestSplit(self,df_log):
        train_data, test_data = df_log[3 : int(len(df_log)*0.7)], df_log[int(len(df_log)*0.7) : ]
        return train_data,test_data
      
     