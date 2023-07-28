menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

script_deposito = """    
                    *****Depósito*****

    Quanto deseja depositar?

    """

script_saque = """
                    *****Saque*****
    Quanto deseja sacar? (Valor Máximo: R$ 500,00)
    """

script_extrato = """
                    *****Extrato*****
    
    """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao =="d":
        valor = float(input(script_deposito))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falou. O valor é inválido")

    elif opcao == "s":
        valor = float(input(script_saque))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Seu saldo é insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print(script_extrato)
        print("Não houveram movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

    elif opcao =="q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
              