# validadar cpf
def validCpf(dig):
    cpf_recebido = str(dig)
    cpf_gerado = cpf_recebido[0:-2]
    cont_regres = 10
    totalizador = 0
    for index in range(18):
        if index > 8:
            index -= 8
        totalizador += (cont_regres * int(cpf_gerado[index]))
        cont_regres -= 1
        if cont_regres < 2:
            d = 11 - (totalizador % 11)
            if d > 9:
                d = 0
            totalizador = 0
            cont_regres = 10
            cpf_gerado += str(d)
    return cpf_gerado == cpf_recebido


print(validCpf(47756855205))