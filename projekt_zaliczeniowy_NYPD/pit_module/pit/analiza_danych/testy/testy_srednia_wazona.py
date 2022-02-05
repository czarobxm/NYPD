import pandas as pd
import pit
from pit.analiza_danych.CONST import procent_pracujacych


def testy_srednia_wazona_dochodu_wojewodztw():
    test_pit_df = pd.DataFrame({'WK':['00','00'],
                                'PK':['02','02'],
                                'GK':['06','08'],
                                'GT':['00','02'],
                                'Dochody wykonane':[10,20]})
    
    test_ludnosc_gminy_df = pd.DataFrame({'WK':['00','00'],
                                          'PK':['02','02'],
                                          'GK':['06','08'],
                                          'GT':['00','02'],
                                          'ogółem':[12,8]})
                
    test_ludnosc_powiaty_df = pd.DataFrame({'WK':['00'],
                                            'PK':['02'],
                                            'GK':['00'],
                                            'GT':['00'],
                                            'ogółem':[20]})

    # testowanie wariancji dochodu gmin w powiecie
    expected_df = pd.DataFrame({'WK':['00'],
                                'PK':['02'],
                                'GK':['00'],
                                'GT':['00'],
                                'srednia ważona':[10*12/20+20*8/20]})

    pd.testing.assert_frame_equal(pit.analiza_danych.srednia_wazona_dochodu_powiatow(test_pit_df, test_ludnosc_gminy_df, test_ludnosc_powiaty_df),expected_df)
    pd.testing.assert_frame_equal(pit.analiza_danych.srednia_wazona_dochodu_powiatow(pd.DataFrame(),pd.DataFrame(),pd.DataFrame()),pd.DataFrame())

    test_pit_df = pd.DataFrame({'WK':['00','00'],
                                'PK':['02','04'],
                                'GK':['00','00'],
                                'GT':['00','00'],
                                'Dochody wykonane':[10,20]})
    
    test_ludnosc_powiaty_df = pd.DataFrame({'WK':['00','00'],
                                          'PK':['02','04'],
                                          'GK':['00','00'],
                                          'GT':['00','00'],
                                          'ogółem':[12,8]})
                
    test_ludnosc_wojewodztwa_df = pd.DataFrame({'WK':['00'],
                                            'PK':['00'],
                                            'GK':['00'],
                                            'GT':['00'],
                                            'ogółem':[20]})

    # testowanie wariancji dochodu gmin w powiecie
    expected_df = pd.DataFrame({'WK':['00'],
                                'PK':['00'],
                                'GK':['00'],
                                'GT':['00'],
                                'srednia ważona':[10*12/20+20*8/20]})

    pd.testing.assert_frame_equal(pit.analiza_danych.srednia_wazona_dochodu_wojewodztw(test_pit_df, test_ludnosc_powiaty_df, test_ludnosc_wojewodztwa_df),expected_df)
    pd.testing.assert_frame_equal(pit.analiza_danych.srednia_wazona_dochodu_wojewodztw(pd.DataFrame(),pd.DataFrame(),pd.DataFrame()),pd.DataFrame())

testy_srednia_wazona_dochodu_wojewodztw()