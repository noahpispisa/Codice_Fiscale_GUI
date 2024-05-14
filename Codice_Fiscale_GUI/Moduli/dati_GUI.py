import tkinter as tk

def data():
    datas = []
    window = tk.Tk()
    window.geometry("750x100")
    window.title("raccolta dati")
    grid = mygrid(window)
    grid[0].pack(anchor="nw")
    submit = mybutton(window,grid[1],datas)
    submit.pack(side="bottom")
    window.mainloop()
    return datas

def mygrid(window):
    data = []
    frame = tk.Frame(window)
    frame.rowconfigure((0,1),weight=1)
    frame.columnconfigure((0,1,2,3),weight=1)
    date_t = mylabel(frame,"Inserire la data di nascita nel formato \"aaaa/mm/gg\"   ")
    date_t.grid(row=0,column=0,sticky="nwe")
    name_t = mylabel(frame,text="inserire il proprio nome e cognome   ")
    name_t.grid(row=0,column=1,sticky="nwe")
    sex_t = mylabel(frame,"inserire il proprio sesso   ")
    sex_t.grid(row=0,column=2,sticky="nwe")
    mun_t = mylabel(frame,"Inserire il comune di nascita   ")
    mun_t.grid(row=0,column=3,sticky="nwe")
    date = myentry(frame)
    date.grid(row=1,column=0,sticky="nwe")
    data.append(date)
    name = myentry(frame)
    name.grid(row=1,column=1,sticky="nwe")
    data.append(name)
    Sex = sex(frame)
    Sex[0].grid(row=1,column=2,sticky="nwe")
    data.append(Sex[1])
    mun = myentry(frame)
    mun.grid(row=1,column=3,sticky="nwe")
    data.append(mun)
    return frame,data

def sex(frame):
    opt = ["M","F"]
    clicked = tk.StringVar()
    clicked.set("M")
    sex = tk.OptionMenu(frame,clicked,*opt)
    return sex,clicked

def mylabel(frame,text):
    label = tk.Label(frame,text=text)
    return label

def myentry(frame):
    entry = tk.Entry(frame)
    return entry

def elaborate(window,lista,datas):
    """la funzione controllo ceh i parametri siano immessi correttamente"""
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

def mybutton(window,list,list1):
    """crea un bottone che quando viene premuto chiama la funzione "elaborate" """
    button = tk.Button(window,text="SUBMIT",command= lambda: elaborate(window,list,list1))
    return button
