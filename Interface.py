import tkinter
import tkinter.messagebox
import driver, tkwindows, usertable, police, vehicle, punish, notice, NOTICEDEMO
# Window Configuration
windows = tkinter.Tk()
windows.attributes("-alpha", 0.8)
windows.title('Traffic Violation Management System      (By Cjc~)')
windows.geometry('1000x500')
# Label
tip1 = tkinter.Label(windows, text='Welcome to Traffic Violation Management System', font=('Arial', 25))\
    .place(x=100, y=50)
tip2 = tkinter.Label(windows, text='User name  :', font=('Arial', 15)).place(x=250, y=150)
tip3 = tkinter.Label(windows, text='Password   :', font=('Arial', 15)).place(x=250, y=210)
tip4 = tkinter.Label(windows, text='Created by Cjc~', font=('Arial', 13)).place(x=800, y=430)
# Entry
userE = tkinter.Entry(windows, font=('Arial', 14))
userE.place(x=400, y=150)
passwordE = tkinter.Entry(windows, show='*', font=('Arial', 14))
passwordE.place(x=400, y=210)
# Radiobutton :choose identity(sudo, police, driver) ：id_var choose only
identity = tkinter.StringVar()
identity.set(1)
tip5 = tkinter.Label(windows, text='Choose Identity :', font=('Arial', 12)).place(x=300, y=280)
id1 = tkinter.Radiobutton(windows, text='Police', variable=identity, value=1, font=('Arial', 12)).place(x=450, y=280)
id2 = tkinter.Radiobutton(windows, text='Driver', variable=identity, value=0, font=('Arial', 12)).place(x=550, y=280)


# login command function
def login():
    identity_var = identity.get()
    user = userE.get()
    password = passwordE.get()
    # python Sequence unpacking
    if usertable.UserSelect(user) != 'error':
        password_sql, user_identity = usertable.UserSelect(user)
        if password == password_sql and identity_var == '1' or '2':
            if identity_var == '1':
                # login police_system
                tkinter.messagebox.showinfo(title='Landing', message='Verification passed')
                if 1:
                    Police_Windows1()
            else:
                # login driver_system
                return
        else:
            tkinter.messagebox.showinfo(title='Landing', message='Password error')
    else:
        tkinter.messagebox.showinfo(title='Landing', message='User name does not exist')


