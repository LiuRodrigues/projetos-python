# Formatação tipo moeda => Exemplo: "R$ 3.00"
def brl(num):
    text = f'R$ ' + str(f'{num:.2f}')
    return text


#  Exemplo: "Produto ...............R$ 3.00"
def texto_tabulado(txt, num):
    texto = txt
    linha = f'{texto}{"":.>{26-len(texto)}}{brl(num)}'
    return linha


