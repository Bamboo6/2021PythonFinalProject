# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatorUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(338, 399)
        Form.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout.addWidget(self.textEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_AC = QPushButton(Form)
        self.pushButton_AC.setObjectName(u"pushButton_AC")

        self.gridLayout.addWidget(self.pushButton_AC, 0, 0, 1, 1)

        self.pushButton_18 = QPushButton(Form)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout.addWidget(self.pushButton_18, 0, 1, 1, 1)

        self.pushButton_17 = QPushButton(Form)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout.addWidget(self.pushButton_17, 0, 2, 1, 1)

        self.pushButton_divide = QPushButton(Form)
        self.pushButton_divide.setObjectName(u"pushButton_divide")

        self.gridLayout.addWidget(self.pushButton_divide, 0, 3, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_multiply = QPushButton(Form)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")

        self.gridLayout.addWidget(self.pushButton_multiply, 1, 3, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_subtract = QPushButton(Form)
        self.pushButton_subtract.setObjectName(u"pushButton_subtract")

        self.gridLayout.addWidget(self.pushButton_subtract, 2, 3, 1, 1)

        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_plus = QPushButton(Form)
        self.pushButton_plus.setObjectName(u"pushButton_plus")

        self.gridLayout.addWidget(self.pushButton_plus, 3, 3, 1, 1)

        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.gridLayout.addWidget(self.pushButton_0, 4, 0, 1, 2)

        self.pushButton_point = QPushButton(Form)
        self.pushButton_point.setObjectName(u"pushButton_point")

        self.gridLayout.addWidget(self.pushButton_point, 4, 2, 1, 1)

        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 4, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)
        self.pushButton_AC.clicked.connect(self.textEdit.clear)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_AC.setText(QCoreApplication.translate("Form", u"AC", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"\u00b1", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"%", None))
        self.pushButton_divide.setText(QCoreApplication.translate("Form", u"\u00f7", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_subtract.setText(QCoreApplication.translate("Form", u"\uff0d", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_plus.setText(QCoreApplication.translate("Form", u"\uff0b", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_point.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi

