import pandas as pd
import string
import os
from ..CONST import *

def czyt_pit_gminy(data_rodzaj_struktury_rok_path):
    # funkcja przyjmująca jako argument ścieżkę do danych z portalu gov.pl zawierających udziały w pit
    # jeśli path istnieje czytamy, jeśli nie zwracamy df
    if os.path.exists(data_rodzaj_struktury_rok_path):
        pit_rodzaj_struktury_rok = pd.read_excel(data_rodzaj_struktury_rok_path, usecols=[0,1,2,3,11], skiprows=list(range(6)), names = col_names_gminy, engine = 'openpyxl')
    else:
        return pd.DataFrame()
    # zmiana identyfikatorów z typu int na string i wstawianie 0 na początek jeśli to potrzebne
    for column in ['WK', 'PK', 'GK', 'GT']:
        for i in range(pit_rodzaj_struktury_rok.shape[0]):
            pit_rodzaj_struktury_rok.loc[:, column] = pit_rodzaj_struktury_rok[column].astype('str')
            if len(pit_rodzaj_struktury_rok.loc[i, column]) == 1:
                pit_rodzaj_struktury_rok.loc[i, column] = '0' + pit_rodzaj_struktury_rok.loc[i, column]
                pass
            pass

    return pit_rodzaj_struktury_rok

