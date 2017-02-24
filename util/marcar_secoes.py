#!/usr/bin/env python3

import re
import collections

SUMARIO = '../recebido/sumario.md'

CAP_RE = re.compile('^Capítulo (\d+)', re.MULTILINE)
SEC_RE = re.compile('(.+?)\s+\d+$', re.MULTILINE)

Secao = collections.namedtuple('Secao', 'num titulo')

def id_cap(num_cap):
    if num_cap == 20:
        return 'A'
    elif num_cap == 21:
        return 'A'
    return str(num_cap)


def ler_sumario():

    with open(SUMARIO, encoding='utf8') as fp:
        md = fp.read()

    num_cap = None
    for lin in md.split('\n\n'):
        casa_cap = CAP_RE.search(lin)
        if casa_cap:
            num_cap = int(casa_cap.group(1))
            print(num_cap)
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
            print(secao)



if __name__ == '__main__':
    ler_sumario()
