import unittest
from pony.orm import db_session, flush
from bookkeeper.models.entities import Expense, Budget


class TestDatabaseEntities(unittest.TestCase):

    @db_session
    def test_expense_creation(self):
        # Создание записи о расходе и проверка атрибутов
        expense = Expense(amount=100.0, category='Продукты')
        flush()
        self.assertIsNotNone(expense.id)
        self.assertEqual(expense.amount, 100.0)
        self.assertEqual(expense.category, 'Продукты')

    @db_session
    def test_budget_creation(self):
        # Создание записи о бюджете и проверка значений
        budget = Budget.select().first()
        self.assertIsNotNone(budget)
        self.assertEqual(budget.monthly, budget.monthly)
        self.assertEqual(budget.weekly, budget.weekly)
        self.assertEqual(budget.daily, budget.daily)


if __name__ == '__main__':
    unittest.main()
