import pandas as pd
import numpy as np
import math

#obliczanie różnicy między poszególnymi jst między latami 2019 i 2020

def obliczanie_roznicy_pit(dochod_na_jst_z_19, dochod_na_jst_z_20):
    # trzeba uzgodnić kody terytorialne dla lat 19,20
    gminy = {}
    for wk, pk, gk, gt in dochod_na_jst_z_19[['WK','PK','GK','GT']].values:
        gminy[wk+pk+gk+gt] = []
    for wk, pk, gk, gt in dochod_na_jst_z_20[['WK','PK','GK','GT']].values:
        gminy[wk+pk+gk+gt] = []

    # dodanie dochodu z roku 2019
    for wk,pk,gk,gt, dochody_wykonane in dochod_na_jst_z_19[['WK','PK','GK','GT','Dochody wykonane']].values:
        gminy[wk+pk+gk+gt].append(dochody_wykonane)
    for key in gminy.keys():
        if len(gminy[key]) != 1:
            gminy[key].append(np.nan)

    # dodanie dochodu z roku 2020
    for wk,pk,gk,gt, dochody_wykonane in dochod_na_jst_z_20[['WK','PK','GK','GT','Dochody wykonane']].values:
        gminy[wk+pk+gk+gt].append(dochody_wykonane)
    for key in gminy.keys():
        if len(gminy[key]) != 2:
            gminy[key].append(np.nan)

    # dane pobrane z tabeli wrzucamy do pandas.DateFrame
    gminy_df = pd.DataFrame()

    for key in gminy.keys():
        wk = key[0:2]
        pk = key[2:4]
        gk = key[4:6]
        gt = key[6:8]
        dochod19 = gminy[key][0]
        dochod20 = gminy[key][1]
        gminy_df = gminy_df.append(pd.Series([wk,pk,gk,gt,dochod19,dochod20]), ignore_index=True)

    gminy_df = gminy_df.sort_values(by=list(range(4)))

    # uzgadnianie kodów terytorialnych
    is_NaN = gminy_df.isnull()
    row_has_NaN = is_NaN.any(axis=1)
    rows_with_NaN = gminy_df[row_has_NaN]
    indices = rows_with_NaN.index
    for k, i in enumerate(indices):
        #jeśli kolumna dochody19 != nan, a kolumna dochody20 == nan wtedy merge dwa wiersze
        if not math.isnan(rows_with_NaN.loc[i,4]) and math.isnan(rows_with_NaN.loc[i,5]):
            if math.isnan(rows_with_NaN.loc[indices[k+1],4]) and not math.isnan(rows_with_NaN.loc[indices[k+1],5]):
                rows_with_NaN.loc[indices[k+1],4] = rows_with_NaN.loc[i,4]
                rows_with_NaN.loc[i,4] = np.NaN

        #jeśli kolumna dochody19 == nan, a kolumna dochody20 != nan wtedy merge dwa wiersze
        if math.isnan(rows_with_NaN.loc[i,4]) and not math.isnan(rows_with_NaN.loc[i,5]):
            if not math.isnan(rows_with_NaN.loc[indices[k+1],4]):
                rows_with_NaN.loc[i,4] = rows_with_NaN.loc[indices[k+1],4]
                rows_with_NaN.loc[indices[k+1],4] = np.NaN

        # jeśli obie kolumny nan usuwamy wiersz
        if math.isnan(rows_with_NaN.loc[i,4]) and math.isnan(rows_with_NaN.loc[i,5]):
            rows_with_NaN = rows_with_NaN.drop(i,axis=0)
        
    # zamiana kodów i uporządkowanie indeksów
    for i in rows_with_NaN.index:
        gminy_df.loc[i,:] = rows_with_NaN.loc[i,:]
    gminy_df = gminy_df.dropna(subset=[5])
    gminy_df = gminy_df.reset_index(drop=True)


    col_name = ['WK','PK','GK','GT','różnica dochodu z pit między 2019 a 2020']
    roznica_dochodu_z_pit_20_19 = pd.DataFrame(columns=col_name)
    for i, [wk,pk,gk,gt] in enumerate(gminy_df[list(range(4))].values):
        roznica = gminy_df.loc[i,5] - gminy_df.loc[i,4]
        roznica_dochodu_z_pit_20_19 = roznica_dochodu_z_pit_20_19.append(pd.Series([wk, pk, gk, gt, roznica], index=col_name), ignore_index=True)
    return roznica_dochodu_z_pit_20_19