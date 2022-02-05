import pandas as pd
from statistics import mean
from .CONST import *

# trzeba policzyć dochod w gminie*(ludnosc w gminie/ludnosc w powiecie)

def srednia_wazona_dochodu_powiatow(dane_pit_gminy, dane_ludnosc_gminy, dane_ludnosc_powiaty):
    if 'Dochody wykonane' not in dane_pit_gminy.columns:
        return pd.DataFrame()
    if 'ogółem' not in dane_ludnosc_gminy.columns or 'ogółem' not in dane_ludnosc_powiaty.columns:
        return pd.DataFrame()
    if 'WK' not in dane_pit_gminy.columns or 'WK' not in dane_ludnosc_gminy.columns or 'WK' not in dane_ludnosc_powiaty.columns:
        return pd.DataFrame()
    if 'PK' not in dane_pit_gminy.columns or 'PK' not in dane_ludnosc_gminy.columns or 'PK' not in dane_ludnosc_powiaty.columns:
        return pd.DataFrame()
    if 'GK' not in dane_pit_gminy.columns or 'GK' not in dane_ludnosc_gminy.columns or 'GK' not in dane_ludnosc_powiaty.columns:
        return pd.DataFrame()
    if 'GT' not in dane_pit_gminy.columns or 'GT' not in dane_ludnosc_gminy.columns or 'GT' not in dane_ludnosc_powiaty.columns:
        return pd.DataFrame()

    col_name = ['WK','PK','GK','GT', 'srednia ważona']
    srednia_wazona_df = pd.DataFrame(columns=col_name)

    # zapis ludnosci dla poszczególnych powiatów i stworzenie miejsca gdize bedziemy trzymac wartosci srednich wazonych
    ludnosc_w_powiatach = {}
    
    for i, [wk, pk, ludnosc] in enumerate(dane_ludnosc_powiaty[['WK','PK','ogółem']].values):
        ludnosc_w_powiatach[wk+pk] = ludnosc
        

    # zapis ludnosci dla poszegolnych powiatow z podziałem na gminy
    ludnosc_w_gminach = {}
    for wk,pk,gk,gt, ludnosc in dane_ludnosc_gminy[['WK','PK','GK','GT','ogółem']].values:
        ludnosc_w_gminach[wk+pk+gk+gt] = ludnosc

    # zapis dochodow dla poszczegolnych powiatow z podziałem na gminy
    dochody_w_gminach = {}
    srednia_wazona = {}
    for wk,pk,gk,gt, dochody in dane_pit_gminy[['WK','PK','GK','GT','Dochody wykonane']].values:
        dochody_w_gminach[wk+pk+gk+gt] = dochody
        srednia_wazona[wk+pk] = []

    for gmina in dochody_w_gminach.keys():
        powiat = gmina[0:4]

        try:
            srednia_wazona[powiat].append(( dochody_w_gminach[gmina]) * (ludnosc_w_gminach[gmina]) / (ludnosc_w_powiatach[powiat]))
        except:
            print(f"nie ma gminy o identyfikatorze {gmina} w spisie ludnosci gmin/powiatów pomimo, że jest w spisie dochodu z pit gmin")


    for key in srednia_wazona.keys():
        try:
            srednia_wazona[key] = sum(srednia_wazona[key])
        except:
            print(f"W powiecie {key} nie ma gmin")

    

    for wkpk in list(srednia_wazona.keys()):
        srednia_wazona_df = srednia_wazona_df.append(pd.Series([wkpk[0:2], wkpk[2:4],'00','00',srednia_wazona[wkpk]], index=col_name),ignore_index=True)
    


    




    return srednia_wazona_df
    
    #return dochod_gmin_w_powiecie