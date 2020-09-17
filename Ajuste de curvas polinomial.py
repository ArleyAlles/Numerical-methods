# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:05:07 2019

@author: Arley
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

t=sy.symbols('t')
y=[67,84,98,125,149,185]
new_y=np.array(y)
x=np.array([0,4,8,12,16,20])
cont=0
cont2=0
entrada=input("Digite o grau do polinômio para fazer o ajuste: ")
ordem=int(entrada)
M_variaveis=np.zeros((ordem+1,ordem+1))
armazenador=[]
new_ordem=ordem+1

"""Cálculo iterativo da matriz de variáveis"""
for i in list(range(new_ordem)):
    
    armazenador.append(np.sum((x**i)*new_y))
    for n in list(range(new_ordem)):
        if n==0 and i==0:
            M_variaveis[i,n]=len(y)
        else:
            if i==0:
                incremento=1
            else:
                incremento=0
                
            M_variaveis[i,n]=np.sum(x**(cont+i+incremento))
            cont=cont+1
            
            if cont>=(ordem+cont2):
                cont=0
                cont2=cont2+1

Y=np.array(armazenador).reshape((ordem+1,1))  

   
"""Cálculo do determinante"""
      
determinante=np.linalg.det(M_variaveis)
print("O determinante da matriz de variáveis é: ")
print(determinante)

"""Condição para saber se a matriz é inversível"""
if determinante==0:
    print("Problema: A matriz é singular (não inversível)")
else:
    Inversa=np.linalg.inv(M_variaveis)
    M_parametros= np.dot(Inversa,Y)
   


"""Gerando a equação polinomial """
vetor_simulacao=np.arange(min(x),max(x)+1,1)
Y_simulacao=[]
tam_vetor=len(vetor_simulacao)
for w in list(range(new_ordem)):
    Y_simulacao.append(M_parametros[w]*(t**w))
    
Y_simul=np.array(Y_simulacao)
Y_si=np.sum(Y_simul)
print(Y_si)


"""Criar os pontos de Y calculado com a equação polinomial gerada"""
Y_ponto=[]
for p in list(range(tam_vetor)):
    pontos=Y_si.subs(t, vetor_simulacao[p])
    Y_ponto.append(pontos)
                                   

"""Gerando os gráficos do predito e observado"""

plt.plot(x,new_y,'bo')   
plt.plot(vetor_simulacao,Y_ponto)  
plt.xlabel("X")
plt.ylabel("Y")

       