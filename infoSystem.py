import os


class Student:
    def __init__(self):
        self.stu_dict = {}

    def insert_info(self):
        while True:
            print("-----P.S.返回上一层请输入exit-----")
            stu_id = input("请输入学号：")
            if stu_id == "exit":
                break
            elif stu_id in self.stu_dict:
                print("学号已存在")
            else:
                name = input("请输入姓名：")
                if name == "exit":
                    break
                age = input("请输入年龄：")
                if age == "exit":
                    break
                score = input("请输入成绩：")
                if score == "exit":
                    break
                self.stu_dict[stu_id] = {"姓名": name,
                                         "年龄": age,
                                         "成绩": score
                                         }

    def del_info(self):
        while True:
            print("-----P.S.返回上一层请输入exit-----")
            stu_id = input("请输入学号：")
            if stu_id == "exit":
                break
            elif stu_id not in self.stu_dict:
                print("学号不存在！（返回上一层请输入exit）")
            else:
                del self.stu_dict[stu_id]
                break

    def alter_info(self):
        while True:
            print("-----P.S.返回上一层请输入exit-----")
            stu_id = input("请输入学号：")
            if stu_id == "exit":
                break
            elif stu_id not in self.stu_dict:
                print("学号不存在！")
            else:
                print("请选择需要修改的信息")
                print("1.学号")
                print("2.姓名")
                print("3.年龄")
                print("4.成绩")
                print("5.所有信息")
                while True:
                    try:
                        opt = int(input("请选择需要修改的项目："))
                        if opt < 1 or opt > 5:
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
                                score = input("请输入成绩：")
                                self.stu_dict[stu_id] = {"成绩": score}
                                break
                            elif opt == 5:
                                while True:
                                    stu_id = input("请输入学号：")
                                    if stu_id not in self.stu_dict:
                                        print("学号不存在")
                                    elif stu_id in self.stu_dict:
                                        name = input("请输入姓名：")
                                        age = input("请输入年龄：")
                                        score = input("请输入成绩：")
                                        self.stu_dict[stu_id] = {"姓名": name,
                                                                 "年龄": age,
                                                                 "成绩": score
                                                                 }
                                        break
                                break
                    except ValueError:
                        print("输入的内容有误！")
            break

    def where_info(self):
        while True:
            print("-----P.S.查询所有信息请输入all，返回上一层请输入exit-----")
            stu_id = input("请输入学号：")
            if stu_id == "all":
                print('\n'.join(self.get_all_info()))
            elif stu_id == "exit":
                break
            elif stu_id not in self.stu_dict:
                print("学号不存在！")
            else:
                print(self.stu_dict[stu_id])

    def get_all_info(self):
        info_output = []
        for i in self.stu_dict:
            # print(i)
            if len(info_output) == 0:
                header = list(self.stu_dict[i].keys())
                # if header:
                header.insert(0, "学号")
                header = "\t".join(header)
                info_output.append(header)
                # else:
                #     info_output = ["系统无数据！"]
                #     break
            if not self.stu_dict[i].values():
                value = "null"
            else:
                value = list(self.stu_dict[i].values())
                value.insert(0, i)
                value = "\t".join(value)
            info_output.append(value)
        return info_output

    def all_info(self):
        if self.stu_dict:
            info_output = self.get_all_info()
            # print("\n".join(info_output))
        else:
            info_output = ["系统无数据！"]
        with open("StuInfoSystem.txt", "w") as f:
            f.write('\n'.join(info_output))
        os.system("notepad StuInfoSystem.txt")


def menu():
    print("-" * 20)
    print("   学生信息管理系统")
    print("-" * 20)
    print("1:添加学生的信息")
    print("2:删除学生的信息")
    print("3:修改的信息")
    print("4:查询学生的信息")
    print("5:输出所有学生的信息")
    print("6:退出系统")
    print("-" * 20)
    while True:
        try:
            select = int(input("请输入操作："))
            if 1 <= select <= 6:
                return select
            else:
                print("输入的选项有误！")
        except ValueError:
            print("输入的内容有误！")


if __name__ == "__main__":
    s = Student()
    while True:
        opt_main = menu()
        if opt_main == 1:
            s.insert_info()
        elif opt_main == 2:
            s.del_info()
        elif opt_main == 3:
            s.alter_info()
        elif opt_main == 4:
            s.where_info()
        elif opt_main == 5:
            s.all_info()
        elif opt_main == 6:
            break
