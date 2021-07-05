#import all functn frm the tkinter
from tkinter import*
from tkinter import messagebox

#function for clearing the content of all text entry boxes
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

#functin for checking error
def check_error():
    #if any of entry field is empty then shw an error msg"clear all entries"
    if(day_field.get()==""or month_field.get()=="" or year_field.get()=="" or
    given_day_field.get()=="" or given_month_field.get()=="" or given_year_field.get()=="" or
    rslt_day_field.get()=="" or rslt_month_field.get()=="" or rslt_year_field):
        messagebox.showerror("Input Error")
        clear_all()
        return -1



#create gui window
age_calculate_window= Tk()
#set background clr f gui window
age_calculate_window.configure(background="light yellow")
#set name of gui window
age_calculate_window.title("AGE CALCULATOR")
#set congifuration of window
age_calculate_window.geometry("500x250")
#Create a DOB label


#create a text entry box for filling or typing the information
day_field=Entry(age_calculate_window)
month_field=Entry(age_calculate_window)
year_field=Entry(age_calculate_window)

given_day_field=Entry(age_calculate_window)
given_month_field=Entry(age_calculate_window)
given_year_field=Entry(age_calculate_window)

rslt_day_field=Entry(age_calculate_window)
rslt_month_field=Entry(age_calculate_window)
rslt_year_field=Entry(age_calculate_window)

age_calculate_window.mainloop()