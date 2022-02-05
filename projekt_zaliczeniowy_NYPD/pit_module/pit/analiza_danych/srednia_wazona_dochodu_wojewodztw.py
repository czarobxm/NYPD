import pandas as pd
from statistics import mean
from .CONST import *

# trzeba policzyć dochod w gminie*(ludnosc w gminie/ludnosc w powiecie)

def srednia_wazona_dochodu_wojewodztw(dane_pit_powiaty, dane_ludnosc_gminy, dane_ludnosc_wojewodztwa):
    if 'Dochody wykonane' not in dane_pit_powiaty.columns:
        return pd.DataFrame()
    if 'ogółem' not in dane_ludnosc_gminy.columns or 'ogółem' not in dane_ludnosc_wojewodztwa.columns:
        return pd.DataFrame()
    if 'WK' not in dane_pit_powiaty.columns or 'WK' not in dane_ludnosc_gminy.columns or 'WK' not in dane_ludnosc_wojewodztwa.columns:
        return pd.DataFrame()
    if 'PK' not in dane_pit_powiaty.columns or 'PK' not in dane_ludnosc_gminy.columns or 'PK' not in dane_ludnosc_wojewodztwa.columns:
        return pd.DataFrame()
    if 'GK' not in dane_pit_powiaty.columns or 'GK' not in dane_ludnosc_gminy.columns or 'GK' not in dane_ludnosc_wojewodztwa.columns:
        return pd.DataFrame()
    if 'GT' not in dane_pit_powiaty.columns or 'GT' not in dane_ludnosc_gminy.columns or 'GT' not in dane_ludnosc_wojewodztwa.columns:
        return pd.DataFrame()
    col_name = ['WK','PK','GK','GT', 'srednia ważona']
    srednia_wazona_df = pd.DataFrame(columns=col_name)

    # zapis ludnosci dla poszczególnych wojewodztw i stworzenie miejsca gdzie bedziemy trzymac wartosci srednich wazonych
    ludnosc_w_wojewodztwach = {}
    for i, [wk, ludnosc] in enumerate(dane_ludnosc_wojewodztwa[['WK','ogółem']].values):
        ludnosc_w_wojewodztwach[wk] = ludnosc

    # zapis ludnosci dla poszegolnych wojewodztw z podziałem na powiaty
    ludnosc_w_powiatach = {}
    for wk,pk, ludnosc in dane_ludnosc_gminy[['WK','PK', 'ogółem']].values:
        ludnosc_w_powiatach[wk+pk] = ludnosc

    # zapis dochodow dla poszczegolnych wojewodztw z podziałem na powiaty
    dochody_w_powiatach = {}
    srednia_wazona = {}
    for wk,pk, dochody in dane_pit_powiaty[['WK','PK','Dochody wykonane']].values:
        dochody_w_powiatach[wk+pk] = dochody
        srednia_wazona[wk] = []

    for powiat in dochody_w_powiatach.keys():
        wojewodztwo = powiat[0:2]

        try:
            srednia_wazona[wojewodztwo].append((dochody_w_powiatach[powiat]) * ( ludnosc_w_powiatach[powiat]) / (ludnosc_w_wojewodztwach[wojewodztwo]))
        except:
            print(f"nie ma powiatu o identyfikatorze {powiat} w spisie ludnosci powiatów pomimo, że jest w spisie dochodu z pit powiatów")

    for key in srednia_wazona.keys():
        try:
            srednia_wazona[key] = sum(srednia_wazona[key])
        except:
            print(f"W wojewodztwie {key} nie ma powiatów")

    

    for wkpk in list(srednia_wazona.keys()):
        srednia_wazona_df = srednia_wazona_df.append(pd.Series([wkpk[0:2], '00','00','00',srednia_wazona[wkpk]], index=col_name),ignore_index=True)
    


    




    return srednia_wazona_df
    
    #return dochod_gmin_w_powiecie