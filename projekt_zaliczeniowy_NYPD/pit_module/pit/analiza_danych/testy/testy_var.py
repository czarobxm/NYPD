import pandas as pd
import numpy as np
import pit
import os

def testy_var():
    
    test_df = pd.DataFrame({'WK':['00','00'],
                            'PK':['02','02'],
                            'GK':['06','08'],
                            'GT':['00','02'],
                            'Dochody wykonane':[0,1]})

    # testowanie wariancji dochodu gmin w powiecie
    expected_df = pd.DataFrame({'WK':['00'],
                                 'PK':['02'],
                                 'GK':['00'],
                                 'GT':['00'],
                                 'wariancja dochodu podległych jednostek':[0.33333333333333337]})

    pd.testing.assert_frame_equal(pit.analiza_danych.wariancja_dochodu_gmin_w_powiecie(test_df),expected_df)
    pd.testing.assert_frame_equal(pit.analiza_danych.wariancja_dochodu_gmin_w_powiecie(pd.DataFrame()),pd.DataFrame())
    
    # testowanie wariancji dochodu powiatow w wojewodztwie
    expected_df = pd.DataFrame({'WK':['00'],
                                 'PK':['00'],
                                 'GK':['00'],
                                 'GT':['00'],
                                 'wariancja dochodu podległych jednostek':[0.33333333333333337]})
    pd.testing.assert_frame_equal(pit.analiza_danych.wariancja_dochodu_powiatow_w_wojewodztwie(test_df),expected_df)
    pd.testing.assert_frame_equal(pit.analiza_danych.wariancja_dochodu_powiatow_w_wojewodztwie(pd.DataFrame()),pd.DataFrame())
