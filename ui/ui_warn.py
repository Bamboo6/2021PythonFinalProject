# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_warn.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_WarnWindow(object):
    def setupUi(self, WarnWindow):
        if not WarnWindow.objectName():
            WarnWindow.setObjectName(u"WarnWindow")
        WarnWindow.resize(225, 92)
        self.centralwidget = QWidget(WarnWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        WarnWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(WarnWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 225, 22))
        WarnWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(WarnWindow)
        self.statusbar.setObjectName(u"statusbar")
        WarnWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WarnWindow)

        QMetaObject.connectSlotsByName(WarnWindow)
    # setupUi

    def retranslateUi(self, WarnWindow):
        WarnWindow.setWindowTitle(QCoreApplication.translate("WarnWindow", u"\u8b66\u544a", None))
        self.label.setText(QCoreApplication.translate("WarnWindow", u"\u8f93\u5165\u5185\u5bb9\u6709\u8bef\uff01\n"
" \u8bf7\u68c0\u67e5\u8f93\u5165\u5185\u5bb9\u7684\u5408\u6cd5\u6027\uff01", None))
    # retranslateUi

