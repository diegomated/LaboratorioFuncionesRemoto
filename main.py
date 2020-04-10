def a_power_b (a,b):
    acu=a
    if b>=0 :
        for i in range (0,b-1,1):
            acu=a*acu
        if b==0 :
            acu=1
            print("resultado: ", acu, "\n")
            return acu
        else:
            print("resultado: ", acu, "\n")
            return acu
    else:
        for i in range (0,b-1,-1):
            acu=acu/a
        if b==0 :
            acu=1
            print("resultado: ", acu, "\n")
            return acu
        else:
            print("resultado: ", acu, "\n")
            return acu


cont=0
contP=0
contI=0
contE=0

while True:
    while True:
        try:
            a=int(input("Numero 1: "))
            break
        except ValueError:
            contE+=1
            print("digito letras o simbolos solo se valen numeros")

    if a==0 :
        break
    
    while True:
        try:
            while True:
                b=int(input("Exponente: "))
                if b>999 or b<-999 :
                    contE+=1
                    print("Exponente demasiado grande (rango -999 - 999)")
                else :
                    break
            break
        except ValueError:
            contE+=1
            print("digito letras o simbolos solo se valen numeros")

    if a_power_b(a,b)%2==0:
        contP+=1
    else :
        contI+=1
    cont+=1

print("\nPotencias: ", cont)
print("Pares: ", contP)
print("Impares:", contI)
print("Errores: ", contE)

