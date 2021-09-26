#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список работников.
    workers = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            name = input("Фамилия и инициалы? ")
            zodiac = input("Знак Зодиака? ")
            year = list(map(int, input("Дата рождения? ").split()))
            # Создать словарь.
            worker = {
                'name': name,
                'zodiac': zodiac,
                'year': year,
            }
            # Добавить словарь в список.
            workers.append(worker)
            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                workers.sort(key=lambda x: x.get('year')[::-1])

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Знак Зодиака",
                    "Дата рождения"
                )
            )
            print(line)

            # Вывести данные о всех сотрудниках.
            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        worker['name'],
                        worker['zodiac'],
                        ' '.join((str(i) for i in worker['year']))
                    )
                )
            print(line)
        elif command == 'whois':
            who = input('Кого ищем?: ')
            count = 0
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Знак Зодиака",
                    "Дата рождения"
                )
            )
            print(line)
            for i, num in enumerate(workers, 1):
                if who == num['name']:
                    count += 1
                    print(
                        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                            count,
                            num['name'],
                            num['zodiac'],
                            ' '.join((str(i) for i in num['year']))))
            print(line)
            if count == 0:
                print('Никто не найден')
        else:
            print('Неизвестная команда', command, file=sys.stderr)