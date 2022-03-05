# Formatação tipo moeda => Exemplo: "R$ 3.00"
def brl(num):
    text = f'R$ ' + str(f'{num:.2f}')
    return text


def qtd(num):
    text = str(f'{num:.2f}')
    return text

    #  Exemplo: "Produto ...............R$ 3.00"


def texto_tabulado(txt, num):
    texto = txt
    linha = f'{texto}{"":.>{30 - len(texto)}}{brl(num)}\n'
    return linha



