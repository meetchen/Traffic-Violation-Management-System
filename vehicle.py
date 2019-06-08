
import pymysql
import tkwindows

def vehicleSelect():
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    select = 'select * from vehicle'
    mycursor.execute(select)
    select = mycursor.fetchall()
    mydb.commit()
    tkwindows.select_windows(select)
    return select


def vehicle_select_id(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    mycursor.execute('select * from vehicle where `sql`.vehicle.vehicle_license_plate = %s', id)
    var = mycursor.fetchone()
    return var


def vehicleUpdate(colunm, var, id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
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


def vehicleAdd(id, data, type, manufacturer):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    add = 'insert into vehicle(vehicle_license_plate, vehicle_date, vehicle_type, vehicle_manufacturer) ' \
          'values (%s, %s, %s, %s)'
    mycursor.execute(add, (id, data, type, manufacturer))
    mydb.commit()


def vehicleDelete(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    delete = 'delete from vehicle where `sql`.vehicle.vehicle_license_plate = %s'
    mycursor.execute(delete, id)
    mydb.commit()



