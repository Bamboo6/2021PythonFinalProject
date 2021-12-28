import os


class Student:
    def __init__(self):
        self.stu_dict = {}

    # 新增信息
    def insert_info(self):
        while True:
            print("-----P.S.返回上一层请输入exit-----")
            stu_id = input("请输入学号：")
            # 直到输入exit才跳出新增信息方法，便于一次添加多条信息
            if stu_id == "exit":
                break
            elif stu_id in self.stu_dict:
                print("******学号已存在！******")
            else:
                name = input("请输入姓名：").replace(" ", "")

                if name == "exit":
                    break
                elif name == "":
                    name = "null"
                age = input("请输入年龄：").replace(" ", "")
                if age == "exit":
                    break
                elif age == "":
                    age = "null"
                score = input("请输入成绩：").replace(" ", "")
                if score == "exit":
                    break
                elif score == "":
                    score = "null"
                # 将新增学生信息以学号为键名，其他内容封装为一个新的字典作为为键值存入字典
                self.stu_dict[stu_id] = {"姓名": name,
                                         "年龄": age,
                                         "成绩": score
                                         }

    def del_info(self):
        while True:
            # 直到输入exit才跳出删除信息方法，便于一次删除多条信息
            print("-----P.S.删除所有信息请输入all，返回上一层请输入exit-----")
            stu_id = input("请输入学号：")
            if stu_id == "exit":
                break
            elif stu_id == "all":
                yn = input("!!!!!!此操作将清空所有学生信息，请输入Y继续：")
                if yn == "Y" or yn == "y":
                    print("所有学生信息已删除")
                    self.stu_dict.clear()
                    break
                else:
                    print("删除操作已取消")
            elif stu_id not in self.stu_dict:
                print("学号不存在！")
            else:
                yn = input("!!!!!!此操作将删除学号为：" + stu_id + " 的学生的所有信息，请输入Y继续：")
                if yn == "Y" or yn == "y":
                    print("学号为：" + stu_id + " 的信息已删除")
                    del self.stu_dict[stu_id]
                else:
                    print("删除操作已取消")

    def alter_menu(self, stu_id):
        print(stu_id, self.stu_dict[stu_id])
        print("请选择需要修改的信息")
        print("1.学号")
        print("2.姓名")
        print("3.年龄")
        print("4.成绩")
        while True:
            # 输入内容错误异常捕获
            try:
                opt = int(input("请选择需要修改的项目："))
                if opt < 1 or opt > 4:
                    print("******输入的选项有误！******")
                else:
                    # 修改学号
                    if opt == 1:
                        while True:
                            new_stu_id = input("请输入新学号：").replace(" ", "")
                            if new_stu_id == "exit":
                                break
                            elif new_stu_id in self.stu_dict:
                                print("******学号已存在！******")
                            elif new_stu_id == "":
                                print("******学号不可为空！******")
                            else:
                                self.stu_dict[new_stu_id] = self.stu_dict[stu_id]
                                del self.stu_dict[stu_id]
                                stu_id = new_stu_id
                                print(stu_id, self.stu_dict[stu_id])
                                break
                        break
                    # 修改姓名
                    elif opt == 2:
                        name = input("请输入姓名：").replace(" ", "")
                        if name == "":
                            name = "null"
                        self.stu_dict[stu_id] = {"姓名": name}
                        print(stu_id, self.stu_dict[stu_id])
                        break
                    # 修改年龄
                    elif opt == 3:
                        age = input("请输入年龄:").replace(" ", "")
                        if age == "":
                            age = "null"
                        self.stu_dict[stu_id] = {"年龄": age}
                        print(stu_id, self.stu_dict[stu_id])
                        break
                    # 修改成绩
                    elif opt == 4:
                        score = input("请输入成绩：").replace(" ", "")
                        if score == "":
                            score = "null"
                        self.stu_dict[stu_id] = {"成绩": score}
                        print(stu_id, self.stu_dict[stu_id])
                        break
            except ValueError:
                print("******输入的内容有误！******")

    def alter_info(self):
        while True:
            # 直到输入exit才跳出修改信息方法，便于一次修改多条信息
            print("-----P.S.返回上一层请输入exit-----")
            stu_id = input("请输入学号：")
            if stu_id == "exit":
                break
            elif stu_id not in self.stu_dict:
                print("******学号不存在！******")
            else:
                self.alter_menu(stu_id)

    # insert("asd" , 18)
    # enhanceInsert(self,dir):
    #     return insert(dir.name , dir.age)
    # aa = onSucess(self.get_all_info);
    # bb = onSucess(self.get_one_info);
    # 判断学生信息字典是否为空
    def is_empty(self, fun):
        if self.stu_dict:
            return fun()
        else:
            print("******系统无数据！请先添加数据！******")

    def get_all_info(self):
        info_output = []
        for i in self.stu_dict:
            if len(info_output) == 0:
                header = list(self.stu_dict[i].keys())
                header.insert(0, "学号")
                header = "\t".join(header)
                info_output.append(header)
            if not self.stu_dict[i].values():
                value = "null"
            else:
                value = list(self.stu_dict[i].values())
                value.insert(0, i)
                value = "\t".join(value)
            info_output.append(value)
        return info_output

    def where_info(self):
        while True:
            print("-----P.S.查询所有信息请输入all，返回上一层请输入exit-----")
            stu_id = input("请输入学号：")
            if stu_id == "all":
                print('\n'.join(self.get_all_info()))
            elif stu_id == "exit":
                break
            elif stu_id not in self.stu_dict:
                print("******学号不存在！******")
            else:
                print(self.stu_dict[stu_id])

    def all_info(self):
        info_output = self.get_all_info()
        with open("StuInfoSystem.txt", "w") as f:
            f.write('\n'.join(info_output))
        os.system("notepad StuInfoSystem.txt")


def menu():
    print("-" * 22)
    print("\t" + "学生信息管理系统")
    print("-" * 22)
    print("1:添加学生的信息")
    print("2:删除学生的信息")
    print("3:修改的信息")
    print("4:查询学生的信息")
    print("5:导出所有学生的信息")
    print("0:退出系统")
    print("-" * 22)
    while True:
        try:
            select = int(input("请输入操作："))
            if 0 <= select <= 5:
                return select
            else:
                print("******输入的选项有误！******")
        except ValueError:
            print("******输入的内容有误！******")


if __name__ == "__main__":
    s = Student()
    while True:
        opt_main = menu()
        if opt_main == 1:
            s.insert_info()
        elif opt_main == 2:
            s.is_empty(s.del_info)
        elif opt_main == 3:
            s.is_empty(s.alter_info)
        elif opt_main == 4:
            s.is_empty(s.where_info)
        elif opt_main == 5:
            s.is_empty(s.all_info)
        elif opt_main == 0:
            break
