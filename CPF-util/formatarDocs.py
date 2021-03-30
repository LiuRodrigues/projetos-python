# colocar pontos no cpf
#######################
def cpf(doc):
    d = doc
    cpf_format = ''
    for c in range(len(d)):
        if c == 3:
            cpf_format += '.'
        elif c == 6:
            cpf_format += '.'
        elif c == 9:
            cpf_format += '-'
        cpf_format += d[c]
    return cpf_format
