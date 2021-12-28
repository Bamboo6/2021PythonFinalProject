# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_calculator.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(315, 550)
        MainWindow.setMinimumSize(QSize(315, 550))
        icon = QIcon()
        icon.addFile(u":/img/apple_calculator_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color:#000000;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLineEdit {\n"
"	font-family:\"PingFang SC\";\n"
"}\n"
"QLabel {\n"
"	font-family:\"PingFang SC\";\n"
"}\n"
"QPushButton {\n"
"	border-radius:35px;\n"
"	border: 8px solid transparent;\n"
"	font-family:\"PingFang SC\";\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_1 = QVBoxLayout()
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setStyleSheet(u"QLabel{\n"
"	color:#ffffff;\n"
"	font: 18pt;\n"
"	background:transparent;\n"
"	border-width:0;\n"
"	border-style:outset\n"
"}")

        self.verticalLayout_1.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 70))
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	color:#ffffff;\n"
"	font: 35pt;\n"
"	background:transparent;\n"
"	border-width:0;\n"
"	border-style:outset;\n"
"	setAlignment:AlignRight;\n"
"}")

        self.verticalLayout_1.addWidget(self.lineEdit)

        self.verticalLayout_1.setStretch(0, 1)
        self.verticalLayout_1.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_ac = QPushButton(self.centralwidget)
        self.pushButton_ac.setObjectName(u"pushButton_ac")
        self.pushButton_ac.setMinimumSize(QSize(70, 70))
        self.pushButton_ac.setStyleSheet(u"QPushButton {\n"
"	color: #000000;\n"
"	font:18pt;\n"
"	border-radius:35px;\n"
"	background-color: #a5a5a5;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #d9d9d9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #d9d9d9;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_ac, 0, 0, 1, 1)

        self.pushButton_del = QPushButton(self.centralwidget)
        self.pushButton_del.setObjectName(u"pushButton_del")
        self.pushButton_del.setMinimumSize(QSize(70, 70))
        self.pushButton_del.setStyleSheet(u"QPushButton {\n"
"	color: #000000;\n"
"	font:18pt;\n"
"	border-radius:35px;\n"
"	border: 8px solid transparent;\n"
"	background-color: #a5a5a5;\n"
"	padding-right:3px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #d9d9d9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #d9d9d9;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/img/backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_del.setIcon(icon1)
        self.pushButton_del.setIconSize(QSize(35, 35))

        self.gridLayout.addWidget(self.pushButton_del, 0, 1, 1, 1)

        self.pushButton_pow = QPushButton(self.centralwidget)
        self.pushButton_pow.setObjectName(u"pushButton_pow")
        self.pushButton_pow.setMinimumSize(QSize(70, 70))
        self.pushButton_pow.setStyleSheet(u"QPushButton {\n"
"	color: #000000;\n"
"	font:25pt;\n"
"	border-radius:35px;\n"
"	background-color: #a5a5a5;\n"
"	padding-top: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #d9d9d9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #d9d9d9;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_pow, 0, 2, 1, 1)

        self.pushButton_divide = QPushButton(self.centralwidget)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        self.pushButton_divide.setMinimumSize(QSize(70, 70))
        self.pushButton_divide.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	font:25pt;\n"
"	border-radius:35px;\n"
"	background-color: #fe9f0b;\n"
"	padding-bottom:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #fbc78d;\n"
"	color: #fe9f0b;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #ffffff;\n"
"	color: #fe9f0b;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_divide, 0, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(70, 70))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(70, 70))
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(70, 70))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_multiply = QPushButton(self.centralwidget)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        self.pushButton_multiply.setMinimumSize(QSize(70, 70))
        self.pushButton_multiply.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	font:25pt;\n"
"	border-radius:35px;\n"
"	background-color: #fe9f0b;\n"
"	padding-bottom:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #fbc78d;\n"
"	color: #fe9f0b;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #ffffff;\n"
"	color: #fe9f0b;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_multiply, 1, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(70, 70))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(70, 70))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(70, 70))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_subtract = QPushButton(self.centralwidget)
        self.pushButton_subtract.setObjectName(u"pushButton_subtract")
        self.pushButton_subtract.setMinimumSize(QSize(70, 70))
        self.pushButton_subtract.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	font:25pt;\n"
"	border-radius:35px;\n"
"	background-color: #fe9f0b;\n"
"	padding-bottom:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #fbc78d;\n"
"	color: #fe9f0b;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #ffffff;\n"
"	color: #fe9f0b;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_subtract, 2, 3, 1, 1)

        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(70, 70))
        self.pushButton_1.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(70, 70))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(70, 70))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_plus = QPushButton(self.centralwidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setMinimumSize(QSize(70, 70))
        self.pushButton_plus.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	font:25pt;\n"
"	border-radius:35px;\n"
"	background-color: #fe9f0b;\n"
"	padding-bottom:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #fbc78d;\n"
"	color: #fe9f0b;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #ffffff;\n"
"	color: #fe9f0b;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_plus, 3, 3, 1, 1)

        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(0, 70))
        self.pushButton_0.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_0, 4, 0, 1, 2)

        self.pushButton_point = QPushButton(self.centralwidget)
        self.pushButton_point.setObjectName(u"pushButton_point")
        self.pushButton_point.setMinimumSize(QSize(70, 70))
        self.pushButton_point.setStyleSheet(u"QPushButton {\n"
"    color: #ffffff;\n"
"	font:25pt;\n"
"    border-radius:35px;\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6e6e6e;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #6e6e6e;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_point, 4, 2, 1, 1)

        self.pushButton_equal = QPushButton(self.centralwidget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        self.pushButton_equal.setMinimumSize(QSize(70, 70))
        self.pushButton_equal.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"	font:25pt;\n"
"	border-radius:35px;\n"
"	background-color: #fe9f0b;\n"
"	padding-bottom:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #fbc78d;\n"
"	color: #fe9f0b;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #ffffff;\n"
"	color: #fe9f0b;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_equal, 4, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 315, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Imitation iOS Calculator", None))
        self.label.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_ac.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.pushButton_del.setText("")
        self.pushButton_pow.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pushButton_divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_subtract.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

