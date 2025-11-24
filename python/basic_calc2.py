## Algoritm description
'''//Basic calc v1
//Get two numbers
//Add, subs, mult, div
//Print results
'''
import os
os.system('clear')
#1.Inicializar vars and/or constants
#print("Please, enter number 1 : ")
num1 = float(input("Please, enter number 1 : "))

#print("Please, enter number 2 : ")
num2 = float(input("Please, enter number 2 : "))


#2. Processes
add = num1 + num2
subs = num1 - num2
mult = num1 * num2
div = num1 / num2

#3.Outputs
'''//print("Addition: ",add, type(add)) 
print("Subtraction: ", subs, type(subs)) 
print ("Multiplication: ", mult, type(mult))
print ("Division: ", div, type(div))//'''
#3.Outputs
print(f"Addition: = {add}") 
print(f"Subtraction: = {subs}") 
print (f"Multiplication: = {mult} ")
print (f"Division: = {div}")
	
	
	
#FinAlgoritmo
