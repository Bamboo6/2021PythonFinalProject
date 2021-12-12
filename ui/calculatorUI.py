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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 263)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(MainWindow)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_ac = QPushButton(MainWindow)
        self.pushButton_ac.setObjectName(u"pushButton_ac")

        self.gridLayout.addWidget(self.pushButton_ac, 0, 0, 1, 1)

        self.pushButton_del = QPushButton(MainWindow)
        self.pushButton_del.setObjectName(u"pushButton_del")

        self.gridLayout.addWidget(self.pushButton_del, 0, 1, 1, 1)

        self.pushButton_pow = QPushButton(MainWindow)
        self.pushButton_pow.setObjectName(u"pushButton_pow")

        self.gridLayout.addWidget(self.pushButton_pow, 0, 2, 1, 1)

        self.pushButton_divide = QPushButton(MainWindow)
        self.pushButton_divide.setObjectName(u"pushButton_divide")

        self.gridLayout.addWidget(self.pushButton_divide, 0, 3, 1, 1)

        self.pushButton_7 = QPushButton(MainWindow)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(MainWindow)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(MainWindow)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_multiply = QPushButton(MainWindow)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")

        self.gridLayout.addWidget(self.pushButton_multiply, 1, 3, 1, 1)

        self.pushButton_4 = QPushButton(MainWindow)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(MainWindow)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(MainWindow)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_subtract = QPushButton(MainWindow)
        self.pushButton_subtract.setObjectName(u"pushButton_subtract")

        self.gridLayout.addWidget(self.pushButton_subtract, 2, 3, 1, 1)

        self.pushButton_1 = QPushButton(MainWindow)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(MainWindow)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(MainWindow)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_plus = QPushButton(MainWindow)
        self.pushButton_plus.setObjectName(u"pushButton_plus")

        self.gridLayout.addWidget(self.pushButton_plus, 3, 3, 1, 1)

        self.pushButton_0 = QPushButton(MainWindow)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.gridLayout.addWidget(self.pushButton_0, 4, 0, 1, 2)

        self.pushButton_point = QPushButton(MainWindow)
        self.pushButton_point.setObjectName(u"pushButton_point")

        self.gridLayout.addWidget(self.pushButton_point, 4, 2, 1, 1)

        self.pushButton_equal = QPushButton(MainWindow)
        self.pushButton_equal.setObjectName(u"pushButton_equal")

        self.gridLayout.addWidget(self.pushButton_equal, 4, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(MainWindow)
        self.pushButton_ac.clicked.connect(self.label.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_ac.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.pushButton_del.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.pushButton_pow.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pushButton_divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_subtract.setText(QCoreApplication.translate("MainWindow", u"\uff0d", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"\uff0b", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

