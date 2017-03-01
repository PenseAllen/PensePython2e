# Capítulo 14: Arquivos

Este capítulo apresenta a ideia de programas “persistentes”, que mantêm dados em armazenamento permanente, e mostra como usar tipos diferentes de armazenamento permanente, como arquivos e bancos de dados.

## 14.1 - Persistência

A maioria dos programas que vimos até agora são transitórios, porque são executados por algum tempo e produzem alguma saída, mas, quando terminam, seus dados desaparecem. Se executar o programa novamente, ele começa novamente do zero.

Outros programas são persistentes: rodam por muito tempo (ou todo o tempo); mantêm pelo menos alguns dos seus dados em armazenamento permanente (uma unidade de disco rígido, por exemplo); e se são desligados e reiniciados, continuam de onde pararam.

Exemplos de programas persistentes são sistemas operacionais, que rodam praticamente durante todo o tempo em que um computador está ligado, e servidores web, que rodam todo o tempo, esperando pedidos de entrada na rede.

Uma das formas mais simples para programas manterem seus dados é lendo e escrevendo arquivos de texto. Já vimos programas que leem arquivos de texto; neste capítulo veremos programas que os escrevem.

Uma alternativa é armazenar o estado do programa em um banco de dados. Neste capítulo apresentarei um banco de dados simples e um módulo, pickle, que facilita o armazenamento de dados de programas.

## 14.2 - Leitura e escrita

Um arquivo de texto é uma sequência de caracteres armazenados em um meio permanente como uma unidade de disco rígido, pendrive ou CD-ROM. Vimos como abrir e ler um arquivo em “Leitura de listas de palavras” na página 133.

Para escrever um arquivo texto, é preciso abri-lo com o modo `'w'` como segundo parâmetro:

```python
>>> fout = open('output.txt', 'w')
```

Se o arquivo já existe, abri-lo em modo de escrita elimina os dados antigos e começa tudo de novo, então tenha cuidado! Se o arquivo não existir, é criado um arquivo novo.

`open` retorna um objeto de arquivo que fornece métodos para trabalhar com o arquivo. O método write põe dados no arquivo:


```python
>>> line1 = "This here's the wattle,\n"
>>> fout.write(line1)
24
```

O valor devolvido é o número de caracteres que foram escritos. O objeto de arquivo monitora a posição em que está, então se você chamar `write` novamente, os novos dados são acrescentados ao fim do arquivo:


```python
>>> line2 = "the emblem of our land.\n"
>>> fout.write(line2)
24
```

Ao terminar de escrever, você deve fechar o arquivo:

```python
>>> fout.close()
```

Se não fechar o arquivo, ele é fechado para você quando o programa termina.

## 14.3 - Operador de formatação

O argumento de `write` tem que ser uma string, então, se quisermos inserir outros valores em um arquivo, precisamos convertê-los em strings. O modo mais fácil de fazer isso é com `str`:

```python
>>> x = 52
>>> fout.write(str(x))
```

Uma alternativa é usar o operador de formatação, `%`. Quando aplicado a números inteiros, `%` é o operador de módulo. No entanto, quando o primeiro operando é uma string, `%` é o operador de formatação.

O primeiro operando é a string de formatação, que contém uma ou várias sequências de formatação que especificam como o segundo operando deve ser formatado. O resultado é uma string.

Por exemplo, a sequência de formatação '%d' significa que o segundo operando deve ser formatado como um número inteiro decimal:

```python
>>> camels = 42
>>> '%d' % camels
'42'
```

O resultado é a string `'42'`, que não deve ser confundida com o valor inteiro `42`.

Uma sequência de formatação pode aparecer em qualquer lugar na string, então você pode embutir um valor em uma sentença:

```python
>>> 'I have spotted %d camels.' % camels
'I have spotted 42 camels.'
```

Se houver mais de uma sequência de formatação na string, o segundo argumento tem que ser uma tupla. Cada sequência de formatação é combinada com um elemento da tupla, nesta ordem.

O seguinte exemplo usa `'%d'` para formatar um número inteiro, `'%g'` para formatar um número de ponto flutuante e `'%s'` para formatar qualquer objeto como uma string:

```python
>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
```

O número de elementos na tupla tem de corresponder ao número de sequências de formatação na string. Além disso, os tipos dos elementos têm de corresponder às sequências de formatação:

```python
>>> '%d %d %d' % (1, 2)
TypeError: not enough arguments for format string
>>> '%d' % 'dollars'
TypeError: %d format: a number is required, not str
```

No primeiro exemplo não há elementos suficientes; no segundo, o elemento é do tipo incorreto.

