from tkinter import *
from tkcalendar import *
import datetime

def print_date():
    selected_date = cal.selection_get()
    print(selected_date)

root = Tk()
root.title("Calendar")
root.geometry("500x400")

# Create Entry widgets for year, month, and day
year_entry = Entry(root, width=10)
year_entry.pack(pady=10)

month_entry = Entry(root, width=10)
month_entry.pack(pady=10)

day_entry = Entry(root, width=10)
day_entry.pack(pady=10)

# Create a function to get the date from the Entry widgets
def get_date():
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())
    cal.selection_set(datetime.date(year, month, day))
    print_date()

# Create a button to set the date in the Calendar widget
set_date_button = Button(root, text="Set Date", command=get_date)
set_date_button.pack(pady=10)

# Create the Calendar widget
cal = Calendar(root, selectmode='day')
cal.pack(pady=10)

# Create a button to print the selected date
print_date_button = Button(root, text="Print Date", command=print_date)
print_date_button.pack(pady=10)

root.mainloop()
