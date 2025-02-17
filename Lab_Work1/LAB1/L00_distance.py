#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():

    # Есть словарь координат городов

    sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
    }

    # Составим словарь словарей расстояний между ними
    # расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    distances = {}

    # TODO здесь заполнение словаря

    distances['Moscow'] = {
    'London': ((550 - 510) ** 2 + (370 - 510) ** 2) ** 0.5,
    'Paris': ((550 - 480) ** 2 + (370 - 480) ** 2) ** 0.5
    }

    distances['London'] = {
    'Moscow': distances['Moscow']['London'],  
    'Paris': ((510 - 480) ** 2 + (510 - 480) ** 2) ** 0.5
    }

    distances['Paris'] = {
    'Moscow': distances['Moscow']['Paris'],
    'London': distances['London']['Paris']
    }
    return distances
if __name__ == "__main__":
    from pprint import pprint
    pprint(main()) 





