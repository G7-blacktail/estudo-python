# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print("Número {} é primo".format(a))
# else:
#     print('Número {} não é primo'.format(a))

# a = int(input('entre com um valor: '))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)


# nota = int(input('Entre com a nota'))
# while nota > 10:
#     nota = int(input('Nota inválida. \n'
#                      'Entre com a nota: '))


# a = 0
#
# while a <= 10:
#     print(a)
#     a += 1

a = float(input('Primeiro bimestre: '))
while a > 10:
    a = float(input("Você digitou um valor inválido. \n"
                    "digite novamente: "))
b = float(input('Segundo bimestre: '))
while b > 10:
    b = float(input("Você digitou um valor inválido. \n"
                    "digite novamente: "))
c = float(input('Terceiro bimestre: '))
while c > 10:
    c = float(input("Você digitou um valor inválido. \n"
                    "digite novamente: "))
d = float(input('Quarto bimestre: '))
while d > 10:
    d = float(input("Você digitou um valor inválido. \n"
                    "digite novamente: "))

media = (a + b + c + d) / 4
if media > 100:
    print('Calculo inválido')
else:
    print('A nota final é: {}'.format(media))
