def a_power_b (a,b):
    acu=a
    for i in range (0,b-1,1):
        acu=a*acu
    return acu


a=int(input("Numero 1: "))
b=int(input("Exponente: "))
print(a_power_b(a,b))



