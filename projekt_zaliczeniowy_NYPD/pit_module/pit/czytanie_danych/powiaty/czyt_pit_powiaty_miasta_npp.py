import pandas as pd
import os
from ..CONST import *

def czyt_pit_powiaty_miasta_npp(dane_pit_powiaty_path, dane_pit_miasta_npp_path):
    # funkcja przyjmująca jako argument ścieżkę do danych z portalu gov.pl zawierających udziały w pit
    if os.path.exists(dane_pit_powiaty_path):
        pit_powiat = pd.read_excel(dane_pit_powiaty_path, usecols=[0,1,2,3,8,11], skiprows=list(range(6)), names = col_names_powiaty, engine = 'openpyxl')
    if os.path.exists(dane_pit_miasta_npp_path):
        pit_miasta_npp = pd.read_excel(dane_pit_miasta_npp_path, usecols=[0,1,2,3,8,11], skiprows=list(range(6)), names = col_names_powiaty, engine = 'openpyxl')
    else:
        return pd.DataFrame()
    
    pit_powiat_miasta_npp = pd.concat([pit_powiat, pit_miasta_npp])
    pit_powiat_miasta_npp.reset_index(drop=True, inplace=True)


    # zmiana identyfikatorów z typu int na string i wstawianie 0 na początek jeśli to potrzebne
    for column in ['WK', 'PK', 'GK', 'GT']:
        for i in range(pit_powiat_miasta_npp.shape[0]):
            pit_powiat_miasta_npp.loc[:, column] = pit_powiat_miasta_npp.loc[:, column].astype('str')
            if pit_powiat_miasta_npp.loc[i, column] == '-':
                pit_powiat_miasta_npp.loc[i, column] = '00'
            if len(pit_powiat_miasta_npp.loc[i, column]) == 1:
                pit_powiat_miasta_npp.loc[i, column] = '0' + pit_powiat_miasta_npp.loc[i, column]
                pass
            pass

    # usunięcie wierszy, w których rozdział !=75621 (sprawdza się dla miast_npp)
    pit_powiat_miasta_npp.drop_duplicates(subset=['WK','PK'], inplace=True)

    # usunięcie kolumny rozdział
    pit_powiat_miasta_npp.drop('Rozdział', axis=1, inplace=True)

    # sortowanie po identyfikatorze powiatu
    pit_powiat_miasta_npp.sort_values(by=['WK','PK'], inplace=True)
    # reset indeksów 
    pit_powiat_miasta_npp.reset_index(drop=True, inplace=True)
    return pit_powiat_miasta_npp

