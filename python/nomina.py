##### Nomina  #####
nombre=""
correo=""
con='S'

def salarios(salario):
    while status=='s' or status=='S':
      salario=salario
    return salario

while con=='s' or con=='S':
   print("Escriba nombres completos: ")
   nombre=input()
   print("Escriba el correo electronico: ")
   correo=input()
   print("Escriba numero mobil: ")
   mobil=input()
   print("Escriba genero en formato: F - M - O")
   genero=input()
   if genero == 'F' or genero =='M' or genero == 'O':
      print(" Escriba el total del salario devengado: ")
      salario=float(input())
      print(" Ingrese año de nacimiento ")
      aNa=float(input())
    else:
      print("Esta mal escrito el genero")  
print("ingrese S o s, para continuar, N o n para terminar")
con=input()      
con='N' or 'n'

#print("El total de salario es " , salarios())
#print("Salario " , salarios())
print("Nombres" ,nombre)
