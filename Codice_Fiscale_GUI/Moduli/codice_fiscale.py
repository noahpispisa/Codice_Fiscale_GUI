class anno():
    def __init__(self,anno,mese,giorno):
        self.anno = anno
        self.mese = mese
        self.giorno = giorno
        return
    
def controllo_lettera_pari(lettera): 
    if (lettera == "A") or (lettera == "0"):
        return 0
    elif (lettera == "B") or (lettera == "1"):
        return 1
    elif (lettera == "C") or (lettera == "2"):
        return 2
    elif (lettera == "D") or (lettera == "3"):
        return 3
    elif (lettera == "E") or (lettera == "4"):
        return 4
    elif (lettera == "F") or (lettera == "5"):
        return 5
    elif (lettera == "G") or (lettera == "6"):
        return 6
    elif (lettera == "H") or (lettera == "7"):
        return 7
    elif (lettera == "I") or (lettera == "8"):
        return 8
    elif (lettera == "J") or (lettera == "9"):
        return 9
    elif (lettera == "K"):
        return 10
    elif (lettera == "L"):
        return 11
    elif (lettera == "M"):
        return 12
    elif (lettera == "N"):
        return 13
    elif (lettera == "O"):
        return 14
    elif (lettera == "P"):
        return 15
    elif (lettera == "Q"):
        return 16
    elif (lettera == "R"):
        return 17
    elif (lettera == "S"):
        return 18
    elif (lettera == "T"):
        return 19
    elif (lettera == "U"):
        return 20
    elif (lettera == "V"):
        return 21
    elif (lettera == "W"):
        return 22
    elif (lettera == "X"):
        return 23
    elif (lettera == "Y"):
        return 24
    else:
        return 25

def controllo_lettera_disp(lettera):
    num = {"0": 1, "1": 0, "2": 5, "3": 7, "4": 9, "5" ,"6", "7", "8": , "9": , "A": , "B": , "C": , "D": , "E": , "F": , "G": , "H": , "I": , "J": , "K": , "L": , "M": , "N": , "O": , "P": , "Q": , "R": , "S": , "T": , "U": , "V": , "W": , "X": , }
    if (lettera == "A") or (lettera == "0"):
        num = 1
    elif (lettera == "B") or (lettera == "1"):
        num = 0
    elif (lettera == "C") or (lettera == "2"):
        num = 5
    elif (lettera == "D") or (lettera == "3"):
        num = 7
    elif (lettera == "E") or (lettera == "4"):
        num = 9
    elif (lettera == "F") or (lettera == "5"):
        num = 13
    elif (lettera == "G") or (lettera == "6"):
        num = 15
    elif (lettera == "H") or (lettera == "7"):
        num = 17
    elif (lettera == "I") or (lettera == "8"):
        num = 19
    elif (lettera == "J") or (lettera == "9"):
        num = 21
    elif (lettera == "K"):
        num = 2
    elif (lettera == "L"):
        num = 4
    elif (lettera == "M"):
        num = 18
    elif (lettera == "N"):
        num = 20
    elif (lettera == "O"):
        num = 11
    elif (lettera == "P"):
        num = 3
    elif (lettera == "Q"):
        num = 6
    elif (lettera == "R"):
        num = 8
    elif (lettera == "S"):
        num = 12
    elif (lettera == "T"):
        num = 14
    elif (lettera == "U"):
        num = 16
    elif (lettera == "V"):
        num = 10
    elif (lettera == "W"):
        num = 22
    elif (lettera == "X"):
        num = 25
    elif (lettera == "Y"):
        num =24
    else:
        num = 23    
    return num

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
    l = lettere[c]
    return l

def comune(comune):
    if comune == "AO":
        cod = "A326"
    elif comune == "TO":
        cod = "L219"
    elif comune =="GE":
        cod = "D969"
    elif comune == "MI":
        cod  = "F205"
    elif comune =="TN":
        cod = "L378"
    elif comune == "VE":
        cod = "L736"
    elif comune == "TS":
        cod = "L424"
    elif comune == "BO":
        cod = "A844"
    elif comune == "FI":
        cod = "D612"
    elif comune == "AN":
        cod = "A271"
    elif comune == "PG":
        cod = "G478"
    elif comune == "RM":
        cod == "H501"
    elif comune == "AQ":
        cod = "A345"
    elif comune == "CB":
        cod = "B519"
    elif comune == "NA":
        cod = "F839"
    elif comune == "BA":
        cod = "A662"
    elif comune == "PZ":
        cod = "G942"
    elif comune == "CZ":
        cod = "C362"
    elif comune == "PA":
        cod = "G273"
    elif comune == "CA":
        cod = "B354"
    return cod

def anno_nascita(anno,sesso):
    nascita = f"{str(anno.anno)[2:]}"
    if sesso == "F":
        anno.giorno += 40   
    if anno.mese == 1:
        nascita += "A"
    elif anno.mese == 2:
        nascita += "B"
    elif anno.mese == 3:
        nascita += "C"
    elif anno.mese == 4:
        nascita += "D"
    elif anno.mese == 5:
        nascita += "E"
    elif anno.mese == 6:
        nascita += "H"
    elif anno.mese == 7:
        nascita += "L"
    elif anno.mese == 8:
        nascita += "M"
    elif anno.mese == 9:
        nascita += "P"
    elif anno.mese == 10:
        nascita += "R"
    elif anno.mese == 11:
        nascita += "S"
    else:
        nascita += "T"
    nascita += f"{anno.giorno}"
    return nascita

def nome_cognome(nome,cognome):
    vocali = ["A","E","I","O","U"]
    cons_n = []
    voc_n = []
    cons_c = []
    voc_c = []
    for i in nome:
        if i not in vocali:
            cons_n.append(i)
        else:
            voc_n.append(i)
    for i in cognome:
        if i not in vocali:
            cons_c.append(i)
        else:
            voc_c.append(i)
    nc = ""
    if len(cons_c) >= 3:
        for i in range(3):
            nc += cons_c[i]
    else:
        for i in range(len(cons_c)):
            nc += cons_c[i]
        c = 0
        while len(nc) < 3:
            nc += voc_c[c]
            c += 1
    if len(cons_n) >= 4:
        nc += cons_n[0] +cons_n[2] + cons_n[3]
    else:
        for i in range(len(cons_n)):
            nc += cons_n[i]
        c = 0
        while len(nc) < 6:
            nc += voc_n[c]
            c += 1
    return nc

def main():
    codice_fiscale = ""
    nome = f.l("Inserisci il tuo nome e cognome: ")
    nome[0] = nome[0].upper()
    nome[1] = nome[1].upper()
    codice_fiscale += nome_cognome(nome[0],nome[1])
    sesso = f.s("Inserire il proprio sesso(M-F): ")
    data_l = f.l("Inserisci la tua data di nascita(aaaa/mm/gg): ","/")
    data_l[1] = int(data_l[1])
    data = anno(data_l[0],data_l[1],data_l[2])
    codice_fiscale += anno_nascita(data,sesso)
    com = f.s("Inserire la sigla del proprio comune: ").upper()
    codice_fiscale += comune(com)
    codice_fiscale += lettera_controllo(codice_fiscale)
    print(f"Il tuo codice fiscale corrisponde a: {codice_fiscale}") 
    return

import funzioniutili as f
main()