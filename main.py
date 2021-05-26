#!usr/bin/env/python3
# -*- coding: utf-8 -*-
#@author: Quiñones Carhuaz Liam
from os import system
def menu():
    print (""""
    1. Listar clientes
    2. Mostrar cliente
    3. Añadir cliente
    4. Modificar cliente
    5. Borrar cliente
    6. Salir
    """)

def notFound():
    print("*----* ERROR *----*")
    print("Verifica que los datos ingresados sean correctos")

def toNum(n):
    try:
        int(n)
        return True
    except:
        return False

def menuLimpio():
    system('cls')
    menu()

def inverseGender(gender):
    if gender == "male":
        return "female"
    else:
        return "male"

def salidaAlMenu():
    key = input("Escriba una tecla para volver al menu: ")

def mifunc(request):
    status_repet = False
    cliente_target = ""
    if (request.lower() in [k[0].lower() for k in clientes]):
        print("Dato encontrado")
        for m in range(len(clientes)):
            if (clientes[m][0].lower() == request.lower()):
                cliente_target = clientes[m]
                print("Estas viendo a ",cliente_target[0])
                #return(clienteobjetivo,status)   
    else:
        notFound()
        status_repet = True
    return ([cliente_target,status_repet])

menuLimpio()

clientes =[["Pedro",{"age":31,"gender":"Male"}],
["Juan",{"age":18,"gender":"male"}],
["Maria",{"age":25,"gender":"female"}],]

while True:
    x = input("Escriba la opcion: ")
    if toNum(x) and int(x) in range(0,7):
        if x == "6":
            print("Adios")
            break

        elif x == "1":
            print("\n\t\tLISTA CLIENTES")
            print("*============================*")
            for j in clientes:
                print("    ",j[0])
            print("*============================*")
            salidaAlMenu()
            menuLimpio()
        elif x == "2":
            print("\n\t\tMOSTRAR CLIENTES")
            while True:
                request = input("Nombre del cliente que desea ver: ")
                if request == "0":
                    break
                if (request.lower() in [k[0].lower() for k in clientes]):
                    print("Dato encontrado")
                    for m in range(len(clientes)):
                        if (clientes[m][0].lower() == request.lower()):
                            print("Estas viendo a ",clientes[m][0])
                        #clientes[m]: ["Pedro",{"age":31,"gender":"Male"}]                   
                        #{"age":31,"gender":"Male"}
                            target = clientes[m][1]
                            print("Edad: ",target["age"])
                            print("Genero: ",target["gender"])
                            print("\n")
                    salidaAlMenu()
                    break
                else:
                    notFound()
            
        elif x == "3":
            print("\n\t\tAÑADIR CLIENTE")
            client_name = input("Nombre: ")
            while True:
                client_age = input("Edad: ")   
                if toNum(client_age):
                    break
                else:
                    notFound()
            while True:
                client_gender = input("Genero (M/F): ")
                if client_gender.lower() in ("m","f"):
                    if client_gender.lower() == "m":
                        client_gender = "male"
                    if client_gender.lower() == "m":
                        client_gender = "female"
                    break
                else:
                    notFound()
            carga_util = [client_name,{"age":client_age,"gender":client_gender}]
            print(carga_util)
            clientes.append(carga_util)
            print("clientes")
            print(clientes)
            salidaAlMenu()

        elif x == "4":
            print("\n\t\tMODIFICAR CLIENTE")
            #clientes[m]: ["Pedro",{"age":31,"gender":"Male"}]
            while True: #**
                request = input("Nombre del cliente a modificar: ")
                rpta = mifunc(request)
                bloque_util = rpta[0]
                if rpta[0] != "":
                    print("\n\t\tMENU")
                    print("""¿Que desea modificar?
        1. Nombre
        2. Age
        3. Gender
        0. SALIR
                    """)
                    option = input("Escriba la opcion: ")
                    if toNum(option) and int(option) in range(0,4):
                        if option == "4":
                            break #**
                        elif option == "1":
                            print("Modificar nombre")
                            new_name = input("Escriba el nuevo nombre: ")
                            bloque_util[0]=new_name
                            #eliminar el elemento
                            clientes.remove(rpta[0])
                            #apendizar la lista actualizada
                            clientes.append(bloque_util)
                            print(clientes)

                        elif option == "2":
                            print("Modificar age")
                            while True:
                                new_age = input("Escriba la nueva edad: ")
                                if toNum(new_age):
                                    bloque_util[1]["age"] = int(new_age)
                                    #eliminar el elemento
                                    clientes.remove(rpta[0])
                                    #apendizar la lista actualizada
                                    clientes.append(bloque_util)
                                    print(clientes)
                                    break
                                else:
                                    notFound()

                        elif option == "3":
                            #rpta[0] o bloque_util = ["Pedro",{"age":31,"gender":"Male"}]
                            gender_actual = bloque_util[1]["gender"]
                            print("Modificar genero")
                            print("Genero actual",gender_actual)
                            while True:
                                confirmacion = input("¿Estas seguro? (Y/N): ")
                                
                                if (confirmacion.lower() in ("y","n")):
                                    if confirmacion == "y":
                                        new_gender = inverseGender(gender_actual)
                                        bloque_util[1]["gender"] = str(new_gender)
                                        #eliminar el elemento
                                        clientes.remove(rpta[0])
                                        #apendizar la lista actualizada
                                        clientes.append(bloque_util)
                                        print(clientes)
                                        break
                                    else:
                                        menuLimpio()
                                        break        
                                else:
                                    notFound()
                                    continue
                if rpta[1] == True:
                    #si la entrada del nombre cliente se repetira
                    continue
                else:
                    break
            salidaAlMenu()
            menuLimpio()

        elif x == "5":
            while True:
                client_borrar_name = input("Nombre del cliente a borrar: ")
                rpta = mifunc(client_borrar_name)
                if rpta[0] != "":
                    bloque_util = rpta[0]
                    clientes.remove(bloque_util)
                    print("El cliente ",client_borrar_name," fue borrado con exito")
                    print(clientes)
                if rpta[1] == True:
                    continue

    else:
        system('cls')
        menu()
        print("INGRESE UNA OPCION VALIDA")
        
