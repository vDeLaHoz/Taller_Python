# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:10:47 2022

@author: vdelahoz6
"""

sueldo = float(input('Ingrese el sueldo del vendedor: $'))
ventas = float(input('Ingrese las ventas realizadas del mes: $'))

comision = ventas*0.15

total = sueldo+comision


print(f'El valor ganado por comision es: ${comision:,}')
print(f'El valor total a pagar es: ${total:,}')
