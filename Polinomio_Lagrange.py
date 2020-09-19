#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:08:54 2020

@author: arley
"""

"""Interpolação com polinômios de lagrange"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy


####################### Dados de NIR #########################################

#dados = pd.DataFrame(pd.read_excel('Resultado 175bar_1000ppm_50C_Heptol.xlsx'))

#X  = np.array(dados.loc[0, :])[10:80]

#Y1 = np.array(dados.loc[1, :])[10:80]

#Y2 = np.array(np.array(dados.loc[2, :]))[20:80]

#Y3 = np.array(np.array(dados.loc[3, :]))[20:80]

#Y4 = np.array(np.array(dados.loc[4, :]))[20:80]


###################### Dados de entrada genérico #####################################
X = np.arange(0, 2*np.pi, 0.3)

Y1 = 5*np.sin(X)


################## Polinômio de Lagrange ####################################

def Lagrange(x, y, grau):   
    
    L, l = 1, 1
    
    Arm_L, F = [], []
    
    Arm_P, P, P_numerico = [], [], []
    
    X = sy.symbols('X')

    """Cálculo das funções de base do polinômio de Lagrange"""
    for i in range(0, grau+1):
        
        for j in range(0, grau+1):
            
            if (i != j):
                
                l = (X - x[j])/(x[i] - x[j])
                
                Arm_L.append(l)
        
        L = np.prod(Arm_L) 
        
        P = y[i]*L 
        
        Arm_P.append(sy.expand(P))
        F.append(Arm_L)
        Arm_L= []
        
        L= 0
        
    P_algebrico = sy.expand(sum(Arm_P))
    
    """Substituindo os valores de x na expressão encontrada"""
    for n in range(len(x)):  
        
        P_numerico.append(P_algebrico.subs(X, x[n]))
        
        
    return P_algebrico, P_numerico, F


############ Gráfico dos dados reais e dos gerados pelo polinômio ############
    
def graf (x, y, grau):
    
    _, P_numerico, _ = Lagrange(x, y, grau)
    
    fig, axe= plt.subplots(1, 1, figsize = (11,7))
    
    axe.plot(x, y, label = 'Experimental')
    
    axe.plot(x, P_numerico, 'k--', label= 'Lagrange')
    
    plt.legend(loc= 'best')
    
    plt.show()
    
    
######################### Execução do código #################################
grau= 13
    
graf(X, Y1, grau)

    
    