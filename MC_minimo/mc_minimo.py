import numpy as np
import matplotlib.pyplot as plt

N0 = 500
lam = 0.1
dt = 0.01
Tmax = 100

# definicion de arreglo con elementos de tipo Bool, 
alive = np.ones(N0, dtype=bool)

times=[]
counts = []

t = 0

while t<Tmax:
    indices = np.where(alive)[0]            #seleccion de elementos aun sin desintegrar
    r = np.random.rand(len(indices))        #generacion de numeros aleatorios entre [0,1]
    decay = r < lam * dt                    #se establece que nucleo decae mediante una comparacion 
                                            #de los num aleatorios asignados como probabilidades 
                                            # #y la probailidad de decaimiento \lambda dt
    alive[indices[decay]] = False           #alive toma los indices donde decay es false y toma ese valor
                                            #se establece que particulas han decaido en el arreglo original 
    times.append(t)                         #se captura el paso de tiempo en una lista 
    counts.append(np.sum(alive))            #se captura el numero total de elementos que aun sobreviven 
                                            #son las particulas que aun no se desintegran

    t+=dt                                   #se aumenta un paso de tiempo y el bucle se reinicia

#plot del numero de particulas que aun no decaen en funcion del tiempo 
#plot los pasos de tiempo vs el conteo de alive=True
plt.plot(times, counts, label='Monte Carlo Mínimo')
plt.legend()
plt.title('Solucion Monte Carlo mínima a la ecuacion de decaimiento \nradioactivo de la forma $N(t) = N_0 e^{-\lambda t}$')
plt.xlabel('t')
plt.ylabel('counts')
#se guarda una imagen del proceso en formato PNG
plt.savefig('MC_minimo/decay_minimo.png')   

