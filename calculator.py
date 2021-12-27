import sys
from qt_core import *
from ui.ui_calculator import Ui_MainWindow
from decimal import *


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 初始化显示界面
        super(Calculator, self).__init__()
        self.setupUi(self)
        self.show()
        # 绑定按钮事件
        self.pushButton_0.clicked.connect(lambda: self.button_event(0))
        self.pushButton_1.clicked.connect(lambda: self.button_event(1))
        self.pushButton_2.clicked.connect(lambda: self.button_event(2))
        self.pushButton_3.clicked.connect(lambda: self.button_event(3))
        self.pushButton_4.clicked.connect(lambda: self.button_event(4))
        self.pushButton_5.clicked.connect(lambda: self.button_event(5))
        self.pushButton_6.clicked.connect(lambda: self.button_event(6))
        self.pushButton_7.clicked.connect(lambda: self.button_event(7))
        self.pushButton_8.clicked.connect(lambda: self.button_event(8))
        self.pushButton_9.clicked.connect(lambda: self.button_event(9))
        self.pushButton_point.clicked.connect(lambda: self.point())
        self.pushButton_ac.clicked.connect(lambda: self.all_clean())
        self.pushButton_equal.clicked.connect(lambda: self.equal())
        self.pushButton_del.clicked.connect(lambda: self.delete())
        self.pushButton_plus.clicked.connect(lambda: self.set_operations("+"))
        self.pushButton_subtract.clicked.connect(lambda: self.set_operations("-"))
        self.pushButton_multiply.clicked.connect(lambda: self.set_operations("×"))
        self.pushButton_divide.clicked.connect(lambda: self.set_operations("÷"))
        self.pushButton_pow.clicked.connect(lambda: self.set_operations("^"))
        # 设置输入区无焦点
        self.lineEdit.setFocusPolicy(Qt.NoFocus)
        # 设置临时区与输入区右对齐并水平居中
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lineEdit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.reset_font()

    # 数字按钮
    def button_event(self, value):
        text = self.lineEdit.text()
        if text == "0":
            text = text[:-1]
        self.lineEdit.setText(text + str(value))

    # 小数点按钮
    # Decimal 会自动处理 1. + 2. 这种错误输入，未再不作处理
    def point(self):
        text = self.lineEdit.text()
        if "." not in text:
            self.lineEdit.setText(text + ".")

    # 清除按钮
    def all_clean(self):
        # 重置输入区样式
        self.reset_font()
        # 置空临时区内容
        self.label.setText("")
        # 输入区归 0
        self.lineEdit.setText("0")

    # 等于按钮事件
    def equal(self):
        # 获取输入区与临时区内容
        text = self.lineEdit.text()
        temp = self.label.text()
        # 运算操作字典
        ops = {"+": (lambda x, y: x + y),
               "-": (lambda x, y: x - y),
               "×": (lambda x, y: x * y),
               "÷": (lambda x, y: x / y),
               "^": (lambda x, y: x ** y),
               }
        # 若临时区与输入区皆不为空则进行运算
        if temp != '' and text != '':
            # 删除临时区的空格以及运算符
            # 获取临时区数值并转换为十进制属性以确保运算精度
            temp_value = Decimal(temp[:-1].replace(' ', ''))
            # 获取临时区运算符
            temp_operator = temp[len(temp) - 1]
            # 获取输入区数值并转换为十进制属性以确保运算精度
            text = Decimal(text)
            # 运算结果
            try:
                result = ops[temp_operator](temp_value, text)
                result_list = str(result).split(".")
                # 当结果包含小数点且不为科学计数法时保留7位小数
                if "." in str(result):
                    if "E" not in str(result):
                        if len(result_list[1]) >= 7:
                            result = result.quantize(Decimal('0.0000000'))
                # 结果大于11位转换为科学计数法
                if len(str(result)) > 11:
                    result = "%e" % result
                    # 修改输入区样式便于完整显示内容
                    self.lineEdit.setStyleSheet(u"QLineEdit{\n"
                                                "	color:#ffffff;\n"
                                                "	font: 28pt;\n"
                                                "	background:transparent;\n"
                                                "	border-width:0;\n"
                                                "	border-style:outset;\n"
                                                "	setAlignment:AlignRight;\n"
                                                "}")
                # 临时区置空
                self.label.setText("")
                # 将结果返回到输入区
                self.lineEdit.setText(str(result))
            except DivisionByZero:
                # 若除数为负数则置空临时区并在输入区提示infinite
                self.label.setText("")
                self.lineEdit.setText("inf")

    # 删除按钮事件，删除输入区一个字符
    def delete(self):
        # 重置输入区样式
        self.reset_font()
        # 获取输入区内容
        text = self.lineEdit.text()
        # 当输入区不为空时进行退格，若退格到最后一位则初始化为0
        if text != "":
            text = text[:-1]
            self.lineEdit.setText(text)
            if text == "":
                self.lineEdit.setText("0")

    # 运算符按钮事件
    def set_operations(self, operator):
        # 重置输入区样式
        self.reset_font()
        # 获取输入区与临时区内容
        text = self.lineEdit.text()
        temp = self.label.text()
        # 若临时区与输入区有内容则直接进行运算
        if temp != "" and text != "":
            self.equal()
            self.label.setText(self.lineEdit.text() + " " + operator)
            self.lineEdit.setText('')
        # 若输入区不为空，则将输入区内容与运算符置入临时区
        elif text != '':
            self.label.setText(text + " " + operator)
            self.lineEdit.setText("")
        # 若临时区不为空，则修改运算符
        elif temp != '':
            temp = temp[:-1].replace(" ", "")
            self.label.setText(temp + " " + operator)

    # 重置输入区样式
    def reset_font(self):
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
                                    "	color:#ffffff;\n"
                                    "	font: 35pt;\n"
                                    "	background:transparent;\n"
                                    "	border-width:0;\n"
                                    "	border-style:outset;\n"
                                    "	setAlignment:AlignRight;\n"
                                    "}")


if __name__ == "__main__":
    app = QApplication()
    # 引入字体
    QtGui.QFontDatabase.addApplicationFont("ui/PingFang.ttf")
    ui = Calculator()
    sys.exit(app.exec())
