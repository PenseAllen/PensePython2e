# Capítulo 12: Tuplas

Este capítulo apresenta mais um tipo integrado, a tupla, e descreve como as listas, os dicionários e as tuplas trabalham juntos. Além disso, apresento um recurso útil para listas de argumentos de comprimento variável: os operadores gather e scatter.

Uma observação: não há consenso sobre como pronunciar “tuple” (em inglês). Algumas pessoas dizem “tuhple”, que rima com “supple”. Porém, no contexto da programação, a maioria das pessoas diz “too-ple”, que rima com “quadruple”.

## 12.1 - Tuplas são imutáveis

Uma tupla é uma sequência de valores. Os valores podem ser de qualquer tipo, e podem ser indexados por números inteiros, portanto, nesse sentido, as tuplas são muito parecidas com as listas. A diferença importante é que as tuplas são imutáveis.

Sintaticamente, uma tupla é uma lista de valores separados por vírgulas:

```python
>>> t = 'a', 'b', 'c', 'd', 'e'
```

Embora não seja sempre necessário, é comum colocar tuplas entre parênteses:

```python
>>> t = ('a', 'b', 'c', 'd', 'e')
```

Para criar uma tupla com um único elemento, é preciso incluir uma vírgula final:


```python
>>> t1 = 'a',
>>> type(t1)
<class 'tuple'>
```

Um único valor entre parênteses não é uma tupla:

```python
>>> t2 = ('a')
>>> type(t2)
<class 'str'>
```

Outra forma de criar uma tupla é com a função integrada `tuple`. Sem argumentos, cria uma tupla vazia:

```python
>>> t = tuple()
>>> t
()
```

Se os argumentos forem uma sequência (string, lista ou tupla), o resultado é uma tupla com os elementos da sequência:

```python
>>> t = tuple('lupins')
>>> t
('l', 'u', 'p', 'i', 'n', 's')
```

Como `tuple` é o nome de uma função integrada, você deve evitar usá-lo como nome de variável.

A maior parte dos operadores de lista também funciona em tuplas. O operador de colchetes indexa um elemento:

```python
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> t[0]
'a'
```

E o operador de fatia seleciona vários elementos:

```python
>>> t[1:3]
('b', 'c')
```

Entretanto, se tentar alterar um dos elementos da tupla, vai receber um erro:

```python
>>> t[0] = 'A'
TypeError: object doesn't support item assignment
```

Como tuplas são imutáveis, você não pode alterar os elementos, mas pode substituir uma tupla por outra:


```python
>>> t = ('A',) + t[1:]
>>> t
('A', 'b', 'c', 'd', 'e')
```

Essa instrução faz uma nova tupla e então a atribui a `t`.

Os operadores relacionais funcionam com tuplas e outras sequências; o Python começa comparando o primeiro elemento de cada sequência. Se forem iguais, vai para os próximos elementos, e assim por diante, até que encontre elementos que sejam diferentes. Os elementos subsequentes não são considerados (mesmo se forem muito grandes).

```python
>>> (0, 1, 2) < (0, 3, 4)
True
>>> (0, 1, 2000000) < (0, 3, 4)
True
```

## 12.2 - Atribuição de tuplas

Muitas vezes, é útil trocar os valores de duas variáveis. Com a atribuição convencional, é preciso usar uma variável temporária. Por exemplo, trocar a e b.

```python
>>> temp = a
>>> a = b
>>> b = temp
```

Essa solução é trabalhosa; a atribuição de tuplas é mais elegante:

```python
>>> a, b = b, a
```

O lado esquerdo é uma tupla de variáveis; o lado direito é uma tupla de expressões. Cada valor é atribuído à sua respectiva variável. Todas as expressões no lado direito são avaliadas antes de todas as atribuições.

O número de variáveis à esquerda e o número de valores à direita precisam ser iguais:

```python
>>> a, b = 1, 2, 3
ValueError: too many values to unpack
```

De forma geral, o lado direito pode ter qualquer tipo de sequência (string, lista ou tupla). Por exemplo, para dividir um endereço de email em um nome de usuário e um domínio, você poderia escrever:

```python
>>> addr = 'monty@python.org'
>>> uname, domain = addr.split('@')
```

O valor de retorno do `split` é uma lista com dois elementos; o primeiro elemento é atribuído a `uname`, o segundo a `domain`:

