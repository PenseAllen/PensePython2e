#!/usr/bin/env python3

import re

MAX_LEN_CODIGO = 50
GLOSSARIO_RE = re.compile(r'^## [B|\d]\d?\.\d\d? - Glossário$', re.MULTILINE)


def pode_ser_codigo(lin):
    if len(lin) > MAX_LEN_CODIGO:
        return False
    if lin.startswith('#'):
        return False
    if lin.startswith('<dt>'):
        return False
    if lin.startswith('<dt>'):
        return False
    if lin.startswith('<dl>'):
        return False
    if lin.startswith('</dl>'):
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
                lin = lin.replace(r'\*', '*')
                bloco.append(lin)
            else:
                saida.append(lin)
        else:
            if bloco:
                saida.append('```python')
                saida.extend(bloco)
                saida.append('```')
                bloco = []
            saida.append(lin)
        lin_ant = lin
    return '\n'.join(saida).replace('\n\n\n', '\n\n')


def main():
    import sys
    caminho_arq = sys.argv[1]
    with open(caminho_arq, encoding='utf8') as fp:
        md = fp.read()
    md = marcar_listagens(md)
    with open(caminho_arq.replace('-', 'novo-', 1), 'wt', encoding='utf8') as fp:
        fp.write(md)


if __name__ == '__main__':
    main()
