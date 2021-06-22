class Usuario:
    def __init__(self, cedula, nombre, apellido, email_address):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email_address
        self.account_balance = 0

    def __str__(self):
        return f"""
CEdula/RUT: {self.cedula}
 Nombre: {self.nombre}
 Apellido: {self.apellido}
 Email: {self.email}
 Account: {self.account_balance}\n"""

    def deposito(self, monto):                                  # depósito / Deposit
        self.account_balance += monto
        print (f"""HOLA! {self.nombre} {self.apellido},
Su depOsito de ${monto} fue realizado de manera exitosa_!!!""")
        self.mostrar_saldo()
        return self

    def giro(self,monto):                                       # giro / retiro / withdrawal
        if self.account_balance >= monto:
            self.account_balance -= monto
            print (f"""HOLA! {self.nombre} {self.apellido},
Su giro por ${monto} fue realizado de manera exitosa_!!!""")
            self.mostrar_saldo()
        else:
            print ("Su giro no se pudo procesar porque no tiene saldo suficiente.\n")
            self.mostrar_saldo()
        return self      

    def mostrar_saldo(self):
        print (f"Su cuenta tiene actualmente saldo: ${self.account_balance}\n")
        return self

    def transfiere_dinero_a(self, otro_usuario, monto):
        print (f"REALIZANDO TRANSFERENCIA ENTRE {self.nombre} y {otro_usuario.nombre} ===============================")
        if self.account_balance >= monto:
            self.giro(monto)
            otro_usuario.deposito(monto)
            print("TRANSFERENCIA REALIZADA =========================================================\n\n")
        else:
            self.mostrar_saldo()
            print (f"Su transferencia por ${monto} a {otro_usuario.nombre} {otro_usuario.apellido} no se procesO por saldo suficiente en su cuenta.\n")
        return self
        

# ____________________________________________________________________________________________________
# ====================================================================================================
print("Vamos a Crear algunos USUARIOs Bancarizados:")
Enrique = Usuario(3791069, "Enrique", "Malaver", "drmalaver@cantv.net")
Juancho = Usuario(12816335, "Juan", "Malaver", "jm2008@gmail.com")
Carol = Usuario(15342869, "Micarol", "Singer", "m.singer@hotmail.com")
print (Enrique, Juancho, Carol)
print("\n\n=============================================================================================")
print("Vamos a realizar varios movimientos.\n")
Enrique.deposito(1000).deposito(1500).deposito(710).giro(1300)
#  Enrique.deposito(1000)
#  Enrique.deposito(1500)
#  Enrique.deposito(710)
#  Enrique.giro(1300)

print("\nVamos a realizar otros movimientos.\n")
Juancho.deposito(1000).giro(1860 * 0.21).giro(1860 * 0.155).deposito(670)
# Juancho.deposito(1000)
# Juancho.giro(1860 * 0.21)
# Juancho.giro(1860 * 0.155)
# Juancho.deposito(670)

print("\nVamos a realizar otros movimientos.\n")
Carol.deposito(3750).giro(780).giro(1100).giro(1320)
# Carol.deposito(3750)
# Carol.giro(780)
# Carol.giro(1100)
# Carol.giro(1320)
print("\n\n=============================================================================================")
print("Ahora vamos a realizar varias TRANSFERENCIAS entre usuarios.\n")
Juancho.transfiere_dinero_a(Carol,319).transfiere_dinero_a(Enrique,500)
# Juancho.transfiere_dinero_a(Carol,319)
# Juancho.transfiere_dinero_a(Enrique,500)