Para obter mais informações sobre o operador de formato, veja https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting. Você pode ler sobre uma alternativa mais eficiente, o método de formatação de strings, em https://docs.python.org/3/library/stdtypes.html#str.format.

## 14.4 - Nomes de arquivo e caminhos

Os arquivos são organizados em diretórios (também chamados de “pastas”). Cada programa em execução tem um “diretório atual”, que é o diretório-padrão da maior parte das operações. Por exemplo, quando você abre um arquivo de leitura, Python o procura no diretório atual.

O módulo `os` fornece funções para trabalhar com arquivos e diretórios (“os” é a abreviação de “sistema operacional” em inglês). `os.getcwd` devolve o nome do diretório atual:


```python
>>> import os
>>> cwd = os.getcwd()
>>> cwd
'/home/dinsdale'
```

`cwd` é a abreviação de “diretório de trabalho atual” em inglês. O resultado neste exemplo é `/home/dinsdale`, que é o diretório-padrão de um usuário chamado “dinsdale”.

Uma string como `'/home/dinsdale'`, que identifica um arquivo ou diretório, é chamada de caminho (path).

Um nome de arquivo simples, como `memo.txt`, também é considerado um caminho, mas é um caminho relativo, porque se relaciona ao diretório atual. Se o diretório atual é `/home/dinsdale`, o nome de arquivo `memo.txt` se referiria a `/home/dinsdale/memo.txt`.

Um caminho que começa com `/` não depende do diretório atual; isso é chamado de caminho absoluto. Para encontrar o caminho absoluto para um arquivo, você pode usar `os.path.abspath`:

```python
>>> os.path.abspath('memo.txt')
'/home/dinsdale/memo.txt'
```

`os.path` fornece outras funções para trabalhar com nomes de arquivo e caminhos. Por exemplo, `os.path.exists` que verifica se um arquivo ou diretório existe:

```python
>>> os.path.exists('memo.txt')
True
```

Se existir, `os.path.isdir` verifica se é um diretório:

```python
>>> os.path.isdir('memo.txt')
False
>>> os.path.isdir('/home/dinsdale')
True
```

De forma similar, `os.path.isfile` verifica se é um arquivo.

os.listdir retorna uma lista dos arquivos (e outros diretórios) no diretório dado:

```python
 >>> os.listdir(cwd)
['music', 'photos', 'memo.txt']
```

Para demonstrar essas funções, o exemplo seguinte “passeia” por um diretório, exibe os nomes de todos os arquivos e chama a si mesmo recursivamente em todos os diretórios:

```python
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
```

`os.path.join` recebe um diretório e um nome de arquivo e os une em um caminho completo.

O módulo `os` fornece uma função chamada `walk`, que é semelhante, só que mais versátil. Como exercício, leia a documentação e use-a para exibir os nomes dos arquivos em um diretório dado e seus subdiretórios. Você pode baixar minha solução em http://thinkpython2.com/code/walk.py.

## 14.5 - Captura de exceções

Muitas coisas podem dar errado quando você tenta ler e escrever arquivos. Se tentar abrir um arquivo que não existe, você recebe um `IOError`:

```python
>>> fin = open('bad_file')
IOError: [Errno 2] No such file or directory: 'bad\_file'
```

Se não tiver permissão para acessar um arquivo:

```python
>>> fout = open('/etc/passwd', 'w')
PermissionError: [Errno 13] Permission denied: '/etc/passwd'
```

E se tentar abrir um diretório para leitura, recebe

```python
>>> fin = open('/home')
IsADirectoryError: [Errno 21] Is a directory: '/home'
```

Para evitar esses erros, você pode usar funções como `os.path.exists` e `os.path.isfile`, mas levaria muito tempo e código para verificar todas as possibilidades (se "Errno 21" significa algo, pode ser que pelo menos 21 coisas podem dar errado).

É melhor ir em frente e tentar, e lidar com problemas se eles surgirem, que é exatamente o que a instrução `try` faz. A sintaxe é semelhante à da instrução `if…else`:

```python
try:
    fin = open('bad_file')
except:
    print('Something went wrong.')
```

O Python começa executando a cláusula `try`. Se tudo for bem, ele ignora a cláusula `except` e prossegue. Se ocorrer uma exceção, o programa sai da cláusula `try` e executa a cláusula `except`.

Lidar com exceções usando uma instrução `try` chama-se capturar uma exceção. Neste exemplo, a cláusula `except` exibe uma mensagem de erro que não é muito útil. Em geral, a captura de uma exceção oferece a oportunidade de corrigir o problema ou tentar novamente, ou, ao menos, de terminar o programa adequadamente.

