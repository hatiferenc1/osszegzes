'''2. Feladat
Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. A bekérés akkor fejeződjön be, amikor a felhasználó intervallumon kívüli értéket ad meg! A program írja ki a megadott intervallumba eső számokat és az összegüket!'''
lista = []
while True:
    szám = int(input('Adj meg egy számot '))
    if -5 <= szám <= 5:
        lista.append(szám)
    else:
        break

összeg = 0 
for i in lista:
    összeg = összeg + i

print(lista)
print(összeg)    