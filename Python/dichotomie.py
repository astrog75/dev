# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:20:27 2022

@author: moty_
"""

# Ce script modélise le problème du pendule simple
# voir : https://professeurb.github.io/ipt/sup/pendule/

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi

omega_0 = 1
duree = 40 # secondes
dt = 0.01 # secondes

temps = np.arange(0, duree+dt, dt)

# Cette fonction retourne les valeurs de theta et theta_point à l'instant t + dt
# en fonction des valeurs de de theta et theta_point à l'instant t
# grâce à un développement limité d'ordre 1
def euler(theta, theta_point):
    nouveau_theta_point = theta_point - pow(omega_0, 2)*sin(theta)*dt
    nouveau_theta = theta + theta_point*dt
    return (nouveau_theta, nouveau_theta_point)

# Cette fonction retourne la liste des valeurs de theta et theta_point en fonction
# des conditions initiales
def simule(theta_0, theta_point_0):
    liste_theta = [theta_0]
    liste_theta_point = [theta_point_0]
    theta = theta_0
    theta_point = theta_point_0
    
    for t in temps[0:len(temps)-1]:
        (nouveau_theta, nouveau_theta_point) = euler(theta, theta_point)
        liste_theta.append(nouveau_theta)
        liste_theta_point.append(nouveau_theta_point)
        theta = nouveau_theta
        theta_point = nouveau_theta_point
    
    return (liste_theta, liste_theta_point)

# print(liste_theta)
# print(liste_theta_point)

def energie(theta, theta_point):
    return 0.5*pow(theta_point, 2) + pow(omega_0, 2)*(1-cos(theta))

def simule_energie(theta_0, theta_point_0):
    
    liste_energie = []
    (liste_theta, liste_theta_point) = simule(theta_0, theta_point_0)
    
    for i in range(len(liste_theta)):
        liste_energie.append(energie(liste_theta[i], liste_theta_point[i]))
    
    return liste_energie

# Plot of the energy evolution
for theta_0 in np.arange(0, 2 + 0.1, 0.1):
    title = "Energy evolution of the pendule simple with theta_0 = " + str(theta_0)
    plt.title(title)
    plt.xlabel("Temps")
    plt.ylabel("Energie mécanique")
    plt.plot(temps, simule_energie(theta_0, 0))
    plt.show()
    

# Plot of the mouvement
for theta_0 in np.arange(0, 2 + 0.1, 0.1):
    title = "Phase diagram with theta_0 = " + str(theta_0)
    plt.title(title)
    plt.xlabel("theta")
    plt.ylabel("theta_point")
    (liste_theta, liste_theta_point) = simule(theta_0, 0)
    plt.plot(liste_theta, liste_theta_point)
    plt.show()

# plt.plot(temps, liste_theta_point)
# plt.title("Evolution of theta_point")
# plt.show()