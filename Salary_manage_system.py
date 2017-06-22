# -*- Coding: utf-8 -*-
# Author: Yu

def inquire_salary(user_name):  # 查询工资函数
    f_inquire = open("info", "r", encoding="utf-8")
    f_inquire_list = f_inquire.readlines()  # 将文件内容转化为列表形式
    # ["Alex 100000\n", "Rain 80000\n", "Egon 50000\n", "Yuan 30000\n"]
    for i in range(len(f_inquire_list)):
        f_inquire_list[i] = f_inquire_list[i].split(" ")  # 再将列表的元素转化为列表
        # [["Alex", "100000\n"], ["Rain", "80000\n"], ["Egon", "50000\n"], ["Yuan", "30000\n"]]
        if user_name in f_inquire_list[i]:  # 判断查询的用户是否在该列表中
            salary = f_inquire_list[i][1].strip()  # 取出工资
            print("%s 的工资是: %s" % (user_name, salary))
    f_inquire.close()

def change_salary(change_word):  #修改员工工资函数
    change_word_list = change_word.split(" ")
    change_word_name = change_word_list[0]
    change_word_salary = change_word_list[1]
    # 将用户输入的修改员工名字和需要修改的金额进行解析
    f_data = ""
    f_change = open("info", "r", encoding="utf-8")
    for line_change in f_change:
        if change_word_name in line_change:  # 如果该用户在该行，这将这行替换为新的员工名字和工资
            line_change = line_change.replace(line_change, change_word_name+" "+change_word_salary+"\n")
        f_data += line_change
    f_change = open("info", "w", encoding="utf-8")
    f_change.write(f_data)
    print("修改成功！")
    f_change.close()

def increase_staff(staff_info):  #增加新员工函数
    f_increase = open("info", "a", encoding="utf-8")  #直接将增加的员工追加在文件后面
    f_increase.write(staff_info)
    f_increase.close()

while True:
    Screen = '''-------------------------------
            1. 查询员工工资;
            2. 修改员工工资;
            3. 增加新员工记录;
            4. 退出
            --------------------------------'''
    print(Screen)
    choice = input(">>: ")
    if choice == "1":
        user_name = input("请输入要查询的员工姓名（例如：Alex）:")
        f_search = open("info", "r", encoding="utf-8")
        f_inquire_str = f_search.read()
        if user_name in f_inquire_str:  # 如果输入的员工在文件中则调用查询员工函数
            inquire_salary(user_name)
        else:  # 如果该员工不在文件中
            print("该用户不存在,请重新输入。")
        f_search.close()
    elif choice == "2":
        change_word = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：")
        change_word_list = change_word.split(" ")
        f_chang = open("info", "r", encoding="utf-8")
        f_chang_str = f_chang.read()
        if change_word_list[0] in f_chang_str:  # 将输入的名字和工资解析出来，用名字去查询是否在文件中
            change_salary(change_word)  # 调用修改员工工资函数
        else:
            print("该用户不存在，请确认之后再输入!")
        f_chang.close()
    elif choice == "3":
        staff_info = input("请输入要增加的员工姓名和工资，共空格分割（例如：Eric 100000）：")
        staff_info_list = staff_info.split(" ")
        f_staff = open("info", "r", encoding="utf-8")
        f_staff_str = f_staff.read()
        if staff_info_list[0] in f_staff_str:  # 将输入的解析为列表，用名字去判断是否在文件中，如果在，则打印提示
            print("你需要增加的员工已经存在!")
        else:  # 如果该员工不在文件中，则调用增加员工函数
            increase_staff(staff_info)
            print("添加员工成功!")
    elif choice == "4":  # 退出
        print("再见！")
        break