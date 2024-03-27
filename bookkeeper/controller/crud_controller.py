from bookkeeper.models.entities import db
import bookkeeper.controller.query_helper as qh
from bookkeeper.config import way
from typing import Any


class CrudController:
    def __init__(self):
        try:
            db.bind(provider='sqlite',
                    filename=way,
                    create_db=True)
            db.generate_mapping(create_tables=True)

        except Exception as e:
            print(e)

    def create(self, entity: str, params: dict[str, Any]):
        if entity == 'Budget':
            qh.add_budget(monthly=params['monthly'], weekly=params['weekly'],
                          daily=params['daily'])
            return

        if entity == 'Expense':
            qh.add_expense(balance=params['balance'], category=params['category'], date=params['date'],
                           description=params['description'])
            return

        raise NotImplementedError(f'Добавление для сущности {entity} не реализовано!')

    def read(self, params=None):
        pass

    def update(self, entity):
        raise NotImplementedError(f'Изменение для сущности {entity} не реализовано!')

    def delete(self, entity):
        raise NotImplementedError(f'Удаление для сущности {entity} не реализовано!')

    def get_total(self):
        pass

    def calculate_residual(self):
        pass
