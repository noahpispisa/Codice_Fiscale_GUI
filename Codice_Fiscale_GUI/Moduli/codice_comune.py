nomefile = "Desktop\\CODICE_FISCALE_GUI\\CODICE_FISCALE_GUI\\Moduli\\lista-codici.txt"
def leggi_file(nomefile):  
    testo = []
    f = open(f"{nomefile}","r")
    riga = f.readline()
    while riga != "":
        riga1 = riga.strip("\n")
        testo.append(riga1.split(";"))
        riga = f.readline()
    f.close()
    return testo

testo = leggi_file(nomefile)

def trova_codice(comune):
    for i in range(len(testo)):
        if comune in testo[i][0]:
            return testo[i][1]
    return -1
