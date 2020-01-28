#6. Utwórz skrypt dodający ułamki zwykłe.

print('Ten program służy do dodawania ułamków zwykłych')

licznik1=int(input('Podaj licznik pierwszej liczby: '))
mianownik1=int(input('Podaj mianownik pierwszej liczby: '))
licznik2=int(input('Podaj licznik drugiej liczby: '))
mianownik2=int(input('Podaj mianownik drugiej liczby: '))

from fractions import Fraction 
wynik= (Fraction(licznik1,mianownik1) + Fraction(licznik2,mianownik2))

print(wynik) 