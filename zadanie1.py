#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    school = {}
    for i in range(7):
        school.update(
            {input(f'Название класса № {i + 1} : '): int(input(f'Количество учеников в классе № {i + 1} : '))})
    print(school)
    klas = input('Введите название класса: ')
    if klas in school:
        print(f'Количество учеников в классе {klas} : {school[klas]} ')
    else:
        print('Такого класса на существует')
    for i in range(2):
        school.update({input(f'Название изменяемого класса {i + 1} : '): int(
            input(f'Количество учеников изменяемого класса {i + 1} : '))})
    print(school)
    for i in range(1):
        school.update(
            {input(f'Название нового класса {i + 1} : '): int(input(f'Количество учеников нового класса {i + 1} : '))})
    print(school)
    del school[input(f'Название расформировываемого класса: ')]
    print(school)
