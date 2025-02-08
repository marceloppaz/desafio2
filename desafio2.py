import textwrap


def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Conta
    [5] Mostrar Contas
    [6] Novo usuário
    [0] Sair

    Selecione a opção desejada: """
    return int(input(textwrap.dedent(menu)))


def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f}\n"
        print("Depósito realizado!")

    else:
        print("Valor inválido")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_diario = numero_saques >= limite_saques

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    if excedeu_diario:
        print("Numero de saques diário excedido.")

    elif excedeu_saldo:
        print("Saldo insuficiente.")

    elif excedeu_limite:
        print("Excedeu seu limite.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor: .2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Valor de saque inválido!")

    return saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===============================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: (dia-mes-ano): ")
    endereco = input("Informe o endereço:")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado!")


def mostrar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,
                                   limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == 3:
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            mostrar_contas(contas)

        elif opcao == 6:
            criar_usuario(usuarios)

        elif opcao == 0:
            break

        else:
            print("Opção Inválida")


main()
