# Programa: programa para cálculo de área de uma circunferencia
# Nome: areaCirc.py
# Autor: Pojucan, M.M.S.
# Data: 29/04/2019
#
import math                                               # módulo de cálculos
print ('\nPrograma de cálculo da área da circunferência') # Apresentacao 
r = float(input('\nDigite o raio da circunferência: '))   # entrada do raio
a = math.pi*(r**2)                                        # cálculo da área 
print ('\nO valor do raio é: {}'.format(r))
print ('\nO valor da área é: {}'.format(a))