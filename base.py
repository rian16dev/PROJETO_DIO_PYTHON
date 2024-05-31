menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuário
[a] Abrir Conta
[q] Sair

=> """

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(*, saldo, extrato, limite, numero_saques, limite_saque):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def num_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (Somente Números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Operação falhou, número de CPF já cadastrado.")
        return

    nome = input("Informe seu nome completo: ")
    data_de_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_de_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": "0001",
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print(f"Conta criada com sucesso! Agência: 0001 Conta: {numero_conta}")
    else:
        print("Operação falhou! Usuário não encontrado.")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saque = 3

    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = saque(
                saldo=saldo, extrato=extrato, limite=limite,
                numero_saques=numero_saques, limite_saque=limite_saque
            )
        elif opcao == "e":
            num_extrato(saldo, extrato=extrato)
        elif opcao == "c":
            criar_usuario(usuarios)
        elif opcao == "a":
            criar_conta