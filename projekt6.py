#6. Utwórz klasę Perceptron zgodnie z modelem McCullocha-Pittsa.
#Przeprowadź eksperyment uczenia neuronu - niech rozpoznaje czy wybrany punkt o współrzędnych x, y znajduje się powyżej lub poniżej zadanej prostej. 

import numpy as np 
  

class Perceptron(): 
   

    def __init__(self,n,c): 
        self.stala_uczenia=c 
        self.liczba_wejsc=n 
        self.waga=[] 

        for i in range(self.liczba_wejsc): 
            self.waga.append(2*np.random.rand(1)[0]-1) 
            

    def aktywacja(self,suma):  #aktywuje perceptron 
        if suma>0: 
            return 1  #dla wartosci powyzej zera bedzie wynosic 1
        else: 
            return -1 #rowne bądz poniżej zera będzie równy -1


    def iloczynSkalarny(self,x): #wylicza sumę potrzebną do aktywacji
        suma=0 
        for i in range(self.liczba_wejsc): 
            suma=suma+x[i]*self.waga[i] 
        return suma 
   

    def odpowiedz(self, x):  #pokazuje ostateczny wynik 1 lub -1
        suma= self.iloczynSkalarny(x) 
        return self.aktywacja(suma) 
    
    
    def dopasuj(self, x, poprawna_odp): #zmienia wagę wejsc w przypadku błędu
        odp = self.odpowiedz(x)
        blad = poprawna_odp - odp
        for i in range (self.liczba_wejsc):
            self.waga[i] = self.waga[i] + self.stala_uczenia * blad * x[i]
  

#Uczenie perceptronu 
            
def cel(xp, yp): #wylicza cel, do którego dążyć będzie perceptron (1 lub -1).
    y_linii = xp #Argumentami będą współrzędne z listy utworzonej w następnym kroku
    if (y_linii - yp)>0:
        return -1
    else:
        return 1
    


for i in range(500):
    x = []
    x.append(40*np.random.rand(1)[0]-20) #utworzenie listy, która ma trzy wartosci: pierwsze dwie losowe to współrzędne, a ostatnia to wartosc testowa równa 1
    x.append(40*np.random.rand(1)[0]-20)
    x.append(1)
    
p = Perceptron(3, 0.05) #Utworzenie perceptronu o liczbie wejsc równej 3 i stałej uczenia się 0.05

poprawna_odp = cel(x[0],x[1])
    
print("Prawidłowy wynik to: {}".format(poprawna_odp))

wynik=p.odpowiedz(x)
print("Wynik perceptronu to: {}".format(wynik))
    

p.dopasuj(x,poprawna_odp)
wynik=p.odpowiedz(x)
    
print("Oczekiwany wynik: {}".format(poprawna_odp))

#Tworzę komunikaty odpowiedzialne za ustalenie wyniku, do którego perceptron ma dążyć, jego odpowiedź oraz, w przypadku złego wyniku, funkcję dopasuj zmieniającą wagę wejscia. Jest ona odpowiedzialna za naukę perceptrona.