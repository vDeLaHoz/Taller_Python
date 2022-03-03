# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:10:47 2022

@author: vdelahoz6
"""

taller1 = float(input('Ingrese la nota del primer taller: '))
taller2 = float(input('Ingrese la nota del segundo taller: '))
taller3 = float(input('Ingrese la nota del tercer taller: '))

promTaller = (taller1+taller2+taller3)/3


examen = float(input('Ingrese la nota del examen: '))
proyecto = float(input('Ingrese la nota del proyecto: '))

calificacion = promTaller*0.5+examen*0.3+proyecto*0.2

print(f'Su calificacion final es: {calificacion}')