# Police_Windows1
def Police_Windows1():
    # Window Configuration
    user = userE.get()
    windows1 = tkinter.Tk()
    windows1.title('Police'+"_"+user.title())
    windows1.attributes("-alpha", 0.95, '-topmost', True)
    windows1.geometry('1200x600')
    # Label  x=50 y=++60
    arp = tkinter.Label(windows1, text=user.title()+',Welcome to Traffic Violation Management System',
                        font=('Arial', 25))
    arp.place(x=100, y=50)
    arp1 = tkinter.Label(windows1, text='Driver_information:', font=('Arial', 13))
    arp1.place(x=200, y=140)
    arp2 = tkinter.Label(windows1, text='Created by Cjc~')
    arp2.place(x=800, y=430)
    arp3 = tkinter.Label(windows1, text='Police_information:', font=('Arial', 13))
    arp3.place(x=200, y=200)
    arp4 = tkinter.Label(windows1, text='Vehicle_information:', font=('Arial', 13))
    arp4.place(x=200, y=260)
    arp5 = tkinter.Label(windows1, text='Notice_information:', font=('Arial', 13))
    arp5.place(x=200, y=320)
    arp6 = tkinter.Label(windows1, text='Punish_information:', font=('Arial', 13))
    arp6.place(x=200, y=380)
    arp7 = tkinter.Label(windows1, text='Notice of traffic violation:', font=('Arial', 13))
    arp7.place(x=200, y=440)
    # Button
    # Driver
    btt = tkinter.Button(windows1, text='Select', font=('Arial', 12), command=driver.driver)
    btt.place(x=400, y=140)
    btt1 = tkinter.Button(windows1, text='Delete', font=('Arial', 12), command=tkwindows.delete_windows)
    btt1.place(x=500, y=140)
    btt2 = tkinter.Button(windows1, text='Update', font=('Arial', 12), command=tkwindows.update_windows)
    btt2.place(x=600, y=140)
    btt3 = tkinter.Button(windows1, text='Insert', font=('Arial', 12), command=tkwindows.insert_windows)
    btt3.place(x=700, y=140)
    # Police
    btt4 = tkinter.Button(windows1, text='Select', font=('Arial', 12), command=police.policeSelect)
    btt4.place(x=400, y=200)
    btt5 = tkinter.Button(windows1, text='Delete', font=('Arial', 12), command=tkwindows.police_delete_windows)
    btt5.place(x=500, y=200)
    btt6 = tkinter.Button(windows1, text='Update', font=('Arial', 12), command=tkwindows.police_update_windows)
    btt6.place(x=600, y=200)
    btt7 = tkinter.Button(windows1, text='Insert', font=('Arial', 12), command=tkwindows.police_insert_windows)
    btt7.place(x=700, y=200)
    # Vehicle
    btt4 = tkinter.Button(windows1, text='Select', font=('Arial', 12), command=vehicle.vehicleSelect)
    btt4.place(x=400, y=260)
    btt5 = tkinter.Button(windows1, text='Delete', font=('Arial', 12), command=tkwindows.vehicle_delete_windows)
    btt5.place(x=500, y=260)
    btt6 = tkinter.Button(windows1, text='Update', font=('Arial', 12), command=tkwindows.vehicle_update_windows)
    btt6.place(x=600, y=260)
    btt7 = tkinter.Button(windows1, text='Insert', font=('Arial', 12), command=tkwindows.vehicle_insert_windows)
    btt7.place(x=700, y=260)
    # Punish
    btt8 = tkinter.Button(windows1, text='Select', font=('Arial', 12), command=punish.punishSelect)
    btt8.place(x=400, y=320)
    btt9 = tkinter.Button(windows1, text='Delete', font=('Arial', 12), command=tkwindows.punish_delete_windows)
    btt9.place(x=500, y=320)
    btt10 = tkinter.Button(windows1, text='Update', font=('Arial', 12), command=tkwindows.punish_update_windows)
    btt10.place(x=600, y=320)
    btt11 = tkinter.Button(windows1, text='Insert', font=('Arial', 12), command=tkwindows.punish_insert_windows)
    btt11.place(x=700, y=320)
    # Notice
    btt12 = tkinter.Button(windows1, text='Select', font=('Arial', 12), command=notice.noticeSelect)
    btt12.place(x=400, y=380)
    btt13 = tkinter.Button(windows1, text='Delete', font=('Arial', 12), command=tkwindows.notice_delete_windows)
    btt13.place(x=500, y=380)
    btt14 = tkinter.Button(windows1, text='Update', font=('Arial', 12), command=tkwindows.notice_update_windows)
    btt14.place(x=600, y=380)
    btt15 = tkinter.Button(windows1, text='Insert', font=('Arial', 12), command=tkwindows.notice_insert_windows)
    btt15.place(x=700, y=380)
    # Ticket
    ticker = tkinter.Button(windows1, text='Establish', font=('Arial', 12), command=NOTICEDEMO.tuple_funciton)
    ticker.place(x=400, y=440)
    windows1.mainloop()


# Driver_delete()
def Driver_delete():
    # Window Configuration
    windows1_delete = tkinter.Toplevel()
    windows1_delete.title = 'Driver_delete'
    windows1_delete.attributes("-alpha", 0.95, '-topmost', True)
    windows1_delete.geometry('1000x500')
    # Label
    top = tkinter.Label(windows1_delete, text='', font=('Arial', 13))
    top.place(x=50, y=50)
    top1 = tkinter.Label(windows1_delete, text='Driver_id', font=('Arial', 12))
    top1.place(x=12, y=70)
    # Entry
    pe = tkinter.Entry(windows1_delete, font=('Arial', 12))
    pe.place(x=50, y=100)
    # Button
    # btt = tkinter.Button(windows1_delete, text='Delete', font=('Arial', 12), commanhxxg d=driver.diverDelete(pe_var))
    # btt.place(x=90, y=150)
    btt1 = tkinter.Button(windows1_delete, text='Delete', font=('Arial', 12))
    btt1.place(x=190, y=250)


# login Button
loginButton = tkinter.Button(windows, text='Login', font=('Arial', 20), command=login).place(x=450, y=350)
# windows loop refresh
windows.mainloop()

