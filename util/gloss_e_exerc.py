#!/usr/bin/env python3

import re

GLOSSARIO_RE = re.compile(r'^## [B|\d]\d?\.\d\d? - Glossário$', re.MULTILINE)
EXERCICIOS_RE = re.compile(r'^## \d\d?\.\d\d? - Exercícios$', re.MULTILINE)

VERBETE_RE = re.compile(r'^(.+?):\n\n', re.MULTILINE)
VERBETE_REPL = r'__\1__<br>\n'

EXERCICIO_RE = re.compile(r'^(Exercício \d\d?\.\d\d?)$', re.MULTILINE)
EXERCICIO_REPL = r'### \1'


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
    corpo = VERBETE_RE.sub(VERBETE_REPL, corpo)
    return md[:inicio] + corpo + md[fim:]


def marcar_exercicios(md):
    casa_exercicio = EXERCICIO_RE.search(md)
    assert casa_exercicio
    md = EXERCICIO_RE.sub(EXERCICIO_REPL, md)
    return md


def main():
    import sys
    caminho_arq = sys.argv[1]
    with open(caminho_arq, encoding='utf8') as fp:
        md = fp.read()
    md = marcar_verbetes(md)
    md = marcar_exercicios(md)
    with open(caminho_arq, 'wt', encoding='utf8') as fp:
        fp.write(md)


if __name__ == '__main__':
    main()
