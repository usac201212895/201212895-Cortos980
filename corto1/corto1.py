#creamos la variable secuencia con int para que el dato esperado sea un numero, se envia un mensaje al usuario pidiendo el numero N
secuencia = int(input("Numero N: "))
#se inicia el bucle general
while secuencia != 1:
    #si el numero de secuencia ingresado es par, se lo divide por dos
    if secuencia % 2 == 0:
        print("%d," % (secuencia), end = "")
        secuencia = secuencia / 2
        #si no cumple y es impar, se le multiplica tres y se le suma uno
    else:
        print("%d," % (secuencia), end = "")
        secuencia = (secuencia * 3) + 1
#la secuencia termina la llegar a 1
    if secuencia == 1:
        print("1")