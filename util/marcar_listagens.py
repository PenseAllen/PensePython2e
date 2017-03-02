#!/usr/bin/env python3

import re

from glossario_dl import marcar_verbetes

MAX_LEN_CODIGO = 50
PREFIXOS_NAO_CODIGO = '# * <dt> <dd> <dl> </dl>'.split()

def pode_ser_codigo(lin):
    if len(lin) > MAX_LEN_CODIGO:
        return False
    for pre in PREFIXOS_NAO_CODIGO:
        if lin.startswith(pre):
            return False
    return True


def marcar_listagens(md):
    lin_ant = ''
    bloco = []
    saida = []
    for lin in md.split('\n'):
        if pode_ser_codigo(lin):
            if lin:
                lin = lin.replace('&gt;', '>')
                lin = lin.replace('&lt;', '<')
                lin = lin.replace(r'\_', '_')
                lin = lin.replace(r'\#', '#')
                lin = lin.replace(r'\*', '*')
                bloco.append(lin)
            else:
                saida.append(lin)
        else:
            if bloco:
                saida.append('```python')
                saida.extend(bloco)
                saida.append('```\n')
                bloco = []
            saida.append(lin)
        lin_ant = lin
    return '\n'.join(saida).replace('\n\n\n', '\n\n').replace('\n\n\n', '\n\n')


def main():
    import sys
    caminho_arq = sys.argv[1]
    with open(caminho_arq, encoding='utf8') as fp:
        md = fp.read()
    #md = marcar_verbetes(md)
    md = marcar_listagens(md)
    with open(caminho_arq.replace('-', 'list-', 1), 'wt', encoding='utf8') as fp:
        fp.write(md)


if __name__ == '__main__':
    main()
