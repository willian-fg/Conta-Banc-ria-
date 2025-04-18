saldo = 1000

def ConsultarSaldo():
 print(saldo)
 
def Depositar():
 valorDoDeposito = input("Insira o valor!")
 saldo = saldo + valorDoDeposito
 
def Saque():
 saque = input(Insira o valor!)
 if saque <= saldo:
  saldo = saldo - saque
 else:
  print("Saldo insuficiente.")
 