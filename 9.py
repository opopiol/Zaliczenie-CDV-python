#9. Utwórz skrypt z interfejsem tekstowym, który wyliczy sumę n kolejnych liczb (użytkownik podaje pierwszą i ostatnią liczbę sumy).
#Uwaga – w zadaniu należy zbudować funkcję własną realizującą dane zadanie

suma=0 

print('Suma n kolejnych liczb: ')  
n=int(input('Podaj pierwszą liczbę: '))  
k=int(input('Podaj drugą liczbę: '))  


for i in range(n,k+1): 
    suma=suma+i
    
 

print("Suma tych liczb wynosi {}".format(suma)) 
    
if (n>k):
    print("Pierwsza liczba nie może być większa od drugiej.")
    
    
def suma_liczb(n,k):
    suma=0
    for i in range(n,k+1): 
        suma=suma+i
    print("Suma tych liczb wynosi {}".format(suma))
    
    