import os
import logging

# Формирование пути, не зависящего от устройства пользователя, до объекта базы данных
way = str(os.getcwd())+'/MG_database.db'


def logging_config(parameter: Exception) -> None:
    """ Данная функция позволяет записывать исключения в файл py_log.log проекта"""

    # Создание логгирующего объекта
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Настройка обработчика и форматировщика для логгирующего объекта logger
    handler = logging.FileHandler('py_log.log', mode='w')
    formatter = logging.Formatter("s%(name)s %(asctime)s %(levelname)s %(message)s")

    # Добавление форматировщика к обработчику
    handler.setFormatter(formatter)

    # Добалвение обработчика к объекту logger
    logger.addHandler(handler)

    # Задание типа сообщений, выводимых объектом logger
    logger.exception('occured. Reason: ')

    if parameter:
        pass
