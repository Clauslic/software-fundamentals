Funcion msg = showGreeting(userName)
	Escribir "Hola ", userName, " Bienvenida"
FinFuncion

Algoritmo Function2
	Definir user_name, message Como Caracter
	Escribir "Enter your name: "
	Leer user_name
	
	message = showGreeting(user_name)
	Escribir message
FinAlgoritmo
