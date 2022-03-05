from lib import *
import useful_formatting
arquivo = 'lista.txt'

linha = ''

with open(arquivo, 'w') as valor:
    valor.write(cab_linhas('LISTA DE COMPRAS', '='))

while True:
    print('Cadastro de produtos. ')
    produto = input('Produto: ').upper()
    quantidade = int(input('Quantidade: '))
    linha += useful_formatting.texto_tabulado(produto, quantidade)
    with open(arquivo, 'w') as a:
        a.write(linha)
    r = input('Deseja continuar ou parar o cadastro? [0:Sair] ')
    if int(r) == 0:
        break

with open(arquivo, 'rt') as arq:
    print(arq.read())
