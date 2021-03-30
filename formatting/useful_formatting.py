# Formatação tipo moeda => Exemplo: "R$ 3.00"
def brl(num, t):
    text = f'R$ ' + str(f'{num:.2f}')
    return text


#  Exemplo: "Macarrão ...............R$ 3.00"
def brl_pontos(txt, num):
    texto, l = txt, ''
    linha = f'{texto} ', f'{brl(num, len(texto)):.>{30 - len(texto)}}'
    for i in linha:
        l += i
    return l


