deposito = 0.0
saque = 0.0
extrato = 0.0
saques_realizados = 0
limite_saques = 3
limite_saque_individual = 500.0

while True:
    opcao = input("Escolha uma das opções abaixo:\n1-Depósito\n2-Saque\n3-Extrato\n4-Sair\n ")

    if opcao == "1":
        depositar = float(input("Digite o valor a ser depositado: "))
        deposito += depositar
        print(f"Depósito no valor de {depositar} foi realizado com sucesso.")

    elif opcao == "2":
        if saques_realizados >= limite_saques:
            print("Limite de saques diários atingido.")
        else:
            sacar = float(input("Digite o valor a ser sacado (máximo 500): "))
            if sacar > limite_saque_individual:
                print(f"O valor máximo para saque é {limite_saque_individual}.")
            elif sacar > deposito:
                print("Saldo insuficiente para realizar o saque.")
            else:
                deposito -= sacar
                saques_realizados += 1
                print(f"Saque no valor de {sacar} foi realizado com sucesso.")
                print(f"Você realizou {saques_realizados} de {limite_saques} saques permitidos hoje.")

    elif opcao == "3":
        saldo = deposito - saque
        print(f"Extrato:\nDepósitos: {deposito}\nSaques: {saque}\nSaldo: {saldo}")

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")
