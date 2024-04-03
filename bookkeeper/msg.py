from PySide6.QtWidgets import QMessageBox


def message_box(text: str) -> None:
    """ Функция, формирующая шаблон окон ошибок"""

    message = QMessageBox()
    message.setWindowTitle('Внимание!')
    message.setText(text)
    message.exec()
