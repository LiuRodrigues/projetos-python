# jogo da forca
from random import choice
import bonequinho
lista_palavras = ['carro', 'caneca', 'boneca', 'menina', 'boi', 'bule']
palavra_escol = choice(lista_palavras)
preenchimento = list('_' * len(palavra_escol))
palpite, digitadas , erros = 0, '', 0
while preenchimento != palavra_escol:
    while True:
        usuario_letra = str(input('digite uma letra: ')).strip().lower()[0]
        digitadas += ' ' + usuario_letra
        if len(usuario_letra) == 1:
            break
    print(f'Letras digitadas {digitadas}')
    palpite += 1
    for index, lt in enumerate(palavra_escol):
        if usuario_letra == lt:
            preenchimento[index] = usuario_letra

    palavra = ''.join(preenchimento)
    print(*preenchimento)
    if not usuario_letra in palavra:
        erros += 1
    print(bonequinho.animar()[erros])
    if palpite == 8:
        if palavra != palavra_escol:
            print(f'\033[31mAcabou para você! A palavra era {(palavra_escol).upper()}\033[m')
        break
    if palavra == palavra_escol:
        print(f'\033[32mParabéns!! Você completou a palavra {(palavra).upper()}\033[m')
        break
