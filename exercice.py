"""
Ejercicio zapato
"""
#listaZapato=[(nombre:"Nike",talla:45),(nombre:"Adidas",talla:45)]



# A program that asks the user to enter a shoe and then asks for the size of the shoe. If the size is
# 45, it asks if you want to buy the shoe. If you want to buy the shoe, it asks if you have enough
# money to buy the shoe. If you have enough money, it tells you that you bought the shoe. If you don't
# have enough money, it tells you to come back later. If you don't want to buy the shoe, it tells you
# to come back later. If the size is not 45, it tells you that the size is not available. If the shoe
# is not Nike, it tells you that the shoe is not available.

def ConsultarDinero():
    respCost = input("Me alcanza el dinero? Si o No \n")
    if(respCost=="Si"):
                print("Muchas gracias por comprar el zapato")
    else:
        print("Esta bie esperemos que vuelva pronto")
def printPrecioZapato():
    print("# PRECIO ES 450bs") 
    ConsultarDinero()
def desicionTalla():
    resp=input("Desea quedarse con el zapato? Si o No \n")
    if(resp=="Si"):
        print("Cual es el precio del zapato?")
        printPrecioZapato()
    else:
        print("Esta bie esperemos que vuelva pronto")

def buscarTalla():
    talla = int(input("Ingrese su talla \n"))
    if(talla == 45):
        print("Si existe el zapato")
        print("Probandose el zapato")
        desicionTalla()
    else:
        print("Lo siento no existe su talla :(")
        
def buscarZapato():
    zapato= input("Ingrese un zapato\n ")
    if(zapato == "Nike"):
        print("Encontrado")
        buscarTalla()
    else:
        print("Lo siento la marca que solicito no existe")

buscarZapato()




print("Fin del ejercicio")
