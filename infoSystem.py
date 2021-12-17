class Student:
    def __init__(self):
        self.stu_dict = {}

    def insert_info(self):
        while True:
            stu_id = input("请输入学号：")
            if stu_id in self.stu_dict:
                print("学号已存在")
            else:
                name = input("请输入姓名：")
                age = input("请输入年龄：")
                py_score = input("请输入 Python 成绩：")
                self.stu_dict[stu_id] = {"姓名": name,
                                         "年龄": age,
                                         "Python 成绩": py_score
                                         }
                break

    def del_info(self):
        while True:
            stu_id = input("请输入学号：")
            if stu_id not in self.stu_dict:
                print("学号不存在")
            else:
                del self.stu_dict[stu_id]
                break

    def alter_info(self):
        while True:
            stu_id = input("请输入学号：")
            if stu_id not in self.stu_dict:
                print("学号不存在")
            else:
                print("请选择需要修改的信息")
                print("1.学号")
                print("2.姓名")
                print("3.年龄")
                print("4.Python 成绩")
                print("5.所有信息")
                while True:
                    opt = eval(input("请选择需要修改的项目："))
                    if opt != 1 and opt != 2 and opt != 3 and opt != 4 and opt != 5:
                        print("输入的选项有误！")
                    else:
                        if opt == 1:
                            while True:
                                new_stu_id = input("请输入新学号")
                                if new_stu_id not in self.stu_dict:
                                    print("学号已存在")
                                else:
                                    self.stu_dict[new_stu_id] = self.stu_dict.pop([stu_id])
                                    break
                            break
                        elif opt == 2:
                            name = input("请输入姓名：")
                            self.stu_dict[stu_id] = {"姓名": name}
                            break
                        elif opt == 3:
                            age = input("请输入年龄:")
                            self.stu_dict[stu_id] = {"年龄": age}
                            break
                        elif opt == 4:
                            py_score = input("请输入 Python 成绩：")
                            self.stu_dict[stu_id] = {"Python 成绩": py_score}
                            break
                        elif opt == 5:
                            while True:
                                stu_id = input("请输入学号：")
                                if stu_id not in self.stu_dict:
                                    print("学号不存在")
                                elif stu_id in self.stu_dict:
                                    name = input("请输入姓名：")
                                    age = input("请输入年龄：")
                                    py_score = input("请输入 Python 成绩：")
                                    self.stu_dict[stu_id] = {"姓名": name,
                                                             "年龄": age,
                                                             "Python 成绩": py_score
                                                             }
                                    break
                            break
            break

    def where_info(self):
        while True:
            stu_id = input("请输入学号：")
            if stu_id not in self.stu_dict:
                print("学号不存在")
            else:
                print(self.stu_dict[stu_id])
                break

    def all_info(self):
        print(self.stu_dict)


def menu():
    print("-" * 30)
    print(" 学生信息管理系统")
    print(" 1:添加学生的信息")
    print(" 2:删除学生的信息")
    print(" 3:修改的信息")
    print(" 4:查询学生的信息")
    print(" 5:遍历学生的信息")
    print(" 6:退出系统")
    print("-" * 30)
    while True:
        select = eval(input("请输入操作："))
        if 1 <= select <= 6:
            return select
        else:
            print("输入的选项有误！")


# print(Student().get_info("name"))
# s = Student()
# s.insert_info()
# s.insert_info()
# print(s.stu_dict)
if __name__ == "__main__":

    s = Student()
    while True:
        opt = menu()
        if opt == 1:
            s.insert_info()
        elif opt == 2:
            s.del_info()
        elif opt == 3:
            s.alter_info()
        elif opt == 4:
            s.where_info()
        elif opt == 5:
            s.all_info()
        elif opt == 6:
            break

