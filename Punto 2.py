# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:10:47 2022

@author: vdelahoz6
"""

pers1 = float(input('Ingrese el valor invertido por la primera persona: $'))
pers2 = float(input('Ingrese el valor invertido por la segunda persona: $'))
pers3 = float(input('Ingrese el valor invertido por la tercera persona: $'))

totalInvertido = pers1+pers2+pers3

print(f'El pocentajo invertido por la primera persona es: {pers1/totalInvertido*100}%')
print(f'El pocentajo invertido por la segunda persona es: {pers2/totalInvertido*100}%')
print(f'El pocentajo invertido por la tercera persona es: {pers3/totalInvertido*100}%')
 