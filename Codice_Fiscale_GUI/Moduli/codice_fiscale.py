import Moduli.codice_comune as c_c

class anno():
    def __init__(self,anno,mese,giorno):
        self.anno = anno
        self.mese = mese
        self.giorno = giorno
        return
    
def controllo_lettera_pari(lettera): 
    numeri={"0": 0,"1": 1, "2": 2, "3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9 ,
            "A": 0,"B": 1, "C": 2, "D": 3,"E": 4,"F": 5,"G": 6,"H": 7,"I": 8,"J": 9 ,
            "K":10,"L": 11,"M": 12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T" :19,
            "U":20,"V": 21,"W": 22,"X":23,"Y":24,"Z": 25
           }
    return numeri[lettera]

def controllo_lettera_disp(lettera):
    num={ 
        "0": 1, "1": 0, "2": 5, "3": 7, "4": 9, "5": 13, "6": 15, "7": 17, "8": 19, "9": 21,
        "A": 1, "B": 0, "C": 5, "D": 7, "E": 9, "F": 13, "G": 15, "H": 17, "I": 19, "J": 21,
        "K": 2, "L": 4, "M": 18,"N":20, "O":11, "P": 3 , "Q": 6 , "R": 8 , "S": 12, "T": 14,
        "U":16, "V": 10,"W": 22,"X":25, "Y":24, "Z":23
        }   
    return num[lettera]

def lettera_controllo(codice):
    c = 0
    l = ""
    for i in range(0,len(codice),2):
        x = codice[i]
        c += controllo_lettera_disp(x)
    for j in range(1,len(codice)-1,2):
        x = codice[j]
        c += controllo_lettera_pari(x)
    c %= 26
    lettere = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return lettere[c]

def anno_nascita(data,sesso):
    nascita = f"{str(data.anno)[2:]}"
    if sesso == "F":
        data.giorno += 40   
    data.mese -= 1
    lettere = "ABCDEHLMPRST"
    nascita += lettere[data.mese]
    if data.giorno >= 10:
        nascita += f"{data.giorno}"
    else:
        nascita += f"0{data.giorno}"
    return nascita

def nome_cognome(nome,cognome):
    vocali = "AEIOU"
    cons_n = ""
    voc_n = ""
    cons_c = ""
    voc_c = ""
    for i in nome:
        if i not in vocali:
            cons_n += i
        else:
            voc_n += i
    for i in cognome:
        if i not in vocali:
            cons_c += i
        else:
            voc_c += i
    nc = ""
    if len(cons_c) >= 3:
        for i in range(3):
            nc += cons_c[i]
    else:
        for i in range(len(cons_c)):
            nc += cons_c[i]
        for i in range(len(voc_c)):
            if len(nc) < 3:
                nc += voc_c[i]
        if len(nc) < 3:
            while len(nc) < 3:
                nc += "X"
    if len(cons_n) >= 4:
        nc += cons_n[0] +cons_n[2] + cons_n[3]
    else:
        for i in range(len(cons_n)):
            nc += cons_n[i]
        for i in range(len(voc_n)):
            if len(nc) < 6:
                nc += voc_n[i]
        if len(nc) < 6:
            while (len(nc)) < 6:
                nc += "X"
    return nc

def creacodice(nome,cognome,nascita,sesso,comune):
    codice = ""
    nascita = anno(nascita[0],nascita[1],nascita[2])
    err = c_c.trova_codice(comune)
    if err != -1:
        codice+=nome_cognome(nome,cognome) + anno_nascita(nascita,sesso) + err
        codice += lettera_controllo(codice)
        return codice
    else: return -1
