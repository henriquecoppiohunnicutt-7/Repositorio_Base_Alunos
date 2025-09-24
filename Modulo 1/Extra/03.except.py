# crie uma funçao chamada calculadora que receba tres parametros:
# dois numeros e ua operaçao(+,-,*,/)
# a função deve retornar o resultado da operação, mas precisa
# tratar as seguintes execoes:
# divisao por zero(zerodivisionerror)
# tipo de dado invalido(valueerror)


def calculadora():
    try:
        n = input('Digite um número ou x para sair do sistema: ')
        if n.lower() == 'x':
            print('Até breve.')
            return
        n1 = input('Digite um número ou x para sair do sistema:')
        if n1.lower() == 'x':
            print('Até breve.')
            return
        operador = input('Informe um operador matemático (+, -, *, /) ou x para sair do sistema: ')
        if operador.lower() == 'x':
            print('Até breve.')
            return
        
        # converter as entradas (inputs) em float
        n = float(n)
        n1 = float(n1)

        if operador == '+':
            resultado = n + n1
        elif operador == '-':
            resultado = n - n1
        elif operador == '*':
            resultado = n * n1
        elif operador == '/':
            if n1 == 0:
                print("Divisão por zero não é permitida.")
                return
            resultado = n / n1
        else:
            print("Operador inválido.")
            return

        print(f'Resultado: {resultado}')

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")