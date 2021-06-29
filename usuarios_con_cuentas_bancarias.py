class Usuario:
    def __init__(self, cedula, nombre, apellido, email_address):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email_address
        self.account = BankAccount(balance = 0, interes_dado = 0.025)

    def __str__(self):
        return f"""
CEdula/RUT: {self.cedula}
 Nombre: {self.nombre}
 Apellido: {self.apellido}
 Email: {self.email}
 Account: {self.account}\n"""

    def deposito(self, monto):                                  # depósito / Deposit
        print(f"HOLA! {self.nombre} {self.apellido}")
        self.account.deposit(monto)
        self.mostrar_saldo()
        return self

    def giro(self,monto):                                       # giro / retiro / withdrawal
        print (f"HOLA! {self.nombre} {self.apellido}")
        self.account.withdraw(monto)
        self.mostrar_saldo()
        return self      

    def mostrar_saldo(self):
        self.account.display_account_info()
        return self

    def transfiere_dinero_a(self, otro_usuario, monto):
        print (f"REALIZANDO TRANSFERENCIA ENTRE {self.nombre} y {otro_usuario.nombre} ===============================")
        print(self.nombre)
        b = self.account.balance
        self.account.withdraw(monto)
        self.account.display_account_info()
        print(otro_usuario.nombre)
        if b >= monto:
            otro_usuario.account.deposit(monto)         #otro_usuario.deposito(monto)
            otro_usuario.account.display_account_info()
            print("#"*17 + "TRANSFERENCIA=REALIZADA" + "%"*17 + "\n\n")
        else:
            otro_usuario.account.display_account_info()
            print("#"*17 + "TRANSFERENCIA -NO- REALIZADA" + "%"*17 + "\n\n")
        return self
############################################CLASE_BANK_ACCOUNT################################################
class BankAccount:
    def __init__(self, balance = 0, interes_dado = 0.025):
        self.balance = balance
        self.interes = interes_dado

    def __str__(self):
        return f"""Saldo actual en cuenta es de  ${self.balance}
y genera {self.interes * 100}% de interes.\n"""
    
    def deposit (self, cantidad):
        self.balance += cantidad
        print(f"DepOsito por ${cantidad} realizado")
        return self

    def withdraw (self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print(f"giro por ${cantidad} realizado")
        else:
            print(f"Fondos insuficientes, giro por ${cantidad} NO realizado. Tarifa de $5 cobrada")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"""Su saldo actual en cuenta es de ${self.balance}
y genera {self.interes * 100}% de interes.\n""")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interes
        return self

# ____________________________________________________________________________________________________
# ====================================================================================================
print("Vamos a Crear algunos USUARIOs Bancarizados:")
Enrique = Usuario(3791069, "Enrique", "Malaver", "drmalaver@cantv.net")
Juancho = Usuario(12816335, "Juan", "Malaver", "jm2008@gmail.com")
Carol = Usuario(15342869, "Micarol", "Singer", "m.singer@hotmail.com")
print (Enrique, Juancho, Carol)
print("\n\n" + "="*97)
print("Vamos a realizar varios movimientos.\n")
#
Enrique.deposito(710)
Enrique.giro(300)
#  
print("\nVamos a realizar otros movimientos.\n")
Juancho.deposito(500)
Juancho.giro(1860 * 0.71)
#  
print("\nVamos a realizar otros movimientos.\n")
Carol.deposito(1750).giro(780)
#
print("\n\n=============================================================================================")
print("Ahora vamos a realizar varias TRANSFERENCIAS entre usuarios.\n")
Juancho.transfiere_dinero_a(Carol,319)
Juancho.transfiere_dinero_a(Enrique,500)
#Juancho.transfiere_dinero_a(Carol,319).transfiere_dinero_a(Enrique,500)