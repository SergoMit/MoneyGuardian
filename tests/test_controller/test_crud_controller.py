import pytest
import unittest
import bookkeeper.controller.query_helper as qh
from bookkeeper.controller.crud_controller import CrudController

from unittest.mock import patch, MagicMock
import datetime as dt

"""
# Пример теста для метода create
def test_create_budget():
    with patch('your_module.qh.add_budget') as mock_add_budget:
        entity = 'Budget'
        params = {'monthly': 1000, 'weekly': 250, 'daily': 50}
        your_class.create(entity, params)
        
        mock_add_budget.assert_called_once_with(monthly=1000, weekly=250, daily=50)
"""

@pytest.fixture
def crudctrl():
    return CrudController()


def test_add_and_read_budget(crudctrl):
    crudctrl.create('Budget', {'monthly': 28_000,
                                     'weekly': 7_000,
                                     'daily': 1_000})
    budget_tup = crudctrl.read('Budget')
    assert budget_tup == ('1000.0', '7000.0', '28000.0')

def test_add_and_read_expense_total(crudctrl):
    date = dt.date.today()
    crudctrl.create('Expense', {'balance': 5_00, 'category': 'Кафе/рестораны', 
                                'date': date, 'description': 'Обед'})
    totals = crudctrl.read('Expense_total')
    assert totals == (str(qh.get_day_total()), str(qh.get_week_total()), str(qh.get_month_total()))

def test_read_expense_residuals(crudctrl):
    residuals = crudctrl.read('Expense_residual')
    assert residuals == (str(qh.get_day_residual()), str(qh.get_week_residual()), str(qh.get_month_residual()))

def test_read_expense_get_data(crudctrl):
    data = crudctrl.read('Expense_data')
    data_info = data[-1]
    assert (data_info.amount, data_info.expense_date, data_info.comment,
             data_info.category) == (500.0, dt.date.today(), 'Обед', 'Кафе/рестораны')

def test_update_expense(crudctrl):
    pass

def test_delete_expense(crudctrl):
    pass
