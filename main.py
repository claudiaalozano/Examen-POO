if __name__ == "__main__":
    operacion = input(print("Bienvenido al banco, van a comenzar las trasacciones(retirar/ingresar/transferir):"))
    from Clases.ejercicio4 import *

    if operacion == "retirar":
        ejercicio = cuenta_bancaria()
        print(ejercicio.retirar_dinero())
    if operacion == "ingresar":
        ejercicio = cuenta_bancaria()
        print(ejercicio.ingresar_dinero())
    if operacion == "transferir":
        ejercicio = cuenta_bancaria()
        print(ejercicio.transferencia())
    
    

