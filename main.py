def a_power_b (a,b):
    acu=a
    for i in range (0,b-1,1):
        acu=a*acu
    return acu


while True:
    a=int(input("Numero 1: "))
    if a==0 :
        break
    b=int(input("Exponente: "))
    print(a_power_b(a,b))



