""" 
В данном модуле содержатся функции, которые обращаются непосредственно
к БД и выполняют определённые манипуляции с данными
"""

import datetime as dt

from pony.orm import *  # type: ignore  # pylint: disable=W0401 disable=W0622 disable=W0614
from bookkeeper.models.entities import db  # type: ignore  # pylint: disable=E0401
from bookkeeper.msg import message_box  # type: ignore  # pylint: disable=E0401
from bookkeeper.config import logging_config  # type: ignore  # pylint: disable=E0401


@db_session  # type: ignore
def first_budget():
    """ Функция, задающая начальный бюджет в пустой базе данных"""
    checking = select(b for b in db.Budget)[:]  # pylint: disable=E1101
    if not checking:
        db.Budget(id=0)  # pylint: disable=E1101


@db_session  # type: ignore
def add_budget(monthly: float, weekly: float, daily: float) -> None:
    """ Функция, реализующая внесение данных о текущем бюджете"""
    try:
        delete(b for b in db.Budget)  # type: ignore  # pylint: disable=E1101
        db.Budget(monthly=monthly, weekly=weekly, daily=daily)  # pylint: disable=E1101
    except Exception as err:
        logging_config(err)
        message_box('Не удалось внести данные в таблицу Budget, обратитесь к файлу py_log.')


@db_session  # type: ignore
def get_budget() -> list[float]:
    """ Функция, реализующая извлечение актуальных данных о бюджете"""
    try:
        first_budget()
        budgets = select(b for b in db.Budget).order_by(-1).first()  # type: ignore  # pylint: disable=E1101
        return [budgets.daily, budgets.weekly, budgets.monthly]
    except Exception as err:
        logging_config(err)
        message_box('Не удалось извлечь данные из таблицы Budget, обратитесь к файлу py_log.')


@db_session  # type: ignore
def add_expense(balance: float, category: str, date: dt.date, description: str | None) -> None:
    """ Функция, реализующая добавление записи о расходах в таблицу Expense """
    try:
        db.Expense(amount=balance, expense_date=date, comment=description, category=category)  # pylint: disable=E1101
    except Exception as err:
        logging_config(err)
        message_box('Не удалось внести данные в таблицу Expense, обратитесь к файлу py_log.')


@db_session  # type: ignore
def delete_expense(trans_id: int) -> None:
    """ Функция, реализующая удаление записи о расходе в таблице Expense"""
    try:
        delete(e for e in db.Expense if e.id == trans_id)  # type: ignore  # pylint: disable=E1101
    except Exception as err:
        logging_config(err)
        message_box('Не удалось удалить данные из таблицы Expense, обратитесь к файлу py_log.')


@db_session  # type: ignore
def update_expense(trans_id: int, balance: float, category: str,
                    date: dt.date, description: str | None) -> None:
    """ Функция, реализующая обновление выбранной транзакции"""
    try:
        expense = db.Expense[trans_id]  # pylint: disable=E1101
        expense.set(amount=balance, expense_date=date, comment=description, category=category)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось обновить данные в таблице Expense, обратитесь к файлу py_log.')


@db_session  # type: ignore
def get_day_total() -> float:
    """ Подсчёт затрат за день"""
    try:
        day_total = select(e.amount for e in db.Expense).where(  # pylint: disable=E1101
            lambda e: e.expense_date == dt.date.today())[:]  # type: ignore
        return sum(day_total)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт day_total, обратитесь к файлу py_log.')


@db_session  # type: ignore
def get_week_total() -> float:
    """ Подсчёт затрат за неделю"""
    try:
        week_interval = dt.date.today() - dt.timedelta(days=7)
        week_total = (select(e.amount for e in db.Expense).where  # type: ignore  # pylint: disable=E1101
                      (lambda e: e.expense_date >= week_interval
                        and e.expense_date <= dt.date.today()))[:]
        return sum(week_total)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт week_total, обратитесь к файлу py_log.')


@db_session  # type: ignore
def get_month_total() -> float:
    """ Подсчёт затрат за месяц"""
    try:
        month_interval = dt.date.today() - dt.timedelta(days=28)
        month_total = (select(e.amount for e in db.Expense).where  # type: ignore  # pylint: disable=E1101
                       (lambda e: e.expense_date >= month_interval
                         and e.expense_date <= dt.date.today()))[:]
        return sum(month_total)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт month_total, обратитесь к файлу py_log.')


def get_day_residual() -> float:
    """ Подсчёт остаточной допустимой суммы расхода за день"""
    try:
        day_residual = get_budget()[0] - get_day_total()
        return day_residual
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт day_residual, обратитесь к файлу py_log.')


def get_week_residual() -> float:
    """ Подсчёт остаточной допустумой суммы расхода за неделю"""
    try:
        week_residual = get_budget()[1] - get_week_total()
        return week_residual

    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт week_residual, обратитесь к файлу py_log.')


def get_month_residual() -> float:
    """ Подсчёт остаточной допустимой суммы расхода за месяц"""
    try:
        month_residual = get_budget()[2] - get_month_total()
        return month_residual
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт month_residual, обратитесь к файлу py_log.')


@db_session  # type: ignore
def get_expense_data():
    """ Сбор данных из таблицы Expense"""
    try:
        expense_data = (select(e for e in db.Expense))[:]  # type: ignore  # pylint: disable=E1101
        return expense_data
    except Exception as err:
        logging_config(err)
        message_box('Не удалось собрать данные о транзакциях из таблицы Expense')
