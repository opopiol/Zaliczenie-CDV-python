#16. Utwórz funkcję własną, która jako argument przyjmować będzie listę argumentów i wartości, a jako wynik będzie wyświetlać sformatowany wykres (stosowny zakres, opis, kolory, legenda) 

from pylab import plot, show, xticks, yticks, title, xlabel, ylabel, legend
  

def wykres(x,y): 

    plot(x,y,'-ob')
    legend(("f(x)",))
    xlabel('x=argumenty')
    ylabel('y=wartosci')
    title('Wykres')
    show()



 