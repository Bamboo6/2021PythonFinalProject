import random
import string
import time

import numpy as np

start = time.perf_counter()
# 生成小写字母
lower_letters = string.ascii_lowercase
# 生成大写字母
upper_letters = string.ascii_uppercase
# 生成所有数字
digits = string.digits
# 激活码单part长度
char_length = 4
# 激活码part数
code_length = 4


# 根据概率随机生成一个字符
def random_char():
    # 依据概率随机数字或字母
    # cha = ""
    # choice_type = np.random.choice([digits, lower_letters, upper_letters], p=[0.2, 0.4, 0.4])
    # cha += random.choice(choice_type)

    choice_type = random.choices(population=[digits, lower_letters, upper_letters],
                                 weights=[0.2, 0.4, 0.4])
    cha = ""
    cha += random.choice("".join(choice_type))
    return cha


def get_part_of_code(n):
    # temp = ""
    # for i in range(n):
    #     # random.seed(random.choice())
    #     result = np.random.choice([digits, letters], p=[0.2, 0.8])
    #     temp = temp + random.choice(result)
    # return temp
    return "".join(random_char() for _ in range(n))
    # return (random_char() for _ in range(n))


def get_code(n):
    # code = ""
    # for i in range(n):
    #     temp = get_part_of_code(4)
    #     if i < (n-1):
    #         code = code + temp + "-"
    # else:
    #     code = code + temp
    # return code[:-1]
    return "-".join(get_part_of_code(char_length) for _ in range(n))
    # return (get_part_of_code(char_length) for _ in range(n))


def get_all_code(n):
    all_code = []
    # test_dict = {}
    i = 0
    while i < n:
        temp = get_code(code_length)
        # if temp in test_dict:
        #     # i -= 1
        #     print("``````")
        #     print(test_dict)
        #     print(temp)
        #     print("---")
        # else:
        #     i += 1
        #     test_dict[temp] = "1"
        if temp not in all_code:
            i += 1
            all_code.append(temp)
            # print("-".join(all_code))
        else:
            print("-".join(all_code) + "-" + temp)
            # i -= 1
            print('重复的激活码: "' + temp + '"已剔除')
    return '\n'.join(all_code)
    # return "\n".join(getCode(codeLength) for i in range(n))
    # return all_code

get_all_code(10000)
# print(get_all_code(1000))

end = time.perf_counter()
print(end - start)
# code = ""
# for i in range(4):
#     temp = ""
#     for j in range(4):
#         p = np.array([0.2, 0.8])
#         result = np.random.choice([digits, letters], p=[0.2, 0.8])
#         temp = temp + random.choice(result)
#     if i < 3:
#         code = code + temp + "-"
#     else:
#         code = code + temp
# print(code)