```python
>>> uname
'monty'
>>> domain
'python.org'
```

## 12.3 - Tuplas como valores de retorno

Falando estritamente, uma função só pode retornar um valor, mas se o valor for uma tupla, o efeito é o mesmo que retornar valores múltiplos. Por exemplo, se você quiser dividir dois números inteiros e calcular o quociente e resto, não é eficiente calcular x/y e depois x%y. É melhor calcular ambos ao mesmo tempo.

A função integrada divmod toma dois argumentos e devolve uma tupla de dois valores: o quociente e o resto. Você pode guardar o resultado como uma tupla:

```python
>>> t = divmod(7, 3)
>>> t
(2, 1)
```

Ou usar a atribuição de tuplas para guardar os elementos separadamente:

```python
>>> quot, rem = divmod(7, 3)
>>> quot
2
>>> rem
1
```

Aqui está um exemplo de função que retorna uma tupla:

```python
def min_max(t):
    return min(t), max(t)
```

`max` e `min` são funções integradas que encontram os maiores e menores elementos de uma sequência. `min_max` calcula ambos e retorna uma tupla de dois valores.

## 12.4 - Tuplas com argumentos de comprimento variável

As funções podem receber um número variável de argumentos. Um nome de parâmetro que comece com `*` reúne vários argumentos em uma tupla. Por exemplo, `printall` recebe qualquer número de argumentos e os exibe:

```python
def printall(*args):
    print(args)
```

O parâmetro com o prefixo `*` pode ter qualquer nome que você goste, mas `args` é o convencional. É assim que a função funciona:

```python
>>> printall(1, 2.0, '3')
(1, 2.0, '3')
```

O complemento de reunir é espalhar. Se você tiver uma sequência de valores e quiser passá-la a uma função como argumentos múltiplos, pode usar o operador `*`. Por exemplo, o `divmod` recebe exatamente dois argumentos; ele não funciona com uma tupla:

```python
>>> t = (7, 3)
>>> divmod(t)
TypeError: divmod expected 2 arguments, got 1
```

No entanto, se você espalhar a tupla, aí funciona:

```python
>>> divmod(*t)
(2, 1)
```

Muitas das funções integradas usam tuplas com argumentos de comprimento variável. Por exemplo, `max` e `min` podem receber qualquer número de argumentos:

```python
>>> max(1, 2, 3)
3
```

Mas sum, não:

```python
>>> sum(1, 2, 3)
TypeError: sum expected at most 2 arguments, got 3
```

Como exercício, escreva uma função chamada `sumall` que receba qualquer número de argumentos e retorne a soma deles.

## 12.5 - Listas e tuplas

`zip` é uma função integrada que recebe duas ou mais sequências e devolve uma lista de tuplas onde cada tupla contém um elemento de cada sequência. O nome da função tem a ver com o zíper, que se junta e encaixa duas carreiras de dentes.

Este exemplo encaixa uma string e uma lista:

```python
>>> s = 'abc'
>>> t = [0, 1, 2]
>>> zip(s, t)
<zip object at 0x7f7d0a9e7c48>
```

O resultado é um objeto `zip` que sabe como percorrer os pares. O uso mais comum de `zip` é em um loop `for`:

```python
>>> for pair in zip(s, t):
...     print(pair)
...
('a', 0)
('b', 1)
('c', 2)
```

Um objeto `zip` é um tipo de iterador, ou seja, qualquer objeto que percorre ou itera sobre uma sequência. Iteradores são semelhantes a listas em alguns aspectos, mas, ao contrário de listas, não é possível usar um índice para selecionar um elemento de um iterador.

Se quiser usar operadores e métodos de lista, você pode usar um objeto `zip` para fazer uma lista:

```python
>>> list(zip(s, t))
[('a', 0), ('b', 1), ('c', 2)]
```

O resultado é uma lista de tuplas; neste exemplo, cada tupla contém um caractere da string e o elemento correspondente da lista.

Se as sequências não forem do mesmo comprimento, o resultado tem o comprimento da mais curta:

```python
>>> list(zip('Anne', 'Elk'))
[('A', 'E'), ('n', 'l'), ('n', 'k')]
```

Você pode usar a atribuição de tuplas em um loop for para atravessar uma lista de tuplas:

```python
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)
```

