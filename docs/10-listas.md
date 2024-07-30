# Capítulo 10: Listas

Este capítulo apresenta um dos tipos integrados mais úteis do Python: listas. Você também aprenderá mais sobre objetos e o que pode acontecer quando o mesmo objeto tem mais de um nome.

## 10.1 - Uma lista é uma sequência

Como uma string, uma lista é uma sequência de valores. Em uma string, os valores são caracteres; em uma lista, eles podem ser de qualquer tipo. Os valores em uma lista são chamados de elementos, ou, algumas vezes, de itens.

Há várias formas para criar uma lista; a mais simples é colocar os elementos entre colchetes (`[` e `]`):

```python
[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']
```

O primeiro exemplo é uma lista de quatro números inteiros. O segundo é uma lista de três strings. Os elementos de uma lista não precisam ser do mesmo tipo. A lista seguinte contém uma string, um número de ponto flutuante, um número inteiro e (olhe só!) outra lista:

```python
['spam', 2.0, 5, [10, 20]]
```

Uma lista dentro de outra lista é uma lista aninhada.

Uma lista que não contém elementos é chamada de lista vazia; você pode criar uma com colchetes vazios [].

Como já se poderia esperar, podemos atribuir uma lista de valores a variáveis:

```python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [42, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [42, 123] []
```

## 10.2 - Listas são mutáveis

A sintaxe para acessar os elementos de uma lista é a mesma que para acessar os caracteres de uma string: o operador de colchete. A expressão dentro dos colchetes especifica o índice. Lembre-se de que os índices começam em 0:

```python
>>> cheeses[0]
'Cheddar'
```

Diferente das strings, listas são mutáveis. Quando o operador de colchete aparece do lado esquerdo de uma atribuição, ele identifica o elemento da lista que será atribuído:


```python
>>> numbers = [42, 123]
>>> numbers[1] = 5
>>> numbers
[42, 5]
```

O primeiro elemento de numbers, que costumava ser 123, agora é 5.

A Figura 10.1 mostra o diagrama de estado para cheeses, numbers e empty.

![Figura 10.1 – Diagrama de estado de três listas.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1001.png)
<br>_Figura 10.1 – Diagrama de estado de três listas._

As listas são representadas pelas caixas com a palavra “lista” fora delas e os elementos da lista dentro delas. cheeses refere-se a uma lista com três elementos indexados como 0, 1 e 2. numbers contém dois elementos e o diagrama mostra que o valor do segundo elemento foi reatribuído de 123 para 5. empty refere-se a uma lista sem elementos.

Índices de listas funcionam da mesma forma que os índices de strings:

* Qualquer expressão de números inteiros pode ser usada como índice.

* Se tentar ler ou escrever um elemento que não existe, você recebe um IndexError.

* Se um índice tiver um valor negativo, ele conta de trás para a frente, a partir do final da lista.

O operador in também funciona com listas:

```python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False
```

## 10.3 - Percorrendo uma lista

A forma mais comum de percorrer os elementos em uma lista é com um loop for. A sintaxe é a mesma que a das strings:

```python
for cheese in cheeses:
    print(cheese)
```

Isso funciona bem se você precisa apenas ler os elementos da lista. Mas se você quer escrever ou atualizar os elementos, você precisa dos índices. Uma forma comum de fazer isso é combinar as funções integradas range e len:

```python
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```

Este loop percorre a lista e atualiza cada elemento. len retorna o número de elementos na lista. range retorna uma lista de índices de 0 a n-1, em que n é o comprimento da lista. Cada vez que passa pelo loop, i recebe o índice do próximo elemento. A instrução de atribuição no corpo usa i para ler o valor antigo do elemento e atribuir o novo valor.

Um loop for que passe por uma lista vazia nunca executa o corpo:

```python
for x in []:
    print('This never happens.')
```

Apesar de uma lista poder conter outra lista, a lista aninhada ainda conta como um único elemento. O comprimento desta lista é quatro:

```python
['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
```

## 10.4 - Operações com listas

O operador `+` concatena listas:

```python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> c
[1, 2, 3, 4, 5, 6]
```

