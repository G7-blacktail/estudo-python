a = float(input('Primeiro bimestre: '))
if a > 10:
    a = float(input("Você digitou um valor inválido. \n"
                    "digite novamente: "))
b = float(input('Segundo bimestre: '))
if b > 10:
    b = float(input("Você digitou um valor inválido. \n"
                    "digite novamente: "))
c = float(input('Terceiro bimestre: '))
if c > 10:
    c = float(input("Você digitou um valor inválido. \n"
                    "digite novamente: "))
d = float(input('Quarto bimestre: '))
if d > 10:
    d = float(input("Você digitou um valor inválido. \n"
                    "digite novamente: "))

media = (a + b + c + d) / 4
if media > 100:
    print('Calculo inválido')
else:
    print('A nota final é: {}'.format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print("Alguma nota exedeu o limite por bimestre")

# a = int(input('Entre com um valor: '))
# b = int(input('Entre com outro valor'))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado número par')
# else:
#     print('nenhum número par foi digitado')


# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('\nfinal do programa')