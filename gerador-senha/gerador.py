# Gerador de Senhas

from random import randint

dados = {'numeros': '0123456789',
         'alfabeto': 'abcçdefghijklmnopqrstuvwxyzABCÇDFGHIJKLMNOPQRSTUVWXYZ',
         'simbolos': '!@#$%&*_?~|<>'
         }
caracteres = list()
senha = list()
while True:
    senha_alfabetica = input('Deseja letras na senha? [S/N]')
    if senha_alfabetica not in 'SsNn':
        print('ERRO! Digite Sim ou Não!')
    else:
        break

senha_numerica = input('Deseja numeros na senha? [S/N]')
senha_simbolos = input('Deseja simbolos na senha? [S/N]')

qtd_dig = int(input('Qual tamanho da senha: '))

if senha_alfabetica in 'Ss':
    caracteres.append(dados['alfabeto'])

if senha_numerica in 'Ss':
    caracteres.append(dados['numeros'])

if senha_simbolos in 'Ss':
    caracteres.append(dados['simbolos'])
caracteres = ''.join(caracteres)
print(caracteres)

# '''
while len(senha) < qtd_dig:
    senha.append(caracteres[randint(0, len(caracteres)-1)])
# '''
senha = ''.join(senha)
print(f'Senha gerada: {senha}')
