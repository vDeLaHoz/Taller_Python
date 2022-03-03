# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:10:47 2022

@author: vdelahoz6
"""

donacion = float(input('Ingrese el valor de la donacion: $'))

tel = donacion*0.1

print(f'El valor correspondiente a telecomunicaciones es: ${tel:,}')

sistemas = donacion*0.25
print(f'El valor correspondiente a sistemas es: ${sistemas:,}')

administracion = donacion*0.35
print(f'El valor correspondiente a administracion es: ${administracion:,}')

contabilidad = donacion*0.3
print(f'El valor correspondiente a contabilidad es: ${contabilidad:,}')

 