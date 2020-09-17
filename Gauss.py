# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:13:58 2019

@author: Arley
"""
import numpy as np

"""Método da eliminação de Gauss para resolução de sistemas lineares"""

"""Matriz de coeficientes"""
coeficientes= np.array([[3, -0.1, -0.2], 
                        [0.1, 7, -0.3],
                        [0.3, -0.2, 10]])

ordem = np.shape(coeficientes)[0]
variaveis_dependentes=  np.array([7.85, -19.3, 71.4])

M= np.zeros((ordem, ordem+1))
M[:, :ordem]= coeficientes
M[:, ordem]= variaveis_dependentes

K=np.ones((1,ordem))
soma=0
x=np.zeros((ordem,1))
b=0
cont=1

print("################### Matriz do sistema linear ######################## ")
print(M) 


"""Algorítmo de escalonamento com tirangularização superior da matriz de coeficientes"""
for i in list(range(ordem)):
    
    pivo=M[i,i] 
    for n in list(range(ordem+1)):
        M[i,n]=M[i,n]/pivo
     
    for t in list(range(ordem-1)):
        fator=t+cont
        if fator<=(ordem-1):
            razao=M[fator,i]
            for c in list(range(ordem+1)):
                M[fator,c]=M[fator,c]-(M[i,c]*razao)
            if c==(ordem-1):
               c=0           
        if t==(ordem-2):
           t=0
    cont=cont+1
    if n==(ordem-1):
       n=0

print(" ")       
print("#################### Matriz escalonada ############################## ")       
print(M)    

"""Cálculo das raízes do sistema"""

lista=list(range(ordem))
Lista=sorted(lista,key=int,reverse=True)
for Q in Lista:
    for L in Lista:
        if Q!=L:
           soma=soma+(M[Q,L]*K[0,L])
           
    if L==0:
        L=ordem-1
      
    x[Q]=(M[Q,(ordem)]-soma)
    soma=0 
    K[0,Q]=x[Q]

print(" ")
print("#################### As raízes do sistema ########################### ")        
print(x)
     
       