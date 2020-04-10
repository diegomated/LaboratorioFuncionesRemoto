def perfect_number (a):
    acu=0
    for i in range (0,a,1):
        if i%2==0 :
            acu=acu+i
    if (acu==a):
        print("El numero es perfecto, como yo")
    else:
        print("El numero no es yo, osea no es perfecto")


a=int(input("Numero: "))

perfect_number(a)
