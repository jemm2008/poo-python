class BankAccount:
    def __init__(self, saldo_inicial = 0, interes_dado = 0.025):
        self.saldo = saldo_inicial
        self.interes = interes_dado

#    def __str__(self):
#        return f"""Saldo actual en cuenta es de  ${self.saldo}
#y genera {self.interes * 100}% de interes.\n"""
    
    def deposit (self, cantidad):
        self.saldo += cantidad
        print(f"DepOsito por ${cantidad} realizado")
        return self

    def withdraw (self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"giro por ${cantidad} realizado")
        else:
            print(f"Fondos insuficientes, giro por ${cantidad} NO realizado. Tarifa de $5 cobrada")
            self.saldo -= 5
        return self

    def display_account_info(self):
        print(f"""Su saldo actual en cuenta es de ${self.saldo}
y genera {self.interes * 100}% de interes.\n""")
        return self

    def yield_interest(self):
        if self.saldo > 0:
            self.saldo += self.saldo * self.interes
        return self

# ______________________________________________________________________________
# ==============================================================================
print("#"*19 + "#CREACION#DE#CUENTAS%" + "%"*19)
cuenta1 = BankAccount ()
cuenta2 = BankAccount (1000)
cuenta3 = BankAccount (350)
print("Cuenta 1:")
cuenta1.display_account_info()
print("Cuenta 2:")
cuenta2.display_account_info()
print("Cuenta 3:")
cuenta3.display_account_info()
#################################################
print("\n\nVamos a hacer varios movimientos...\n\n")
print("Resultados:\n")
print("Cuenta 1:")
cuenta1.deposit(550).deposit(387).deposit(1100).withdraw(775).yield_interest().display_account_info()
print("Cuenta 2:")
cuenta2.deposit(250).deposit(1310).withdraw(110).withdraw(75).withdraw(200).withdraw(50).yield_interest().display_account_info()
print("Cuenta 3:")
cuenta3.deposit(110).withdraw(350).withdraw(257).yield_interest().display_account_info()