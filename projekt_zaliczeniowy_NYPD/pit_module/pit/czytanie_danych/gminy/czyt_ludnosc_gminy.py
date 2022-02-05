import pandas as pd
import numpy as np
import os
import string

def czyt_ludnosc_gminy(ludnosc_w_gminach_path):
    col_names = ['specyfikacja', 'identyfikator', 'ogółem', 'mężczyźni', 'kobiety', 'miasta']
    # jeśli path istnieje czytamy, jeśli nie zwracamy df
    if os.path.exists(ludnosc_w_gminach_path):
        sheets_dict = pd.read_excel(ludnosc_w_gminach_path, usecols=list(range(3)), names = col_names, skiprows=list(range(7)), sheet_name=None) # wczytywanie pliku excel
    else:
        return pd.DataFrame()
    # wszystkie sheet'sy wrzucamy do jednego dateframe'a
    ludnosc_w_gminach = pd.DataFrame() # do full table zapiszemy wszystkie informacje zawarte w kolejnych sheetsach
    for name, sheet in sheets_dict.items():
        sheet['sheet'] = name
        sheet = sheet.rename(columns=lambda x: x.split('\n')[-1])
        ludnosc_w_gminach = ludnosc_w_gminach.append(sheet)

    ludnosc_w_gminach = ludnosc_w_gminach.reset_index(drop=True)

    # przepisywanie potrzebnych wartości do odpowiednio podpisanych kolumn i wierszy
    col_names = ['identyfikator','wiek produkcyjny','wiek poprodukcyjny', 'ogółem']
    ludnosc_placaca_pit = pd.DataFrame(columns=col_names)

    for i in ludnosc_w_gminach.index:
        # zapisywanie identyfikatora
        try:
            int(ludnosc_w_gminach.loc[i,'identyfikator'])
        except:
            is_id=False
        else:
            is_id = True

        if(is_id):
            id = str(ludnosc_w_gminach.loc[i,'identyfikator'])
        # zapisywanie ludnosci wieku produkcyjnego dla identyfikatora
        if(ludnosc_w_gminach.loc[i,'specyfikacja'] == '   Wiek  produkcyjny          '):
            wiek_produkcyjny = ludnosc_w_gminach.loc[i,'ogółem']
        # zapisywanie ludnosci wieku poprodukcyjnego dla identyfikatora
        if(ludnosc_w_gminach.loc[i,'specyfikacja'] == '   Wiek  poprodukcyjny        '):
            wiek_poprodukcyjny = ludnosc_w_gminach.loc[i,'ogółem']
            ludnosc_placaca_pit = ludnosc_placaca_pit.append(pd.Series([id, wiek_produkcyjny, wiek_poprodukcyjny, wiek_produkcyjny+wiek_poprodukcyjny], index=col_names),ignore_index=True)

    

    # poprawianie identyfikatorów, żeby każdy miał 8 znaków, z czego każde kolejne dwie cyfry odpowiadają za kolejny podział terytorialny
    for i in range(ludnosc_placaca_pit.shape[0]):
        ludnosc_placaca_pit.loc[i, 'identyfikator'] = ludnosc_placaca_pit.loc[i,'identyfikator'][:6] + '0' + ludnosc_placaca_pit.loc[i,'identyfikator'][6:] # dodanie brakującego '0' na przedostatnim miejscu identyfikatora

    # podzielenie identyfikatora na na 4 części 
    WK = []
    PK = []
    GK = []
    GT = []

    for i in range(ludnosc_placaca_pit.shape[0]):
        WK.append(ludnosc_placaca_pit.loc[i, 'identyfikator'][0:2])
        PK.append(ludnosc_placaca_pit.loc[i, 'identyfikator'][2:4])
        GK.append(ludnosc_placaca_pit.loc[i, 'identyfikator'][4:6])
        GT.append(ludnosc_placaca_pit.loc[i, 'identyfikator'][6:8])

    # zamiania jednej kolumny -identyfikator- na 4 bardziej doprecyzowane
    ludnosc_placaca_pit.insert(1,'WK', WK)
    ludnosc_placaca_pit.insert(2,'PK', PK)
    ludnosc_placaca_pit.insert(3,'GK', GK)
    ludnosc_placaca_pit.insert(4,'GT', GT)
    
    # sortowowanie elementow tabeli po rosnacym identyfikatorze
    ludnosc_placaca_pit.sort_values(by=['identyfikator'], inplace=True)

    # usunięcie niepotrzebnych kolumn
    ludnosc_placaca_pit.drop('identyfikator', axis=1, inplace=True)

    # reset indeksów
    ludnosc_placaca_pit.reset_index(inplace=True, drop=True)

    return ludnosc_placaca_pit