O operador `*` repete a lista um dado número de vezes:

```python
>>> [0] * 4
[0, 0, 0, 0]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

O primeiro exemplo repete `[0]` quatro vezes. O segundo exemplo repete a lista `[1, 2, 3]` três vezes.

## 10.5 - Fatias de listas

O operador de fatiamento também funciona com listas:

```python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']
```

Se você omitir o primeiro índice, a fatia começa no início. Se você omitir o segundo, a fatia vai até o final. Se você omitir ambos, a fatia é uma cópia da lista inteira.

```python
>>> t[:]
['a', 'b', 'c', 'd', 'e', 'f']
```

Como as listas são mutáveis, pode ser útil fazer uma cópia antes de executar operações que as alterem.

Um operador de fatia à esquerda de uma atribuição pode atualizar vários elementos:

```python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> t
['a', 'x', 'y', 'd', 'e', 'f']
```

## 10.6 - Métodos de listas

O Python oferece métodos que operam em listas. Por exemplo, `append` adiciona um novo elemento ao fim de uma lista:

```python
>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> t
['a', 'b', 'c', 'd']
```

`extend` toma uma lista como argumento e adiciona todos os elementos:

```python
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> t1
['a', 'b', 'c', 'd', 'e']
```

Este exemplo deixa t2 intocado.

`sort` classifica os elementos da lista em ordem ascendente:

```python
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> t
['a', 'b', 'c', 'd', 'e']
```

A maior parte dos métodos de listas são nulos; eles alteram a lista e retornam None. Se você escrever t = t.sort() por acidente, ficará desapontado com o resultado.

## 10.7 - Mapeamento, filtragem e redução

Para somar o total de todos os números em uma lista, você pode usar um loop como esse:

```python
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total
```

`total` é inicializado com 0. Cada vez que o programa passa pelo loop, `x` recebe um elemento da lista. O operador `+=` oferece uma forma curta de atualizar uma variável. Esta instrução de atribuição aumentada,

```python
total += x
```
é equivalente a

```python
total = total + x
```
No decorrer da execução do loop, `total` acumula a soma dos elementos; uma variável usada desta forma às vezes é chamada de acumuladora.

Somar todos elementos de uma lista é uma operação tão comum que o Python a oferece como uma função integrada, `sum`:

```python
>>> t = [1, 2, 3]
>>> sum(t)
6
```

Uma operação como essa, que combina uma sequência de elementos em um único valor, às vezes é chamada de redução.

Algumas vezes você quer percorrer uma lista enquanto cria outra. Por exemplo, a função seguinte recebe uma lista de strings e retorna uma nova lista que contém strings com letras maiúsculas:

```python
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
```

`res` é inicializado com uma lista vazia; cada vez que o programa passa pelo loop, acrescentamos o próximo elemento. Então `res` é outro tipo de acumulador.

Uma operação como `capitalize_all` às vezes é chamada de mapeamento porque ela “mapeia” uma função (nesse caso o método `capitalize`) sobre cada um dos elementos em uma sequência.

Outra operação comum é selecionar alguns dos elementos de uma lista e retornar uma sublista. Por exemplo, a função seguinte recebe uma lista de strings e retorna uma lista que contém apenas strings em letra maiúscula:

```python
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
```

`isupper` é um método de string que retorna True se a string contiver apenas letras maiúsculas.

Uma operação como `only_upper` é chamada de filtragem porque filtra alguns dos elementos e desconsidera outros.

As operações de lista mais comuns podem ser expressas como uma combinação de mapeamento, filtragem e redução.

## 10.8 - Como excluir elementos

Há várias formas de excluir elementos de uma lista. Se souber o índice do elemento que procura, você pode usar `pop`:

```python
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> t
['a', 'c']
>>> x
'b'
```

`pop` altera a lista e retorna o elemento que foi excluído. Se você não incluir um índice, ele exclui e retorna o último elemento.

Se não precisar do valor removido, você pode usar a instrução `del`:

```python
>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> t
['a', 'c']
```

Se souber o elemento que quer excluir (mas não o índice), você pode usar `remove`:

```python
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> t
['a', 'c']
```
O valor devolvido por `remove` é `None`.

Para remover mais de um elemento, você pode usar `del` com um índice de fatia:

```python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del t[1:5]
>>> t
['a', 'f']
```

Como sempre, a fatia seleciona todos os elementos até, mas não incluindo, o segundo índice.

## 10.9 - Listas e strings

Uma string é uma sequência de caracteres e uma lista é uma sequência de valores, mas uma lista de caracteres não é a mesma coisa que uma string. Para converter uma string em uma lista de caracteres, você pode usar list:

```python
>>> s = 'spam'
>>> t = list(s)
>>> t
['s', 'p', 'a', 'm']
```

Como `list` é o nome de uma função integrada, você deve evitar usá-lo como nome de variável. Também evito usar `l` porque parece demais com 1. É por isso que uso `t`.

A função `list` quebra uma string em letras individuais. Se você quiser quebrar uma string em palavras, você pode usar o método `split`:


```python
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> t
['pining', 'for', 'the', 'fjords']
```

Um argumento opcional chamado delimiter especifica quais caracteres podem ser usados para demonstrar os limites das palavras. O exemplo seguinte usa um hífen como delimitador:

```python
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> t = s.split(delimiter)
>>> t
['spam', 'spam', 'spam']
```

`join` é o contrário de `split`. Ele toma uma lista de strings e concatena os elementos. `join` é um método de string, então é preciso invocá-lo no delimitador e passar a lista como parâmetro:

```python
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> s = delimiter.join(t)
>>> s
'pining for the fjords'
```

Nesse caso, o delimitador é um caractere de espaço, então `join` coloca um espaço entre as palavras. Para concatenar strings sem espaços, você pode usar a string vazia `''`, como delimitador.

<a id="sec:10.10"></a>
## 10.10 - Objetos e valores

Se executarmos essas instruções de atribuição:

```python
a = 'banana'
b = 'banana'
```

Sabemos que a e b se referem a uma string, mas não sabemos se elas se referem à mesma string. Há dois estados possíveis, mostrados na Figura 10.2.

![Figura 10.2 – Diagramas de estado possíveis com duas variáveis.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1002.png)
<br>_Figura 10.2 – Diagramas de estado possíveis com duas variáveis._

Em um caso, a e b se referem a dois objetos diferentes que têm o mesmo valor. No segundo caso, elas se referem ao mesmo objeto.

Para verificar se duas variáveis se referem ao mesmo objeto, você pode usar o operador is:


```python
>>> a = 'banana'
>>> b = 'banana'
>>> a is b
True
```

Nesse exemplo, o Python criou apenas um objeto de string e tanto a quanto b se referem a ele. Mas quando você cria duas listas, você tem dois objetos:


```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
```

Então o diagrama de estado fica igual ao da Figura 10.3.

![Figura 10.3 – Diagrama de estado com variáveis associadas a listas distintas, de mesmo valor.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1003.png)
<br>_Figura 10.3 – Diagrama de estado com variáveis associadas a listas distintas, de mesmo valor._

Nesse caso, diríamos que as duas listas são equivalentes, porque elas têm os mesmos elementos, mas não idênticas, porque elas não são o mesmo objeto. Se dois objetos forem idênticos, eles também são equivalentes, mas se eles forem equivalentes, não são necessariamente idênticos.

Até agora, temos usado “objeto” e “valor” de forma intercambiável, mas é mais exato dizer que um objeto tem um valor. Se avaliar [1, 2, 3], você tem um objeto de lista cujo valor é uma sequência de números inteiros. Se outra lista tem os mesmos elementos, dizemos que tem o mesmo valor, mas não é o mesmo objeto.

## 10.11 - Alias

Se a se refere a um objeto e você atribui b = a, então ambas as variáveis se referem ao mesmo objeto.

```python
>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
```
O diagrama de estado ficará igual à Figura 10.4.

![Figura 10.4 – Diagrama de estado com duas variáveis associadas à mesma lista.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1004.png)
<br>_Figura 10.4 – Diagrama de estado com duas variáveis associadas à mesma lista._

A associação de uma variável com um objeto é chamada de referência. Neste exemplo, há duas referências ao mesmo objeto.

Um objeto com mais de uma referência tem mais de um nome, então dizemos que o objeto tem um alias.

Se o objeto com alias é mutável, alterações feitas em um alias afetam o outro também.


```python
>>> b[0] = 42
>>> a
[42, 2, 3]
```

Apesar de esse comportamento poder ser útil, ele é passível de erros. Em geral, é mais seguro evitar usar alias ao trabalhar com objetos mutáveis.

Para objetos imutáveis como strings, usar alias não é um problema tão grande. Neste exemplo:

```python
a = 'banana'
b = 'banana'
```

Quase nunca faz diferença se a e b se referem à mesma string ou não.

## 10.12 - Argumentos de listas

Ao passar uma lista a uma função, a função recebe uma referência à lista. Se a função alterar a lista, quem faz a chamada vê a mudança. Por exemplo, delete\_head remove o primeiro elemento de uma lista:



```python
def delete_head(t):
    del t[0]
