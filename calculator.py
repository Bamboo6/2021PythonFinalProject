import sys
from qt_core import *
from ui.ui_calculator import Ui_MainWindow
from decimal import *
import re


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        # self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setupUi(self)
        self.show()

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

        self.lineEdit.setFocusPolicy(Qt.NoFocus)

    def button_event(self, value):
        numbers = self.lineEdit.text()
        self.lineEdit.setText(numbers + str(value))
        # self.clearRepeat()

    def all_clean(self):
        self.label.setText('')
        self.lineEdit.setText('')
        # self.lineEdit.setFocus()

    def equal(self):
        text = self.lineEdit.text()
        temp = self.label.text()
        ops = {"+": (lambda x, y: x + y),
               "-": (lambda x, y: x - y),
               "×": (lambda x, y: x * y),
               "÷": (lambda x, y: x / y),
               "^": (lambda x, y: x ** y),
               }

        if temp != '' and text != '':
            temp_value = Decimal(temp[:-1].replace(' ', ''))
            temp_operator = temp[len(temp) - 1]
            text = Decimal(text)
            result = ops[temp_operator](temp_value, text)
            # join_values = str(temp + text).replace(' ', '').replace('÷', '/').replace('×', '*').replace('^', '**')
            # result = eval(join_values)
            # result = Decimal(result).quantize(Decimal('0.00000000'))
            # result = float(Decimal(result))
            # result = re.sub(r"0*$", "", str(result))
            if len(str(result)) >= 11:
                result = "%e" % result
            self.label.setText('')
            self.lineEdit.setText(str(result))
        # self.lineEdit.setFocus()

    # def clearRepeat(self):
    #     text = str(self.lineEdit.text())
    #     text = text.replace(',', '.').replace('+', '').replace('/', '').replace('*', '').replace('--', '-')
    #     return self.lineEdit.setText(text.replace('..', '.'))

    def delete(self):
        text = self.lineEdit.text()
        if text != '':
            values = text[:-1]
            self.lineEdit.setText(values)
        # self.lineEdit.setFocus()

    def set_operations(self, operator):
        text = self.lineEdit.text()
        temp = self.label.text()
        if temp != '' and text != '':
            operation = str(temp + text).replace(' ', '').replace('÷', '/').replace('×', '*').replace('^', '**')
            result = eval(operation)
            self.label.setText(str(result) + ' ' + operator)
            self.lineEdit.setText('')
        elif text != '':
            self.label.setText(text + ' ' + operator)
            self.lineEdit.setText('')
        elif temp != '':
            temp = temp[:-1].replace(' ', '')
            self.label.setText(temp + ' ' + operator)
        # self.lineEdit.setFocus()


if __name__ == "__main__":
    app = QApplication()
    QtGui.QFontDatabase.addApplicationFont('ui/PingFang.ttf')
    ui = Calculator()
    sys.exit(app.exec())
