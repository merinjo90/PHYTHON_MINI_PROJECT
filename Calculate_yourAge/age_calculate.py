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
    if(day_field.get()=="" or month_field.get()=="" or year_field.get()=="" or
    given_day_field.get()=="" or given_month_field.get()=="" or given_year_field.get()==""):
        messagebox.showerror("Input Error")
        clear_all()
        return -1

#function to calculate age
def calcuate_age():
    #check for error
    value=check_error()
    print(value)
    #if error occure then return
    if value == -1:
        return
    else:
        #take a value from the respective entry boxes get method returns current text as string
        birth_day=int(day_field.get())
        birth_month=int(month_field.get())
        birth_year=int(year_field.get())

        given_day=int(given_day_field.get())
        given_month=int(given_month_field.get())
        given_year=int(given_year_field.get())

        #if birth date is greater then given birth_mnth
        #then do not count this month and add 30 to the date so as to subtract the date and get the remaining days

        month=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(birth_day>given_day):
            given_month=given_month-1
            given_day=given_day+month[birth_month-1]

        #if birth month exceed given month,then donot count this year and add 12 to the month
        # so that we can subtract and find out the difference
        if(birth_month>given_month):
            given_year=given_year-1
            given_month=given_month+12
        #calcuate day,month,year
        calc_day=given_day-birth_day
        calc_month=given_month-birth_month
        calc_year=given_year-birth_year
        rslt_day_field.insert(10,str(calc_day))
        rslt_month_field.insert(10,str(calc_month))
        rslt_year_field.insert(10,str(calc_year))




#if __name__="__main__":
#create gui window
age_calculate_window= Tk()
#set background clr f gui window
age_calculate_window.configure(background="light blue")
#set name of gui window
age_calculate_window.title("AGE CALCULATOR")
#set congifuration of window
age_calculate_window.geometry("500x250")


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

#Create a DOB label
dob=Label(age_calculate_window,text="Date of Birth",bg="white")
dob.grid(row=0,column=1)
given_date=Label(age_calculate_window,text="Given Date",bg="white")
given_date.grid(row=0,column=4)

day=Label(age_calculate_window,text="Date",bg="light blue")
day.grid(row=1,column=0)
day_field.grid(row=1,column=1)
month=Label(age_calculate_window,text="Month",bg="light blue")
month.grid(row=2,column=0)
month_field.grid(row=2,column=1)
year=Label(age_calculate_window,text="Year",bg="light blue")
year.grid(row=3,column=0)
year_field.grid(row=3,column=1)

givDay=Label(age_calculate_window,text="Given Date",bg="light blue")
givDay.grid(row=1,column=3)
given_day_field.grid(row=1,column=4)
givMonth=Label(age_calculate_window,text="Given Month",bg="light blue")
givMonth.grid(row=2,column=3)
given_month_field.grid(row=2,column=4)
givYear=Label(age_calculate_window,text="Given Year",bg="light blue")
givYear.grid(row=3,column=3)
given_year_field.grid(row=3,column=4)

rsltDay=Label(age_calculate_window,text="Date",bg="light blue")
rsltDay.grid(row=9,column=2)
rslt_day_field.grid(row=10,column=2)
rsltMonth=Label(age_calculate_window,text="Month",bg="light blue")
rsltMonth.grid(row=7,column=2)
rslt_month_field.grid(row=8,column=2)
rsltYear=Label(age_calculate_window,text="Year",bg="light blue")
rsltYear.grid(row=5,column=2)
rslt_year_field.grid(row=6,column=2)

resultAge=Button(age_calculate_window,text="Calculated Age",bg="green",command=calcuate_age)
resultAge.grid(row=4,column=2)


clearAllEntry=Button(age_calculate_window,text="Reset",fg="Black",bg="blue",command=clear_all)
clearAllEntry.grid(row=12,column=2)

age_calculate_window.mainloop()