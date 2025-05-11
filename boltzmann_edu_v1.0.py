#!/usr/bin/python

#This is a simple program that calculates population distribution using Boltzmann Distribution. 
#ATTENTION: FOR THIS APP, THE BOLTZMANN CONSTANT VALUE USED IS 0.008314 (kJ/mol.K). SO, TO RUN THIS APP PROPERLY, THE USER WILL BE REQUIRED TOCONVERT THE UNITS.

#Importing modules to run the aplication:
import math

print("Bem-vindo ao Boltzmann v1.0" )

#Setting the Boltzmann Constant:
R = 0.008314

#Defining the values from the data available to the user:
valor1 = float(input("Adicione o valor da Energia livre do reagente (em kJ/mol): "))
valor2 = float(input("Adicione o valor da Energia livre do produto (em kJ/mol): "))
valor3 = float(input("Adicione o valor da Temperatura desejada (em K): "))

#Making the calculations using the Boltzmann Distribuition Formula:
delta_E = valor2 - valor1

razao = math.exp(-delta_E / (R*valor3))

#Printing the result:
print("A razão entre os valores adicionados foi de",razao)

#Some comments/improvements to do:
#1)To improve this script, the next step is to generalize it even more, for example:

#a)Add a conversion units tool (using different values of R???)

#b)This script has been conceived to calculate the distribution between two species only (i.e., A to B or the total free energy from products and the total free energy from reactants). Would be better to include a code that sums up the free energies from each component of products 
#and reactants through some conditions, asking "Do you need to sum the free energies from each component of the products and reactants?", for example.
