# IMPORTS
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from qt_core import *
from ui.ui_calculator import Ui_MainWindow


# import files_rc

# IMPORT QSS
# from styles import *


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)
        self.show()

        def button_event(value):
            numbers = self.lineEdit.text()
            self.lineEdit.setText(numbers + str(value))
            # self.clearRepeat()
            # print(numbers + str(value))

        self.pushButton_0.clicked.connect(lambda: button_event(0))
        self.pushButton_1.clicked.connect(lambda: button_event(1))
        self.pushButton_2.clicked.connect(lambda: button_event(2))
        self.pushButton_3.clicked.connect(lambda: button_event(3))
        self.pushButton_4.clicked.connect(lambda: button_event(4))
        self.pushButton_5.clicked.connect(lambda: button_event(5))
        self.pushButton_6.clicked.connect(lambda: button_event(6))
        self.pushButton_7.clicked.connect(lambda: button_event(7))
        self.pushButton_8.clicked.connect(lambda: button_event(8))
        self.pushButton_9.clicked.connect(lambda: button_event(9))
        self.pushButton_point.clicked.connect(lambda: button_event('.'))

        # BT CL
        def clearFields():
            self.label.setText('')
            self.lineEdit.setText('')
            self.lineEdit.setFocus()

        self.pushButton_ac.clicked.connect(lambda: clearFields())

        self.pushButton_plus.clicked.connect(lambda: self.setOperations("+"))
        self.pushButton_subtract.clicked.connect(lambda: self.setOperations("-"))
        self.pushButton_multiply.clicked.connect(lambda: self.setOperations("×"))
        self.pushButton_divide.clicked.connect(lambda: self.setOperations("÷"))
        self.pushButton_pow.clicked.connect(lambda: self.setOperations("^"))

        self.pushButton_equal.clicked.connect(lambda: self.returnValue())
        self.pushButton_del.clicked.connect(lambda: self.clearClick())
    # globals()['operator'] = ''

    def setOperations(self, operator):
        value = self.lineEdit.text()
        tempValue = self.label.text()

        if tempValue != '' and value != '':
            join_values = str(tempValue + value).replace(' ', '').replace('÷', '/').replace('×', '*').replace('^', '**')
            result = eval(join_values)
            self.label.setText(str(result) + ' ' + operator)
            self.lineEdit.setText('')
            # globals()['operator'] = operator
        elif value != '':
            self.label.setText(value + ' ' + operator)
            self.lineEdit.setText('')
            # globals()['operator'] = operator
        elif tempValue != '':
            tempValue = tempValue[:-1].replace(' ', '')
            self.label.setText(tempValue + ' ' + operator)
            # globals()['operator'] = operator
        self.lineEdit.setFocus()

    def returnValue(self):
        value = self.lineEdit.text()
        tempValue = self.label.text()

        if tempValue != '' and value != '':
            join_values = str(tempValue + value).replace(' ', '').replace('÷','/').replace('×','*').replace('^', '**')
            result = eval(join_values)
            self.label.setText('')
            self.lineEdit.setText(str(result))
        self.lineEdit.setFocus()
    
    # def clearRepeat(self):
    #     text = str(self.lineEdit.text())
    #     text = text.replace(',', '.').replace('+', '').replace('/', '').replace('*', '').replace('--', '-')
    #     return self.lineEdit.setText(text.replace('..', '.'))

    def clearClick(self):
        values = self.lineEdit.text()
        if values != '':
            values = values[:-1]
            self.lineEdit.setText(values)
        self.lineEdit.setFocus()
    


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # QtGui.QFontDatabase.addApplicationFont('fonts/Roboto-Regular.ttf')
    ui = Calculator()
    sys.exit(app.exec())