Cada vez que o programa passa pelo loop, o Python seleciona a próxima tupla na lista e atribui os elementos letter e number. A saída deste loop é:

```python
0 a
1 b
2 c
```

Se combinar `zip`, `for` e atribuição de tuplas, você pode fazer uma expressão útil para percorrer duas (ou mais) sequências ao mesmo tempo. Por exemplo, `has_match` recebe duas sequências, `t1` e `t2` e retorna `True` se houver um índice `i` tal que `t1[i] == t2[i]`:

```python
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False
```

Se precisar atravessar os elementos de uma sequência e seus índices, você pode usar a função integrada `enumerate`:

```python
for index, element in enumerate('abc'):
    print(index, element)
```

O resultado de `enumerate` é um objeto `enumerate`, que itera sobre uma sequência de pares; cada par contém um índice (começando de 0) e um elemento da sequência dada. Neste exemplo, a saída é

```python
0 a
1 b
2 c
```

De novo.

## 12.6 - Dicionários e tuplas

Os dicionários têm um método chamado `items` que devolve uma sequência de tuplas, onde cada tupla é um par chave-valor:

```python
>>> d = {'a':0, 'b':1, 'c':2}
>>> t = d.items()
>>> t
dict_items([('c', 2), ('a', 0), ('b', 1)])
```

O resultado é um objeto `dict_items`, que é um iterador que percorre os pares chave-valor. Você pode usá-lo em um loop `for`, desta forma:

```python
>>> for key, value in d.items():
...     print(key, value)
...
c 2
a 0
b 1
```

Como se poderia esperar de um dicionário, os itens não estão em nenhuma ordem em particular.

Indo em outra direção, você pode usar uma lista de tuplas para inicializar um novo dicionário:

```python
>>> t = [('a', 0), ('c', 2), ('b', 1)]
>>> d = dict(t)
>>> d
{'a': 0, 'c': 2, 'b': 1}
```

Combinar `dict` com `zip` produz uma forma concisa de criar um dicionário:


```python
>>> d = dict(zip('abc', range(3)))
>>> d
{'a': 0, 'c': 2, 'b': 1}
```

O método de dicionário `update` também recebe uma lista de tuplas e as adiciona, como pares chave-valor, a um dicionário existente.

É comum usar tuplas como chaves em dicionários (principalmente porque você não pode usar listas). Por exemplo, uma lista telefônica poderia mapear pares de sobrenome e primeiro nome a números de telefone. Supondo que tenhamos definido last, first e number, podemos escrever:

```python
directory[last, first] = number
```

A expressão entre chaves é uma tupla. Podemos usar atribuição de tuplas para atravessar este dicionário:

```python
for last, first in directory:
    print(first, last, directory[last,first])
```

Este loop atravessa as chaves em directory, que são tuplas. Ele atribui os elementos de cada tupla para `last` e `first`, e então exibe o nome e número de telefone correspondente.

Há duas formas de representar tuplas em um diagrama de estado. A versão mais detalhada mostra os índices e elementos como aparecem em uma lista. Por exemplo, a tupla ('Cleese', 'John') apareceria como na Figura 12.1.

![Figura 12.1 – Diagrama de estado de uma tupla.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1201.png)
<br>_Figura 12.1 – Diagrama de estado de uma tupla._

No entanto, em um diagrama maior, você pode querer omitir os detalhes. Por exemplo, um diagrama da lista telefônica poderia ser como o da Figura 12.2.


![Figura 12.2 – Diagrama de estado de um dicionário com chaves do tipo tupla.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1202.png)
<br>_Figura 12.2 – Diagrama de estado de um dicionário com chaves do tipo tupla._

Aqui as tuplas são mostradas usando a sintaxe do Python para simplificar o gráfico. O número de telefone no diagrama é a linha de reclamações da BBC, então, por favor, não ligue para lá.

## 12.7 - Sequências de sequências

Eu me concentrei em listas de tuplas, mas quase todos os exemplos neste capítulo também funcionam com listas de listas, tuplas de tuplas e tuplas de listas. Para evitar enumerar as combinações possíveis, às vezes é mais fácil falar sobre sequências de sequências.

Em muitos contextos, os tipos diferentes de sequências (strings, listas e tuplas) podem ser usados de forma intercambiável. Então, como escolher uma em vez da outra?

