#30. Wynegeruj listę 1000 liczb losowych o rozkładzie normalnym. Wykreśl histogram oraz średnią, medianę, dominantę, odchylenie standardowe, wariancję, skośność i kurtozę 

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import kurtosis
from collections import Counter 

def skosnosc(lista):
    avg=np.mean(lista)
    return 1/len(lista)*sum((lista-avg)**3)/(np.std(lista))**3

liczby=np.random.normal(size=1000)

plt.hist(liczby)

print("Srednia wynosi: {}".format(np.mean(liczby)))
print("Mediana wynosi: {}".format(np.median(liczby)))
print("Dominanta wynosi: {}".format(Counter(liczby).most_common(1)))
print("Odchylenie standardowe wynosi: {}".format(np.std(liczby)))
print("Wariancja wynosi: {}".format(np.var(liczby)))
print("Skosnosc wynosi: {}".format(skosnosc(liczby)))
print("Kurtoza wynosi: {}".format(kurtosis(liczby)))



