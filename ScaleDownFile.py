# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:01:03 2020

@author: Ijaz
"""

import numpy as np
from StationarityTestFile import TestForStationarity

class ScaleDown:
    def Scale_down(self,df_close):
          
        test_for_stat = TestForStationarity()
        is_stat = test_for_stat.test_stationarity(df_close)
        if(is_stat!=True):
            df_log = np.log(df_close)
        else:
            df_log = df_close
        return df_log
     