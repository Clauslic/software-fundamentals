//Algoritm description
//Basic calc v1
//Get two numbers
//Add, subs, mult, div
//Print results

Algoritmo basic_calc
	//1. Define vars and/or const
	Definir num1, num2, add, subs, mult Como Entero
	Definir div Como Real
	//2. Inicializar vars and/or const
	//Inputs
	Escribir "Enter number 1: " 
	Leer num1
	
	Escribir "Enter number 2: " 
	Leer num2
	
	//3. Processes
	add = num1 + num2;
	subs = num1 - num2;
	mult = num1 * num2;
	div = num1 / num2
	//4.Outputs
	Mostrar "Addition: ", add;
	Mostrar "Subtraction: ", subs;
	Mostrar "Multiplication: ", mult;
	Mostrar "Division: ", div;
FinAlgoritmo
