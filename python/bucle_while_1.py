import os
os.system('clear')
status= True
acum=numT=par=imPar=parPo=parNeg=imParPo=imParNe=nega=posi=posiIm=negaIm=0
while status:
    print("Press any number (0 to exi):")
    num=float(input())
    acum+=num
    numT=numT+1
   
    if num%2==0:
        par=par+1
        if num>0:
            parPo=parPo+1
            posi=posi+1
        else:
            parNeg=parNeg+1    
                #print("Total pares" ,par )
            nega=nega+1    
    else:
        if num>0:
            imParPo=imParPo+1
            posiIm=posiIm+1
        else:
            imParNe=imParNe+1
            negaIm=negaIm+1      
        imPar=imPar+1
            
        #print("total numeros", numT)
    if num == 0:
        break#status=false
print("Total  suma: ", acum)
print(" El total de numeros digitados son ", numT-1)
print(" El total de pares digitados son ", par-1)
print(" El total de Impares digitados son ", imPar) 
print(" El total de positivos digitados son ", posi+posiIm) 
print(" El total de negativos digitados son ", (nega+negaIm)-1)  
print(" El total de pares positivos digitados son ", parPo) 
print(" El total de pares negativos digitados son ", parNeg-1)
print(" El total de Impares positivos digitados son ", imParPo-1)
print(" El total de Impares negativos digitados son ", imParNe)   