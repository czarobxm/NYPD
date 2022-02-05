import pandas as pd
import os
from ..CONST import *

def czyt_pit_powiaty(data_rodzaj_struktury_rok_path):
    # funkcja przyjmująca jako argument ścieżkę do danych z portalu gov.pl zawierających udziały w pit
    if os.path.exists(data_rodzaj_struktury_rok_path):
        pit_rodzaj_struktury_rok = pd.read_excel(data_rodzaj_struktury_rok_path, usecols=[0,1,2,3,8,11], skiprows=list(range(6)), names = col_names_powiaty, engine = 'openpyxl')
    else:
        return pd.DataFrame()
    
    # zmiana identyfikatorów z typu int na string i wstawianie 0 na początek jeśli to potrzebne
    for column in ['WK', 'PK', 'GK', 'GT']:
        for i in range(pit_rodzaj_struktury_rok.shape[0]):
            pit_rodzaj_struktury_rok.loc[:, column] = pit_rodzaj_struktury_rok.loc[:, column].astype('str')
            if pit_rodzaj_struktury_rok.loc[i, column] == '-':
                pit_rodzaj_struktury_rok.loc[i, column] = '00'
            if len(pit_rodzaj_struktury_rok.loc[i, column]) == 1:
                pit_rodzaj_struktury_rok.loc[i, column] = '0' + pit_rodzaj_struktury_rok.loc[i, column]
                pass
            pass

    # usunięcie wierszy, w których rozdział !=75621 (sprawdza się dla miast_npp)
    pit_rodzaj_struktury_rok = pit_rodzaj_struktury_rok.drop_duplicates(subset=['WK','PK'])

    # usunięcie kolumny rozdział
    pit_rodzaj_struktury_rok.drop('Rozdział', axis=1, inplace=True)

    # reset indeksów 
    pit_rodzaj_struktury_rok.reset_index(drop=True, inplace=True)
    return pit_rodzaj_struktury_rok

