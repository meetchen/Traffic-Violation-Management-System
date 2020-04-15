import tkinter as tk
import windows1


def notice_windows():

    notice_windows = tk.Tk()
    notice_windows.geometry('800x700')
    # label
    # driver
    title = tk.Label(text='Notice of traffic violation', font=('Arial', 20))
    title.place(x=200, y=20)
    id = tk.Label(text='Identifier :', font=('Arial', 13))
    id.place(x=500, y=55)
    # -----
    line0 = tk.Label(text='__________________________________________________________________________________________'
                          '______________________________________')
    line0.place(x=30, y=75)

    driver_name = tk.Label(text='Name :', font=('Arial', 13))
    driver_name.place(x=50, y=100)
    driver_name_var = tk.Label(text=tuple[1],  font=('Arial', 13))
    driver_name_var.place(x=110, y=100)

    driver_id = tk.Label(text='Control License Number :', font=('Arial', 13))
    driver_id.place(x=400, y=100)
    driver_id_var = tk.Label(text=tuple[0], font=('Arial', 13))
    driver_id_var.place(x=590, y=100)

    driver_address = tk.Label(text='Address :', font=('Arial', 13))
    driver_address.place(x=50, y=140)
    driver_address_var = tk.Label(text=tuple[3], font=('Arial', 13))
    driver_address_var.place(x=130, y=140)

    driver_post_code = tk.Label(text='Post Code :', font=('Arial', 13))
    driver_post_code.place(x=50, y=180)
    driver_post_code = tk.Label(text=tuple[4], font=('Arial', 13))
    driver_post_code.place(x=150, y=180)

    driver_phone = tk.Label(text='Telephone :', font=('Arial', 13))
    driver_phone.place(x=400, y=180)
    driver_phone = tk.Label(text=tuple[2], font=('Arial', 13))
    driver_phone.place(x=500, y=180)
    # -----
    line1 = tk.Label(text='__________________________________________________________________________________________'
                          '______________________________________')
    line1.place(x=30, y=200)
    # vehicle
    vehicle_id = tk.Label(text='Vehicle License Plate Number :', font=('Arial', 13))
    vehicle_id.place(x=50, y=235)
    vehicle_id = tk.Label(text=tuple[-4], font=('Arial', 13))
    vehicle_id.place(x=290, y=235)

    vehicle_type = tk.Label(text='Type :', font=('Arial', 13))
    vehicle_type.place(x=400, y=235)
    vehicle_type = tk.Label(text=tuple[-2], font=('Arial', 13))
    vehicle_type.place(x=460, y=235)

    vehicle_manufacturer = tk.Label(text='Manufacturer :', font=('Arial', 13))
    vehicle_manufacturer.place(x=50, y=275)
    vehicle_manufacturer = tk.Label(text=tuple[-1], font=('Arial', 13))
    vehicle_manufacturer.place(x=170, y=275)

    vehice_date = tk.Label(text='Date of manufacture :', font=('Arial', 13))
    vehice_date.place(x=400, y=275)
    vehice_date = tk.Label(text=tuple[-3], font=('Arial', 13))
    vehice_date.place(x=570, y=275)
    # -----
    line2 = tk.Label(text='__________________________________________________________________________________________'
                          '______________________________________')
    line2.place(x=30, y=295)
    # notice
    notice_data = tk.Label(text='Violation Date :', font=('Arial', 13))
    notice_data.place(x=50, y=335)
    notice_data = tk.Label(text=tuple[7], font=('Arial', 13))
    notice_data.place(x=170, y=335)

    notice_time = tk.Label(text='Time :', font=('Arial', 13))
    notice_time.place(x=400, y=335)
    notice_time = tk.Label(text=tuple[6], font=('Arial', 13))
    notice_time.place(x=460, y=335)

    notice_place = tk.Label(text='Place :', font=('Arial', 13))
    notice_place.place(x=50, y=375)
    notice_place = tk.Label(text=tuple[8], font=('Arial', 13))
    notice_place.place(x=110, y=375)

    notice_record = tk.Label(text='Record :', font=('Arial', 13))
    notice_record.place(x=400, y=375)
    notice_record = tk.Label(text=tuple[9], font=('Arial', 13))
    notice_record.place(x=470, y=375)

    # -----
    line3 = tk.Label(text='__________________________________________________________________________________________'
                          '______________________________________')
    line3.place(x=30, y=395)
    # punish
    punish_type = tk.Label(text='Punish_type: ', font=('Arial', 13))
    punish_type.place(x=50, y=435)
    # punish_type = tk.Label(text=tuple[-5], font=('Arial', 13))
    # punish_type.place(x=100, y=435)
    punish_type1 = tk.Label(text='□Warning', font=('Arial', 13))
    punish_type1.place(x=150, y=475)
    punish_type2 = tk.Label(text='□Fine', font=('Arial', 13))
    punish_type2.place(x=400, y=475)
    punish_type3 = tk.Label(text='□Temporary withholding of driver license', font=('Arial', 13))
    punish_type3.place(x=150, y=515)
    # -----
    line4 = tk.Label(text='__________________________________________________________________________________________'
                          '______________________________________')
    line4.place(x=30, y=535)
    # Police Signature
    police_signature = tk.Label(text='Police Signature :', font=('Arial', 13))
    police_signature.place(x=50, y=575)
    police_id = tk.Label(text='Police Id :', font=('Arial', 13))
    police_id.place(x=400, y=575)
    # -----
    line5 = tk.Label(text='__________________________________________________________________________________________'
                          '______________________________________')
    line5.place(x=30, y=605)
    # driver signature
    driver_signature = tk.Label(text='Driver Signature :', font=('Arial', 13))
    driver_signature.place(x=50, y=645)
    notice_windows.mainloop()


def tuple_funciton():
    global tuple
    tuple = windows1.notice_get_windows()
    tuple = windows1.notice_combination(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4])
    print(tuple)
    notice_windows()

