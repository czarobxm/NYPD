import pandas as pd
import numpy as np
import math


def export_to_excel_powiaty(path_to_excel, dochod_na_jst_2019, dochod_na_jst_2020, ludnosc_w_jst_2020, sredni_dochod_opodatkowany_20, wariancja_dochodu, srednia_wazona):

    powiaty = {}
    for wk, pk, gk, gt in ludnosc_w_jst_2020[['WK','PK','GK','GT']].values:
        powiaty[wk+pk] = []
    for wk, pk, gk, gt in dochod_na_jst_2019[['WK','PK','GK','GT']].values:
        powiaty[wk+pk] = []
    for wk, pk, gk, gt in dochod_na_jst_2020[['WK','PK','GK','GT']].values:
        powiaty[wk+pk] = []



    # dodanie dochodu z roku 2019
    for wk,pk,gk,gt, dochody_wykonane in dochod_na_jst_2019[['WK','PK','GK','GT','Dochody wykonane']].values:
        powiaty[wk+pk].append(dochody_wykonane)
    for key in powiaty.keys():
        if len(powiaty[key]) != 1:
            powiaty[key].append(np.nan)

    # dodanie dochodu z roku 2020
    for wk,pk,gk,gt, dochody_wykonane in dochod_na_jst_2020[['WK','PK','GK','GT','Dochody wykonane']].values:
        powiaty[wk+pk].append(dochody_wykonane)
    for key in powiaty.keys():
        if len(powiaty[key]) != 2:
            powiaty[key].append(np.nan)

    # dodanie ludnosci
    for wk,pk,gk,gt, ludnosc_ogolem in ludnosc_w_jst_2020[['WK','PK','GK','GT','ogółem']].values:
        powiaty[wk+pk].append(ludnosc_ogolem)
    for key in powiaty.keys():
        if len(powiaty[key]) != 3:
            powiaty[key].append(np.nan)

    # dodanie średniego dochodu opodatkowanego
    for wk,pk,gk,gt, sredni_dochod in sredni_dochod_opodatkowany_20[['WK','PK','GK','GT','średni dochód']].values:
        powiaty[wk+pk].append(sredni_dochod)
    for key in powiaty.keys():
        if len(powiaty[key]) != 4:
            powiaty[key].append(np.nan)

    # dodanie wariancji
    for wk,pk,gk,gt, wariancja in wariancja_dochodu[['WK','PK','GK','GT','wariancja dochodu podległych jednostek']].values:
        powiaty[wk+pk].append(wariancja)
    for key in powiaty.keys():
        if len(powiaty[key]) != 5:
            powiaty[key].append(np.nan)

    # dodanie sredniej wazonej
    for wk,pk,gk,gt, wazona in srednia_wazona[['WK','PK','GK','GT','srednia ważona']].values:
        powiaty[wk+pk].append(wazona)
    for key in powiaty.keys():
        if len(powiaty[key]) != 6:
            powiaty[key].append(np.nan)
            

    powiaty_df = pd.DataFrame()

    for key in powiaty.keys():
        wk = key[0:2]
        pk = key[2:4]
        gk = '00'
        gt = '00'
        dochod19 = powiaty[key][0]
        dochod20 = powiaty[key][1]
        ludnosc_ogolem = powiaty[key][2]
        sredni_dochod = powiaty[key][3]
        wariancja = powiaty[key][4]
        wazona = powiaty[key][5]

        powiaty_df = powiaty_df.append(pd.Series([wk,pk,gk,gt,dochod19,dochod20,ludnosc_ogolem,sredni_dochod, wariancja, wazona]), ignore_index=True)

    powiaty_df = powiaty_df.sort_values(by=list(range(4)))

    is_NaN = powiaty_df.isnull()
    row_has_NaN = is_NaN.any(axis=1)
    rows_with_NaN = powiaty_df.loc[row_has_NaN,:]
    indices = rows_with_NaN.index
    
    for k, i in enumerate(indices):
        #jeśli kolumna dochody19 != nan, a kolumna dochody20 == nan wtedy merge dwa wiersze
        if not math.isnan(rows_with_NaN.loc[i,4]) and math.isnan(rows_with_NaN.loc[i,5]):
            if math.isnan(rows_with_NaN.loc[indices[k+1],4]) and not math.isnan(rows_with_NaN.loc[indices[k+1],5]):
                rows_with_NaN.loc[indices[k+1],4] = rows_with_NaN.loc[i,4]
                if not math.isnan(rows_with_NaN.loc[i,6]): rows_with_NaN.loc[indices[k+1],6] = rows_with_NaN.loc[i,6]
                rows_with_NaN.at[i, 4] = np.NaN
                pass
            
         
        #jeśli kolumna dochody19 == nan, a kolumna dochody20 != nan wtedy merge dwa wiersze
        if math.isnan(rows_with_NaN.loc[i,4]) and not math.isnan(rows_with_NaN.loc[i,5]):
            if not math.isnan(rows_with_NaN.loc[indices[k+1],4]):
                rows_with_NaN.loc[i,4] = rows_with_NaN.loc[indices[k+1],4]
                rows_with_NaN.loc[indices[k+1],4] = np.NaN
            
        
        # jeśli obie kolumny nan usuwamy wiersz
        if math.isnan(rows_with_NaN.loc[i,4]) and math.isnan(rows_with_NaN.loc[i,5]):
            rows_with_NaN = rows_with_NaN.drop(i,axis=0)
        
        

    for i in rows_with_NaN.index:
        powiaty_df.loc[i,:] = rows_with_NaN.loc[i,:]

    powiaty_df = powiaty_df.sort_values(by=list(range(4)))

    powiaty_df = powiaty_df.rename(columns={0:'WK',1:'PK',2:'GK',3:'GT',4:'Dochody wykonane 19',5:'Dochody wykonane 20',6:'ludnosc ogółem',7:'średni dochod opodatkowany',8:'wariancja dochodu podległych jednostek', 9:'srednia wazona'})
    powiaty_df.to_excel(path_to_excel)
