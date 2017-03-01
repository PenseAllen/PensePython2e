#!/usr/bin/env python3

import re

GLOSSARIO_RE = re.compile(r'^## [B|\d]\d?\.\d\d? - Glossário$', re.MULTILINE)
EXERCICIOS_RE = re.compile(r'^## \d\d?\.\d\d? - Exercícios$', re.MULTILINE)

VERBETE_RE = re.compile(r'\n__(.+?)__<br>\n([^\n]+)\n')
VERBETE_REPL = r'\n<dt><a id="glos:\1" href="#termo:\1">\1</a></dt>\n<dd>\2</dd>\n'


def marcar_verbetes(md):
    casa_glossario = GLOSSARIO_RE.search(md)
    assert casa_glossario
    inicio = casa_glossario.span()[1] + 1
    casa_exercicios = EXERCICIOS_RE.search(md[inicio:])
    if casa_exercicios:
        fim = inicio + casa_exercicios.span()[0]
    else:
        fim = len(md)
    corpo = md[inicio:fim]
    casa_verbete = VERBETE_RE.search(corpo)
    assert casa_verbete
    corpo = '\n<dl>' + VERBETE_RE.sub(VERBETE_REPL, corpo) + '</dl>\n\n'
    return md[:inicio] + corpo + md[fim:]


def main():
    import sys
    caminho_arq = sys.argv[1]
    with open(caminho_arq, encoding='utf8') as fp:
        md = fp.read()
    md = marcar_verbetes(md)
    with open(caminho_arq.replace('-', 'glos-', 1), 'wt', encoding='utf8') as fp:
        fp.write(md)


if __name__ == '__main__':
    main()
