import numpy as np
import scipy.integrate as integrate

def f(var,a):
    return np.exp(-a*var**2)

#Calcul del’intégrale 
# On metla fonction en premier argument 
# #Les bornes de l’integrale sont donnees ensuite 
# args=(1,) est l'argument que vous avez passé. Cela signifie que vous fixez la valeur de a à 1 pour cette intégrale.
I1,incertitude =integrate.quad(f,-np.inf,np.inf,args=(1,))
print('\n I1 égale à :',I1)

# on affiche le résultat de la fonction simplifié :

simplified_function = np.sqrt(np.pi)

print('\n La forme simplifié de l\'intégrale égale à :',simplified_function)

print((simplified_function==I1))
