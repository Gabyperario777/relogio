import datetime
import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()
root.title("Digital Clock - Brazil")
root.geometry("300x200")
root.configure(bg="black")

def update_time():
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))) 
    formatted_time = now.strftime("%H:%M:%S")
    time_label.config(text=formatted_time)
    time_label.after(1000, update_time)

time_label = tk.Label(root, font=("ds-digital", 80), 
                      bg="black", fg="#90EE90")
time_label.pack(pady=50)

update_time()

root.mainloop()