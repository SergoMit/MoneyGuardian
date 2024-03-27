from pony.orm import *
from models.entities import Budget, Expense


@db_session
def add_budget(monthly: float, weekly: float, daily: float):
    try:
        Budget(monthly=monthly, weekly=weekly, daily=daily)
    except Exception as e:
        print(e)  # TODO: This should be sent to GUI in a user-friendly manner


@db_session
def get_budget() -> tuple[list[float]]:
    try:
        q = select(b for b in Budget).order_by(lambda: desc(b.id)).limit(1)
        budget = q.to_list()[0]
        return tuple([budget.monthly, budget.weekly, budget.daily])  # TODO: return the object itself for GUI?
    except Exception as e:
        print(e)  # TODO: This should be sent to GUI in a user-friendly manner


@db_session
def add_expense(balance, category, date, description):
    """
    :param balance:
    :param category:
    :param date:
    :param description:
    :return:
    """
    try:
        Expense(amount=balance, expense_date=date, comment=description, category=category)
    except Exception as e:
        print(e)


@db_session
def get_expense():
    pass


@db_session()
def get_day_total():
    """
    Подсчёт затрат за день
    """
    pass


@db_session()
def get_week_total():
    """
    Подсчёт затрат за неделю
    """
    pass


@db_session()
def get_month_total():
    """
    Подсчёт затрат за месяц
    """
    pass


@db_session()
def get_residual():
    """
    Подсчёт остаточной допустимой суммы расхода
    """
    pass

@db_session()
def get_month_total():
    pass

@db_session()
def get_residual():
    pass
