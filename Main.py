from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import MainWindow
import sys


# class DraggableWindow(MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlags(Qt.FramelessWindowHint)
#
#         self.draggable = False
#         self.offset = QPoint()
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.draggable = True
#             self.offset = event.pos()
#
#     def mouseMoveEvent(self, event):
#         if self.draggable:
#             self.move(event.globalPos() - self.offset)
#
#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.draggable = False

class IndexWindow(QWidget):
    def __init__(self):
        super().__init__()

        # ---设置窗口圆角---
        rect = QRectF(0, 0, 900, 600)
        path = QPainterPath()
        path.addRoundedRect(rect, 8, 8)
        polygon = path.toFillPolygon().toPolygon()
        region = QRegion(polygon)
        self.setMask(region)
        # ----------------

        self.skinname = "origin"
        self.draggable = True
        self.offset = None
        self.init_ui()
    def init_ui(self):
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.MiniButtuon.clicked.connect(self.MinimizeWindow)
        self.ui.SkinButton.clicked.connect(self.ChangeSkin)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.draggable:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and self.draggable:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = None

    # 关闭按钮的实现
    def CloseWindow(self):
        QApplication.quit()

    #最小化按钮的实现
    def MinimizeWindow(self):
        self.showMinimized()

    def ChangeSkin(self):
        if self.skinname == "origin":
            self.ui.ProcessButton.setStyleSheet("")
            self.ui.ProcessButton.setStyleSheet("QPushButton{\n"
                                             "    background-color: red;\n"
                                             "    border-radius: 18;\n"
                                             "}\n"
                                             ":hover{\n"
                                             "    \n"
                                             "    background-color: black;\n"
                                             "}")
            self.skinname = "test-skin"
        else:
            self.ui.ProcessButton.setStyleSheet("")
            self.ui.ProcessButton.setStyleSheet("QPushButton{\n"
                                             "    background-color: rgb(43, 128, 247);\n"
                                             "    border-radius: 18;\n"
                                             "}\n"
                                             ":hover{\n"
                                             "    \n"
                                             "    background-color: rgb(126, 216, 255);\n"
                                             "}")
            self.skinname = "origin"




if __name__ == '__main__':


    app = QApplication(sys.argv)
    indexWindow = IndexWindow()
    indexWindow.setWindowFlags(Qt.FramelessWindowHint)
    indexWindow.show()
    sys.exit(app.exec_())