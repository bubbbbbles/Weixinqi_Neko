# 示例框架
import os
import csv
os.getcwd()
os.chdir('/Users/mirai/Documents/大学作业/大一下/程序设计/python文件/Final Project')


def menu():
    print("""
        —————————————————————学生信息管理系统———————————————————————-
        |                                                           |
        |         1 录入学生信息                                    |
        |         2 从文件录入学生信息                              |
        |         3 查找学生信息                                    |
        |         4 删除学生信息                                    |
        |         5 显示所有学生信息                                |
        |         6 清空所有学生信息                                |
        |         0 退出系统                                        |
        |                                                           |
        --------------------------------------------------------------
        """)
class Student():#学生信息的类
    def __init__(self, ID, name, gender, Chinese, Math, English):
        self.ID = ID
        self.name = name
        self.gender = gender
        self.Chinese = Chinese
        self.Math = Math
        self.English = English


def check(student_str):#判别格式正确还是不正确  
    student_list=student_str.strip().split(",")
    if len(student_list)!=6:
        print("输入的信息长度错误")
        return False
    if len(str(student_list[0]))!=5 or (str(student_list[0]))[0]=="0":
        print("输入学号错误，学号:需要时纯数字，5位，第一位不允许为0")
        return False
    if not student_list[1].isalpha():
        print("输入姓名错误，姓名中英均可，长度不限")
        return False
    if student_list[2]=="男" or student_list[2]=="女":
        print("输入性别错误，性别需要是男或者女")
        return False
    if (int(float(student_list[3]))==float(student_list[3]) and float(student_list[3])>=0 and float(student_list[3])<=100):
        print("语文成绩输入错误，语文成绩需要是0-100，整数")
        return False
    if (int(float(student_list[4]))==float(student_list[4]) and float(student_list[4])>=0 and float(student_list[4])<=100):
        print("数学成绩输入错误，数学成绩需要是0-100，整数")
        return False
    if (int(float(student_list[5]))==float(student_list[5]) and float(student_list[5])>=0 and float(student_list[5])<=100):
        print("英语成绩输入错误，英语成绩需要是0-100，整数")
        return False
    else:
        return True
    

def insert(student_list):#录入学生信息
    while(True):
        Str = input('请输入学生信息，格式如"学号，姓名，性别，语文成绩，数学成绩，英语成绩"：')
        if not check(Str):
            print("输入格式不正确,请重新输入")
            continue
        for student in student_list:
            if student.ID==int((Str.split(","))[0]):
                    print("学号已经存在，输入以更新")
                    student.ID==int((Str.split(","))[0])
                    student.name=(Str.split(","))[1]
                    student.gender=(Str.split(","))[2]
                    student.Chinese=int((Str.split(","))[3])
                    student.Math=int((Str.split(","))[4])
                    student.English = int((Str.split(","))[5])
                    break
        else:
            new_student = Student(int((Str.split(","))[0]),(Str.split(","))[1],(Str.split(","))[2],int((Str.split(","))[3]), int((Str.split(","))[4]), int((Str.split(","))[5]))
            student_list.append(new_student)
            print('新学生信息添加成功')
        if_continue = input('继续输入（Y/n）?')
        if if_continue.lower()=='n':
                break
        if if_continue.upper()=='Y':
                continue


def check_condition(search_condition):
    search_condition_list=search_condition.split()
    if "in" in search_condition_list:
        if len(search_condition_list)==4:
            if search_condition_list[1]=="not" and search_condition_list[2]=="in" and (search_condition_list[3]=="学号" or search_condition_list[3]=="姓名" or search_condition_list[3]=="性别" or search_condition_list[3]=="语文成绩" or search_condition_list[3]=="数学成绩" or search_condition_list[3]=="英语成绩"):
                return True
        elif len(search_condition_list)==3:
            if search_condition_list[1]=="in" and (search_condition_list[2]=="学号" or search_condition_list[2]=="姓名" or search_condition_list[2]=="性别" or search_condition_list[2]=="语文成绩" or search_condition_list[2]=="数学成绩" or search_condition_list[2]=="英语成绩"):
                return True
        else:
            return False
    elif len(search_condition_list)!=3:
        return False
    else:
        genre=search_condition_list[0]
        operator=search_condition_list[1]
        value=search_condition_list[2]#可以不用
        if genre not in ["学号","姓名","性别","语文成绩","数学成绩","英语成绩"] or operator not in ["==","!=","<",">",">=","<="]:
            return False
        else:
            return True


