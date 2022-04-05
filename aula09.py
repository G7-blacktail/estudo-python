
def escrever_arquivo(texto):
    diretorio = 'C:\Users\gfreitas\Desktop\Documentação\Bootcampsarquivos\bootcamps\'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    #escrever_arquivo('primeira linha')
    #atualizar_arquivo('\nSegunda linha')
    ler_arquivo('teste.txt')