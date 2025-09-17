# crie um programa que some todos os numeros impares
# que são multiplos de 3 e 1 a 30 e apresente o resultado.

# etapas para resoluçao
# 1) criar um for de para captar os numeros ímpares
# 2) criar uma condicional para checar se o numeo é multiplo de 3
# 3) somar os numeros que atende a condicional
# 4) apresentar os resultados

multiplo_tres = 0# variavel que ira receber os nimeros impares e multiplo de 3
for i in range (1,31,2): # contagem dos numeros impares
    if i % 3 == 0: # checagem se os numeros sao multiplos
        print(i, end=',') # apresentacao dos numeros que atendem os requisitos (na mesma linha)
        multiplo_tres += i
print()
print(f'a soma dos numeros impares multiplo de 3 neste intervalo é {multiplo_tres}.')