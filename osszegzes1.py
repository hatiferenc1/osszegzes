'''1.1 Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában!

 A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!'''
import random
lista = []

for i in range(5):
    szám = random.randint(1,10)
    lista.append(szám)

összeg = 0
for i in lista:
    összeg = összeg + i




print(összeg)
print(lista)    
