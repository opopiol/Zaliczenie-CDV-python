#4. Utwórz klasę Vector3D. Wykorzystaj całą wiedzę jaką posiadasz na temat wektorów w przestrzeni.
#Zdefiniuj wszystkie znane Ci operacje. 

import numpy as np 
import math as math 

  


class Vector3D(): 
    def __init__(self,x,y,z): 

        self.x=x 
        self.y=y 
        self.z=z 

         
         

    def wspolrzedne(self): 

        return(self.x,self.y, self.z) #Funkcja ta pozwala na wyswietlanie wspolrzednych wektora.

         
    

    def suma_w(self,b): 

        self.x=self.x+b.x 
        self.y=self.y+b.y 
        self.z=self.z+b.z 
        print(self.x,self.y,self.z)  #Dzięki tej funkcji można zwiększyć wektor o inny wektror, czyli pozwala na obliczeniu ich sumy.


         

    def roznica_w(self,b): 

        self.x=self.x-b.x 
        self.y=self.y-b.y 
        self.z=self.z-b.z 
        print(self.x,self.y,self.z) #Dzięki tej funkcji można zmniejszyć wektor o inny wektror, czyli pozwala na obliczeniu ich różnicy.

     

    def mn_liczba(self,c): 

        self.x=self.x*c 
        self.y=self.y*c 
        self.z=self.z*c 
        print(self.x,self.y,self.z) #Funkcja pozwala na wymnożenie wektora przez liczbę. 


    def mn_w(self,b): 

        self.x=self.x*b.x 
        self.y=self.y*b.y 
        self.z=self.z*b.z 
        print(self.x) 
        print(self.y)  
        print(self.z)  #Funkcja wymnaża wektor przez drugi wektor.

     

    def modul(self): 
        print(((self.x)**2+(self.y)**2+(self.z)**2)**0.5) #Funkcja oblicza moduł 

     

    def w_przeciw(self): 
        return (-self.x,-self.y,-self.z) #Funkcja wyznacza wektor przeciwny. 
    