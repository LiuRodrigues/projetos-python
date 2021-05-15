#  Lista de Preços com Tupla
from cabeçalho import cab_linhas, lin
from useful_formatting import brl, texto_tabulado


produtos, c = [], 0
while c == 0:
    produtos.append(texto_tabulado(input('Produto: ').upper(), float(input('Quantidade: '))))
    c = int(input('Digite [0] Para continuar [1] Para sair: '))

titulo = cab_linhas('LISTAGEM DE COMPRAS', '=')
print(f'{titulo}\n{"COD PRODUTO"} {"QTD": >25}')

for pos, nome in enumerate(produtos):
    print(f'{pos + 1:0>3}', nome)
print(lin('-', 38))

with open('lista.txt', 'w') as arquivo:
    arquivo.write(str(cab_linhas('LISTAGEM DE COMPRAS', '=')))
    arquivo.write('\n{} {}{: >25}'.format('COD', 'PRODUTO', 'QTDE') + '\n')
    arquivo.write(lin('-', 38) + '\n')

    for pos, valor in enumerate(produtos):
        arquivo.write(str(f'{pos + 1:0>3} ') + (str(valor) + '\n'))
    arquivo.write(lin('-', 38) + '\n')
