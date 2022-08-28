from cProfile import label
from calendar import month
from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calendario")
root.geometry("500x350")
root.config(bg="gray")

cal = Calendar(root, select="dia", años=2022, month=8, dia=27)
cal.pack(pady=20, fill="both", expand= "yes")

def fecha():
    Label.config(text="Fecha de hoy" + cal.get_date()) 

Button = Button(root, text="fecha", command=fecha)
Button.pack(pady=20)

Label = Label(root, text="")
Label.pack(pady=20) 


root.mainloop() 