## 14.6 - Bancos de dados

Um banco de dados é um arquivo organizado para armazenar dados. Muitos bancos de dados são organizados como um dicionário, porque mapeiam chaves a valores. A maior diferença entre um banco de dados e um dicionário é que o banco de dados está em um disco (ou outro armazenamento permanente), portanto persiste depois que o programa termina.

O módulo dbm fornece uma interface para criar e atualizar arquivos de banco de dados. Como exemplo, criarei um banco de dados que contém legendas de arquivos de imagem.

Abrir um banco de dados é semelhante à abertura de outros arquivos:

```python
>>> import dbm
>>> db = dbm.open('captions', 'c')
```

O modo 'c' significa que o banco de dados deve ser criado, se ainda não existir. O resultado é um objeto de banco de dados que pode ser usado (para a maior parte das operações) como um dicionário.

Quando você cria um novo item, dbm atualiza o arquivo de banco de dados:

```python
>>> db['cleese.png'] = 'Photo of John Cleese.'
```

Quando você acessa um dos itens, dbm lê o arquivo:

```python
>>> db['cleese.png']
b'Photo of John Cleese.'
```

O resultado é um objeto `bytes`, o que explica o prefixo `b`. Um objeto `bytes` é semelhante a uma string, em muitos aspectos. Quando você avançar no Python, a diferença se tornará importante, mas, por enquanto, podemos ignorá-la.

Se fizer outra atribuição a uma chave existente, o dbm substitui o valor antigo:

```python
>>> db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
>>> db['cleese.png']
b'Photo of John Cleese doing a silly walk.'
```

Alguns métodos de dicionário, como keys e items, não funcionam com objetos de banco de dados. No entanto, a iteração com um loop `for`, sim:

```python
for key in db:
    print(key, db[key])
```

Como em outros arquivos, você deve fechar o banco de dados quando terminar:

```python
>>> db.close()
```

## 14.7 - Usando o Pickle

Uma limitação de `dbm` é que as chaves e os valores têm que ser strings ou bytes. Se tentar usar algum outro tipo, vai receber um erro.

O módulo `pickle` pode ajudar. Ele traduz quase qualquer tipo de objeto em uma string conveniente para o armazenamento em um banco de dados, e então traduz strings de volta em objetos.

pickle.dumps recebe um objeto como parâmetro e retorna uma representação de string:


```python
>>> import pickle
>>> t = [1, 2, 3]
>>> pickle.dumps(t)
b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
```

O formato não é óbvio para leitores humanos; o objetivo é que seja fácil para o `pickle` interpretar. `pickle.loads` reconstitui o objeto:

```python
>>> t1 = [1, 2, 3]
>>> s = pickle.dumps(t1)
>>> t2 = pickle.loads(s)
>>> t2
[1, 2, 3]
```

Embora o novo objeto tenha o mesmo valor que o antigo, não é (em geral) o mesmo objeto:

```python
>>> t1 == t2
True
>>> t1 is t2
False
```

Em outras palavras, usar o `pickle.dumps` e `pickle.loads` tem o mesmo efeito que copiar o objeto.

Você pode usar o `pickle` para guardar variáveis que não são strings em um banco de dados. Na verdade, esta combinação é tão comum que foi encapsulada em um módulo chamado `shelve`.

## 14.8 - Pipes

A maior parte dos sistemas operacionais fornece uma interface de linha de comando, conhecida como shell. Shells normalmente fornecem comandos para navegar nos sistemas de arquivos e executar programas. Por exemplo, em Unix você pode alterar diretórios com `cd`, exibir o conteúdo de um diretório com `ls` e abrir um navegador web digitando (por exemplo) `firefox`.

Qualquer programa que possa ser aberto no shell também pode ser aberto no Python usando um objeto pipe, que representa um programa em execução.

Por exemplo, o comando Unix `ls -l` normalmente exibe o conteúdo do diretório atual no formato longo. Você pode abrir ls com `os.popen[1]`:

```python
>>> cmd = 'ls -l'
>>> fp = os.popen(cmd)
```

O argumento é uma string que contém um comando shell. O valor de retorno é um objeto que se comporta como um arquivo aberto. É possível ler a saída do processo ls uma linha por vez com readline ou receber tudo de uma vez com read:

```python
>>> res = fp.read()
```

Ao terminar, feche o pipe como se fosse um arquivo:


```python
>>> stat = fp.close()
>>> print(stat)
None
```

