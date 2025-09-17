# crie um codigo que faça a conversão de moeda do real para dolar e vice-versa

# Etapas da resolução:
# 1) criar uma variavel chamada cotacao
# 2) solicitar ao usuario a opçao de conversasao desejada
# 3) apresentar o resultado da conversão de moeda
# 4) perguntar se ele deseja continuar a conversão

# taxa de câmbio (exemplo: 1 dólar = 5 reais)
cotacao = 5.0

while True:
    print("Escolha a opção de conversão:")
    print("1 - Real para Dólar")
    print("2 - Dólar para Real")
    opcao = input("Digite 1 ou 2: ")

    if opcao == "1":
        valor_real = float(input("Digite o valor em reais: R$ "))
        valor_dolar = valor_real / cotacao
        print(f"R$ {valor_real:.2f} equivalem a US$ {valor_dolar:.2f}")
    elif opcao == "2":
        valor_dolar = float(input("Digite o valor em dólares: US$ "))
        valor_real = valor_dolar * cotacao
        print(f"US$ {valor_dolar:.2f} equivalem a R$ {valor_real:.2f}")
    else:
        print("Opção inválida, tente novamente.")

    continuar = input("Deseja realizar outra conversão? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break