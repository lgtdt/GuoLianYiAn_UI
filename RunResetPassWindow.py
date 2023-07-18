from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import ResetPassWindow
import sys


class ResetPassFrame(QWidget):
    def __init__(self):
        super().__init__()
        # ---设置窗口圆角---
        rect = QRectF(0, 0, 380, 430)
        path = QPainterPath()
        path.addRoundedRect(rect, 8, 8)
        polygon = path.toFillPolygon().toPolygon()
        region = QRegion(polygon)
        self.setMask(region)
        # ----------------

        self.init_ui()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.MessageLabel1.setVisible(False)
        self.ui.MessageLabel2.setVisible(False)
        self.ui.MessageLabel3.setVisible(False)

    def init_ui(self):
        self.ui = ResetPassWindow.Ui_ResetPassWindow()
        self.ui.setupUi(self)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.CancelButton.clicked.connect(self.CloseWindow)

    def CloseWindow(self):
        self.ui.OldPassInput.setText("")
        self.ui.NewPassInput.setText("")
        self.ui.ConfirmPassInput.setText("")
        self.close()