Ela é usada assim:
>>> letters = ['a', 'b', 'c']
>>> delete_head(letters)
>>> letters
['b', 'c']
```

O parâmetro t e a variável letters são alias para o mesmo objeto. O diagrama da pilha fica igual ao da Figura 10.5.

![Figura 10.5 – Diagrama da pilha: `__main__` e `delete_head` compartilham referências à mesma lista.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1005.png)
<br>_Figura 10.5 – Diagrama da pilha:_ `__main__` _e_ `delete_head` _compartilham referências à mesma lista._

Como a lista é compartilhada por dois frames, desenhei-a entre eles.

É importante distinguir entre operações que alteram listas e operações que criam novas listas. Por exemplo, o método `append` altera a lista, mas o operador `+` cria uma nova lista:

```python
>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> t1
[1, 2, 3]
>>> t2
None
```

Note que `append` altera a lista e retorna `None` (na realidade, o console do Python omite o `None` da saída, mas você pode conferir usando `t2 is None`).

```python
>>> t3 = t1 + [4]
>>> t1
[1, 2, 3]
>>> t3
[1, 2, 3, 4]
>>> t1
```

O operador `+` cria uma nova lista e deixa a lista original inalterada.

Essa diferença é importante quando você escreve funções que devem alterar listas. Por exemplo, esta função não remove a cabeça de uma lista:

```python
def bad_delete_head(t):
    t = t[1:]              # ERRADO!
