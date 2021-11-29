## program szyfrujący/deszyfrujący teksty szygrami podstawieniowymi
## takimi jak GA-DE-RY-PO-LU-KI

def szyfruj(tekst, rodzaj_szyfru):
    # tworzymy słownik dwukierunkowy do szyfrowania/odszyfrowywania
    dict = {}

    for i in range(len(rodzaj_szyfru)):
        
        if i % 2 == 1: # to znaczy i nieparzyste
            dict[rodzaj_szyfru[i].upper()] = rodzaj_szyfru[i-1].upper()
            dict[rodzaj_szyfru[i].lower()] = rodzaj_szyfru[i-1].lower()
        else:
            dict[rodzaj_szyfru[i].upper()] = rodzaj_szyfru[i+1].upper()
            dict[rodzaj_szyfru[i].lower()] = rodzaj_szyfru[i+1].lower()

    # szyfrowanie
    tekst_list = list(tekst)

    for i in range(len(tekst)):
        if tekst_list[i] in dict:
            tekst_list[i] = dict[tekst_list[i]]
        else:
            pass

    tekst = "".join(tekst_list)
    return tekst
        
print("szyfrowanie za pomocą gaderypoluki")
a = szyfruj("Ola ma kota", "gaderypoluki")
print(a)

print("szyfrowanie za pomocą politykarenu")
a = szyfruj("Ola ma kota", "politykarenu")
print(a)


print("szyfrowanie za pomocą koniecmatury")
a = szyfruj("Ola ma kota", "koniecmatury")
print(a)


print("sprawdzenie czy polecenie szyfruj(szyfruj(tekst) zwróci tekst, gdzie tekst = Ola ma kota")
a = szyfruj(szyfruj("Ola ma kota", "koniecmatury"), "koniecmatury")
print(a)


