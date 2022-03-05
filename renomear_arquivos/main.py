import os

caminho_busca = os.path.abspath('main')  #input('Digite o caminho da busca: ')
caminho_busca, nome_arquivo = os.path.split(caminho_busca)

cont = 0
for raiz, diretorios, arquivos in os.walk(caminho_busca):
    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        nome_do_arquivo, ext_arquivo = os.path.splitext(arquivo)
        print()
        print('Caminho do arquivo:', caminho_completo)
        print('Nome do arquivo:', nome_do_arquivo)
        print('Extensão do arquivo:', ext_arquivo)
        cont += 1
print()
print(f'{cont} arquivo(s) encontrado(s)')