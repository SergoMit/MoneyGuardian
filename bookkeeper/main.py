import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6 import QtCore

from view.MoneyGuardianUI import Ui_MainWindow
from view.MG_new_transactionUI import Ui_Dialog_new
from view.MG_edit_transactionUI import Ui_Dialog_edit
from view.MG_delete_transactionUI import Ui_Dialog_delete
from view.MG_set_budgetUI import Ui_Dialog_budget
from controller.crud_controller import CrudController


class MoneyGuardian(QMainWindow):
    """
    Класс MoneyGuardian формирует главное окно GUI-приложения Money Guardian

    Основное применение - данный класс обращается к автоматически сгенерированному образу интерфейса
    Ui_MainWindow, внося в него весь необходимый функционал. Все остальные классы файла main.py связаны
    непосредственно с MoneyGuardian.

    Note:
        Возможны проблемы с отображением шрифта BigCaslon, внедрённого в графический интерфейс, в Windows.
        В MacOS данный шрифт встроен в операционную систему по умолчанию.

    Methods
    ----------
    open_new_transaction_window()
        Функция, предоставляющая доступ к окну создания транзакции при нажатии кнопки "Создать"
    open_edit_transaction_window()
        Функция, предоставляющая доступ к окну изменения транзакции при нажатии кнопки "Изменить"
    open_delete_transaction_window()
        Функция, предоставляющая доступ к окну удаления транзакции при нажатии кнопки "Удалить"
    open_set_budget_window()
        Функция, предоставляющая доступ к окну задания бюджета при нажатии кнопки "Бюджет"
    reload_data()
        Функция, реализующая обновление данных во всех виджетах главного окна при загрузке приложения
        и реализации транзакции/бюджета
    view_data()
        Функция, реализующая перезагрузку виджета таблицы со всеми совершёнными транзакциями
    """
    def __init__(self) -> None:
        super(MoneyGuardian, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.controller = CrudController()

        self.new_transaction_window = None
        self.delete_transaction_window = None
        self.edit_transaction_window = None
        self.set_budget_window = None

        self.model = TableModel()
        self.ui.tableView.setModel(self.model)

        self.ui.new_button.clicked.connect(lambda: self.open_new_transaction_window())
        self.ui.del_button.clicked.connect(lambda: self.open_delete_transaction_window())
        self.ui.change_button.clicked.connect(lambda: self.open_edit_transaction_window())
        self.ui.budget_button.clicked.connect(lambda: self.open_set_budget_window())

        self.reload_data()
        self.view_data()

    def open_new_transaction_window(self) -> None:
        self.new_transaction_window = NewTransactionWindow()
        self.new_transaction_window.exec()
        self.reload_data()
        self.view_data()

    def open_edit_transaction_window(self) -> None:
        self.edit_transaction_window = EditTransactionWindow()
        self.edit_transaction_window.exec()
        self.reload_data()
        self.view_data()

    def open_delete_transaction_window(self) -> None:
        self.delete_transaction_window = DeleteTransactionWindow()
        self.delete_transaction_window.exec()
        self.reload_data()
        self.view_data()

    def open_set_budget_window(self) -> None:
        self.set_budget_window = SetBudgetWindow()
        self.set_budget_window.exec()
        self.reload_data()
        self.view_data()

    def reload_data(self) -> None:
        self.ui.day_expense.setText(self.controller.read('Expense_total')[0])
        self.ui.week_expense.setText(self.controller.read('Expense_total')[1])
        self.ui.month_expense.setText(self.controller.read('Expense_total')[2])

        self.ui.day_budget.setText(self.controller.read('Budget')[0])
        self.ui.week_budget.setText(self.controller.read('Budget')[1])
        self.ui.month_budget.setText(self.controller.read('Budget')[2])

        if self.controller.read('Expense_residual')[0][0] == '-':
            self.ui.day_residual.setStyleSheet('color: red')
        else:
            self.ui.day_residual.setStyleSheet('color: white')
        self.ui.day_residual.setText(self.controller.read('Expense_residual')[0])

        if self.controller.read('Expense_residual')[1][0] == '-':
            self.ui.week_residual.setStyleSheet('color: red')
        else:
            self.ui.week_residual.setStyleSheet('color: white')
        self.ui.week_residual.setText(self.controller.read('Expense_residual')[1])

        if self.controller.read('Expense_residual')[2][0] == '-':
            self.ui.month_residual.setStyleSheet('color: red')
        else:
            self.ui.month_residual.setStyleSheet('color: white')
        self.ui.month_residual.setText(self.controller.read('Expense_residual')[2])

    def view_data(self):
        self.model.setitems(self.controller.read('Expense_data'))


class NewTransactionWindow(QDialog):
    """
    Класс NewTransactionWindow формирует окно создания транзакции с использованием
    сгенерированного класса Ui_Dialog_new при нажатии кнопки "Создать" главного окна

    Основное применение - реализует внесение данных о новой транзакции в таблицу
    Expense базы данных

    Methods
    ----------
    add_new_transaction()
        Функция, реализующая создание новой транзакции.
        Формируется словарь из значений, внесённых пользователем, и передаётся в метод create
        класса CrudController
    """

    def __init__(self) -> None:
        super(NewTransactionWindow, self).__init__()
        self.ui_window_new = Ui_Dialog_new()
        self.ui_window_new.setupUi(self)

        self.ui_window_new.save_button.clicked.connect(lambda: self.add_new_transaction())

    def add_new_transaction(self) -> None:
        balance = self.ui_window_new.amount.text()
        category = self.ui_window_new.cb_category.currentText()
        date = self.ui_window_new.data.text()
        description = self.ui_window_new.descript.text()

        parameter = {'balance': balance, 'category': category, 'date': date, 'description': description}

        CrudController().create('Expense', parameter)

        self.close()


class EditTransactionWindow(QDialog):
    """
    Класс EditTransactionWindow формирует окно изменения транзакции с использованием
    сгенерированного класса Ui_Dialog_edit при нажатии кнопки "Изменить" главного окна

    Основное применение - реализует изменение данных уже существующей транзакции в таблице
    Expense базы данных

    Methods
    ----------
    edit_current_transaction()
        Функция, реализующая логику изменения транзакции по указанному id транзакции.
        Формируется словарь из значений, внесённых пользователем, и передаётся в метод update
        класса CrudController
    """

    def __init__(self) -> None:
        super(EditTransactionWindow, self).__init__()
        self.ui_window_edit = Ui_Dialog_edit()
        self.ui_window_edit.setupUi(self)

        self.ui_window_edit.edit_button.clicked.connect(lambda: self.edit_current_transaction())

    def edit_current_transaction(self) -> None:
        transaction_id = self.ui_window_edit.edit_id_transaction.text()
        balance = self.ui_window_edit.edit_amount.text()
        category = self.ui_window_edit.edit_cb_category.currentText()
        date = self.ui_window_edit.edit_date.text()
        description = self.ui_window_edit.edit_descript.text()

        parameters = {'transaction_id': transaction_id, 'balance': balance, 'category': category, 'date': date,
                      'description': description}
        CrudController().update(parameters)

        self.close()


class DeleteTransactionWindow(QDialog):
    """
    Класс DeleteTransactionWindow формирует окно удаления транзакции с использованием
    сгенерированного класса Ui_Dialog_delete при нажатии кнопки "Удалить" главного окна

    Основное применение - реализует удаление уже существующей транзакции из таблицы
    Expense базы данных

    Methods
    ----------
    delete_current_transaction()
        Функция, реализующая логику удаления транзакции по указанному id.
        Обращается к методу delete класса CrudController
    """

    def __init__(self) -> None:
        super(DeleteTransactionWindow, self).__init__()
        self.ui_window_delete = Ui_Dialog_delete()
        self.ui_window_delete.setupUi(self)

        self.ui_window_delete.delete_button.clicked.connect(lambda: self.delete_current_transaction())

    def delete_current_transaction(self) -> None:
        transaction_id = self.ui_window_delete.delete_id.text()
        CrudController().delete(transaction_id)
        self.close()


class SetBudgetWindow(QDialog):
    """
    Класс SetBudgetWindow формирует окно задания бюджета с использованием
    сгенерированного класса Ui_Dialog_budget при нажатии кнопки Бюджет главного окна

    Основное применение - реализует задание бюджета в таблицу Budget базы данных

    Methods
    ----------
    set_budget()
        Функция, реализующая назначение бюджета на день, неделю, месяц.
        Формируется словарь со значениями, внесёнными пользователем, и передаётся в метод create
        класса CrudController
    """

    def __init__(self) -> None:
        super(SetBudgetWindow, self).__init__()
        self.ui_budget_window = Ui_Dialog_budget()
        self.ui_budget_window.setupUi(self)

        self.ui_budget_window.save_budget_button.clicked.connect(lambda: self.set_budget())

    def set_budget(self) -> None:
        budget_per_day = self.ui_budget_window.bud_per_day.text()
        budget_per_week = self.ui_budget_window.bud_per_week.text()
        budget_per_month = self.ui_budget_window.bud_per_month.text()

        parameter = {'daily': budget_per_day, 'weekly': budget_per_week, 'monthly': budget_per_month}
        MoneyGuardian().controller.create('Budget', parameter)

        self.close()


class TableModel(QtCore.QAbstractTableModel):
    """
    Класс TableModel формирует табличный виджет со всеми совершёнными транзакциями с использованием
    сгенерированного объекта tableView

    Основное применение - отображение таблицы со всеми транзакциями, совершёнными пользователем

    Methods
    ----------
    setitems()
        Функция, задающая цикл обновления данных табличного виджета
    rowCount()
        Функция, задающая число строк, в которых будут отображаться данные таблицы.
        Их количество соотвествует числу записей в таблице Expenses базы данных
    columnCount()
        Функция, задающая число столбцов, в которых будут отображаться данные таблицы.
        Их количество соотвествует числу столбцов в таблице Expenses базы данных (6)
    data()
        Функция, отвечающая за распределение соответствующих типов данных по столбцам и
        строкам табличного виджета
    headerData()
        Функция, сопоставляющая имя столбца с его положением в виджете

    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.items = CrudController.read('Expense_data')

    def setitems(self, items: tuple[str, str, str]) -> None:
        self.beginResetModel()
        self.items = items
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        return 6

    def data(self, index, role: QtCore.Qt.ItemDataRole = ...) -> str | None:
        if not index.isValid():
            return

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            expense_info = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{expense_info.id}'
            elif col == 1:
                return f'{expense_info.amount}'
            elif col == 2:
                return f'{expense_info.expense_date}'
            elif col == 3:
                return f'{expense_info.added_date}'
            elif col == 4:
                return f'{expense_info.comment}'
            elif col == 5:
                return f'{expense_info.category}'

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole = ...) -> str:
        """В соответствии со столбцами таблицы Expense: id, amount, expense_date, added_date, comment, category"""

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: "id",
                    1: "Сумма",
                    2: "Дата совершения",
                    3: "Дата добавления",
                    4: "Комментарий",
                    5: "Категория"
                }.get(section)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoneyGuardian()
    window.show()

    sys.exit(app.exec())
