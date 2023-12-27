from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setWindowTitle("App")
        MainWindow.setWindowFlags(qtc.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(qtc.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.btn_frame = qtw.QFrame(MainWindow)
        self.btn_frame.setObjectName("btn_frame")
        self.btn_frame.setGeometry(qtc.QRect(490, 20, 130, 50))

        self.exit_btn = qtw.QPushButton(self.btn_frame)
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.setGeometry(qtc.QRect(95, 14, 18, 18))
        self.exit_btn.setToolTip("Exit")
        self.exit_shadow = qtw.QGraphicsDropShadowEffect()
        self.exit_shadow.setColor(qtg.QColor(0, 0, 0, 150))
        self.exit_shadow.setBlurRadius(5)
        self.exit_shadow.setXOffset(2)
        self.exit_shadow.setYOffset(2)
        self.exit_btn.setGraphicsEffect(self.exit_shadow)

        self.min_btn = qtw.QPushButton(self.btn_frame)
        self.min_btn.setObjectName("min_btn")
        self.min_btn.setGeometry(qtc.QRect(55, 20, 22, 10))
        self.min_btn.setToolTip("Minimize")
        self.min_shadow = qtw.QGraphicsDropShadowEffect()
        self.min_shadow.setColor(qtg.QColor(0, 0, 0, 150))
        self.min_shadow.setBlurRadius(5)
        self.min_shadow.setXOffset(2)
        self.min_shadow.setYOffset(2)
        self.min_btn.setGraphicsEffect(self.min_shadow)

        self.title_frame = qtw.QFrame(MainWindow)
        self.title_frame.setObjectName("title_frame")
        self.title_frame.setGeometry(qtc.QRect(20, 20, 510, 50))
        self.title_shadow = qtw.QGraphicsDropShadowEffect()
        self.title_shadow.setColor(qtg.QColor(0, 0, 0, 100))
        self.title_shadow.setBlurRadius(3)
        self.title_shadow.setXOffset(3)
        self.title_shadow.setYOffset(0)
        self.title_frame.setGraphicsEffect(self.title_shadow)

        self.title_label = qtw.QLabel("APP TITLE", self.title_frame)
        self.title_label.setObjectName("title_label")
        self.title_label.setGeometry(qtc.QRect(7, 7, 350, 35))

        self.accent_frame = qtw.QFrame(MainWindow)
        self.accent_frame.setObjectName("accent_frame")
        self.accent_frame.setGeometry(qtc.QRect(20, 65, 600, 10))
        self.accent_shadow = qtw.QGraphicsDropShadowEffect()
        self.accent_shadow.setColor(qtg.QColor(0, 0, 0, 100))
        self.accent_shadow.setBlurRadius(3)
        self.accent_shadow.setXOffset(0)
        self.accent_shadow.setYOffset(-2)
        self.accent_frame.setGraphicsEffect(self.accent_shadow)

        self.main_frame = qtw.QFrame(MainWindow)
        self.main_frame.setObjectName("main_frame")
        self.main_frame.setGeometry(qtc.QRect(20, 70, 600, 385))
        self.main_shadow = qtw.QGraphicsDropShadowEffect()
        self.main_shadow.setColor(qtg.QColor(0, 0, 0, 125))
        self.main_shadow.setBlurRadius(4)
        self.main_shadow.setXOffset(0)
        self.main_shadow.setYOffset(4)
        self.main_frame.setGraphicsEffect(self.main_shadow)
