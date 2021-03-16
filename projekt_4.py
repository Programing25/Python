#Poznajmy instrukcje warunkowe (narazie tylko if)
import time

a = input("Podaj 1 liczbę do sprawdzenia: ")
b = input("Podaj 2 liczbę do sprawdzenia: ")
if (b > a):
  d = a-b
  print("liczba " + a + " jest większa od " + b )
elif(a > b):
  print("liczba " + b + " jest większa od " + a )
elif(a==b):
    print("Przecierz te liczby wynoszą tyle samo!")
else:
    print("Errrrrrror... Wykryłem błąd nie jestem w tanie tego policzyć :(")


#P.S bonus otwórz link podspodem. Hasło: 
#1327
#link:
#https://pastebin.com/RhyuBauz