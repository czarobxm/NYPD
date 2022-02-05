import pandas as pd
from statistics import variance


def wariancja_dochodu_powiatow_w_wojewodztwie(dane_pit_powiaty):
    if 'Dochody wykonane' not in dane_pit_powiaty.columns:
        return pd.DataFrame()
    if 'WK' not in dane_pit_powiaty.columns:
        return pd.DataFrame()
    dochod_powiatow_w_wojewodztwach = {}
    for wk, dochod in list(dane_pit_powiaty[['WK', 'Dochody wykonane']].values):
        if wk not in dochod_powiatow_w_wojewodztwach:
            dochod_powiatow_w_wojewodztwach[wk] = [dochod]
        if wk in dochod_powiatow_w_wojewodztwach:
            dochod_powiatow_w_wojewodztwach[wk].append(dochod)

    col_name = ['WK','PK','GK','GT', 'wariancja dochodu podległych jednostek']
    wariancja_dochodu_powiatow_w_wojewodztwie_df = pd.DataFrame(columns=col_name)

    for wk in list(dochod_powiatow_w_wojewodztwach.keys()):
        wariancja = variance(dochod_powiatow_w_wojewodztwach[wk])
        wariancja_dochodu_powiatow_w_wojewodztwie_df = wariancja_dochodu_powiatow_w_wojewodztwie_df.append(pd.Series([wk,'00','00','00',wariancja], index=col_name),ignore_index=True)
    
    return wariancja_dochodu_powiatow_w_wojewodztwie_df