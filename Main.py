# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:05:30 2020

@author: Ijaz
"""
from DumpModel import DumpModel_
from PredictFromModel import PredictFromModel_
from PredictForRangeDate import PredictForRange

def main():
    #DumpModel_obj = DumpModel_()
    #DumpModel_obj.Dump_model_to_path()
    
    
    PredictFromModel_obj = PredictFromModel_()
    input_date = '2017-04-03'
    stock = PredictFromModel_obj.Predict_stock_for_date(input_date)
    print(stock)
    
    PredictForRange_obj = PredictForRange()
    
    PredictForRange_obj.Predict_stock_for_range('2013-04-08')
    
    
    
    
if __name__ ==  "__main__" :
    main()    