O valor de retorno é o status final do processo `ls`; `None` significa que terminou normalmente (sem erros).

Por exemplo, a maior parte dos sistemas Unix oferece um comando chamado `md5sum`, que lê o conteúdo de um arquivo e calcula uma assinatura digital. Você pode ler sobre o MD5 em http://en.wikipedia.org/wiki/Md5. Este comando fornece uma forma eficiente de verificar se dois arquivos têm o mesmo conteúdo. A probabilidade de dois conteúdos diferentes produzirem a mesma assinatura digital é muito pequena (isto é, muito pouco provável que aconteça antes do colapso do universo).

Você pode usar um pipe para executar o `md5sum` do Python e receber o resultado:

```python
>>> filename = 'book.tex'
>>> cmd = 'md5sum ' + filename
>>> fp = os.popen(cmd)
>>> res = fp.read()
>>> stat = fp.close()
>>> print(res)
1e0033f0ed0656636de0d75144ba32e0 book.tex
>>> print(stat)
None
```

## 14.9 - Escrevendo módulos

Qualquer arquivo que contenha código do Python pode ser importado como um módulo. Por exemplo, vamos supor que você tenha um arquivo chamado `wc.py` com o seguinte código:

```python
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount('wc.py'))
```

Quando este programa é executado, ele lê a si mesmo e exibe o número de linhas no arquivo, que é 7. Você também pode importá-lo desta forma:

```python
>>> import wc
7
```

Agora você tem um objeto de módulo wc:

```python
>>> wc
<module 'wc' from 'wc.py'>
```

O objeto de módulo fornece o linecount:

```python
>>> wc.linecount('wc.py')
7
```

Então é assim que se escreve módulos no Python.

O único problema com este exemplo é que quando você importa o módulo, ele executa o código de teste no final. Normalmente, quando se importa um módulo, ele define novas funções, mas não as executa.

Os programas que serão importados como módulos muitas vezes usam a seguinte expressão:

```python
if __name__ == '__main__':
    print(linecount('wc.py'))
```

`__name__` é uma variável integrada, estabelecida quando o programa inicia. Se o programa estiver rodando como um script, `__name__` tem o valor `'__main__'`; neste caso, o código de teste é executado. Do contrário, se o módulo está sendo importado, o código de teste é ignorado.

Como exercício, digite este exemplo em um arquivo chamado wc.py e execute-o como um script. Então execute o interpretador do Python e import wc. Qual é o valor de `__name__` quando o módulo está sendo importado?

Atenção: se você importar um módulo que já tenha sido importado, o Python não faz nada. Ele não relê o arquivo, mesmo se tiver sido alterado.

Se quiser recarregar um módulo, você pode usar a função integrada `reload`, mas isso pode causar problemas, então o mais seguro é reiniciar o interpretador e importar o módulo novamente.

## 14.10 - Depuração

Quando estiver lendo e escrevendo arquivos, você pode ter problemas com whitespace. Esses erros podem ser difíceis para depurar, porque os espaços, tabulações e quebras de linha normalmente são invisíveis:

```python
>>> s = '1 2\t 3\n 4'
>>> print(s)
1 2      3
 4
```

A função integrada `repr` pode ajudar. Ela recebe qualquer objeto como argumento e retorna uma representação em string do objeto. Para strings, representa caracteres de whitespace com sequências de barras invertidas:

```python
>>> print(repr(s))
'1 2\t 3\n 4'
```

Isso pode ser útil para a depuração.

Outro problema que você pode ter é que sistemas diferentes usam caracteres diferentes para indicar o fim de uma linha. Alguns sistemas usam newline, representado por `\n`. Outros usam um caractere de retorno, representado por `\r`. Alguns usam ambos. Se mover arquivos entre sistemas diferentes, essas inconsistências podem causar problemas.

Para a maior parte dos sistemas há aplicações para converter de um formato a outro. Você pode encontrá-los (e ler mais sobre o assunto) em http://en.wikipedia.org/wiki/Newline. Ou, é claro, você pode escrever um por conta própria.

## 14.11 - Glossário

<dl>
<dt><a id="glos:persistente" href="#termo:persistente">persistente</a></dt>
<dd>Relativo a um programa que roda indefinidamente e mantém pelo menos alguns dos seus dados em armazenamento permanente.</dd>

<dt><a id="glos:operador de formatação" href="#termo:operador de formatação">operador de formatação</a></dt>
<dd>Um operador, %, que recebe uma string de formatação e uma tupla e gera uma string que inclui os elementos da tupla formatada como especificado pela string de formatação.</dd>

