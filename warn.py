import sys

from qt_core import *
from ui.ui_warn import Ui_WarnWindow


class Warn(QMainWindow, Ui_WarnWindow):
    def __init__(self):
        # 初始化显示界面
        super(Warn, self).__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    # 高分屏适配
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication()
    # 引入字体
    QtGui.QFontDatabase.addApplicationFont('ui/PingFang.ttf')
    ui = Warn()
    sys.exit(app.exec())
