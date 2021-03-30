# ================================
#          LISTA DE COMPRAS
# ================================

def cab_linhas(msg, tipo):
    titulo = msg
    tamanho = len(titulo) * 2
    linhas = tipo * len(titulo) * 2
    return f'{linhas}\n{titulo: ^{tamanho}}\n{linhas}\n'


def lin(tipo, qu):
    linha = tipo * qu
    return f'{linha}'




