
lista = [1, 10]


try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisiao = 10 / 1
    numero = lista[1]
    print('Fechando o arquivo')


except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero')
except IndexError:
    print('Erro desconhecido')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre execeção')
finally:
    print('sempre executa')
    print('fechando arquivo')
