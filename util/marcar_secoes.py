#!/usr/bin/env python3

import re
import collections
import glob
import os

from separar_capitulos import NOME_CAPS

SUMARIO = '../recebido/sumario.md'
DIR_DOCS = '../docs/'

CAP_RE = re.compile('^Capítulo (\d+)', re.MULTILINE)
SEC_RE = re.compile('(.+?)\s+\d+$', re.MULTILINE)

Secao = collections.namedtuple('Secao', 'num titulo')

def id_cap(num_cap):
    if num_cap == 20:
        return 'A'
    elif num_cap == 21:
        return 'B'
    return str(num_cap)


def ler_sumario():

    sumario = {}

    with open(SUMARIO, encoding='utf8') as fp:
        md = fp.read()

    num_cap = None
    for lin in md.split('\n\n'):
        casa_cap = CAP_RE.search(lin)
        if casa_cap:
            num_cap = int(casa_cap.group(1))
            num_secao = 0
        elif num_cap is not None:
            lin = lin.replace('\xa0', ' ')  # \xa0 = NBSP
            casa_secao = SEC_RE.search(lin)
            assert casa_secao, 'NAO CASOU: ' + lin
            tit_secao = casa_secao.group(1)

            if tit_secao[0] == '!':
                num_subsecao += 1
                secao = Secao('{}.{}.{}'.format(id_cap(num_cap), num_secao, num_subsecao),
                              tit_secao[1:])
            else:
                num_secao += 1
                num_subsecao = 0
                secao = Secao('{}.{}'.format(id_cap(num_cap), num_secao), tit_secao)
            # print(secao)
            sumario.setdefault(id_cap(num_cap), []).append(secao)

    return sumario

def marcar(md, sumario_cap):
    ultimo_local = 0
    for secao in sumario_cap:
        local = md.find('\n' + secao.titulo, ultimo_local+1)
        assert local > ultimo_local, secao
        ultimo_local = local
        decoracao = '## {} - '.format(secao.num)
        if secao.num.count('.') == 2:
            decoracao = '#' + decoracao
        md = md[:local+1] + decoracao + md[local+1:]

    return md


def marcar_caps(sumario):
    for path_arq in glob.glob(DIR_DOCS+'*-*.md'):
        nome_arq = os.path.basename(path_arq)
        id_cap = nome_arq.split('-')[0].lstrip('0')
        if not id_cap:
            continue # prefácio não tem seções no sumário

        with open(path_arq, encoding='utf8') as fp:
            md = fp.read()
        print(nome_arq, id_cap)
        md = marcar(md, sumario[id_cap])
        with open(path_arq, 'wt', encoding='utf8') as fp:
            fp.write(md)


if __name__ == '__main__':
    sumario = ler_sumario()
    marcar_caps(sumario)
