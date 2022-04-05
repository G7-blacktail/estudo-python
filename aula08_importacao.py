from aula07_televisao import Televisao
from aula07_calculadora2 import Calculadora
from aula08_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora()
    print(calculadora.soma(5, 2))
    lista = ['cachorro','gato','elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra da lista: {}'.format(total_letras))
    # print(contador_letras(lista))
    print(teste())