import tkinter as tk

def richiesta_dati():
    window = tk.Tk()
    window.title("richiesta dati")
    window.geometry("500x100")
    drop_menu(window)
    window.mainloop()
    return

def drop_menu(window):
    months = ["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"]
    clicked = tk.StringVar()
    clicked.set(months[0])
    drop = tk.OptionMenu(window, clicked, *months)
    drop.pack(anchor= "nw")
    print(clicked.get())
    return



window = richiesta_dati()