```

O operador de fatia cria uma nova lista e a atribuição faz t se referir a ela, mas isso não afeta quem faz chamada.

```python
>>> t4 = [1, 2, 3]
>>> bad_delete_head(t4)
>>> t4
[1, 2, 3]
```

No início de `bad_delete_head`, t e t4 se referem à mesma lista. No final, t se refere a uma nova lista, mas t4 ainda se refere à lista original, inalterada.

Uma alternativa é escrever uma função que crie e retorne uma nova lista. Por exemplo, `tail` retorna tudo, exceto o primeiro elemento de uma lista:

```python
def tail(t):
    return t[1:]
```

Esta função deixa a lista original inalterada. Ela é usada assim:

```python
>>> letters = ['a', 'b', 'c']
>>> rest = tail(letters)
>>> rest
['b', 'c']
```

## 10.13 - Depuração

O uso descuidado de listas (e de outros objetos mutáveis) pode levar a longas horas de depuração. Aqui estão algumas armadilhas comuns e formas de evitá-las:

1. A maior parte dos métodos de listas alteram o argumento e retornam None. Isto é o oposto dos métodos de strings, que retornam uma nova string e deixam a original intocada.

        Se você está acostumado a escrever código de strings desta forma:

```python
        word = word.strip()
```

        É tentador escrever código de listas como este:

```python
        t = t.sort()            # ERRADO!
