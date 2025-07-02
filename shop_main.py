from PyQt5 import QtWidgets

from shop import Ui_MainWindow
from database import Database


class Window(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = Database()
        self.load_data()

    def load_data(self):
        self.tabWidget.setCurrentIndex(0)  # переключиться на первую вкладку

        self.products_data = self.db.fetch_all("""
                                               SELECT products.id,
                                                      products.name,
                                                      categories.name AS category_name,
                                                      products.price
                                               FROM products
                                                   JOIN categories
                                               ON products.categories = categories.id
                                               """)

        self.data_products.setColumnCount(3)
        self.data_products.setRowCount(len(self.products_data))

        for row_index, row in enumerate(self.products_data):
            self.data_products.setItem(row_index, 0, QtWidgets.QTableWidgetItem(str(row['name'])))
            self.data_products.setItem(row_index, 1, QtWidgets.QTableWidgetItem(str(row['category_name'])))
            self.data_products.setItem(row_index, 2, QtWidgets.QTableWidgetItem(str(row['price'])))

        self.db.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())
