import string

# creating diciotnaries - lowercases, uppercases and numbers
d = dict.fromkeys(string.ascii_lowercase, 0)
D = dict.fromkeys(string.ascii_uppercase, 0)
n = {
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----."
}

signs = [".-",
         "-...",
         "-.-.",
         "-..",
         ".",
         "..-.",
         "--.",
         "....",
         "..",
         ".---",
         "-.-",
         ".-..",
         "--",
         "-.",
         "---",
         ".--.",
         "--.-",
         ".-.",
         "...",
         "-",
         "..-",
         "...-",
         ".--",
         "-..-",
         "-.--",
         "--.."]

pl = {}
polish_letters = "ąćęłńóśżź"
polish_signs = [".-.-",
                "-.-..",
                "..-..",
                ".-..-",
                "--.--",
                "---.",
                "...-...",
                "--..-.",
                "--..-"]

# assigning values to keys
for key in list(d):
    d[key] = signs[list(d).index(key)]

for key in list(D):
    D[key] = signs[list(D).index(key)]

for key in list(polish_letters):
    pl[key] = list(polish_signs)[list(polish_letters).index(key)]

# combinig three dictionaries
morseWrite = dict(d,**D)
morseWrite = dict(morseWrite,**n)
morseWrite = dict(morseWrite, **pl)

# adding space as "/"
morseWrite[" "] = "/"




# making dicitonary for reading morse code
morseRead={}
for elem in signs:
    morseRead[elem]= string.ascii_lowercase[signs.index(elem)]

for elem in polish_signs:
    morseRead[elem]= polish_letters[polish_signs.index(elem)]

# adding space " " to dictionary as ""
morseRead[''] = " "

#print(morseWrite)
#print(morseRead)

"""
NOW WE HAVE OUR DICTIONARY READY TO READ AND WRITE MORSE CODE
"""

def listToString(list):
    s = "" 
    return (s.join(list))

def morse(sentence):
    # checking if we have to read or write morse code
    if sentence[0] == '-' or sentence[0] == '.' or sentence[0] == '/': # we have to read morse code

        translation = []
        words = sentence.split("/")

        for elem in words:
            translation.append(morseRead[elem])

        return listToString(translation)

        
    else: # we have to write morse code
        translation = []
        
        for elem in sentence:
            translation.append(morseWrite[elem])
            if elem != ' ':
                translation.append("/")

        return listToString(translation)



print(morse("Ala ma kota"))
print(morse(".-/.-../.-//--/.-//-.-/---/-/.-"))
print(morse("--../.-/--..-./---./.-..-/-.-..//--./..-../...-.../.-../.-.-//.---/.-/--..-/--.--"))
print(morse( "Zażółć gęślą jaźń"))