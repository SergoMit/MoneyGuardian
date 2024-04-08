import os
from bookkeeper.config import way


def test_way():
    assert str(os.getcwd())+'/MG_database.db' == way
