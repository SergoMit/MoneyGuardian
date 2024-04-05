""" В данном модуле определены сущности таблиц, которые сгенерируются при первом подключении к БД"""

import logging

from datetime import date
from pony.orm import *  # type: ignore  # pylint: disable=W0401 disable=W0622 disable=W0614
from config import way  # type: ignore  # pylint: disable=E0401
from msg import message_box  # type: ignore  # pylint: disable=E0401


db = Database()  # type: ignore


class Expense(db.Entity):  # type: ignore
    """ Класс, отвечающий за формирование таблицы Expense в БД"""

    id = PrimaryKey(int, auto=True)  # type: ignore
    amount = Required(float)  # type: ignore
    expense_date = Required(date, default=date.today())  # type: ignore
    added_date = Required(date, default=date.today())  # type: ignore
    comment = Optional(str)  # type: ignore
    category = Required(str)  # type: ignore


class Budget(db.Entity):  # type: ignore
    """ Класс, отвечающий за формирование таблицы Budget в БД"""

    id = PrimaryKey(int, auto=True)  # type: ignore
    monthly = Required(float, default=56000)  # type: ignore
    weekly = Required(float, default=14000)  # type: ignore
    daily = Required(float, default=2000)  # type: ignore


try:
    db.bind(provider='sqlite',
            filename=way,
            create_db=True)
    db.generate_mapping(create_tables=True)
except Exception as e:
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w',
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.info(e)
    message_box('Ошибка подключения к базе данных, обратитесь к файлу py_log.')
    raise SystemExit