def search(student_list):
    search_condition=input("请输入想查找的条件(以空格隔开)")
    if not check_condition(search_condition):
        print("输入条件格式错误")
    if check_condition(search_condition):
        print("输入条件格式正确,查询中")
        search_condition = search_condition.replace("姓名","str(student.name)").replace("学号","student.ID") \
            .replace("性别","str(student.gender)").replace("语文成绩","student.Chinese")\
            .replace("数学成绩","student.Math").replace("英语成绩","student.English")
        search_condition_list=search_condition.split()
        flag=None
        counter=0
        for student in student_list:
            if "not" in search_condition_list:
                if "str(student.name)" in search_condition_list or "str(student.gender)" in search_condition_list:
                    search_condition_list[0]='"'+str((search_condition_list)[0])+'"'
                    search_condition_list=["==" if x=="in" else x for x in search_condition_list]
                    search_condition_list.remove("not")
                    if eval(" ".join(search_condition_list)):
                        flag=False
                        break
                    else:
                        flag=True
                else:
                    new_search_condition=str(eval(search_condition_list[3]))+" == "+str(search_condition_list[0])
                    if eval(new_search_condition):
                        flag=False
                        break
                    else:
                        flag=True

            elif search_condition_list[1]=="in":
                if "str(student.name)" in search_condition_list or "str(student.gender)" in search_condition_list:
                    search_condition_list[0]='"'+str((search_condition_list)[0])+'"'
                    search_condition_list=["==" if x=="in" else x for x in search_condition_list]
                    if eval(" ".join(search_condition_list)):
                        flag=True
                        break
                    else:
                        flag=False
                else:
                    new_search_condition=str(eval(search_condition_list[2]))+" == "+str(search_condition_list[0])
                    if eval(new_search_condition):
                        flag=True
                        break
                    else:
                        flag=False
             
            elif "str(student.name)" in search_condition_list or "str(student.gender)" in search_condition_list:
                search_condition_list[2]='"'+str((search_condition_list)[2])+'"'
                search_condition_list[2]="str("+str((search_condition_list)[2])+")"
                if eval(" ".join(search_condition_list)):
                    print("查询学生存在")
                    print(f"学号：{student.ID} 姓名：{student.name} 性别：{student.gender} 语文成绩：{student.Chinese} 数学成绩：{student.Math} 英语成绩：{student.English}")
                    break       
                else:
                    counter+=1
            else:
                if eval(" ".join(search_condition_list)):
                    print("查询学生存在")
                    print(f"学号：{student.ID} 姓名：{student.name} 性别：{student.gender} 语文成绩：{student.Chinese} 数学成绩：{student.Math} 英语成绩：{student.English}")
                    break
                else:
                    counter+=1
        if flag==True:
            print("查询结果是正确")
        if flag==False:
            print("查询结果是不正确")
        if counter==len(student_list):
            print("查询学生不存在")

        if_continue = input(f"是否要继续查找（Y/n）？")
        if if_continue.lower() == 'n':
            return
        if if_continue.upper() == 'Y':
            search(student_list)
            
                    

