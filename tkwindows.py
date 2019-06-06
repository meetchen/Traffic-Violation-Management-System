import tkinter as tk
import driver
import punish
import PIL
import police
import vehicle
import punish


# Print select windows
def select_windows(var):
    # window configuration
    window = tk.Tk()
    text1 = tk.Text(window)
    window.attributes("-alpha", 0.95, '-topmost', True)
    window.geometry('300x200')
    window.title('Query interface')
    text1.pack()
    # Print each piece of data and change lines
    for va in var:
        global Var
        Var = ''
        for v in va:
            temp = v
            # int -> str for +
            Var = Var + '  ' + str(temp)
        Var = Var + '\n'
        text1.insert('end', Var)
    window.mainloop()


# Driver_delete()
def delete_windows():
    # Window Configuration
    windows1_delete = tk.Tk()
    windows1_delete.title = 'Delete interface'
    windows1_delete.attributes("-alpha", 0.95, '-topmost', True)
    windows1_delete.geometry('1000x500')
    # Label
    top = tk.Label(windows1_delete, text='', font=('Arial', 13))
    top.place(x=50, y=50)
    top1 = tk.Label(windows1_delete, text='Driver_id', font=('Arial', 12))
    top1.place(x=12, y=70)
    # Entry
    pe = tk.Entry(windows1_delete, font=('Arial', 12))
    pe.place(x=50, y=100)

    # function
    def delete_function():
        pe_var = pe.get()
        driver.diverDelete(pe_var)
    # Button
    btt1 = tk.Button(windows1_delete, text='Delete', font=('Arial', 12), command=delete_function)
    btt1.place(x=190, y=250)
    windows1_delete.mainloop()


# driver update windows
def update_windows():
    # Windows Configuration
    windows = tk.Tk()
    windows.title('Update interface')
    windows.attributes("-alpha", 0.95, '-topmost', True)
    windows.geometry('1000x500')
    # Entry
    # entry1 = tk.Entry(windows, font=('Arial', 12))
    # entry1.place(x=200, y=50)
    entry2 = tk.Entry(windows, font=('Arial', 12))
    entry2.place(x=200, y=80)
    entry3 = tk.Entry(windows, font=('Arial', 12))
    entry3.place(x=200, y=110)
    # Label
    label1 = tk.Label(windows, text='Target list ；')
    label1.place(x=50, y=50)
    label2 = tk.Label(windows, text='Driver_id :')
    label2.place(x=50, y=80)
    label3 = tk.Label(windows, text='Modified values :')
    label3.place(x=50, y=110)
    # Radiobutton
    rad = tk.Variable()
    rad.set('driver_phone')
    rad1 = tk.Radiobutton(windows, text='Driver_name', variable=rad, value='driver_name', font=('Arial', 12))
    rad1.place(x=200, y=50)
    rad2 = tk.Radiobutton(windows, text='Driver_address', variable=rad, value='driver_address', font=('Arial', 12))
    rad2.place(x=400, y=50)
    rad3 = tk.Radiobutton(windows, text='Driver_post_code', variable=rad, value='driver_phone', font=('Arial', 12))
    rad3.place(x=600, y=50)
    rad4 = tk.Radiobutton(windows, text='Driver_phone', variable=rad, value='driver_post_code', font=('Arial', 12))
    rad4.place(x=800, y=50)

    # function
    def update_command():
        entry1_var = rad.get()
        entry2_var = entry2.get()
        entry3_var = entry3.get()
        driver.diverUpdate(entry1_var, entry3_var, entry2_var)
    # Button
    button1 = tk.Button(windows, text='Update', command=update_command)
    button1.place(x=65, y=130)
    windows.mainloop()


