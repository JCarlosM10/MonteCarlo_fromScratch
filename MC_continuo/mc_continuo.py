import numpy as np 
import matplotlib.pyplot as plt

#N0 = 500
def decay(N0):
    lam = 0.05

    #definicion de parametro de decaimiento como proporcion N(t)=1/r(t)N_0
    r = np.random.rand(N0)

    # definicion de tiempo de vida para una particula usando el parametro de decaimiento
    lifetimes = -np.log(r) / lam

    #definicion de un alpso de tiempo para la simulación y numero de pasos
    t = np.linspace(0,100,50)

    # suma de los elementos que estab por encima del umbral de decaimiento
    # aquellas particulas cuyo timpo de decaimiento es mayor al tiempo transcurrido 
    # sobreviven mientras que aquellas que tienen un tiempo menor ya han decaido 
    N_t = [np.sum(lifetimes > ti) for ti in t]

    # uso de la expresion analitica de la solucion 
    analytic = N0 * np.exp(-lam * t)

    #plot de las soluciones Monte Carlo y analitica, comparativa visual
    plt.plot(t, N_t, label='Monte Carlo')
    plt.plot(t, analytic, '--', label='Analítica $N(t)=N_0 e^{-\lambda t}$')
    plt.title('Monte Carlo vs Solucion analítica',
    '\nVisualización de Convergencia Estadística y Reduccion de Varianza')
    plt.xlabel('time $t$')
    plt.ylabel('counts $N$')
    plt.legend()
    plt.savefig(f'MC_continuo/graphs/decay_continuo_{N0}.png')
    plt.close()
