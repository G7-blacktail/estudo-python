# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))


soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('soma: {soma}. \nsubtração: {subtracao} .'
      '\nMultiplicação : {multiplicacao}. '
      '\nDivisão: {divisao}. '
      '\nResto: {resto}. '.format(soma=soma,
                                  subtracao=subtracao,
                                  multiplicacao=multiplicacao,
                                  divisao=divisao,
                                  resto=resto))

print(resultado)

# x = '1'
# soma2 = int(x) + 1
# print(soma2)