Para começar com o óbvio, as strings são mais limitadas que outras sequências porque os elementos têm de ser caracteres. Também são imutáveis. Se precisar da capacidade de alterar caracteres em uma string (em vez de criar outra string) você pode querer usar uma lista de caracteres.

As listas são mais comuns que as tuplas, principalmente porque são mutáveis. Mas há alguns casos em que você pode preferir tuplas:

1. Em alguns contextos, como em uma instrução `return`, é sintaticamente mais simples criar uma tupla que uma lista.

2. Se quiser usar uma sequência como uma chave de dicionário, é preciso usar um tipo imutável como uma tupla ou string.

3. Se estiver passando uma sequência como um argumento a uma função, usar tuplas reduz o potencial de comportamento inesperado devido a alias.

Como tuplas são imutáveis, elas não fornecem métodos como `sort` e `reverse`, que alteram listas existentes. Porém, o Python fornece a função integrada `sorted`, que recebe qualquer sequência e retorna uma nova lista com os mesmos elementos ordenados, e `reversed`, que recebe uma sequência e retorna um iterador que percorre a lista em ordem reversa.

## 12.8 - Depuração

As listas, os dicionários e as tuplas são exemplos de estruturas de dados; neste capítulo estamos começando a ver estruturas de dados compostas, como as listas de tuplas ou dicionários que contêm tuplas como chaves e listas como valores. As estruturas de dados compostas são úteis, mas são propensas ao que chamo de erros de forma; isto é, erros causados quando uma estrutura de dados tem o tipo, tamanho ou estrutura incorretos. Por exemplo, se você estiver esperando uma lista com um número inteiro e eu der apenas o número inteiro (não em uma lista), não vai funcionar.

Para ajudar a depurar esses tipos de erro, escrevi um módulo chamado `structshape`, que fornece uma função, também chamada `structshape`, que recebe qualquer tipo de estrutura de dados como argumento e retorna uma string, que resume sua forma. Você pode baixá-la em http://thinkpython2.com/code/structshape.py.

Aqui está o resultado de uma lista simples:

```python
>>> from structshape import structshape
>>> t = [1, 2, 3]
>>> structshape(t)
'list of 3 int'
```

Um programa mais sofisticado pode escrever “list of 3 ints”, mas é mais fácil não lidar com plurais. Aqui está uma lista de listas:

```python
>>> t2 = [[1,2], [3,4], [5,6]]
>>> structshape(t2)
'list of 3 list of 2 int'
```

Se os elementos da lista não forem do mesmo tipo, `structshape` os agrupa, na ordem, por tipo:

```python
>>> t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
>>> structshape(t3)
'list of (3 int, float, 2 str, 2 list of int, int)'
```

Aqui está uma lista de tuplas:

```python
>>> s = 'abc'
>>> lt = list(zip(t, s))
>>> structshape(lt)
'list of 3 tuple of (int, str)'
```
E aqui está um dicionário com três itens que mapeia números inteiros a strings:

```python
>>> d = dict(lt)
>>> structshape(d)
'dict of 3 int->str'
```

Se estiver com problemas para monitorar suas estruturas de dados, o `structshape` pode ajudar.

## 12.9 - Glossário

<dl>
<dt><a id="glos:tupla" href="#termo:tupla">tupla</a></dt>
<dd>Sequência imutável de elementos.</dd>

<dt><a id="glos:atribuição de tupla" href="#termo:atribuição de tupla">atribuição de tupla</a></dt>
<dd>Atribuição com uma sequência no lado direito e uma tupla de variáveis à esquerda. O lado direito é avaliado e então seus elementos são atribuídos às variáveis à esquerda.</dd>

<dt><a id="glos:gather" href="#termo:gather">gather</a></dt>
<dd>Operação para montar uma tupla com argumento de comprimento variável.</dd>

<dt><a id="glos:scatter" href="#termo:scatter">scatter</a></dt>
<dd>Operação para tratar uma sequência como uma lista de argumentos.</dd>

<dt><a id="glos:objeto zip" href="#termo:objeto zip">objeto zip</a></dt>
<dd>O resultado de chamar uma função integrada zip; um objeto que se repete por uma sequência de tuplas.</dd>

<dt><a id="glos:iterador" href="#termo:iterador">iterador</a></dt>
<dd>Objeto que pode se repetir por uma sequência, mas que não oferece operadores de lista e métodos.</dd>

