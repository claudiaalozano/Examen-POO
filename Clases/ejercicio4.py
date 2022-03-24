import random
class cuenta_bancaria:
    def retirar_dinero (self,saldo):
        id = random.choice(lista) 
        self.retirar = saldo - 78
        print("Ha retirado 78 €, el dinero de su cuenta desciende a 9922€ .")
    def ingresar_dinero (self,saldo):
        id = random.choice(lista)
        self.ingreso = saldo + 575
        print("ha realizado un ingreso de 575€, el saldo de su cuenta asciende a 10575€")
    def transferencia(self, saldo):
        id1= random.choice(lista)
        id2= random.choice(lista)
        
        while True:
            if id1 != id2 :
                quitar =  saldo - 1000
                transferir = saldo + 1000
                print ("Usted ha retirado de la cuenta " , id1 , "1000€, por lo que el saldo desciende a ", quitar , " y han sido transferidos a la cuenta " , id2 , " y su saldo asciende a " , transferir)
            else:
                break
        






saldo = 10000 # como las tres tienen el mismo saldo solo creo esta variable
id_1= random.randint(100000000000,999999999999)
id_2= random.randint(100000000000,999999999999)
id_3= random.randint(100000000000,999999999999)
lista = [id_1 , id_2 , id_3]