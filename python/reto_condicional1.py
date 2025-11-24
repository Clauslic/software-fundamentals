import random
random.seed()   #Prepare random number generator

print("Lanzando los dados")
dad1 = int(random.random() * 6) + 1
dad2 = int(random.random() * 6) + 1
print("Primer dado :" + str(dad1))
if dad1 % 2 == 0:
    parImp1 = "Es par"
    print("El dado 1 es: " + parImp1)
else:
    parImp1 = "Es impar"
    print("El dado 1 es: " + parImp1)
print("El segundo dado es:" + str(dad2))
if dad2 % 2 == 0:
    parImp2 = "Es par"
    print("El dado 2 es: " + parImp2)
else:
    parImp2 = "Es impar"
    print("El dado 2 es: " + parImp2)
if dad1 == dad2:
    print("YOU WIN")
else:
    print("GAME OVER")