def delete(student_list):
    search_condition=input("请输入删除的学生条件（使用比较运算法（>,>=,==,!=,<,<=))")
    if not check_condition(search_condition):
        print("输入条件格式错误")
    if check_condition(search_condition):
        print("输入条件格式正确,查询中")
        search_condition = search_condition.replace("姓名","str(student.name)").replace("学号","student.ID") \
            .replace("性别","str(student.gender)").replace("语文成绩","student.Chinese")\
            .replace("数学成绩","student.Math").replace("英语成绩","student.English")
        search_condition_list=search_condition.split()
        if "str(student.name)" in search_condition_list or "str(student.gender)" in search_condition_list:
            search_condition_list[2]='"'+str((search_condition_list)[2])+'"'

        counter=0
        for student in student_list:
            if "str(student.name)" in search_condition_list or "str(student.gender)" in search_condition_list:
                search_condition_list[2]="str("+str(search_condition_list[2])+")"
                if eval(" ".join(search_condition_list)):
                    if_continue=input("查询学生存在，是否移除？(Y/n)")
                    if if_continue.lower()=='n':
                        break
                    if if_continue.upper()=='Y':
                        counter+=1
                        student_list.remove(student)
                        print("学生存在并已移除")
            else:
                if eval(" ".join(search_condition_list)):
                    if_continue=input("查询学生存在，是否移除？(Y/n)")
                    if if_continue.lower()=='n':
                        break
                    if if_continue.upper()=='Y':
                        counter+=1
                        student_list.remove(student)
                        print("学生存在并已移除")
        if counter== 0:
            print("查询学生不存在")


def print_all(student_list):
    for student in student_list:
        print(f"学号：{student.ID} 姓名：{student.name} 性别：{student.gender} 语文成绩：{student.Chinese} 数学成绩：{student.Math} 英语成绩：{student.English}")


def delete_all(student_list):
    if_continue=input('请确认（Y/n）')
    if if_continue.upper()=="Y":
        student_list.clear()
        print("已清除所有信息")
    elif if_continue.lower()=="n":
        print("已结束清除")
    else:
        print("清除确认输入错误")


def save(student_list):
    with open("./student.csv",mode='w') as f:
        f_csv= csv.writer(f)
        for student in student_list:
            f_csv.writerow([student.ID,student.name,student.gender,student.Chinese,student.Math,student.English])
    print("已保存至文件'student.csv'")


def insert_file(student_list):
    filename=input("请输入文件名")#文件储存要在同一级：file1.csv是正确的，file2.csv是错误的内容
    try:
        with open(filename,mode="r") as f:
            f_csv= csv.reader(f, delimiter=",")
            for new_student in f_csv:
                if check(",".join(new_student)):
                    for student in student_list:
                        if int((new_student)[0]) == student.ID:
                            print("学号已存在，以新导入的为准")
                            student.name=new_student[1]
                            student.gender=new_student[2]
                            student.Chinese=int(new_student[3])
                            student.Math=int(new_student[4])
                            student.English=int(new_student[5])
                            print("已更新")
                            break
                    else:
                        student_list.append(Student(int(new_student[0]),new_student[1],new_student[2],int(new_student[3]),int(new_student[4]),int(new_student[5])))
                else:
                    print("文件输入内容有一行内容错误")
        print("录入结束")
    except FileNotFoundError:
        print("文件不存在")
    except:
        print("存在其他错误")


def detect_file(student_list):
    filename="file_start.csv"
    try:
        with open(filename,mode="r",encoding="utf-8") as f:
            f_csv = csv.reader(f, delimiter=",")
            for new_student in f_csv:
                if check(",".join(new_student)):
                    student_list.append(Student(int(new_student[0]), new_student[1], new_student[2],
                                                int(new_student[3]), int(new_student[4]), int(new_student[5])))
                else:
                    print("文件输入格式有一行内容内容错误")
            print("已导入外部文件")
    except FileNotFoundError:
        print("文件不存在")
    except:
        print("存在其他错误")


def main():
    print("*****欢迎登陆学生信息管理系统*****")
    flag_on = True
    student_list=[]
    detect_file(student_list)
    while flag_on:
        menu()  # 显示页面菜单
        option = (input("请选择："))  # 选择菜单项
        if option == '0':  # 退出选择界面
            save(student_list)
            print("您已经退出学生信息管理系统！")
            flag_on = False
        elif option == '1':  # 录入学生成绩信息
            insert(student_list)
        elif option == '2':  # 文件录入
            insert_file(student_list)
        elif option == '3':  # 查询学生成绩信息
            search(student_list)
        elif option == '4':  # 删除学生成绩信息
            delete(student_list)
        elif option == '5':  # 显示所有学生信息
            print_all(student_list)
        elif option == '6':  # 清空所有信息
            delete_all(student_list)
        else:
            print("输入错误，请重新输入")


if __name__ == "__main__":
    main()