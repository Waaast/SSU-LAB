from LAB1.L00_distance import main as distance
from LAB1.L01_circle import main as circle
from LAB1.L02_operations import main as operations
from LAB1.L03_favorite_movies import main as favorite_movies
from LAB1.L04_my_family import main as my_family
from LAB1.L05_zoo import main as zoo
from LAB1.L06_songs_list import main as songs_list
from LAB1.L07_secret import main as secret
from LAB1.L08_garden import main as garden
from LAB1.L09_shopping import main as shopping
from LAB1.L10_store import main as store
from pprint import pprint

def main():
    print("Запуск всех заданий:")
    print("==================================================================================\
          \nЗадание 00")
    dis=distance()
    pprint(dis)
    print("==================================================================================\
          \nЗадание 01")
    dis=circle()
    print(dis)
    print("==================================================================================\
          \nЗадание 02")
    dis=operations()
    print(dis)
    print("==================================================================================\
          \nЗадание 03")
    dis=favorite_movies()
    print(dis)
    print("==================================================================================\
          \nЗадание 04")
    dis=my_family()
    print(dis)
    print("==================================================================================\
          \nЗадание 05")
    dis=zoo()
    print(dis)
    print("==================================================================================\
          \nЗадание 06")
    dis=songs_list()
    print(dis)
    print("==================================================================================\
          \nЗадание 07")
    dis=secret()
    print(dis)
    print("==================================================================================\
          \nЗадание 08")
    dis=garden()
    print(dis)
    print("==================================================================================\
          \nЗадание 09")
    dis=shopping()
    pprint(dis)
    print("==================================================================================\
          \nЗадание 10")
    dis=store()
    print(dis)
    return "ЗАДАНИЯ ВЫПОЛНЕНЫ!!!"

print(main())