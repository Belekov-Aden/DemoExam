import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Редактор текста")
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.create_menu_bar()

    def create_menu_bar(self):
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&Файл", self)

        file_menu.addAction("Открыть", self.action_clicked)
        file_menu.addAction("Сохранить", self.action_clicked)

        self.menu_bar.addMenu(file_menu)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self)[0]

            with open(fname, "r", encoding="utf-8") as f:
                self.text_edit.setText(f.read())

        elif action.text() == "Сохранить":
            fname = QFileDialog.getSaveFileName(self)[0]
            with open(fname, "w", encoding="utf-8") as f:
                f.write(self.text_edit.toPlainText())


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
