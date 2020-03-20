# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:24:24 2020

@author: Ijaz
"""

from ReadCsvFile import ReadData
from StationarityTestFile import TestForStationarity
from ScaleDownFile import ScaleDown
from TrainTestSplitFile import TrainTest
from ArimaModelBuildFile import ArimaModel
import pickle



 #read csv data
class DumpModel_:
    def Dump_model_to_path(file_path):
        
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
        model_build = ArimaModel()
        model = model_build.ArimaModelBuild(train_data)
        
        pickle.dump(model, open('model.pkl','wb'))
        print("Model Dumped!")

    
        
    
    
    
        
    
     
         
    
    