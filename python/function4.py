#genere dos numeros enteros aleatorios entre 0 y 1000 los sume y muestre en pantalla el resultado
# dos funciones para el mismo resultado
# funcion 1 calc_add1: sin retorno
#function 2 calc_add2: con retorno
from random import randint
def calc_add0():
    x = randint(1,1000)
    y = randint(1,1000)
    add = x + y
    print(f"[F0. Basic] Addition is : {add}" )

def calc_add1(x, y):
    
    add = x + y
    print(f"[F1. Without return] Addition is: {add}")

def calc_add2(x, y):
    add = x + y 
    return add   
#################################MAIN##########################
n1 = randint(1,1000)
n2 = randint(1,1000)
calc_add0()
calc_add1(n1, n2)
answer = calc_add2(n1 ,n2)
print(f"[F2. Without return] addition is:  {answer}")


