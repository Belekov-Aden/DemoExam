import sys

from PyQt5 import QtWidgets
from window import Ui_MainWindow

from card_categories import Ui_Form
from card_products import Ui_Form as CardProductsTemplate
from form_category import Ui_Form as FormCategoryAddTemplate
from form_products import Ui_Form as FormProductsTemplate
from database import Database


class FormCategoryChange(QtWidgets.QDialog, FormCategoryAddTemplate):
    def __init__(self, parent, category_id, category_name):
        super().__init__()
        self.setupUi(self)

        self.db = Database()
        self.parent = parent
        self.category_id = category_id

        self.setWindowTitle("Изменение категории")
        self.form_btn_add_category.setText('Сохранить')

        self.form_name_category.setPlainText(category_name)

        self.form_btn_add_category.clicked.connect(self.update_category)

    def update_category(self):
        new_name = self.form_name_category.toPlainText()  # или .text(), если QLineEdit
        try:
            self.db.execute('UPDATE categories SET name = %s WHERE id = %s', (new_name, self.category_id))
            self.parent.load_data()
            self.close()
        except Exception as e:
            print(f"Ошибка при обновлении категории: {e}")


class FormCategoryAdd(QtWidgets.QDialog, FormCategoryAddTemplate):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)

        self.db = Database()
        self.parent = parent

        self.form_btn_add_category.clicked.connect(self.add_category)

    def add_category(self):
        try:
            self.db.execute('INSERT INTO categories (name) VALUES (%s)', (self.form_name_category.toPlainText(),))
            self.parent.load_data()
        except Exception as e:
            print(e)


class FormProductsChange(QtWidgets.QDialog, FormProductsTemplate):
    def __init__(self, id_, name, category_id, price, count, parent):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Изменение продукта")
        self.btn_add_product.setText('Сохранить')

        self.db = Database()
        self.parent = parent
        self.product_id = id_

        self.lbl_name_product.setPlainText(name)
        self.lbl_price_product.setPlainText(str(price))
        self.lbl_count_product.setPlainText(str(count))

        self.load_categories(category_id)  # ← передаём id текущей категории

        self.btn_add_product.clicked.connect(self.save_product)

    def save_product(self):
        try:

            self.db.execute('UPDATE products SET name = %s, categories = %s, price = %s, count = %s WHERE id = %s  ',
                            (self.lbl_name_product.toPlainText(), self.categoriesComboBox.currentData(),
                             str(self.lbl_price_product.toPlainText()), str(self.lbl_count_product.toPlainText()),
                             self.product_id))

            self.parent.load_data()
            self.close()
        except Exception as e:
            print(e)

    def load_categories(self, selected_category_id):

        self.categories = self.db.fetch_all('SELECT * FROM categories ORDER BY id')

        for row in self.categories:
            self.categoriesComboBox.addItem(row["name"], row["id"])

        # установить текущую категорию
        index = self.categoriesComboBox.findData(selected_category_id)
        if index != -1:
            self.categoriesComboBox.setCurrentIndex(index)


class FormProductsAdd(QtWidgets.QDialog, FormProductsTemplate):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Добавление продукта")

        self.db = Database()
        self.parent = parent

        self.btn_add_product.clicked.connect(self.add_product)
        self.load_combo_box_categories()

    def load_combo_box_categories(self):
        self.categories = self.db.fetch_all('SELECT * FROM categories order by id')

        for row in self.categories:
            self.categoriesComboBox.addItem(str(row['name']), row['id'])

    def add_product(self):
        try:
            self.db.execute('INSERT INTO products (name, categories, price, count) VALUES (%s, %s, %s, %s)',
                            (self.lbl_name_product.toPlainText(), self.categoriesComboBox.currentData(),
                             str(self.lbl_price_product.toPlainText()), str(self.lbl_count_product.toPlainText())))
            self.parent.load_data()

        except Exception as e:
            print(f"Error: {e}")


class CardCategoriesWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, id_, name, parent_window):
        super().__init__()
        self.setupUi(self)
        self.parent = parent_window

        self.db = Database()

        self.id_ = id_
        self.name_label_categories.setText(name)

        self.btn_change_categories.clicked.connect(self.change_category)
        self.btn_del_categories.clicked.connect(self.delete_category)

    def change_category(self):
        form_change_category = FormCategoryChange(self.parent, self.id_, self.name_label_categories.text())
        form_change_category.exec_()

    def delete_category(self):
        try:
            self.db.execute('delete from categories where id = %s', (str(self.id_),))
            self.parent.load_data()
        except Exception as e:
            print(f"Ошибка при удалении категории: {e}")


class CardProductsWidget(QtWidgets.QWidget, CardProductsTemplate):
    def __init__(self, id_, name, category_id, count, price, parent_window):
        super().__init__()
        self.setupUi(self)

        self.id_ = id_
        self.category_id = category_id  # ← сохраняем id категории
        self.price = price
        self.count = count

        self.parent_window = parent_window

        self.lbl_name.setText(name)
        self.lbl_category.setText(self.get_category_name_by_id(category_id))  # ← выводим имя
        self.lbl_count_and_price.setText(f'{count} / {price}')

        self.btn_change_products.clicked.connect(self.change_products)

    def get_category_name_by_id(self, category_id):
        db = Database()
        row = db.fetch_one('SELECT name FROM categories WHERE id = %s', (category_id,))
        return row["name"] if row else "Неизвестно"

    def change_products(self):
        form_change_product = FormProductsChange(
            id_=self.id_,
            name=self.lbl_name.text(),
            category_id=self.category_id,  # ← добавь это поле
            price=self.price,
            count=self.count,
            parent=self.parent_window
        )
        form_change_product.exec_()


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



        self.setWindowTitle("Склад")
        self.btn_add_category.clicked.connect(self.add_category)

        self.btn_add_products.clicked.connect(self.add_product)

        # Database connection
        self.db = Database()
        self.load_data()

    def load_data(self):
        self.setup_cards_layout()
        categories = self.db.fetch_all('SELECT * FROM categories order by id')
        products = self.db.fetch_all('SELECT * FROM products order by id')

        for category in categories:
            self.add_category_card(category["id"], category["name"])

        for product in products:
            self.add_product_card(product["id"], product["name"], product["categories"], product["count"],
                                  product["price"])

    def add_product(self):
        add_product = FormProductsAdd(self)
        add_product.exec_()

    def add_category(self):
        add_category_form = FormCategoryAdd(self)
        add_category_form.exec_()

    def setup_cards_layout(self):
        # Удаляем старые виджеты из cards_layout (категории)
        if hasattr(self, 'cards_layout'):
            while self.cards_layout.count():
                item = self.cards_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        else:
            self.cards_layout = QtWidgets.QVBoxLayout()
            self.scrollAreaWidgetContents.setLayout(self.cards_layout)

        # Удаляем старые виджеты из card_layout_products (товары)
        if hasattr(self, 'card_layout_products'):
            while self.card_layout_products.count():
                item = self.card_layout_products.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        else:
            self.card_layout_products = QtWidgets.QVBoxLayout()
            self.scrollAreaProducts.setLayout(self.card_layout_products)

    def add_product_card(self, id_, name, category, count, price):
        card = CardProductsWidget(id_, name, category, count, price, parent_window=self)
        self.card_layout_products.addWidget(card)

    def add_category_card(self, id_, name):
        card = CardCategoriesWidget(id_, name, parent_window=self)
        self.cards_layout.addWidget(card)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
