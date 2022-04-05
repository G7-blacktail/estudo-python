conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
print("União: {}".format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2)
print("Intersecção: {}".format(conjunto_interseccao))

conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print("Diferença entre conjunto_diferencia1: {}".format(conjunto_diferenca1))
print("Diferença entre conjunto_diferencia2: {}".format(conjunto_diferenca2))


conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print("Diferença simétrica entre os conjuntos iniciais: {}".format(conjunto_dif_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_suset = conjunto_a.issubset(conjunto_b)
print("O conjunto A é subconjunto de B:\n {}".format(conjunto_suset))
conjunto_suset = conjunto_b.issubset(conjunto_a)
print("O conjunto B é subconjunto de A:\n {}".format(conjunto_suset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print("B é superconjunto de A: \n {}".format(conjunto_superset))
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print("A é superconjunto de B: \n {}\n".format(conjunto_superset))

lista = ['cachorro', 'gato', 'cachorro', 'elefante', 'girafa']
print("{}\n".format(lista))
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

# conjunto = {1, 2, 3, 4, 4 , 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)