def perfect_number (num):
    acu=0
    for i in range (1,num,1):
        if num%i==0 :
            acu=acu+i
    if (acu==num):
        print("El numero es perfecto, como yo")
    else:
        print("El numero no es yo, osea no es perfecto")


a=int(input("Numero: "))

perfect_number(a)
