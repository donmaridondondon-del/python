"""
l=[]
print("Ingresa la lista y acomodalo de mayor a menor....bueno....no")
c=int(input("Coloca el tamaño de la lista: "))
l.append(float(input("Ingrese la lista: ")))
nm=l[0]
nme=l[0]
for i in range(c-1):
    l.append(float(input("Ingrese la lista: ")))
    if l[i+1]>nm:
        nm=l[i+1]
    if l[i+1]<nme:
        nme=[i+1]
print(l)
print("El número mayor es: ",nm," y el número menor es: ",nme)
"""

    
        
        
    
    
        
    
    
