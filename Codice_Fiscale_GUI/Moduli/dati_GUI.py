import tkinter as tk
from tkinter import messagebox

def data():
    datas = []
    window = tk.Tk()
    window.geometry("500x120")
    window.title("raccolta dati")
    window.resizable(height=0,width=0)
    grid = mygrid(window)
    grid[0].pack(anchor="nw")
    submit = mybutton(window,grid[1],datas)
    submit.pack(anchor="sw")
    window.mainloop()
    return datas

def mygrid(window):
    data = []
    frame = tk.Frame(window)
    frame.rowconfigure((0,1,2,3),weight=1)
    frame.columnconfigure(0,weight=1)
    date = myentry(frame,"Inserire la propria data di nascita nel formato \"aaaa/mm/gg\": ")
    date.grid(row=0,column=0,sticky="nwe")
    data.append(date)
    name = myentry(frame,"Inserire il proprio nome e cognome: ")
    name.grid(row=1,column=0,sticky="nwe")
    data.append(name)
    Sex = sex(frame)
    Sex[0].grid(row=2,column=0,sticky="w")
    data.append(Sex[1])
    mun = myentry(frame,"Inserire il proprio coune di nascita: ")
    mun.grid(row=3,column=0,sticky="nwe")
    data.append(mun)
    return frame,data

def sex(frame):
    opt = ["M","F"]
    clicked = tk.StringVar()
    clicked.set("M")
    sex = tk.OptionMenu(frame,clicked,*opt)
    return sex,clicked

def myentry(frame,testo = ""):
    entry = tk.Entry(frame,width=len(testo)+20)
    entry.insert("0",testo)
    entry.bind("<ButtonPress-1>",func= lambda event: entry.delete("0",str(len(testo))))
    return entry

def elaborate(window,lista,datas):
    """la funzione controllo che i parametri siano immessi correttamente"""
    date = lista[0].get()
    name = lista[1].get()
    mun = lista[3].get()
    lista1 = [date,name,mun]
    if lista1 != ["","",""]:
        date = date.split("/")
        if ((len(date) == 3) and ((date[1].isnumeric()) and (date[2].isnumeric()))):
            date[2] = int(date[2])
            date[1] = int(date[1])
            if (((date[1] in [1,3,5,7,8,10,12]) and (date[2]<= 31)) or ((date[1] == 2) and (date[2] <= 29)) or ((date[1] in [4,6,9,11]) and (date[2] <= 30))):
                if lista1[1] != "" :
                    name = lista1[1]
                    name = name.upper()
                    name = name.split()
                if ((len(date) == 3) and (len(name) == 2) and (mun != "")):
                    datas.append(name[0])
                    datas.append(name[1])
                    datas.append(date)
                    datas.append(lista[2].get())
                    datas.append(mun.upper())
                    window.destroy()
                    return
    messagebox.showwarning("attenzione","Inserire tutti i dati nel modo richiesto")
    return 

def mybutton(window,list,list1):
    """crea un bottone che quando viene premuto chiama la funzione "elaborate" """
    button = tk.Button(window,text="SUBMIT",command= lambda: elaborate(window,list,list1))
    return button
