from dao.driver import driver_select_id
from dao.notice import notice_select_id
from dao.police import police_select_id
from dao.punish import punish_select_id
from dao.vehicle import vehicle_select_id
import tkinter as tk
'''
    Fields of each function are extracted and combined.
'''


def notice_combination(driver_id, notice_id ,police_id, punish_id, vehicle_id):
    driver_tuple = driver_select_id(driver_id)
    notice_tuple = notice_select_id(notice_id)
    police_tuple = police_select_id(police_id)
    punish_tuple = punish_select_id(punish_id)
    vehicle_tuple = vehicle_select_id(vehicle_id)
    notice_combination_tuple = driver_tuple + notice_tuple + police_tuple + punish_tuple + vehicle_tuple
    return notice_combination_tuple


def notice_get_windows():
    # Windows Configuration
    windows = tk.Tk()
    windows.title('Update interface')
    windows.attributes("-alpha", 0.95, '-topmost', True)
    windows.geometry('1000x500')
    # Entry
    entry1 = tk.Entry(windows, font=('Arial', 12))
    entry1.place(x=200, y=50)
    entry2 = tk.Entry(windows, font=('Arial', 12))
    entry2.place(x=200, y=80)
    entry3 = tk.Entry(windows, font=('Arial', 12))
    entry3.place(x=200, y=110)
    entry4 = tk.Entry(windows, font=('Arial', 12))
    entry4.place(x=200, y=140)
    entry5 = tk.Entry(windows, font=('Arial', 12))
    entry5.place(x=200, y=170)
    # Label
    label1 = tk.Label(windows, text='Driver_id ；')
    label1.place(x=50, y=50)
    label2 = tk.Label(windows, text='Notice_id :')
    label2.place(x=50, y=80)
    label3 = tk.Label(windows, text='Police_id :')
    label3.place(x=50, y=110)
    label4 = tk.Label(windows, text='Punish_id :')
    label4.place(x=50, y=140)
    label5 = tk.Label(windows, text='Vehicle_id:')
    label5.place(x=50, y=170)

    # function
    def update_command():
        Driver_id = entry1.get()
        Notice_id = entry2.get()
        Police_id = entry3.get()
        Punish_id = entry4.get()
        Vehicle_id = entry5.get()
        global tuple
        tuple = (Driver_id, Notice_id, Police_id, Punish_id, Vehicle_id)
        print(tuple)
    # Button
    button1 = tk.Button(windows, text='Create', command=update_command)
    button1.place(x=65, y=200)
    windows.mainloop()
    return tuple

