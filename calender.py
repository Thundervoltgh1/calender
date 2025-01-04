from tkinter import*
import calendar
root=Tk()
root.title("Calender")
root.geometry("400x400")
root.config(background="Blue")
a=Label(root,text="")
a.grid(row=1,column=1)
r=Label(root,text="CALENDER",bg="white",fg="Blue",font=("Ariel",50,'bold'))
r.grid(row=2,column=2)
e=Entry(root,bg="Grey",fg="white")
e.grid(row=3,column=2)
def show_calender():
    newtk=Tk()
    newtk.config(background="White")
    newtk.title("Calender")
    newtk.geometry("600x600")
    cal=int(e.get())
    cal1=calendar.calendar(cal)
    h=Label(newtk,text=cal1,font="Consolas 10 bold")
    h.grid(row=5,column=1,padx=20)

    newtk.mainloop()
s=Button(root,text="Show",fg="green",bg='white',command=show_calender)  
s.grid(row=4,column=2)
d=Button(root,text="exit",fg="red",bg='white',command=exit)
d.grid(row=5,column=2)


root.mainloop()
