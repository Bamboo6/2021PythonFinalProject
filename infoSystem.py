class Student:
    def __init__(self):
        # self.stu_info = {"姓名": "1",
        #                  "年龄": "",
        #                  "Python 成绩": ""
        #                  }
        self.stu_dict = {}
        # {
        #     "students": {
        #         "11": {}
        #     },
        #     "teachers": {
        #         "3333"
        #     }
        #
        # }
        # self.stu_dict["students"]["11"]["age"]
        # self.stu_dict["113123"] = {
        #     "age": 11,
        #
        # }
        # {
        #     "11": {
        #         age: 11
        #     },
        #     "22": {
        #         age: 12
        #     }
        # }

    def insert_info(self):
        # stu_info = {"姓名": "",
        #             "年龄": "",
        #             "Python 成绩": ""
        #             }
        while True:
            stu_id = input("请输入学号：")
            if stu_id in self.stu_dict:
                print("学号已存在")
            # self.insert_info()
            else:
                name = input("请输入姓名：")
                age = input("请输入年龄：")
                py_score = input("请输入 Python 成绩：")
                self.stu_dict[stu_id] = {"姓名": name,
                                         "年龄": age,
                                         "Python 成绩": py_score
                                         }
                break

            # stu_info["姓名"] = name
            # stu_info["年龄"] = age
            # stu_info["Python 成绩"] = py_score


# for i in students:
#     if stu_id == i['stu_id']:
#         print("该学号已经存在")
#         return
#     else:
#         self.stu_info["name"] = name
#         self.stu_info["age"] = age
#         self.stu_info["stu_id"] = stu_id
#         self.stu_info["py_score"] = py_score
# temp.append(self.stu_info)

# def get_info(self, opt):
# return self.stu_info[opt]


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
    select = eval(input("请输入操作："))
    return select


# print(Student().get_info("name"))
s = Student()
s.insert_info()
s.insert_info()
print(s.stu_dict)
# if __name__ == "__main__":
#     menu()