```

        Como sort retorna None, a próxima operação que você executar com t provavelmente vai falhar.

        Antes de usar métodos e operadores de listas, você deve ler a documentação com cuidado e testá-los no modo interativo.


2. Escolha o termo e fique com ele.

        Parte do problema com listas é que há muitas formas de fazer coisas com elas. Por exemplo, para remover um elemento de uma lista você pode usar pop, remove, del ou até uma atribuição de fatia.

        Para adicionar um elemento você pode usar o método append ou o operador +. Assumindo que t é uma lista e x é um elemento da lista, isto está correto:

```python
        t.append(x)
        t = t + [x]
        t += [x]
        E isto está errado:
        t.append([x])          # ERRADO!
        t = t.append(x)        # ERRADO!
        t + [x]                # ERRADO!
        t = t + x              # ERRADO!
```

        Experimente cada um desses exemplos no modo interativo para conferir se você entendeu o que fazem. Note que apenas o último causa um erro de tempo de execução; os outros três são legais, mas eles fazem a coisa errada.

3. Faça cópias para evitar o uso de alias.

        Se quiser usar um método como sort, que altera o argumento, mas precisa manter a lista original, você pode fazer uma cópia:



```python
        >>> t = [3, 1, 2]
        >>> t2 = t[:]
        >>> t2.sort()
        >>> t
        [3, 1, 2]
        >>> t2
        [1, 2, 3]
```

        Neste exemplo você poderia usar também a função integrada sorted, que retorna uma nova lista classificada e deixa a original intocada.



```python
        >>> t2 = sorted(t)
        >>> t
        [3, 1, 2]
        >>> t2
        [1, 2, 3]
