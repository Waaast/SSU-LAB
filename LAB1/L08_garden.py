#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
    # в саду сорвали цветы
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

    # на лугу сорвали цветы
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

    # создайте множество цветов, произрастающих в саду и на лугу
    # garden_set =
    # meadow_set =
    # TODO здесь ваш код
    garden_set =set(garden)
    meadow_set =set(meadow)
    # выведите на консоль все виды цветов
    # TODO здесь ваш код
    print(garden_set | meadow_set)
    # выведите на консоль те, которые растут и там и там
    # TODO здесь ваш код
    tgt = garden_set & meadow_set
    print(tgt)
    # выведите на консоль те, которые растут в саду, но не растут на лугу
    # TODO здесь ваш код
    print(garden_set-meadow_set)
    # выведите на консоль те, которые растут на лугу, но не растут в саду
    # TODO здесь ваш код
    print(meadow_set-garden_set)
    return ""
if __name__ == "__main__":
    print(main()) 