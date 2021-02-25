'''1.2 Feladat
Módosítsd úgy a fenti programot, hogy a program csak a páros számokat adja össze!'''

import random
lista = []

for i in range(5):
    szám = random.randint(1,10)
    lista.append(szám)

összeg = 0
for i in lista:
    if i % 2 == 0:
        összeg = összeg + i




print(összeg)
print(lista)    
