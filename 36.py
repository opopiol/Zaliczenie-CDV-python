#36. Utwórz klasę Prostokąt, a następnie na jej podstawie (korzystając z mechanizmu dziedziczenia) utwórz klasę Kwadrat 

import matplotlib.pyplot as plt  

class Prostokat(): 
    def __init__(self,a,b): 
        self.a=a 
        self.b=b 
        
class Kwadrat(Prostokat): 
    def __init__(self,a): 
        super().__init__(a,a) 