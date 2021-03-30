from formatting import useful_formatting
produtos, c = [], 0
while c < 2:
    produtos.append(useful_formatting.texto_tabulado(input('Produto:'), float(input('Preço: '))))
    c += 1

for pos, nome in enumerate(produtos):
    print(pos, nome)