```

## 10.14 - Glossário

<dl>
<dt><a id="glos:lista" href="#termo:lista">lista</a></dt>
<dd>Uma sequência de valores.</dd>

<dt><a id="glos:elemento" href="#termo:elemento">elemento</a></dt>
<dd>Um dos valores em uma lista (ou outra sequência), também chamado de item.</dd>

<dt><a id="glos:lista aninhada" href="#termo:lista aninhada">lista aninhada</a></dt>
<dd>Uma lista que é um elemento de outra lista.</dd>

<dt><a id="glos:acumuladora" href="#termo:acumuladora">acumuladora</a></dt>
<dd>Variável usada em um loop para adicionar ou acumular um resultado.</dd>

<dt><a id="glos:atribuição aumentada" href="#termo:atribuição aumentada">atribuição aumentada</a></dt>
<dd>Instrução que atualiza o valor de uma variável usando um operador como +=.</dd>

<dt><a id="glos:redução" href="#termo:redução">redução</a></dt>
<dd>Padrão de processamento que atravessa uma sequência e acumula os elementos em um único resultado.</dd>

<dt><a id="glos:mapeamento" href="#termo:mapeamento">mapeamento</a></dt>
<dd>Padrão de processamento que atravessa uma sequência e executa uma operação em cada elemento.</dd>

<dt><a id="glos:filtragem" href="#termo:filtragem">filtragem</a></dt>
<dd>Padrão de processamento que atravessa uma lista e seleciona os elementos que satisfazem algum critério.</dd>

<dt><a id="glos:objeto" href="#termo:objeto">objeto</a></dt>
<dd>Algo a que uma variável pode se referir. Um objeto tem um tipo e um valor.</dd>

<dt><a id="glos:equivalente" href="#termo:equivalente">equivalente</a></dt>
<dd>Ter o mesmo valor.</dd>

<dt><a id="glos:idêntico" href="#termo:idêntico">idêntico</a></dt>
<dd>Ser o mesmo objeto (o que implica equivalência).</dd>

<dt><a id="glos:referência" href="#termo:referência">referência</a></dt>
<dd>Associação entre uma variável e seu valor.</dd>

<dt><a id="glos:alias" href="#termo:alias">alias</a></dt>
<dd>Uma circunstância onde duas ou mais variáveis se referem ao mesmo objeto.</dd>

<dt><a id="glos:delimitador" href="#termo:delimitador">delimitador</a></dt>
<dd>Um caractere ou uma string usada para indicar onde uma string deve ser dividida.</dd>

</dl>

## 10.15 - Exercícios

Você pode baixar as soluções para estes exercícios em https://github.com/AllenDowney/ThinkPython2/raw/master/code/list\_exercises.py.

### Exercício 10.1

Escreva uma função chamada `nested_sum` que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo:

```python
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
```

### Exercício 10.2

Escreva uma função chamada cumsum que receba uma lista de números e retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original. Por exemplo:

```python
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
```

### Exercício 10.3

Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com todos os elementos originais, exceto os primeiros e os últimos elementos. Por exemplo:

```python
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
```

### Exercício 10.4

Escreva uma função chamada chop que tome uma lista alterando-a para remover o primeiro e o último elementos, e retorne None. Por exemplo:

```python
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
```

### Exercício 10.5

Escreva uma função chamada is\_sorted que tome uma lista como parâmetro e retorne True se a lista estiver classificada em ordem ascendente, e False se não for o caso. Por exemplo:

```python
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
```

### Exercício 10.6

Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra. Escreva uma função chamada is\_anagram que tome duas strings e retorne True se forem anagramas.

### Exercício 10.7

Escreva uma função chamada has\_duplicates que tome uma lista e retorne True se houver algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.

### Exercício 10.8

Este exercício pertence ao assim chamado Paradoxo de aniversário, sobre o qual você pode ler em http://en.wikipedia.org/wiki/Birthday\_paradox.

Se há 23 alunos na sua sala, quais são as chances de dois deles fazerem aniversário no mesmo dia? Você pode estimar esta probabilidade gerando amostras aleatórias de 23 dias de aniversário e verificando as correspondências. Dica: você pode gerar aniversários aleatórios com a função randint no módulo random.

Se quiser, você pode baixar minha solução em https://github.com/AllenDowney/ThinkPython2/raw/master/code/birthday.py.

### Exercício 10.9

Escreva uma função que leia o arquivo words.txt e construa uma lista com um elemento por palavra. Escreva duas versões desta função, uma usando o método append e outra usando a expressão `t = t + [x]`. Qual leva mais tempo para ser executada? Por quê?

Solução: https://github.com/AllenDowney/ThinkPython2/raw/master/code/wordlist.py.


### Exercício 10.10

Para verificar se uma palavra está na lista de palavras, você pode usar o operador in, mas isso seria lento porque pesquisaria as palavras em ordem.

Como as palavras estão em ordem alfabética, podemos acelerar as coisas com uma busca por bisseção (também conhecida como pesquisa binária), que é semelhante ao que você faz quando procura uma palavra no dicionário. Você começa no meio e verifica se a palavra que está procurando vem antes da palavra no meio da lista. Se for o caso, procura na primeira metade da lista. Se não, procura na segunda metade.

De qualquer forma, você corta o espaço de busca restante pela metade. Se a lista de palavras tiver 113.809 palavras, o programa seguirá uns 17 passos para encontrar a palavra ou concluir que não está lá.

Escreva uma função chamada in\_bisect que receba uma lista ordenada, um valor-alvo e devolva o índice do valor na lista se ele estiver lá, ou None se não estiver.

Ou você pode ler a documentação do módulo bisect e usá-lo!

Solução: https://github.com/AllenDowney/ThinkPython2/raw/master/code/inlist.py.

### Exercício 10.11

Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva um programa que encontre todos os pares inversos na lista de palavras.

Solução: https://github.com/AllenDowney/ThinkPython2/raw/master/code/reverse_pair.py.

### Exercício 10.12

Duas palavras “interligam-se” quando, ao tomarmos letras alternadas de cada uma, formamos uma palavra nova. Por exemplo, “shoe” e “cold” interligam-se para formar “schooled”.

Solução: https://github.com/AllenDowney/ThinkPython2/raw/master/code/interlock.py. Crédito: este exercício foi inspirado por um exemplo em http://puzzlers.org.

1. Escreva um programa que encontre todos os pares de palavras que se interligam. Dica: não enumere todos os pares!

2. Você pode encontrar palavras que sejam interligadas de três em três; isto é, cada terceira letra forma uma palavra, começando da primeira, segunda ou terceira?
