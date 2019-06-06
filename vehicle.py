import tkinter as tk
import pymysql
import tkinter.messagebox


def vehicleSelect():
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    select = 'select * from vehicle'
    mycursor.execute(select)
    select = mycursor.fetchall()
    mydb.commit()
    tk.messagebox.showinfo(title='机动车表', message=select)


def vehicleUpdate(colunm, var, id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    if colunm == 'vehicle_date':
        update = 'update vehicle set vehicle_date = %s where `sql`.vehicle.vehicle_license_plate = %s'
    elif colunm == 'vehicle_type':
        update = 'update vehicle set vehicle_type = %s where `sql`.vehicle.vehicle_license_plate = %s'
    elif colunm == 'vehicle_manufacturer':
        update = 'update vehicle set vehicle_manufacturer = %s where `sql`.vehicle.vehicle_license_plate = %s'
    else:
        print('error')
        return
    mycursor.execute(update, (var, id))
    mydb.commit()


def vehicleAdd(data, type, manufacturer):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    add = 'insert into vehicle(vehicle_date, vehicle_type, vehicle_manufacturer) values (%s, %s, %s)'
    mycursor.execute(add, (data, type, manufacturer))
    mydb.commit()


def vehicleDelete(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    delete = 'delete from vehicle where `sql`.vehicle.vehicle_license_plate = %s'
    mycursor.execute(delete, id)
    mydb.commit()

