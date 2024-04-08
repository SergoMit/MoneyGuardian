"""
В данном модуле содержится класс CrudController,
предназначенный для реализации операций create, read, update,
delete в зависимости от запроса пользователя
"""

from typing import Any
from bookkeeper.msg import message_box  # type: ignore  # pylint: disable=E0401
from bookkeeper.config import logging_config  # type: ignore  # pylint: disable=E0401

import bookkeeper.controller.query_helper as qh  # type: ignore  # pylint: disable=E0401


class CrudController:
    """
    Класс CrudController осуществляет основные операции с данными: создание,
    чтение, обновление, удаление, а также подсчёт затрат и нахождение остатка

    Основное применение - данный класс обеспечивают всю логику обработки
    запросов, исходящих из файла main.py

    Methods
    ----------
    create(entity, params)
        Осуществляет запись в таблицы Budget и Expense базы данных
    read(params)
        Осуществляет чтение из БД, передаёт результаты расходов за день, месяц, неделю и
        месяц, неделю и соотвествующий свободный остаток, а также сообщает сведения о всех
        текущих транзакциях главному окну приложения
    update(params)
        Осуществляет изменение уже существующей записи в таблице Expense
    delete(params)
        Осуществляет удаление выбранной записи из таблицы Expense
    """

    @staticmethod
    def create(entity: str, params: dict[str, Any]) -> None:
        """ Осуществляет запись в таблицы Budget и Expense базы данных"""
        try:
            if entity == 'Budget':
                qh.add_budget(monthly=params['monthly'], weekly=params['weekly'],
                              daily=params['daily'])
                return
        except Exception as err:
            logging_config(err)
            message_box('Возникла ошибка при создании бюджета,\
                         обратитесь к файлу py_log.')
            raise SystemExit

        try:
            if entity == 'Expense':
                qh.add_expense(balance=params['balance'], category=params['category'],
                               date=params['date'], description=params['description'])
                return
        except Exception as err:
            logging_config(err)
            message_box('Возникла ошибка при создании расхода,\
                         обратитесь к файлу py_log.')
            raise SystemExit

    @staticmethod
    def read(params: str) -> tuple[str, str, str] | list[Any]:
        """
        Осуществляет чтение из БД, передаёт результаты расходов за день, месяц, неделю и
        соотвествующий свободный остаток, а также сообщает сведения о всех текущих
        транзакциях главному окну приложения
        """
        if params == 'Budget':
            try:
                budgets = (str(qh.get_budget()[0]), str(qh.get_budget()[1]),
                           str(qh.get_budget()[2]))
                return budgets
            except Exception as err:
                logging_config(err)
                message_box('Возникла ошибка при формировании бюджета,\
                             обратитесь к файлу py_log.')
                raise SystemExit

        if params == 'Expense_total':
            try:
                totals = (str(qh.get_day_total()), str(qh.get_week_total()),
                          str(qh.get_month_total()))
                return totals
            except Exception as err:
                logging_config(err)
                message_box('Возникла ошибка при формировании затрат,\
                             обратитесь к файлу py_log.')
                raise SystemExit

        if params == 'Expense_residual':
            try:
                residuals = (str(qh.get_day_residual()), str(qh.get_week_residual()),
                             str(qh.get_month_residual()))
                return residuals
            except Exception as err:
                logging_config(err)
                message_box('Возникла ошибка при формировании остатка,\
                             обратитесь к файлу py_log.')
                raise SystemExit

        if params == 'Expense_data':
            try:
                return qh.get_expense_data()
            except Exception as err:
                logging_config(err)
                message_box('Возникла ошибка при формировании данных о транзакциях,\
                             обратитесь к файлу py_log.')
                raise SystemExit

    @staticmethod
    def update(params: dict[str, Any]) -> None:
        """ Осуществляет изменение уже существующей записи в таблице Expense"""
        try:
            qh.update_expense(trans_id=params['transaction_id'],
                              balance=params['balance'],
                              category=params['category'], date=params['date'],
                              description=params['description'])
        except Exception as err:
            logging_config(err)
            message_box('Возникла ошибка во время обновления транзакции,\
                         обратитесь к файлу py_log.')
            raise SystemExit

    @staticmethod
    def delete(params: int) -> None:
        """ Осуществляет удаление выбранной записи из таблицы Expense"""
        try:
            qh.delete_expense(params)

        except Exception as err:
            logging_config(err)
            message_box('Возникла ошибка во время удаления транзакции,\
                         обратитесь к файлу py_log.')
            raise SystemExit
