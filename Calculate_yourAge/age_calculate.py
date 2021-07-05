#import all functn frm the tkinter
from tkinter import*
from tkinter import messagebox

def clear_all():
    day_field.delete(0,END)
    month_field.delete(0,END)
    year_field.delete(0,END)

    given_day_field.delete(0,END)
    given_month_field.delete(0,END)
    given_year_field.delete(0,END)

    rslt_day_field.delete(0,END)
    rslt_month_field.delete(0,END)
    rslt_year_field.delete(0,END)

def check_error():
    


#create gui window
ageCalculator= Tk()
#set background clr f gui window
ageCalculator.configure(background="light yellow")
#set name of gui window
ageCalculator.title("AGE CALCULATOR")
#set congifuration of window
ageCalculator.geometry("500x250")
#Create a DOB label


#ageCalculator.mainloop()