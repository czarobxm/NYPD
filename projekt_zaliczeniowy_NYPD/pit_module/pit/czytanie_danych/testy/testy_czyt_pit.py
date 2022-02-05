import pandas as pd
import numpy as np
import pytest
import pit
import os


def testy_czyt_pit():
    # sprawdzenie czy działa obsługa nieistniejących plików
    test_df = pit.czyt_pit_gminy('s.xlsx')
    pd.testing.assert_frame_equal(test_df,pd.DataFrame())

    test_df = pit.czyt_pit_powiaty('s.xlsx')
    pd.testing.assert_frame_equal(test_df,pd.DataFrame())

    test_df = pit.czyt_pit_powiaty_miasta_npp('s.xlsx','s.xlsx')
    pd.testing.assert_frame_equal(test_df,pd.DataFrame())

    test_df = pit.czyt_pit_wojewodztwa('s.xlsx')
    pd.testing.assert_frame_equal(test_df,pd.DataFrame())

    # sprawdzenie czy działa obsługa pustych dateframeow
    test_dict = {}
    for i in range(15):
        test_dict[i] = i
    test_df = pd.DataFrame(columns=list(range(15)))
    test_df = test_df.append(test_dict, ignore_index=True)
    test_df.to_excel('test_file.xlsx')

    expected_df = pd.DataFrame(columns=['WK', 'PK', 'GK', 'GT', 'Dochody wykonane'])

    test_df = pit.czyt_pit_gminy('test_file.xlsx')    
    pd.testing.assert_frame_equal(test_df,expected_df)

    test_df = pit.czyt_pit_powiaty('test_file.xlsx')
    pd.testing.assert_frame_equal(test_df,expected_df,check_index_type=False)

    test_df = pit.czyt_pit_powiaty_miasta_npp('test_file.xlsx','test_file.xlsx')
    pd.testing.assert_frame_equal(test_df,expected_df,check_index_type=False)

    test_df = pit.czyt_pit_wojewodztwa('test_file.xlsx')    
    pd.testing.assert_frame_equal(test_df,expected_df)
    os.remove('test_file.xlsx')

