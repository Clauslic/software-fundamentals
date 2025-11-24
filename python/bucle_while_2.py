'''def numbers():
    i=2
    while i<=20:
        print(i)
        i+=2

#########   Main   ###########
numbers()'''
def numbers():
    add=0
    i=1
    while i<=100:
        add+=i
        i+=1
    return add

########   Main     ########
total=numbers() 
print(F"Total: {total}")   