# INFORME SE O ALUNO ESTA APROVADO(MEDIA>=7), recuperaçao(5<media<7) ou reprovado.
#apresente as notas que o aluno tirou, a media e o status de sua situaçao

#lista
#for
#if/elif/else

notas =[]

for i in range(4):# faz a pergunta 4 vezes
    nota = float(input(f'informe a nota da prova{i+1}:'))
    if nota > 0:# so aceita nota positiva
        notas.append(nota)# notas.append(nota) adiciona um elemento no fianl da lista
    else:
        print('valor invalido')
print(f'suas notas são {notas}')
media = sum(notas)/len(notas)# a função sun(notas) soma todas as notas d alista

if media >= 7:
    print(f"sua notas foram{notas}, sua{media:.2f} e voce esta aprovado.")
elif 5 <= media < 7: # se a media for de 5 a 6.99
    print(f"suas notas foram{notas}, sua {media:.2f} e está em recuperação.")
else:# notas abaixo de 5, ou seja, de 4.99 para baixo
    print(f"suas notas foram{notas}, sua  {media:.2f} e está reprovado.")