def numeros_primos(numero):
    if(numero!=2 and numero!=3):
        if(numero%2==0 or numero%3==0 ):
            print("No es un numero primo")
    else:
        print("Es un numero primo")

numeros_primos(47)