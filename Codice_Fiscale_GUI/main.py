import Moduli.codice_fiscale as c_f
import Moduli.dati_GUI as GUI
from tkinter import messagebox

def main():
    codice = -1
    rip = bool()
    while ((codice == -1) or (rip == True)):
        dati = GUI.data()
        try:
            codice = c_f.creacodice(dati[0],dati[1],dati[2],dati[3],dati[4])
            if codice == -1:
                messagebox.showerror(title="comune sbagliato",message=f"comune non valido: \"{dati[4]}\"")
            else:
                messagebox.showinfo(title="codice fiscale",message=f"il tuo codice fiscale è:\n{codice}")
                rip = messagebox.askyesno(title="ripetere?",message="Vuoi ripetere il programma?")
        except IndexError:
            codice = 0
            rip = False
            pass
    return

main()