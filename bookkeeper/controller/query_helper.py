import datetime as dt

from pony.orm import *
from models.entities import Expense, Budget
from models.entities import db
from msg import message_box
from config import logging_config


@db_session
def first_budget():
    checking = select(b for b in db.Budget)[:]
    if not checking:
        Budget(id=0)


@db_session
def add_budget(monthly: float, weekly: float, daily: float) -> None:
    """ Функция, реализующая внесение данных о текущем бюджете"""
    try:
        delete(b for b in db.Budget)
        Budget(monthly=monthly, weekly=weekly, daily=daily)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось внести данные в таблицу Budget, обратитесь к файлу py_log.')


@db_session
def get_budget() -> list[float]:
    """ Функция, реализующая извлечение актуальных данных о бюджете"""
    try:
        first_budget()
        budgets = select(b for b in db.Budget).order_by(-1).first()
        return [budgets.daily, budgets.weekly, budgets.monthly]
    except Exception as err:
        logging_config(err)
        message_box('Не удалось извлечь данные из таблицы Budget, обратитесь к файлу py_log.')


@db_session
def add_expense(balance: float, category: str, date: dt.date, description: str | None) -> None:
    """ Функция, реализующая добавление записи о расходах в таблицу Expense """
    try:
        Expense(amount=balance, expense_date=date, comment=description, category=category)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось внести данные в таблицу Expense, обратитесь к файлу py_log.')


@db_session
def delete_expense(trans_id: int) -> None:
    """ Функция, реализующая удаление записи о расходе в таблице Expense"""
    try:
        delete(e for e in db.Expense if e.id == trans_id)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось удалить данные из таблицы Expense, обратитесь к файлу py_log.')


@db_session
def update_expense(trans_id: int, balance: float, category: str, date: dt.date, description: str | None) -> None:
    """ Функция, реализующая обновление выбранной транзакции"""
    try:
        expense = Expense[trans_id]
        expense.set(amount=balance, expense_date=date, comment=description, category=category)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось обновить данные в таблице Expense, обратитесь к файлу py_log.')


@db_session
def get_day_total() -> float:
    """
    Подсчёт затрат за день
    """
    try:
        day_total = select(e.amount for e in db.Expense).where(lambda e: e.expense_date == dt.date.today())[:]
        return sum(day_total)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт day_total, обратитесь к файлу py_log.')


@db_session
def get_week_total() -> float:
    """
    Подсчёт затрат за неделю
    """
    try:
        week_interval = dt.date.today() + dt.timedelta(days=7)
        week_total = (select(e.amount for e in db.Expense).where
                      (lambda e: e.expense_date <= week_interval and e.expense_date >= dt.date.today()))[:]
        return sum(week_total)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт week_total, обратитесь к файлу py_log.')


@db_session
def get_month_total() -> float:
    """
    Подсчёт затрат за месяц
    """
    try:
        month_interval = dt.date.today() + dt.timedelta(days=28)
        month_total = (select(e.amount for e in db.Expense).where
                       (lambda e: e.expense_date <= month_interval and e.expense_date >= dt.date.today()))[:]
        return sum(month_total)
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт month_total, обратитесь к файлу py_log.')


def get_day_residual() -> float:
    """Подсчёт остаточной допустимой суммы расхода за день"""
    try:
        day_residual = get_budget()[0] - get_day_total()
        return day_residual
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт day_residual, обратитесь к файлу py_log.')


def get_week_residual() -> float:
    """Подсчёт остаточной допустумой суммы расхода за неделю"""
    try:
        week_residual = get_budget()[1] - get_week_total()
        return week_residual

    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт week_residual, обратитесь к файлу py_log.')


def get_month_residual() -> float:
    """Подсчёт остаточной допустимой суммы расхода за месяц"""
    try:
        month_residual = get_budget()[2] - get_month_total()
        return month_residual
    except Exception as err:
        logging_config(err)
        message_box('Не удалось выполнить расчёт month_residual, обратитесь к файлу py_log.')


@db_session
def get_expense_data():
    """Сбор данных из таблицы Expense"""
    try:
        expense_data = (select(e for e in db.Expense))[:]
        return expense_data
    except Exception as err:
        logging_config(err)
        message_box('Не удалось собрать данные о транзакциях из таблицы Expense')
