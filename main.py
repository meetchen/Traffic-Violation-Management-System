import pymysql
import driver
import NOTICEDEMO
# driver.driver()
# driver.driverAdd('袁博文', 184845451, '西安科技大学临潼校区', '7926')


def driveradd():
    name = input("请输入用户名")
    phone = input("请输入电话")
    address = input("请输入地址")
    post_code = input("请输入邮政编码")
    print(name, phone, address, post_code)
    driver.driverAdd(name, phone, address, post_code)


def driverupdate():

    column = input("请输入需要修改的列名")
    name = input("请输入修改的目标值")
    id = input("请输入属性列对应的序号")
    driver.diverUpdate(column, name, id)


def driverdelete():

    id = input("请输入要删除的属性列的对应序号")
    driver.diverDelete(id)



NOTICEDEMO.tuple_funciton()