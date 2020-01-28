#21. Utwórz fukcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, a jej wynikiem będzie średnia arytmetyczna.
#Porównaj jej wynik z wynikiem fukcji mean z pakietu numpy 

import numpy as np 

def srednia(x): 
    return sum(x)/len(x) 

#Na konsoli wprawdzam: x=[4,6,7,0], tworząc listę.
#Następnie wprowadzam srednia(x)
#Otrzymuję wynik: 4.25
#Importuję np z biblioteki numpy, aby porównować mój wynik z wynikiekm jej funkcji mean
#Korzystając z funkcji mean wprowadzam: np.mean(x)
#Otrzymuję ten sam wynik, czyli: 4.25
