#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:08:54 2020

@author: arley
"""

"""Interpolação com polinômios de lagrange"""

#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy


####################### Dados de NIR #########################################

#dados = pd.DataFrame(pd.read_excel('Resultado 175bar_1000ppm_50C_Heptol.xlsx'))

#X  = np. array(np.array(dados.loc[0, :]))[1:]

#Y1 = np.array(np.array(dados.loc[1, :]))[1:]

#Y2 = np.array(np.array(dados.loc[2, :]))[1:]

#Y3 = np.array(np.array(dados.loc[3, :]))[1:]

#Y4 = np.array(np.array(dados.loc[4, :]))[1:]


###################### Dados de entrada #####################################
X=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

Y1=[0.08, 0.12, 0.18, 0.19, 0.187, 0.193, 0.178, 0.165, 0.16, 0.11, 0.13, 0.12]


################## Polinômio de Lagrange ####################################

def Lagrange(x, y):   
    
    L, l = 1, 1
    
    Arm_P, P, P_numerico = [], [], []
    
    grau= np.shape(x)[0] 
    
    X = sy.symbols('X')

    """Cálculo das funções de base do polinômio de Lagrange"""
    for i in range(0, grau):
        
        for j in range(0, grau):
            
            if (i != j):
                
                l = (X - x[j])/(x[i] - x[j])
            
            L = L*l 
        
        P = y[i]*L 
        
        Arm_P.append(sy.expand(P))
        
        L = 1
        
    P_algebrico = sy.expand(sum(Arm_P))
    
    """Substituindo os valores de x na expressão encontrada"""
    for i in range(len(x)):  
        
        P_numerico.append(P_algebrico.subs(X, x[i]))
        
        
    return P_algebrico, P_numerico


############ Gráfico dos dados reais e dos gerados pelo polinômio ############
    
def graf (x, y):
    
    P_algebrico, P_numerico = Lagrange(x, y)
    
    fig, axe= plt.subplots(1, 1, figsize = (11,7))
    
    axe.plot(x, y, label = 'Experimental')
    
    axe.plot(x, P_numerico, 'k--', label= 'Lagrange')
    
    plt.legend(loc= 'best')
    
    plt.show()
    
    
######################### Execução do código #################################
    
graf(X, Y1)
    
    
    