import pandas as pd
from statistics import variance


def wariancja_dochodu_gmin_w_powiecie(dane_pit_gminy):
    if 'Dochody wykonane' not in dane_pit_gminy.columns:
        return pd.DataFrame()
    if 'WK' not in dane_pit_gminy.columns:
        return pd.DataFrame()
    if 'PK' not in dane_pit_gminy.columns:
        return pd.DataFrame()
    dochod_gmin_w_powiecie = {}
    col_name = ['WK','PK','GK','GT', 'wariancja dochodu podległych jednostek']
    wariancja_dochodu_gmin_w_powiecie_df = pd.DataFrame(columns=col_name)

    for wk, pk, dochod in list(dane_pit_gminy[['WK', 'PK', 'Dochody wykonane']].values):
        if wk+pk not in dochod_gmin_w_powiecie:
            dochod_gmin_w_powiecie[wk+pk] = [dochod]
        if wk+pk in dochod_gmin_w_powiecie:
            dochod_gmin_w_powiecie[wk+pk].append(dochod)
    
    for wkpk in list(dochod_gmin_w_powiecie.keys()):
        wariancja = variance(dochod_gmin_w_powiecie[wkpk])
        wariancja_dochodu_gmin_w_powiecie_df = wariancja_dochodu_gmin_w_powiecie_df.append(pd.Series([wkpk[0:2], wkpk[2:4],'00','00',wariancja], index=col_name),ignore_index=True)
    
    return wariancja_dochodu_gmin_w_powiecie_df