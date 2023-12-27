import sys
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw
from gui.ui_main import Ui_MainWindow


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.mwin = Ui_MainWindow()
        self.mwin.setupUi(self)

        self.mwin.exit_btn.clicked.connect(self._exit)
        self.mwin.min_btn.clicked.connect(self.minimize)
        self.mwin.title_frame.mouseMoveEvent = self.MoveWindow

    def _exit(self):
        sys.exit(0)

    def minimize(self):
        self.showMinimized()

    def MoveWindow(self, event):
        if event.buttons() == qtc.Qt.MouseButton.LeftButton:
            self.move(
                self.pos() + event.globalPosition().toPoint() - self.clickPosition
            )
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()
