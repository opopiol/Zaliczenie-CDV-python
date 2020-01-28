#14. Utworzyć skrypt z interfejsem tekstowym, który będzie zwracać wiersz n-tego rzędu z trójkąta Pascala (użytkownik podaje n, program zwraca odpowiadający wiersz trójkąta) 


def silnia(n):  
    silnia=1  
    for i in range(1,n+1):  
        silnia=silnia*i 

    return silnia 
  

def newton(n,k):
    wynik= (silnia(n)/(silnia(k)*silnia(n-k))) 
    return wynik


print("Jest to program, który zwraca wiersz n-tego rzędu z trójkąta Pascala")
x=int(input("Podaj n, dla którego chcesz wyswietlić wiersz:"))

def pascal(x):
    lista=[]
    
    for i in range(x+1):
        lista.append(int(newton(x,i)))
    return lista

wynik=pascal(x)
print(wynik)  

