#  Gerador de CPFs

from random import randint
from formatarDocs import cpf # modulo interno
numero = str(randint(100000000, 999999999))
novo_cpf = numero.replace(numero[0], '0')  # gerar cpf com inicial em 0.
# novo_cpf = numero + '5'  # "5" é o dígito que identifica UF do cpf.
reverso = 10
tot = 0
#  --- Loop no CPF ---
for index in range(18):
    if index > 8:  # índice vai de 0 a 9
        index -= 8  #  reinicia índice 1 a 10
    tot += int(novo_cpf[index]) * reverso
    reverso -= 1
    if reverso < 2:
        reverso = 10
        d = 11 - (tot % 11)
        if d > 9:
            d = 0
        novo_cpf += str(d)
        tot = 0
print('CPF gerado: ', cpf(novo_cpf))
