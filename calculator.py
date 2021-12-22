import sys
from qt_core import *
from ui.ui_calculator import Ui_MainWindow
from decimal import *


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 初始化显示界面
        super(Calculator, self).__init__()
        # self.setWindowFlags(Qt.CustomizeWindowHint)
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
        self.pushButton_point.clicked.connect(lambda: self.button_event('.'))
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

    # 数字按钮事件
    def button_event(self, value):
        numbers = self.lineEdit.text()
        self.lineEdit.setText(numbers + str(value))

    # 清除按钮事件
    def all_clean(self):
        self.label.setText('')
        self.lineEdit.setText('')

    # 等于按钮事件
    def equal(self):
        # 获取临时区内容与当前输入区内容
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
            result = ops[temp_operator](temp_value, text)
            # 结果超出长度后转换为科学计数法
            if len(str(result)) >= 11:
                result = "%e" % result
            # 临时区置空
            self.label.setText('')
            # 将结果返回到输入区
            self.lineEdit.setText(str(result))

    # 删除按钮事件，删除输入区一个字符
    def delete(self):
        text = self.lineEdit.text()
        if text != '':
            values = text[:-1]
            self.lineEdit.setText(values)

    # 运算符按钮事件
    def set_operations(self, operator):
        text = self.lineEdit.text()
        temp = self.label.text()
        # 若临时区与输入区有内容则直接进行运算
        if temp != '' and text != '':
            self.equal()
            self.label.setText(self.lineEdit.text() + ' ' + operator)
            self.lineEdit.setText('')
        # 若输入区不为空，则将输入区内容与运算符置入临时区
        elif text != '':
            self.label.setText(text + ' ' + operator)
            self.lineEdit.setText('')
        # 若临时区不为空，则修改运算符
        elif temp != '':
            temp = temp[:-1].replace(' ', '')
            self.label.setText(temp + ' ' + operator)


if __name__ == "__main__":
    # 高分屏适配
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication()
    # 引入字体
    QtGui.QFontDatabase.addApplicationFont('ui/PingFang.ttf')
    ui = Calculator()
    sys.exit(app.exec())
