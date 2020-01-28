#32. Utwórz funckję, która na zadanej macierzy zapisze wzór ustalonych struktur
#(blok, ul, bochenek, łódka, światła uliczne, żaba, latarnia

import numpy as np 
import matplotlib.pyplot as plt 

  
def macierz(n): 
    a = np.random.choice([0,255], n*n, p=[0.2,0.8]).reshape(n,n) 
    return a 

  

m = np.zeros(10*10).reshape(10,10) 
plt.imshow(m) 

  

def addSwiatla_uliczne(i,j,grid):   
    swiatla_uliczne = np.array([[0,255,0],[0,255,0],[0,255,0]])   
    rx=swiatla_uliczne.shape[0] 
    ry=swiatla_uliczne.shape[1] 
    

    grid[i:i+rx, j:j+ry] = swiatla_uliczne 
    plt.imshow(grid) 
    return grid  
    


def addUl(i,j,grid):   
    ul = np.array([[0,255,255,0],[255,0,0,255],[0,255,255,0],])   
    rx=ul.shape[0] 
    ry=ul.shape[1] 


    grid[i:i+rx, j:j+ry] = ul 
    plt.imshow(grid) 
    return grid 

     


def addBochenek(i,j,grid):    
    bochenek = np.array([[0,255,255,0],[255,0,0,255],[0,255,0,255],[0,0,255,0]])   
    rx=bochenek.shape[0] 
    ry=bochenek.shape[1] 
 

    grid[i:i+rx, j:j+ry] = bochenek 
    plt.imshow(grid) 
    return grid 

  

def addLodz(i,j,grid):    
    lodz = np.array([[255,255,0],[255,0,255],[0,255,0]])   
    rx=lodz.shape[0] 
    ry=lodz.shape[1] 
  

    grid[i:i+rx, j:j+ry] = lodz 
    plt.imshow(grid) 
    return grid 

  

def addBlok(i,j,grid):   
    blok = np.array([[255,255,],[255,255,]])   
    rx=blok.shape[0] 
    ry=blok.shape[1] 

     
    grid[i:i+rx, j:j+ry] = blok 
    plt.imshow(grid) 
    return grid 

     

def addZaba(i,j,grid):   
    zaba = np.array([[0,255,255,255],[255,255,255,0]])   
    rx=zaba.shape[0] 
    ry=zaba.shape[1] 

     
    grid[i:i+rx, j:j+ry] = zaba 
    plt.imshow(grid) 
    return grid 

     

def addLatarnia(i,j,grid):   
    latarnia = np.array([[255,255,0,0],[255,0,0,0],[0,0,0,255],[0,0,255,255]])   
    rx=latarnia.shape[0] 
    ry=latarnia.shape[1] 
    

    grid[i:i+rx, j:j+ry] = latarnia 
    plt.imshow(grid) 
    return grid 