<dt><a id="glos:string de formatação" href="#termo:string de formatação">string de formatação</a></dt>
<dd>String usada com o operador de formatação, que contém sequências de formatação.</dd>

<dt><a id="glos:sequência de formatação" href="#termo:sequência de formatação">sequência de formatação</a></dt>
<dd>Sequência de caracteres em uma string de formatação, como %d, que especifica como um valor deve ser formatado.</dd>

<dt><a id="glos:arquivo de texto" href="#termo:arquivo de texto">arquivo de texto</a></dt>
<dd>Sequência de caracteres guardados em armazenamento permanente, como uma unidade de disco rígido.</dd>

<dt><a id="glos:diretório" href="#termo:diretório">diretório</a></dt>
<dd>Uma coleção de arquivos nomeada, também chamada de pasta.</dd>

<dt><a id="glos:caminho" href="#termo:caminho">caminho</a></dt>
<dd>String que identifica um arquivo.</dd>

<dt><a id="glos:caminho relativo" href="#termo:caminho relativo">caminho relativo</a></dt>
<dd>Caminho que inicia no diretório atual.</dd>

<dt><a id="glos:caminho absoluto" href="#termo:caminho absoluto">caminho absoluto</a></dt>
<dd>Caminho que inicia no diretório de posição mais alta (raiz) no sistema de arquivos.</dd>

<dt><a id="glos:capturar" href="#termo:capturar">capturar</a></dt>
<dd>Impedir uma exceção de encerrar um programa usando as instruções try e except.</dd>

<dt><a id="glos:banco de dados" href="#termo:banco de dados">banco de dados</a></dt>
<dd>Um arquivo cujo conteúdo é organizado como um dicionário, com chaves que correspondem a valores.</dd>

<dt><a id="glos:objeto bytes" href="#termo:objeto bytes">objeto bytes</a></dt>
<dd>Objeto semelhante a uma string.</dd>

<dt><a id="glos:shell" href="#termo:shell">shell</a></dt>
<dd>Programa que permite aos usuários digitar comandos e executá-los para iniciar outros programas.</dd>

<dt><a id="glos:objeto pipe" href="#termo:objeto pipe">objeto pipe</a></dt>
<dd>Objeto que representa um programa em execução, permitindo que um programa do Python execute comandos e leia os resultados.</dd>

</dl>

## 14.12 - Exercícios

### Exercício 14.1

Escreva uma função chamada sed que receba como argumentos uma string-padrão, uma string de substituição e dois nomes de arquivo; ela deve ler o primeiro arquivo e escrever o conteúdo no segundo arquivo (criando-o, se necessário). Se a string-padrão aparecer em algum lugar do arquivo, ela deve ser substituída pela string de substituição.

Se ocorrer um erro durante a abertura, leitura, escrita ou fechamento dos arquivos, seu programa deve capturar a exceção, exibir uma mensagem de erro e encerrar.

Solução: http://thinkpython2.com/code/sed.py.

### Exercício 14.2

Se você baixar minha solução do Exercício 12.2 em http://thinkpython2.com/code/anagram_sets.py, verá que ela cria um dicionário que mapeia uma string ordenada de letras à lista de palavras que podem ser soletradas com aquelas letras. Por exemplo, `'opst'` mapeia à lista `['opts', 'post', 'pots', 'spot', 'stop', 'tops']`.

Escreva um módulo que importe `anagram_sets` e forneça duas novas funções: `store_anagrams` deve guardar o dicionário de anagramas em uma “prateleira” (objeto criado pelo módulo `sheve`); `read_anagrams` deve procurar uma palavra e devolver uma lista dos seus anagramas.

Solução: http://thinkpython2.com/code/anagram_db.py.

### Exercício 14.3

Em uma grande coleção de arquivos MP3 pode haver mais de uma cópia da mesma música, guardada em diretórios diferentes ou com nomes de arquivo diferentes. A meta deste exercício é procurar duplicatas.

1. Escreva um programa que procure um diretório e todos os seus subdiretórios, recursivamente, e retorne uma lista de caminhos completos de todos os arquivos com um dado sufixo (como .mp3). Dica: os.path fornece várias funções úteis para manipular nomes de caminhos e de arquivos.

2. Para reconhecer duplicatas, você pode usar md5sum para calcular uma “soma de controle” para cada arquivo. Se dois arquivos tiverem a mesma soma de controle, provavelmente têm o mesmo conteúdo.

3. Para conferir o resultado, você pode usar o comando Unix `diff`.

Solução: http://thinkpython2.com/code/find\_duplicates.py.
