#!/usr/bin/env python3

import re

NOME_CAPS = {
    0 : 'prefacio',
    1 : 'jornada',
    2 : 'vars-expr-instr',
    3 : 'funcoes',
    4 : 'caso-interface',
    5 : 'cond-recur',
    6 : 'funcoes-result',
    7 : 'iteracao',
    8 : 'strings',
    9 : 'caso-palavras',
    10 : 'listas',
    11 : 'dicionarios',
    12 : 'tuplas',
    13 : 'caso-estruturas',
    14 : 'arquivos',
    15 : 'classes-objetos',
    16 : 'classes-funcoes',
    17 : 'classes-metodos',
    18 : 'heranca',
    19 : 'extra',
    20 : 'depuracao',
    21 : 'analise-algorit',
}

DIR_CAPITULOS = '../recebido/capitulos/'

def main():
    with open('../recebido/PenseEmPython.md', encoding='utf8') as fp:
        md = fp.read()

    cap_sep = re.compile(r'^capítulo\s+\d+\n\n', re.MULTILINE)

    caps = cap_sep.split(md)

    for i, cap in enumerate(caps):
        quebra = cap.find('\n\n')
        titulo = cap[:quebra]
        corpo = cap[quebra:]
        parte = 'Apêndice'
        if i == 20:
            prefixo = 'A'
        elif i == 21:
            prefixo = 'B'
        else:
            parte = 'Capítulo'
            prefixo = format(i, '02d')
        nome_arq = prefixo + '-' + NOME_CAPS[i] + '.md'
        parte += ' ' + prefixo.lstrip('0')
        print('{}. [{}]({})'.format(prefixo.lstrip('0'), titulo, nome_arq))
        # ATENÇÃO: as instruções a seguir SOBRESCREVEM os arquivos no diretório
        # DIR_CAPITULOS
        #with open(DIR_CAPITULOS + nome_arq, 'wt', encoding='utf8') as fp:
        #    fp.write('# ' + parte + ': ' + titulo + corpo)

if __name__ == '__main__':
    main()
