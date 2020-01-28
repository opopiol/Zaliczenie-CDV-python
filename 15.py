#15. Utwórz skrypt, w którym zamieścisz 3 listy danych, zawierające po 14 temperatur dla 3 wybranych miast na kolejne 14 dni oraz utwórz wykres z tych danych.
#Twój wykres powinien mieć 3 linie z zaznaczonymi punktami danych za pomocą różnych znaczników, tytuł, opisane osie oraz legendę

from pylab import plot, show, xticks, yticks, title, xlabel, ylabel, legend, savefig 

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14] 

y=[7,7,9,8,6,4,2,0,-1,-3,4,6,8,5] 
y2=[6,8,11,12,9,9,7,6,6,5,3,2,5,8] 
y3=[-1,0,-3,3,4,7,8,6,5,3,0,-2,-4,0] 

y4=[0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
  

plot(x,y,'-or',x,y2,'-db',x,y3,'-sy',x,y4,'--k') 
  

xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14], fontsize='10', fontname='Arial') 
yticks([-4,-2,0,2,4,6,8,10,12]) 

  
title("Prognoza pogody na dwa tygodnie", fontsize='20', fontname='Arial') 
xlabel("Dzień miesiąca", fontsize='15', fontname='Arial')  
ylabel("Temperatura", fontsize='15', fontname='Arial')  

  
legend(["Poznań","Berlin","Kraków"])  
  

