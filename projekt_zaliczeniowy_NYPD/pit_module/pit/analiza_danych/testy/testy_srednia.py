import pandas as pd
import pit
from pit.analiza_danych.CONST import procent_pracujacych

def testy_srednia():
    test_pit_df = pd.DataFrame({'WK':['00','00'],
                            'PK':['02','02'],
                            'GK':['06','08'],
                            'GT':['00','02'],
                            'Dochody wykonane':[2,4]})
    
    test_ludnosc_df = pd.DataFrame({'WK':['00','00'],
                            'PK':['02','02'],
                            'GK':['06','08'],
                            'GT':['00','02'],
                            'ogółem':[2,8]})

    # testowanie wariancji dochodu gmin w powiecie
    expected_df = pd.DataFrame({'WK':['00','00'],
                                 'PK':['02','02'],
                                 'GK':['06','08'],
                                 'GT':['00','02'],
                                 'średni dochód':[2/(2*procent_pracujacych),4/(8*procent_pracujacych)]})

    pd.testing.assert_frame_equal(pit.analiza_danych.sredni_dochod_opodatkowany(test_pit_df, test_ludnosc_df),expected_df)
    pd.testing.assert_frame_equal(pit.analiza_danych.sredni_dochod_opodatkowany(pd.DataFrame(),pd.DataFrame()),pd.DataFrame())

testy_srednia()
    

