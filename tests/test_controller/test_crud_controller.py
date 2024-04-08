import pytest
import datetime as dt
import bookkeeper.controller.query_helper as qh
from bookkeeper.controller.crud_controller import CrudController


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
    data_before = crudctrl.read('Expense_data')[-1]
    crudctrl.update({'transaction_id': data_before.id, 'balance': 1_000, 'category': 'Аксессуары',
                     'date': dt.date.today(), 'description': 'Чехол'})
    data_after = crudctrl.read('Expense_data')[-1]
    assert data_before.id == data_after.id
    assert (data_after.amount, data_after.category, data_after.expense_date, 
            data_after.comment) == (1000.0, 'Аксессуары', dt.date.today(), 'Чехол')
      
def test_delete_expense(crudctrl):
    crudctrl.create('Expense', {'balance': 5_00, 'category': 'Кафе/рестораны', 'date': dt.date.today(), 'description': 'Обед'})
    crudctrl.delete(crudctrl.read('Expense_data')[-1].id)
    current_data = crudctrl.read('Expense_data')[-1] 
    assert (current_data.amount, current_data.category, current_data.expense_date,
             current_data.comment) != (500.0, 'Кафе/рестораны', dt.date.today(), 'Обед')
