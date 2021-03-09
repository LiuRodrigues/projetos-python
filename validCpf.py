# validadar cpf
def validCpf(dig):
    cpf_recebido = dig
    cpf_gerado = cpf_recebido[0:9]
    cont_regres = 10
    totalizador = 0
    for index in range(18):
        if index > 8:
            index -= 8
        totalizador += (cont_regres * int(cpf_recebido[index]))
        cont_regres -= 1
        if cont_regres < 2:
            cont_regres = 10
            d = 11 - (totalizador % 11)
            if d > 9:
                d = 0
            cpf_gerado += str(d)
            totalizador = 0
            return cpf_gerado