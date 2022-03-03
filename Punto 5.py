# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:10:47 2022

@author: vdelahoz6
"""

redes = int(input('Ingrese la cantidad de estudiantes de redes: '))
contabilidad = int(input('Ingrese la cantidad de estudiantes de contabilidad: '))
diseño = int(input('Ingrese la cantidad de estudiantes de diseño: '))

totalEstudiantes = redes+contabilidad+diseño

print(f'El porcentaje de alumnos de redes es: {redes/totalEstudiantes*100}%')
print(f'El porcentaje de alumnos de contabilidad es: {contabilidad/totalEstudiantes*100}%')
print(f'El porcentaje de alumnos de diseño es: {diseño/totalEstudiantes*100}%')

