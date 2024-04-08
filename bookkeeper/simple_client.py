"""
Простой тестовый скрипт для терминала
"""

import bookkeeper.controller.query_helper as qh

lines = '------------------------------------------------------------'
space = '                                                            '
while True:
    try:
        print(f'Введите буквами одно из следующих слов для\n\
              \rвывода соответствующей информации на экран:\n\
            \r"расходы" "бюджет" "остаток" "транзакции" "выход"\n\
            \r{lines}\n\r{space}',sep=' ')
        cmd = input('$> ').strip(' ')
    except EOFError:
        break
    if not cmd:
        continue
    if cmd == 'расходы':
        try:
            print(f'День: {qh.get_day_total()}\nНеделя:{qh.get_week_total()}\n\
                  \rМесяц: {qh.get_month_total()}\n\r{lines}\n\r{space}', sep= ' ')
        except Exception:
            break
    elif cmd == 'бюджет':
        try:
            print(f'День: {qh.get_budget()[0]}\nНеделя:{qh.get_budget()[1]}\n\
                  \rМесяц: {qh.get_budget()[1]}\n\r{lines}\n\r{space}', sep= ' ')
        except Exception:
            break
    elif cmd == 'остаток':
        try:
            print(f'День: {qh.get_day_residual()}\nНеделя:{qh.get_week_residual()}\n\
                  \rМесяц: {qh.get_month_residual()}\n\r{lines}\n\r{space}', sep= ' ')
        except Exception:
            break
    elif cmd == 'транзакции':
        try:
            qh.get_expense_data().show()
            print(f'{lines}\n\r{space}')
        except Exception:
            break
    elif cmd == 'выход':
        raise SystemExit
