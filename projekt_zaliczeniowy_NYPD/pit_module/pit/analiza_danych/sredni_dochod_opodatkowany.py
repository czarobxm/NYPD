# trzeba podzielić dochód na gminę, przez liczbę mieszkańców gminy

from turtle import pd
import pandas as pd
from .CONST import procent_pracujacych

def sredni_dochod_opodatkowany(dane_pit, dane_ludnosc):
    if 'Dochody wykonane' not in dane_pit.columns:
        return pd.DataFrame()
    if 'ogółem' not in dane_ludnosc.columns:
        return pd.DataFrame()
    if 'WK' not in dane_pit.columns or 'WK' not in dane_ludnosc.columns:
        return pd.DataFrame()
    if 'PK' not in dane_pit.columns or 'PK' not in dane_ludnosc.columns:
        return pd.DataFrame()
    if 'GK' not in dane_pit.columns or 'GK' not in dane_ludnosc.columns:
        return pd.DataFrame()
    if 'GT' not in dane_pit.columns or 'GT' not in dane_ludnosc.columns:
        return pd.DataFrame()

    # policz średni dochód opodatkowany
    if(dane_pit.shape[0] != dane_ludnosc.shape[0]):
        print("nie wszystkie jednostki będą opisane w zestawieniu-w którymś z plików jest inna liczba jst")
    
    col_name = ['WK','PK','GK','GT', 'średni dochód']
    sredni_dochod = pd.DataFrame(columns=col_name)

    for i, [wk,pk,gk,gt] in enumerate(dane_pit[['WK','PK','GK','GT']].values):
        if list(dane_pit.loc[i, ['WK','PK','GK','GT']]) == [wk, pk, gk ,gt]:
            wartosc_sredniego_dochodu = (dane_pit.loc[i, 'Dochody wykonane']) / (procent_pracujacych * dane_ludnosc.loc[i,'ogółem'])
            sredni_dochod = sredni_dochod.append(pd.Series([wk,pk,gk,gt, wartosc_sredniego_dochodu ], index=col_name), ignore_index=True)
        pass
    
    return sredni_dochod