import random
import string
import sys

from qt_core import *
from ui.ui_activationCode import Ui_MainWindow


# import time

# start = time.perf_counter()
class ActivationCode(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 初始化显示界面
        super(ActivationCode, self).__init__()
        self.setupUi(self)
        self.show()

        # 生成小写字母
        self.lower_letters = string.ascii_lowercase
        # 生成大写字母
        self.upper_letters = string.ascii_uppercase
        # 生成所有数字
        self.digits = string.digits
        # 激活码单part长度
        self.char_length = int(self.lineEdit_char.text())
        # 激活码part数
        self.code_length = int(self.lineEdit_part.text())
        # 数字概率
        self.digits_pr = int(self.lineEdit_digits.text())
        # 小写字母概率
        self.lower_letters_pr = int(self.lineEdit_low_letters.text())
        # 大写字母概率
        self.upper_letters_pr = int(self.lineEdit_up_letters.text())
        self.lineEdit_result.setText(self.get_code(self.code_length))
        # 绑定按钮事件
        self.pushButton_preview.clicked.connect(lambda: self.preview())
        self.pushButton_generate.clicked.connect(lambda: self.button_event(0))
        # 设置预览框无焦点
        self.lineEdit_result.setFocusPolicy(Qt.NoFocus)
        self.lineEdit_result.setAlignment(Qt.AlignHCenter)

    # 根据概率随机生成一个字符
    def random_char(self):
        # 依据概率随机数字或字母
        choice_type = random.choices(population=[self.digits, self.lower_letters, self.upper_letters],
                                     weights=[self.digits_pr, self.lower_letters_pr, self.upper_letters_pr])
        cha = ""
        cha += random.choice("".join(choice_type))
        return cha

    def get_part_of_code(self, n):
        # temp = ""
        # for i in range(n):
        #     # random.seed(random.choice())
        #     result = np.random.choice([digits, letters], p=[0.2, 0.8])
        #     temp = temp + random.choice(result)
        # return temp
        return "".join(self.random_char() for _ in range(n))
        # return (random_char() for _ in range(n))

    # 预览
    def preview(self):
        code = self.get_code(self.code_length)
        self.lineEdit_result.setText(code)

    def get_code(self, n):
        # 激活码单part长度
        self.char_length = int(self.lineEdit_char.text())
        # 激活码part数
        self.code_length = int(self.lineEdit_part.text())
        # 数字概率
        self.digits_pr = int(self.lineEdit_digits.text())
        # 小写字母概率
        self.lower_letters_pr = int(self.lineEdit_low_letters.text())
        # 大写字母概率
        self.upper_letters_pr = int(self.lineEdit_up_letters.text())
        code = "-".join(self.get_part_of_code(self.char_length) for _ in range(n))
        # code = ""
        # for i in range(n):
        #     temp = get_part_of_code(4)
        #     if i < (n-1):
        #         code = code + temp + "-"
        # else:
        #     code = code + temp
        # return code[:-1]
        return code
        # return (get_part_of_code(char_length) for _ in range(n))

    def get_all_code(self, n):
        all_code = []
        # test_dict = {}
        i = 0
        while i < n:
            temp = self.get_code(self.code_length)
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

    # get_all_code(10)
    # print(get_all_code(10))

    # end = time.perf_counter()
    # print(end - start)
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


if __name__ == "__main__":
    # 高分屏适配
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication()
    # 引入字体
    QtGui.QFontDatabase.addApplicationFont('ui/PingFang.ttf')
    ui = ActivationCode()
    sys.exit(app.exec())
