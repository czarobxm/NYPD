import pandas as pd
import numpy as np
import math


def export_to_excel_gminy(path_to_excel, dochod_na_jst_gminy_2019, dochod_na_jst_gminy_2020, ludnosc_w_gminach_2020, sredni_dochod_opodatkowany_gminy):

    gminy = {}
    for wk, pk, gk, gt in ludnosc_w_gminach_2020[['WK','PK','GK','GT']].values:
        gminy[wk+pk+gk+gt] = []
    for wk, pk, gk, gt in dochod_na_jst_gminy_2019[['WK','PK','GK','GT']].values:
        gminy[wk+pk+gk+gt] = []
    for wk, pk, gk, gt in dochod_na_jst_gminy_2020[['WK','PK','GK','GT']].values:
        gminy[wk+pk+gk+gt] = []



    # dodanie dochodu z roku 2019
    for wk,pk,gk,gt, dochody_wykonane in dochod_na_jst_gminy_2019[['WK','PK','GK','GT','Dochody wykonane']].values:
        gminy[wk+pk+gk+gt].append(dochody_wykonane)
    for key in gminy.keys():
        if len(gminy[key]) != 1:
            gminy[key].append(np.nan)

    # dodanie dochodu z roku 2020
    for wk,pk,gk,gt, dochody_wykonane in dochod_na_jst_gminy_2020[['WK','PK','GK','GT','Dochody wykonane']].values:
        gminy[wk+pk+gk+gt].append(dochody_wykonane)
    for key in gminy.keys():
        if len(gminy[key]) != 2:
            gminy[key].append(np.nan)

    # dodanie ludnosci
    for wk,pk,gk,gt, ludnosc_ogolem in ludnosc_w_gminach_2020[['WK','PK','GK','GT','ogółem']].values:
        gminy[wk+pk+gk+gt].append(ludnosc_ogolem)
    for key in gminy.keys():
        if len(gminy[key]) != 3:
            gminy[key].append(np.nan)

    # dodanie średniego dochodu opodatkowanego
    for wk,pk,gk,gt, sredni_dochod in sredni_dochod_opodatkowany_gminy[['WK','PK','GK','GT','średni dochód']].values:
        gminy[wk+pk+gk+gt].append(sredni_dochod)
    for key in gminy.keys():
        if len(gminy[key]) != 4:
            gminy[key].append(np.nan)
            

    gminy_df = pd.DataFrame()

    for key in gminy.keys():
        wk = key[0:2]
        pk = key[2:4]
        gk = key[4:6]
        gt = key[6:8]
        dochod19 = gminy[key][0]
        dochod20 = gminy[key][1]
        ludnosc_ogolem = gminy[key][2]
        sredni_dochod = gminy[key][3]
        gminy_df = gminy_df.append(pd.Series([wk,pk,gk,gt,dochod19,dochod20,ludnosc_ogolem,sredni_dochod]), ignore_index=True)

    gminy_df = gminy_df.sort_values(by=list(range(4)))

    is_NaN = gminy_df.isnull()
    row_has_NaN = is_NaN.any(axis=1)
    rows_with_NaN = gminy_df.loc[row_has_NaN,:]
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
        gminy_df.loc[i,:] = rows_with_NaN.loc[i,:]

    gminy_df = gminy_df.sort_values(by=list(range(4)))

    # zmiana nazwy kolumn i usunięcie wierszy z przedawionymi identyfikatorami
    gminy_df = gminy_df.rename(columns={0:'WK',1:'PK',2:'GK',3:'GT',4:'Dochody wykonane 19',5:'Dochody wykonane 20',6:'ludnosc ogółem',7:'średni dochod opodatkowany'})

    gminy_df = gminy_df.dropna(subset=['ludnosc ogółem'], axis=0)

    indices_to_drop = []
    for i in gminy_df.index:
        if math.isnan(gminy_df.loc[i,'Dochody wykonane 20']) and math.isnan(gminy_df.loc[i,'średni dochod opodatkowany']) and not math.isnan(gminy_df.loc[i,'Dochody wykonane 19']):
            indices_to_drop.append(i)
        
    gminy_df = gminy_df.drop(indices_to_drop)

    # wrzucenie dateframea do excela
    gminy_df.to_excel(path_to_excel, index=False)
