import numpy as np
import matplotlib.pyplot as plt
# import cmath

a = -2
b = np.sqrt(3)

while True:
    z1 = a / (1 - 1j * b)  # Définition du premier nombre complexe
    z2 = 1 / ((1 + abs(a)*1j) * (b**2 - 1j))
    z3 = (1 + abs(a)*1j) / (1 - abs(a)*1j)

    fig, axes = plt.subplots()
    axes.scatter(z1.real, z1.imag, color='blue', label=r"$z_1$")
    axes.scatter(z2.real, z2.imag, color='red', label=r"$z_2$")
    axes.scatter(z3.real, z3.imag, color='green', label=r"$z_3$")
    axes.set_xlabel(r"Partie réelle")
    axes.set_ylabel(r"Partie imaginaire")
    print(z1)
    axes.grid()
    axes.legend()
    fig.show()
    if input ("appuyer sur une touche pour quitter"):
        break
    break

    