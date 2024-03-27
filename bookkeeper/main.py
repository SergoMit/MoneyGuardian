import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from view.MoneyGuardianUI_main import Ui_MainWindow
from view.MG_new_trans_UI import Ui_Dialog_new
from view.MG_edit_trans_UI import Ui_Dialog_edit
from view.MG_delete_trans_UI import Ui_Dialog_delete
from view.MG_budget_set_UI import Ui_Dialog_budget
from controller.crud_controller import CrudController


class MoneyGuardian(QMainWindow):
    def __init__(self) -> None:
        super(MoneyGuardian, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.controller = CrudController()

        self.new_transaction_window = None
        self.delete_transaction_window = None
        self.edit_transaction_window = None
        self.set_budget_window = None

        self.ui.new_button.clicked.connect(lambda: self.open_new_transaction_window())
        self.ui.del_button.clicked.connect(lambda: self.open_delete_transaction_window())
        self.ui.change_button.clicked.connect(lambda: self.open_edit_transaction_window())
        self.ui.budget_button.clicked.connect(lambda: self.open_set_budget_window())

    def open_new_transaction_window(self):
        self.new_transaction_window = NewTransactionWindow()
        self.new_transaction_window.show()

    def open_delete_transaction_window(self):
        self.delete_transaction_window = DeleteTransactionWindow()
        self.delete_transaction_window.show()

    def open_edit_transaction_window(self):
        self.edit_transaction_window = EditTransactionWindow()
        self.edit_transaction_window.show()

    def open_set_budget_window(self):
        self.set_budget_window = SetBudgetWindow()
        self.set_budget_window.show()

    def reload_data(self):
        """
        Функция, реализующая логику обновления данных во всех виджетах главного окна
        """
        self.ui.day_expense.setText(self.controller.get_total())
        self.ui.week_expense.setText(self.controller.get_total())
        self.ui.month_expense.setText(self.controller.get_total())
        self.ui.day_budget.setText(self.controller.read())
        self.ui.week_budget.setText(self.controller.read())
        self.ui.month_budget.setText(self.controller.read())
        self.ui.day_residual.setText(self.controller.calculate_residual())
        self.ui.week_residual.setText(self.controller.calculate_residual())
        self.ui.month_residual.setText(self.controller.calculate_residual())

    def view_data(self):
        """
        Формирование модели представления таблицы Expense из базы данных MG_database
        """
        pass


class NewTransactionWindow(QDialog):
    """
    Формирование окна, реализующего создание транзакции с использованием
    сгенерированного класса Ui_dialog
    """

    def __init__(self):
        super(NewTransactionWindow, self).__init__()
        self.ui_window_new = Ui_Dialog_new()
        self.ui_window_new.setupUi(self)

        self.ui_window_new.save_button.clicked.connect(lambda: self.add_new_transaction())

    def add_new_transaction(self):
        """
        Функция, реализующая создание новой транзакции.
        Формируется словарь из значений, внесённых пользователем, и передаётся в метод create
        класса CrudController
        """

        balance = self.ui_window_new.amount.text()
        category = self.ui_window_new.cb_category.currentText()
        date = self.ui_window_new.data.text()
        description = self.ui_window_new.descript.text()

        parameter = {'balance': balance, 'category': category, 'date': date, 'description': description}

        CrudController().create('Expense', parameter)
        MoneyGuardian().view_data()
        MoneyGuardian().reload_data()

        self.close()


class DeleteTransactionWindow(QDialog):
    """
    Формирование окна, реализуюшего удаление транзакции с использованием сгенерированного класса
    """

    def __init__(self):
        super(DeleteTransactionWindow, self).__init__()
        self.ui_window_delete = Ui_Dialog_delete()
        self.ui_window_delete.setupUi(self)

        self.ui_window_delete.delete_button.clicked.connect(lambda: self.delete_current_transaction())

    def delete_current_transaction(self):
        """
        Функция, реализующая логику удаления транзакции
        """
        MoneyGuardian().reload_data()
        MoneyGuardian().view_data()
        self.close()


class EditTransactionWindow(QDialog):
    """
    Формирование окна, реализующего изменение транзакции с использованием сгенерированного класса
    """

    def __init__(self):
        super(EditTransactionWindow, self).__init__()
        self.ui_window_edit = Ui_Dialog_edit()
        self.ui_window_edit.setupUi(self)

        self.ui_window_edit.edit_button.clicked.connect(lambda: self.edit_current_transaction())

    def edit_current_transaction(self):
        """
        Функция, реализующая логику изменения транзакции, выбранной из виджета QTableView
        """
        MoneyGuardian().reload_data()
        MoneyGuardian().view_data()
        self.close()


class SetBudgetWindow(QDialog):
    """
    Формирование диалогового окна, реализующего назначение бюджета, с использованием
    сгенерированного класса Ui_Dialog_budget
    """

    def __init__(self):
        super(SetBudgetWindow, self).__init__()
        self.ui_budget_window = Ui_Dialog_budget()
        self.ui_budget_window.setupUi(self)

        self.ui_budget_window.save_budget_button.clicked.connect(lambda: self.set_budget())

    def set_budget(self):
        """
        Функция, реализующая назначение бюджета на день, неделю, месяц.
        Формируется словарь со значениями, внесёнными пользователем, и передаётся в метод create
        класса CrudController
        """
        budget_per_day = self.ui_budget_window.bud_per_day.text()
        budget_per_week = self.ui_budget_window.bud_per_week.text()
        budget_per_month = self.ui_budget_window.bud_per_month.text()

        parameter = {'daily': budget_per_day, 'weekly': budget_per_week, 'monthly': budget_per_month}
        MoneyGuardian().controller.create('Budget', parameter)

        MoneyGuardian().reload_data()
        MoneyGuardian().view_data()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoneyGuardian()
    window.show()

    sys.exit(app.exec())
