from PyQt5 import QtWidgets

from shop import Ui_MainWindow
from add_product_form import Ui_Form
from database import Database


class AddFormProduct(QtWidgets.QWidget, Ui_Form):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)

        self.main_window = main_window

        self.db = Database()
        self.load_data_categories()

        self.btn_add_product.clicked.connect(self.add_product)

    def load_data_categories(self):
        data = self.db.fetch_all("SELECT name, id FROM categories")

        for row in data:
            self.comboBox_categories.addItem(row['name'], row['id'])
            # name — показывается, id — сохраняется в ComboBox как userData


    def add_product(self):
        name = self.form_add_name_product.toPlainText()
        category_id = int(self.comboBox_categories.currentData())  # ✅ получаем ID, а не текст
        price = float(self.form_add_price_product.toPlainText())

        if name and category_id and price:
            self.db.execute(
                'INSERT INTO products (name, categories, price) VALUES (%s, %s, %s)',
                (name, category_id, price)
            )

            self.main_window.load_data()  # обновляем таблицу в главном окне
            self.close()

class Window(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Магазин")

        self.db = Database()
        self.load_data()

        self.btn_add.clicked.connect(self.show_window_add_product)

    def show_window_add_product(self):
        self.window_add_product = AddFormProduct(self)
        self.window_add_product.show()

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



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())
