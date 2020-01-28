#25. Utwórz fukcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, a jej wynikiem będzie drugi moment centralny (wariancja) 

def wariacja(x): 
    suma=0; 
    for i in x: 
        suma+=((i-(sum(x)/len(x)))**2) 
    return (suma/len(x)) 



