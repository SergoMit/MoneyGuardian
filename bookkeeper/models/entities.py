from datetime import date
from pony.orm import *
from config import way
import logging
from msg import message_box

""" В данном модуле определены сущности таблиц, которые сгенерируются при первом подключении к БД"""

db = Database()


class Expense(db.Entity):
    id = PrimaryKey(int, auto=True)
    amount = Required(float)
    expense_date = Required(date, default=date.today())
    added_date = Required(date, default=date.today())
    comment = Optional(str)
    category = Required(str)


class Budget(db.Entity):
    id = PrimaryKey(int, auto=True)
    monthly = Required(float, default=56000)
    weekly = Required(float, default=14000)
    daily = Required(float, default=2000)


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