<dt><a id="glos:estrutura de dados" href="#termo:estrutura de dados">estrutura de dados</a></dt>
<dd>Coleção de valores relacionados, muitas vezes organizados em listas, dicionários, tuplas etc.</dd>

<dt><a id="glos:erro de forma" href="#termo:erro de forma">erro de forma</a></dt>
<dd>Erro causado pelo fato de o valor ter a forma incorreta; isto é, tipo ou tamanho incorreto.</dd>

</dl>

## 12.10 - Exercícios

### Exercício 12.1

Escreva uma função chamada `most_frequent` que receba uma string e exiba as letras em ordem decrescente de frequência. Encontre amostras de texto de vários idiomas diferentes e veja como a frequência das letras varia entre os idiomas. Compare seus resultados com as tabelas em http://en.wikipedia.org/wiki/Letter_frequencies.

Solução: http://thinkpython2.com/code/most_frequent.py.

### Exercício 12.2

Mais anagramas!

1. Escreva um programa que leia uma lista de palavras de um arquivo (veja “Leitura de listas de palavras”, na página 133) e imprima todos os conjuntos de palavras que são anagramas.

        Aqui está um exemplo de como a saída pode parecer:

```python
        ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
        ['retainers', 'ternaries']
        ['generating', 'greatening']
        ['resmelts', 'smelters', 'termless']
```

        Dica: você pode querer construir um dicionário que mapeie uma coleção de letras a uma lista de palavras que podem ser soletradas com essas letras. A pergunta é: como representar a coleção de letras de forma que possa ser usada como uma chave?

2. Altere o programa anterior para que exiba a lista mais longa de anagramas primeiro, seguido pela segunda mais longa, e assim por diante.

3. No Scrabble, um “bingo” é quando você joga todas as sete peças na sua estante, junto com uma peça no tabuleiro, para formar uma palavra de oito letras. Que coleção de oito letras forma o maior número possível de bingos? Dica: há sete.

Solução: http://thinkpython2.com/code/anagram_sets.py.

### Exercício 12.3

Duas palavras formam um “par de metátese” se você puder transformar uma na outra trocando duas letras, por exemplo, “converse” e “conserve”. Escreva um programa que descubra todos os pares de metátese no dicionário. Dica: não teste todos os pares de palavras e não teste todas as trocas possíveis.

Solução: http://thinkpython2.com/code/metathesis.py. Crédito: este exercício foi inspirado por um exemplo em http://puzzlers.org.

### Exercício 12.4

Aqui está outro quebra-cabeça do programa Car Talk (http://www.cartalk.com/content/puzzlers):

Qual é a palavra inglesa mais longa, que permanece uma palavra inglesa válida, conforme vai removendo suas letras, uma após a outra?

Agora, as letras podem ser retiradas do fim ou do meio, mas você não pode reajustar nenhuma delas. Cada vez que remove uma letra, você acaba com outra palavra inglesa. Se fizer isto, eventualmente você acabará com uma letra e isso também será uma palavra inglesa; uma encontrada no dicionário. Quero saber qual é a palavra mais longa e quantas letras tem?

Vou dar um pequeno exemplo modesto: Sprite. Ok? Você começa com sprite, tira uma letra do interior da palavra, tira o r, e ficamos com a palavra spite, então tiramos o e do fim, ficamos com spit, tiramos o s, ficamos com pit, it e I.

Escreva um programa que encontre todas as palavras que podem ser reduzidas desta forma, e então encontre a mais longa.

Este exercício é um pouco mais desafiador que a maioria, então aqui estão algumas sugestões:

1. Você pode querer escrever uma função que receba uma palavra e calcule uma lista de todas as palavras que podem ser formadas retirando uma letra. Esses são os “filhos” da palavra.

2. Recursivamente, uma palavra é redutível se algum de seus filhos for redutível. Como caso base, você pode considerar a string vazia redutível.

3. A lista de palavras que forneci, words.txt, não contém palavras de uma letra só. Portanto, você pode querer acrescentar “I”, “a”, e a string vazia.

4. Para melhorar o desempenho do seu programa, você pode querer memorizar as palavras conhecidas por serem redutíveis.

Solução: http://thinkpython2.com/code/reducible.py.
