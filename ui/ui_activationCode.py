# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_activationCode.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(328, 405)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_char = QLineEdit(self.centralwidget)
        self.lineEdit_char.setObjectName(u"lineEdit_char")

        self.horizontalLayout.addWidget(self.lineEdit_char)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_part = QLineEdit(self.centralwidget)
        self.lineEdit_part.setObjectName(u"lineEdit_part")

        self.horizontalLayout_2.addWidget(self.lineEdit_part)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_up_letters = QLineEdit(self.centralwidget)
        self.lineEdit_up_letters.setObjectName(u"lineEdit_up_letters")

        self.horizontalLayout_3.addWidget(self.lineEdit_up_letters)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_low_letters = QLineEdit(self.centralwidget)
        self.lineEdit_low_letters.setObjectName(u"lineEdit_low_letters")

        self.horizontalLayout_4.addWidget(self.lineEdit_low_letters)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_digits = QLineEdit(self.centralwidget)
        self.lineEdit_digits.setObjectName(u"lineEdit_digits")

        self.horizontalLayout_5.addWidget(self.lineEdit_digits)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.pushButton_preview = QPushButton(self.centralwidget)
        self.pushButton_preview.setObjectName(u"pushButton_preview")

        self.verticalLayout.addWidget(self.pushButton_preview)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_result = QLineEdit(self.centralwidget)
        self.lineEdit_result.setObjectName(u"lineEdit_result")

        self.horizontalLayout_6.addWidget(self.lineEdit_result)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_result_2 = QLineEdit(self.centralwidget)
        self.lineEdit_result_2.setObjectName(u"lineEdit_result_2")

        self.horizontalLayout_7.addWidget(self.lineEdit_result_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.pushButton_generate = QPushButton(self.centralwidget)
        self.pushButton_generate.setObjectName(u"pushButton_generate")

        self.verticalLayout.addWidget(self.pushButton_generate)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 328, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6fc0\u6d3b\u7801\u751f\u6210\u5668", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5355\u90e8\u5206\u5b57\u7b26\u6570", None))
        self.lineEdit_char.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6fc0\u6d3b\u7801\u90e8\u4efd\u6570", None))
        self.lineEdit_part.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5199\u5b57\u6bcd\u6982\u7387", None))
        self.lineEdit_up_letters.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u5199\u5b57\u6bcd\u6982\u7387", None))
        self.lineEdit_low_letters.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"  \u6570 \u5b57 \u6982 \u7387  ", None))
        self.lineEdit_digits.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_preview.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"  \u7ed3 \u679c \u9884 \u89c8  ", None))
        self.lineEdit_result.setText(QCoreApplication.translate("MainWindow", u"7DR4-aAWX-VvhM-JUsf", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"  \u751f \u6210 \u6570 \u91cf  ", None))
        self.lineEdit_result_2.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_generate.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u5e76\u5bfc\u51fa", None))
    # retranslateUi

