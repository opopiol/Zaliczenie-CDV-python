#34. Utwórz pustą klasę Figura, a następnie utwórz dwie instancje tej klasy. Sprawdź czy są sobie równe 

class Figura:
    def __init__(self, wysokosc, szerokosc):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc

#Na konsoli wykonuję następujące działania:      
#f1=Figura 
#f2=Figura
#f1==f2

#Otrzymuje taki rezultat
#Out[134]: True 
        
#Także dwie instancje tej klasy są sobie równe