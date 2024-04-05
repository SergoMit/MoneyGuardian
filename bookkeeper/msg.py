""" Данный модуль содержит функцию, формирующую шаблон окон ошибок"""

from PySide6 import QtWidgets


def message_box(text: str) -> None:
    """ Функция, формирующая шаблон окон ошибок"""

    message = QtWidgets.QMessageBox()
    message.setWindowTitle('Внимание!')
    message.setText(text)
    message.exec()
