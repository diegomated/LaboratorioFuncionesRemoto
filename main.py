def a_power_b (a,b):
    acu=a
    for i in range (0,b-1,1):
        acu=a*acu
    
    print("resultado: ", acu, "\n")
    return acu


cont=0
contP=0
contI=0

while True:
    a=int(input("Numero 1: "))
    if a==0 :
        break
    b=int(input("Exponente: "))
    if a_power_b(a,b)%2==0:
        contP+=1
    else :
        contI+=1
    cont+=1

print("\nnumero de potencias: ", cont)
print("Pares: ", contP)
print("Impares:", contI)

