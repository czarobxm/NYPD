import pandas as pd
import pit
from pit.analiza_danych.CONST import procent_pracujacych

def testy_roznica():
    test_pit_19_df = pd.DataFrame({'WK':['00','00'],
                                   'PK':['02','02'],
                                   'GK':['06','08'],
                                   'GT':['00','02'],
                                   'Dochody wykonane':[2,5]})
            
    test_pit_20_df = pd.DataFrame({'WK':['00','00'],
                                   'PK':['02','02'],
                                   'GK':['06','08'],
                                   'GT':['00','02'],
                                   'Dochody wykonane':[5,2]})

    # testowanie wariancji dochodu gmin w powiecie
    expected_df = pd.DataFrame({'WK':['00','00'],
                                 'PK':['02','02'],
                                 'GK':['06','08'],
                                 'GT':['00','02'],
                                 'różnica dochodu z pit między 2019 a 2020':[3.0,-3.0]})

    pd.testing.assert_frame_equal(pit.analiza_danych.obliczanie_roznicy_pit(test_pit_19_df, test_pit_20_df),expected_df)
    #pd.testing.assert_frame_equal(pit.analiza_danych.sredni_dochod_opodatkowany(pd.DataFrame(),pd.DataFrame()),pd.DataFrame())

testy_roznica()
