lista = [7, 3, 10, 1, 100, 50]
lista_animais = ['cachorro', 'gato', 'elefante','lobo','arrara']
print(lista_animais[1]+'\n')

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista))

tupla_animal = tuple(lista_animais)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)


# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)
#
# lista_animais.reverse()
# print(lista_animais)

# for x in lista_animais:
#     print(x)
#
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(str(soma) + '\n')
#
# print(max(lista))
# print('\n')
# print(max(lista_animais) + '\n')

# novo_lista = lista_animais * 3
# print(novo_lista)

# if 'tubarão' in lista_animais:
#     print('\nExiste um tubarão na lista de animais')
# else:
#     print('\nNão existe um tubarão na lista de animais')

# if 'Lobo' in lista_animais:
#     print('Existe um lobo na lista de animais')
# else:
#     print('Não existe um lobo na lista de animais. \n'
#           'O lobo será incluido')
#     lista_animais.append('lobo')
#     print(lista_animais)

# if 'gato' in lista_animais:
#     print('Existe um gato na lista de animais')
# else:
#     print('Não existe um gato na lista de animais')

# lista_animais.pop(1)
# print(lista_animais)

# lista_animais.remove('elefante')
# print(lista_animais)