# driver insert windows
def insert_windows():
    windows = tk.Tk()
    windows.title('Insert interface')
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

    # Label
    label1 = tk.Label(windows, text='Driver_name ；')
    label1.place(x=50, y=50)
    label2 = tk.Label(windows, text='Driver_address :')
    label2.place(x=50, y=80)
    label3 = tk.Label(windows, text='Driver_phone :')
    label3.place(x=50, y=110)
    label4 = tk.Label(windows, text='Driver_post_code :')
    label4.place(x=50, y=140)

    # function
    def insert_command():
        entry1_var = entry1.get()
        entry2_var = entry2.get()
        entry3_var = entry3.get()
        entry4_var = entry4.get()
        driver.driver_insert(entry1_var, entry3_var, entry2_var, entry4_var)
    # Button
    button1 = tk.Button(windows, text='insert', command=insert_command)
    button1.place(x=125, y=160)
    windows.mainloop()


# police select windows
def police_select_windows(var):
    # window configuration
    window = tk.Tk()
    text1 = tk.Text(window)
    window.attributes("-alpha", 0.95, '-topmost', True)
    window.geometry('300x200')
    window.title('Query interface')
    text1.pack()
    # Print each piece of data and change lines
    for va in var:
        global Var
        Var = ''
        for v in va:
            temp = v
            # int -> str for +
            Var = Var + '  ' + str(temp)
        Var = Var + '\n'
        text1.insert('end', Var)
    window.mainloop()


# police insert windows
def police_insert_windows():
    # windows configuration
    windows = tk.Tk()
    windows.title('Insert interface')
    windows.attributes("-alpha", 0.95, '-topmost', True)
    windows.geometry('1000x500')

    # Entry
    entry1 = tk.Entry(windows, font=('Arial', 12))
    entry1.place(x=200, y=50)

    # Label
    label1 = tk.Label(windows, text='Police_name ；')
    label1.place(x=50, y=50)

    # function
    def insert_command():
        entry1_var = entry1.get()
        police.policeAdd(entry1_var)
    # Button
    button1 = tk.Button(windows, text='insert', command=insert_command)
    button1.place(x=125, y=160)
    windows.mainloop()


# police update windows
def police_update_windows():
    # Windows Configuration
    windows = tk.Tk()
    windows.title('Update interface')
    windows.attributes("-alpha", 0.95, '-topmost', True)
    windows.geometry('1000x500')
    # Entry
    # entry1 = tk.Entry(windows, font=('Arial', 12))
    # entry1.place(x=200, y=50)
    entry2 = tk.Entry(windows, font=('Arial', 12))
    entry2.place(x=200, y=80)
    entry3 = tk.Entry(windows, font=('Arial', 12))
    entry3.place(x=200, y=110)
    # Label
    label1 = tk.Label(windows, text='Target list ；')
    label1.place(x=50, y=50)
    label2 = tk.Label(windows, text='Police_id :')
    label2.place(x=50, y=80)
    label3 = tk.Label(windows, text='Modified values :')
    label3.place(x=50, y=110)
    # Radiobutton
    rad = tk.Variable()
    rad.set('1')
    rad1 = tk.Radiobutton(windows, text='Driver_name', variable=rad, value='police_name', font=('Arial', 12))
    rad1.place(x=200, y=50)

    # function
    def update_command():
        entry2_var = entry2.get()
        entry3_var = entry3.get()
        police.policeUpdate(entry2_var, entry3_var)
    # Button
    button1 = tk.Button(windows, text='Update', command=update_command)
    button1.place(x=65, y=130)
    windows.mainloop()


# police_delete()
def police_delete_windows():
    # Window Configuration
    windows1_delete = tk.Tk()
    windows1_delete.title = 'Delete interface'
    windows1_delete.attributes("-alpha", 0.95, '-topmost', True)
    windows1_delete.geometry('1000x500')
    # Label
    top = tk.Label(windows1_delete, text='', font=('Arial', 13))
    top.place(x=50, y=50)
    top1 = tk.Label(windows1_delete, text='Police_id', font=('Arial', 12))
    top1.place(x=12, y=70)
    # Entry
    pe = tk.Entry(windows1_delete, font=('Arial', 12))
    pe.place(x=50, y=100)

    # function
    def delete_function():
        pe_var = pe.get()
        police.policeDelete(pe_var)
    # Button
    btt1 = tk.Button(windows1_delete, text='Delete', font=('Arial', 12), command=delete_function)
    btt1.place(x=190, y=250)
    windows1_delete.mainloop()
