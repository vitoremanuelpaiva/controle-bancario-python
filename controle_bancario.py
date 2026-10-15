# Controle bancário simples no terminal: consultar saldo, depositar e sacar.
def depositar(deposito , saldo_atual):
    """Soma o valor do depósito ao saldo e devolve o novo saldo."""
    saldo_final = saldo_atual + deposito
    return saldo_final


def saque(valor , saldo_atual):
    """Subtrai o valor do saque ao saldo e devolve o novo saldo."""
    return saldo_atual - valor

saldo = 0   # o saldo começa zerado a cada vez que o programa abre

while True:
    print("======== ESCOLHA UMA OPÇÃO ========\n")
    print("1 - Olhar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    opcao = int(input("Escolha :"))
    # não permite escolher valores diferentes dos recomendados na tela
    if opcao < 1 or opcao > 4:
        print("Opção invalida!")
        print("Por favor digite um valor que esta na sua tela!")
    else:
        match opcao:
            case 1:
                print(f"Seu saldo atual é de : {saldo:.2f}")
            case 2:
                dep = float(input("Digite o valor que você deseja depositar :"))
                # não permite depositar valores negativos ou igual a 0
                if dep <= 0:
                    print("Digite um valor de deposito maior do que zero!")
                else:
                    saldo = depositar(dep,saldo)
                    print(f"Você depositou {dep}, Seu saldo atual ficou : {saldo:.2f}")
            case 3:
                sac = float(input("Digite o valor que você quer sacar :"))
                # não permite sacar valores negativos ou iguais a 0
                if sac <= 0:
                    print("Digite um valor de saque maior do que zero!")
                # não permite sacar mais do que o saldo disponível
                elif sac > saldo:
                    print("Saldo insuficiente para saque!")
                    print("Pois seu valor do saque é mais alto que seu saldo!")
                    print("Digite um valor correspondente ao seu saldo.")
                else:
                    saldo = saque(sac,saldo)
                    print("Seu saque foi feito com sucesso!")
                    print(f"Seu saque foi de {sac}, seu saldo atual ficou {saldo:.2f}")
            case 4:
                print("Saindo do programa...")
                break

print(f"Saldo final : {saldo:.2f}")