import os
import random
import string
import sys
from qt_core import *
from ui.ui_activationCode import Ui_MainWindow
from ui.ui_warn import Ui_WarnWindow


class ActivationCode(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 初始化显示界面
        super(ActivationCode, self).__init__()
        self.setupUi(self)
        self.show()

        # 警告窗口初始化
        self.child_init = ChildWindow()
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
        # 数字权重
        self.digits_pr = int(self.lineEdit_digits.text())
        # 小写字母权重
        self.lower_letters_pr = int(self.lineEdit_low_letters.text())
        # 大写字母权重
        self.upper_letters_pr = int(self.lineEdit_up_letters.text())
        # 预览
        self.lineEdit_result.setText(self.get_code())
        # 绑定按钮事件
        self.pushButton_preview.clicked.connect(lambda: self.preview())
        self.pushButton_generate.clicked.connect(lambda: self.get_all_code())
        # 设置预览框无焦点
        self.lineEdit_result.setFocusPolicy(Qt.NoFocus)
        # 设置输入框水平居中
        self.lineEdit_result.setAlignment(Qt.AlignHCenter)
        self.lineEdit_num.setAlignment(Qt.AlignHCenter)
        self.lineEdit_char.setAlignment(Qt.AlignHCenter)
        self.lineEdit_up_letters.setAlignment(Qt.AlignHCenter)
        self.lineEdit_low_letters.setAlignment(Qt.AlignHCenter)
        self.lineEdit_digits.setAlignment(Qt.AlignHCenter)
        self.lineEdit_part.setAlignment(Qt.AlignHCenter)

    # 根据概率随机生成一个字符
    def random_char(self):
        # 依据权重随机数字或字母
        choice_type = random.choices(population=[self.digits, self.lower_letters, self.upper_letters],
                                     weights=[self.digits_pr, self.lower_letters_pr, self.upper_letters_pr])
        cha = ""
        cha += random.choice("".join(choice_type))
        return cha

    # 获取一个部分的激活码
    def get_part_of_code(self, n):
        return "".join(self.random_char() for _ in range(n))

    # 获取一条完整激活码
    def get_code(self):
        # 输入内容有误异常捕获
        try:
            # 激活码单part长度
            self.char_length = int(self.lineEdit_char.text())
            # 激活码part数
            self.code_length = int(self.lineEdit_part.text())
            # 数字权重
            self.digits_pr = int(self.lineEdit_digits.text())
            # 小写字母权重
            self.lower_letters_pr = int(self.lineEdit_low_letters.text())
            # 大写字母权重
            self.upper_letters_pr = int(self.lineEdit_up_letters.text())
            code = "-".join(self.get_part_of_code(self.char_length) for _ in range(self.code_length))
            return code
        except ValueError:
            # 输入内容有误弹出警告窗口
            self.child_init.show()

    # 预览
    def preview(self):
        code = self.get_code()
        self.lineEdit_result.setText(code)

    # 生产大量激活码
    def get_all_code(self):
        try:
            # 获取生成数量
            num = int(self.lineEdit_num.text())
            all_code = []
            i = 0
            count_num = 0
            while i < num:
                temp = self.get_code()
                if temp not in all_code:
                    i += 1
                    all_code.append(temp)
                else:
                    count_num += 1
                    # 重复的激活码太多则跳出
                    if count_num >= 100:
                        self.child_init.show()
                        break
            if count_num < 100:
                # 生成完成后将结果写入记事本并打开
                with open("ActivationCode.txt", "w") as f:
                    f.write('\n'.join(all_code))
                os.system("notepad ActivationCode.txt")
        except ValueError:
            # 生成数量输入有误则弹出警告窗口
            self.child_init.show()


# 创建警告窗口类
class ChildWindow(QMainWindow, Ui_WarnWindow):
    def __init__(self):
        super(ChildWindow, self).__init__()
        # 引入警告窗口类
        self.ui = Ui_WarnWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication()
    # 引入字体
    QtGui.QFontDatabase.addApplicationFont('ui/PingFang.ttf')
    ui = ActivationCode()
    sys.exit(app.exec())
