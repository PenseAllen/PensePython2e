# Capítulo 11: Dicionários

Este capítulo apresenta outro tipo integrado chamado dicionário. Dicionários são um dos melhores recursos do Python; eles são os blocos de montar de muitos algoritmos eficientes e elegantes.

## 11.1 - Um dicionário é um mapeamento

Um dicionário se parece com uma lista, mas é mais geral. Em uma lista, os índices têm que ser números inteiros; em um dicionário, eles podem ser de (quase) qualquer tipo.

Um dicionário contém uma coleção de índices, que se chamam chaves e uma coleção de valores. Cada chave é associada com um único valor. A associação de uma chave e um valor chama-se par chave-valor ou item.

Em linguagem matemática, um dicionário representa um mapeamento de chaves a valores, para que você possa dizer que cada chave “mostra o mapa a” um valor. Como exemplo, vamos construir um dicionário que faz o mapa de palavras do inglês ao espanhol, portanto as chaves e os valores são todos strings.

A função dict cria um novo dicionário sem itens. Como dict é o nome de uma função integrada, você deve evitar usá-lo como nome de variável.


```python
>>> eng2sp = dict()
>>> eng2sp
{}
```

As chaves {} representam um dicionário vazio. Para acrescentar itens ao dicionário, você pode usar colchetes:

```python
>>> eng2sp['one'] = 'uno'
```

Esta linha cria um item que mapeia da chave 'one' ao valor 'uno'. Se imprimirmos o dicionário novamente, vemos um par chave-valor com dois pontos entre a chave e o valor:

```python
>>> eng2sp
{'one': 'uno'}
```

Este formato de saída também é um formato de entrada. Por exemplo, você pode criar um dicionário com três itens:

```python
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
```

Porém, se exibir `eng2sp`, pode se surpreender:

```python
>>> eng2sp
{'one': 'uno', 'three': 'tres', 'two': 'dos'}
```

A ordem dos pares chave-valor pode não ser a mesma. Se você digitar o mesmo exemplo no seu computador, pode receber um resultado diferente. Em geral, a ordem dos itens em um dicionário é imprevisível.

No entanto, isso não é um problema porque os elementos de um dicionário nunca são indexados com índices de números inteiros. Em vez disso, você usa as chaves para procurar os valores correspondentes:

```python
>>> eng2sp['two']
'dos'
```

A chave `'two'` sempre mapeia ao valor `'dos'`, assim a ordem dos itens não importa.

Se a chave não estiver no dicionário, você recebe uma exceção:

```python
>>> eng2sp['four']
KeyError: 'four'
```

A função `len` é compatível com dicionários; ela devolve o número de pares chave-valor:

```python
>>> len(eng2sp)
3
```

O operador `in` funciona em dicionários também; ele acusa se algo aparece como chave no dicionário (aparecer como valor não é o suficiente).

```python
>>> 'one' in eng2sp
True
>>> 'uno' in eng2sp
False
```

Para ver se algo aparece como um valor em um dicionário, você pode usar o método `values`, que devolve uma coleção de valores, e então usar o operador `in`:

```python
>>> vals = eng2sp.values()
>>> 'uno' in vals
True
```

O operador `in` usa algoritmos diferentes para listas e dicionários. Para listas, ele procura os elementos da lista em ordem, como descrito em “Busca”, na página 123. Conforme a lista torna-se mais longa, o tempo de busca também fica proporcionalmente mais longo.

Para dicionários, o Python usa um algoritmo chamado hashtable (tabela de dispersão), que tem uma propriedade notável: o operador `in` leva praticamente o mesmo tempo na busca, não importa quantos itens estejam no dicionário. Eu explico como isso é possível em “Hashtables”, na página 302, mas a explicação pode não fazer sentido até que você tenha lido mais alguns capítulos.

## 11.2 - Um dicionário como uma coleção de contadores

Suponha que você receba uma string e queira contar quantas vezes cada letra aparece nela. Há vários modos de fazer isso:

1. Você pode criar 26 variáveis, uma para cada letra do alfabeto. Então pode atravessar a string e, para cada caractere, incrementar o contador correspondente, provavelmente usando uma condicional encadeada.

2. Você pode criar uma lista com 26 elementos. Então pode converter cada caractere em um número (com a função integrada ord), usar o número como índice na lista e incrementar o respectivo contador.

3. Você pode criar um dicionário com caracteres como chaves e contadores como valores correspondentes. Na primeira vez que visse um caractere, você acrescentaria um item ao dicionário. Depois disso, incrementaria o valor de um item existente.

Cada uma dessas opções executa o mesmo cálculo, mas o implementa de forma diferente.

Uma implementação é um modo de executar um cálculo; algumas implementações são melhores que outras. Por exemplo, uma vantagem da implementação de dicionários é que não precisamos saber de antemão quais letras aparecem na string e só é preciso criar espaço para as letras que realmente venham a aparecer.

O código poderia ser assim:

```python
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
```

O nome da função é `histogram`, um termo estatístico para uma coleção de contadores (ou frequências).

A primeira linha da função cria um dicionário vazio. O loop for atravessa a string. Cada vez que passa pelo loop, se o caractere c não estiver no dicionário, criamos um item com a chave c e o valor inicial 1 (pois já vimos esta letra uma vez). Se o c já estiver no dicionário, incrementamos d [c].

Funciona assim:

```python
>>> h = histogram('brontosaurus')
>>> h
{'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
```

O histograma indica que as letras 'a' e 'b' aparecem uma vez; 'o' aparece duas vezes, e assim por diante.

Os dicionários têm um método chamado `get`, que toma uma chave e um valor padrão. Se a chave aparecer no dicionário, `get` retorna o valor correspondente; se não for o caso, ele retorna o valor padrão. Por exemplo:

```python
>>> h = histogram('a')
>>> h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('b', 0)
0
```

Como exercício, use o `get` para escrever a função `histogram` de forma mais concisa. Tente eliminar a instrução `if`.

## 11.3 - Loop e dicionários

Se usar um dicionário em uma instrução `for`, ela percorre as chaves do dicionário. Por exemplo, `print_hist` exibe cada chave e o valor correspondente:

```python
def print_hist(h):
    for c in h:
        print(c, h[c])
```

Isso é o que aparece:

```python
>>> h = histogram('parrot')
>>> print_hist(h)
a 1
p 1
r 2
t 1
o 1
```

Novamente, as chaves não estão em nenhuma ordem determinada. Para atravessar as chaves em ordem ascendente, você pode usar a função integrada `sorted`:

```python
>>> for key in sorted(h):
...     print(key, h[key])
a 1
o 1
p 1
r 2
t 1
```

## 11.4 - Busca reversa

Considerando um dicionário `d` e uma chave `k`, é fácil encontrar o valor correspondente `v = d [k]`. Esta operação chama-se busca.

Mas e se você tiver `v` e quiser encontrar `k`? Você tem dois problemas: em primeiro lugar, pode haver mais de uma chave que esteja mapeada ao valor `v`. Dependendo da aplicação, quem sabe você pode escolher um, ou talvez tenha de fazer uma lista que contenha todos eles. Em segundo lugar, não há sintaxe simples para fazer uma busca reversa; é preciso procurar.

Aqui está uma função que recebe um valor e retorna a primeira chave mapeada ao valor dado:

```python
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()
```

Essa função é mais um exemplo do padrão de busca, mas usa um recurso que ainda não tínhamos visto: `raise`. A instrução `raise` causa uma exceção; neste caso, causa um `LookupError`, que é uma exceção integrada, usada para indicar que uma operação de busca falhou.

Se chegarmos ao fim do loop significa que `v` não aparece no dicionário como um valor, portanto apresentaremos uma exceção.

Aqui está um exemplo de uma busca reversa bem sucedida:

```python
>>> h = histogram('parrot')
>>> k = reverse_lookup(h, 2)
>>> k
'r'
```

E uma mal sucedida:

```python
>>> k = reverse_lookup(h, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in reverse_lookup
LookupError
```

O efeito causado por você ao apresentar uma exceção é igual ao causado pelo Python quando faz o mesmo: ele exibe um traceback e uma mensagem de erro.

A instrução raise pode receber uma mensagem de erro detalhada como argumento opcional. Por exemplo:

```python
>>> raise LookupError('value does not appear in the dictionary')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
LookupError: value does not appear in the dictionary
```

Uma busca reversa é muito mais lenta que uma busca no sentido normal; se for preciso fazê-lo muitas vezes, ou se o dicionário ficar muito grande, o desempenho do seu programa será prejudicado.

## 11.5 - Dicionários e listas

As listas podem aparecer como valores em um dicionário. Por exemplo, se você receber um dicionário que mapeie letras e frequências, é uma boa ideia invertê-lo; isto é, crie um dicionário que mapeie de frequências a letras. Como pode haver várias letras com a mesma frequência, cada valor no dicionário invertido deve ser uma lista de letras.

Aqui está uma função que inverte um dicionário:

```python
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
```

Cada vez que o programa passar pelo loop, a key recebe uma chave de d e val recebe o valor correspondente. Se val não estiver em inverse significa que não foi vista antes, então criamos um item e o inicializamos com um item avulso (em inglês, singleton, uma lista que contém um único elemento). Se não for o caso é porque vimos esse valor antes, então acrescentamos a chave correspondente à lista.

Aqui está um exemplo:

```python
>>> hist = histogram('parrot')
>>> hist
{'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
>>> inverse = invert_dict(hist)
>>> inverse
{1: ['a', 'p', 't', 'o'], 2: ['r']}
```

A Figura 11.1 é um diagrama de estado mostrando hist e inverse. Um dicionário é representado como uma caixa com o tipo dict acima dela e os pares chave-valor no interior. Se os valores forem números inteiros, de ponto flutuante ou strings, desenho-os dentro da caixa, mas normalmente prefiro desenhar listas do lado de fora, para manter o diagrama simples.

![Figura 11.1 – Diagrama de estado de um dicionário e seu inverso.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1101.png)
<br>_Figura 11.1 – Diagrama de estado de um dicionário e seu inverso._

As listas podem ser valores em um dicionário, como mostra este exemplo, mas não podem ser chaves. Isso é o que acontece se você tentar:

```python
>>> t = [1, 2, 3]
>>> d = dict()
>>> d[t] = 'oops'
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: list objects are unhashable
```

Já mencionei que um dicionário é implementado usando uma hashtable e isso significa que é preciso que as chaves possam ser hashable (que seja possível computar seu hash, e que este valor de hash seja imutável).

`hash` é uma função que recebe um valor (de qualquer tipo) e devolve um número inteiro. Dicionários usam esses números inteiros, chamados valores `hash`, para guardar e buscar pares chave-valor.

Este sistema funciona perfeitamente se as chaves forem imutáveis. Porém, se as chaves são mutáveis, como listas, coisas ruins acontecem. Por exemplo, quando você cria um par chave-valor, o Python guarda a chave na posição correspondente. Se você modificar a chave e então guardá-la novamente, ela iria para uma posição diferente. Nesse caso, você poderia ter duas entradas para a mesma chave, ou pode não conseguir encontrar uma chave. De qualquer forma, o dicionário não funcionaria corretamente.

É por isso que as chaves têm de ser hashable, e tipos mutáveis como listas, não são. A forma mais simples de resolver esta limitação é usar tuplas, que serão vistas no próximo capítulo.

Como os dicionários são mutáveis, eles não podem ser usados como chaves, mas podem ser usados como valores.

## 11.6 - Memos

Se usou a função de fibonacci em “Mais um exemplo”, na página 101, pode ter notado que quanto maior o argumento dado mais tempo a função leva para ser executada. Além disso, o tempo de execução aumenta rapidamente.

Para entender por que, considere a Figura 11.2, que mostra o gráfico de chamada de `fibonacci` com n=4.

![Figura 11.2 – Gráfico de chamada para fibonacci.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1102.png)
<br>_Figura 11.2 – Gráfico de chamada para_ `fibonacci`.

Um gráfico de chamada mostra um conjunto de frames de função, com linhas que unem cada frame aos frames das funções que chama. Na parte de cima do gráfico, `fibonacci` com `n=4` chama `fibonacci` com `n=3` e `n=2`. Por sua vez, `fibonacci` com `n=3` chama `fibonacci` com `n=2` e `n=1`. E assim por diante.

Conte quantas vezes `fibonacci(0)` e `fibonacci(1)` são chamadas. Essa é uma solução ineficiente para o problema, e piora conforme o argumento se torna maior.

Uma solução é acompanhar os valores que já foram calculados, guardando-os em um dicionário. Um valor calculado anteriormente que é guardado para uso posterior é chamado de memo. Aqui está uma versão com memos de `fibonacci`:

```python
known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
```

`known` é um dicionário que monitora os números de Fibonacci que já conhecemos. Começa com dois itens: 0 mapeia a 0 e 1 mapeia a 1.

Sempre que `fibonacci` é chamada, ela verifica `known`. Se o resultado já estiver lá, pode voltar imediatamente. Se não for o caso, é preciso calcular o novo valor, acrescentá-lo ao dicionário e devolvê-lo.

Se você executar essa versão de `fibonacci` e a comparar com a original, descobrirá que é muito mais rápida.

## 11.7 - Variáveis globais

No exemplo anterior, known é criada fora da função, então pertence ao frame especial chamado `__main__`. As variáveis em `__main__` às vezes são chamadas de globais, porque podem ser acessadas de qualquer função. Em contraste com as variáveis locais, que desaparecem quando sua função termina, as variáveis globais persistem de uma chamada da função à seguinte.

É comum usar variáveis globais para `flags`; isto é, variáveis booleanas que indicam (“flag”) se uma condição é verdadeira. Por exemplo, alguns programas usam um `flag` denominado verbose para controlar o nível de detalhe da saída:

```python
verbose = True
def example1():
    if verbose:
        print('Running example1')
```

Se tentar reatribuir uma variável global, você pode se surpreender. O próximo exemplo mostra como acompanhar se a função foi chamada:

```python
been_called = False
def example2():
    been_called = True        # ERRADO
```

Porém, se executá-la, você verá que o valor de `been_called` não se altera. O problema é que `example2` cria uma nova variável local chamada `been_called`. A variável local some quando a função termina e não tem efeito sobre a variável global.

Para reatribuir uma variável global dentro de uma função é preciso declarar a variável como global antes de usá-la:

```python
been_called = False
def example2():
    global been_called
    been_called = True
```

A instrução `global` diz ao interpretador algo como “Nesta função, quando digo `been_called`, estou falando da variável global; não crie uma local”.

Aqui está um exemplo que tenta atualizar uma variável global:

```python
count = 0
def example3():
    count = count + 1        # ERRADO
```

Se executá-la, você recebe:

```python
UnboundLocalError: local variable 'count' referenced before assignment
```

O Python supõe que `count` seja local, e dentro desta suposição, a variável está sendo lida antes de ser escrita. A solução, mais uma vez, é declarar `count` como global:

```python
def example3():
    global count
    count += 1
```

Se uma variável global se referir a um valor mutável, você pode alterar o valor sem declarar a variável:

```python
known = {0:0, 1:1}
def example4():
    known[2] = 1
```

Então você pode adicionar, retirar e substituir elementos de uma lista global ou dicionário, mas se quiser reatribuir a variável, precisa declará-la:

```python
def example5():
    global known
    known = dict()
```

As variáveis globais podem ser úteis, mas se você tiver muitas delas e alterá-las com frequência, isso poderá dificultar a depuração do programa.

## 11.8 - Depuração

Ao trabalhar com conjuntos de dados maiores, depurar exibindo e verificando a saída à mão pode ser trabalhoso. Aqui estão algumas sugestões para depurar grandes conjuntos de dados:

<dl>

<dt>Reduza a entrada</dt>

  <dd>Se for possível, reduza o tamanho do conjunto de dados. Por exemplo, se o programa lê um arquivo de texto, comece com apenas as 10 primeiras linhas, ou com o menor exemplo que puder encontrar. Você pode editar os próprios arquivos ou alterar o programa para que leia só as primeiras n linhas (é melhor).</dd>

  <dd>Se houver um erro, você pode reduzir n ao menor valor que manifeste o erro, e então aumentá-lo gradativamente até encontrar e corrigir o erro.</dd>

<dt>Verifique os resumos e tipos</dt>

  <dd>Em vez de imprimir e verificar o conjunto de dados inteiro, pense em exibir resumos dos dados: por exemplo, o número de itens em um dicionário ou o total de uma lista de números.</dd>

  <dd>Uma causa comum de erros em tempo de execução são valores de tipo incompatível. Para depurar essa espécie de erro, muitas vezes basta exibir o tipo de um valor.</dd>

<dt>Crie autoverificações</dt>

  <dd>É possível escrever o código para verificar erros automaticamente. Por exemplo, se estiver calculando a média de uma lista de números, você pode verificar se o resultado não é mais alto que o maior elemento da lista ou mais baixo que o menor. Isso é chamado de “verificação de sanidade” porque descobre resultados “insanos”.</dd>

  <dd>Outro tipo de verificação compara os resultados de dois cálculos diferentes para ver se são consistentes. Isso é chamado de “verificação de consistência”.</dd>

<dt>Formate a saída</dt>

  <dd>A formatação da saída para depuração pode facilitar a busca de erros. Vimos um exemplo em “Depuração”, na página 172. O módulo `pprint` apresenta uma função `pprint` que exibe tipos integrados em um formato mais legível para humanos (`pprint` é a abreviação de “pretty print” (bela exibição)).</dd>

</dl>

Reforçando, o tempo que você passar construindo o scaffolding (o andaime) pode reduzir o tempo de depuração.


## 11.9 - Glossário

<dl>
<dt><a id="glos:mapeamento" href="#termo:mapeamento">mapeamento</a></dt>
<dd>Relação na qual cada elemento de um conjunto corresponde a um elemento de outro conjunto.</dd>

<dt><a id="glos:dicionário" href="#termo:dicionário">dicionário</a></dt>
<dd>Mapeamento de chaves aos seus valores correspondentes.</dd>

<dt><a id="glos:par chave-valor" href="#termo:par chave-valor">par chave-valor</a></dt>
<dd>Representação do mapeamento de uma chave a um valor.</dd>

<dt><a id="glos:item" href="#termo:item">item</a></dt>
<dd>Em um dicionário, outro nome para um par chave-valor.</dd>

<dt><a id="glos:chave" href="#termo:chave">chave</a></dt>
<dd>Objeto que aparece em um dicionário como a primeira parte de um par chave-valor.</dd>

<dt><a id="glos:valor" href="#termo:valor">valor</a></dt>
<dd>Objeto que aparece em um dicionário como a segunda parte de um par chave-valor. Isso é mais específico que o nosso uso anterior da palavra “valor”.</dd>

<dt><a id="glos:implementação" href="#termo:implementação">implementação</a></dt>
<dd>Uma forma de executar um cálculo.</dd>

<dt><a id="glos:hashtable" href="#termo:hashtable">hashtable</a></dt>
<dd>Algoritmo usado para implementar dicionários de Python.</dd>

<dt><a id="glos:função hash" href="#termo:função hash">função hash</a></dt>
<dd>Função usada por uma hashtable para calcular a posição de uma chave.</dd>

<dt><a id="glos:hashable" href="#termo:hashable">hashable</a></dt>
<dd>Um tipo que tem uma função hash. Tipos imutáveis como números inteiros, de ponto flutuante e strings são hashable; tipos mutáveis, como listas e dicionários, não são.</dd>

<dt><a id="glos:busca" href="#termo:busca">busca</a></dt>
<dd>Operação de dicionário que recebe uma chave e encontra o valor correspondente.</dd>

<dt><a id="glos:busca reversa" href="#termo:busca reversa">busca reversa</a></dt>
<dd>Operação de dicionário que recebe um valor e encontra uma ou várias chaves que o mapeiem.</dd>

<dt><a id="glos:instrução raise" href="#termo:instrução raise">instrução raise</a></dt>
<dd>Instrução que (deliberadamente) causa uma exceção.</dd>

<dt><a id="glos:item avulso (singleton)" href="#termo:item avulso (singleton)">item avulso (singleton)</a></dt>
<dd>Uma lista (ou outra sequência) com um único elemento.</dd>

<dt><a id="glos:gráfico de chamada" href="#termo:gráfico de chamada">gráfico de chamada</a></dt>
<dd>Um diagrama que mostra cada frame criado durante a execução de um programa, com uma flecha apontando quem chama a quem é chamado.</dd>

<dt><a id="glos:memo" href="#termo:memo">memo</a></dt>
<dd>Valor já calculado, guardado para não ter que fazer o mesmo cálculo no futuro.</dd>

<dt><a id="glos:variável global" href="#termo:variável global">variável global</a></dt>
<dd>Variável definida fora de uma função. As variáveis globais podem ser acessadas de qualquer função.</dd>

<dt><a id="glos:instrução global" href="#termo:instrução global">instrução global</a></dt>
<dd>Instrução que declara um nome de variável global.</dd>

<dt><a id="glos:flag" href="#termo:flag">flag</a></dt>
<dd>Variável booleana usada para indicar se uma condição é verdadeira.</dd>

<dt><a id="glos:declaração" href="#termo:declaração">declaração</a></dt>
<dd>Instrução tal como global, que diz ao interpretador algo a respeito de uma variável.</dd>

</dl>

## 11.10 - Exercícios

### Exercício 11.1

Escreva uma função que leia as palavras em words.txt e guarde-as como chaves em um dicionário. Não importa quais são os valores. Então você pode usar o operador in como uma forma rápida de verificar se uma string está no dicionário.

Se fez o Exercício 10.10, você pode comparar a velocidade desta implementação com o operador in de listas e a busca por bisseção.

### Exercício 11.2

Leia a documentação do método de dicionário setdefault e use-o para escrever uma versão mais concisa de invert\_dict.

Solução: http://thinkpython2.com/code/invert_dict.py.

### Exercício 11.3

Memorize a função de Ackermann do Exercício 6.2 e veja se a memorização permite avaliar a função com argumentos maiores. Dica: não.

Solução: http://thinkpython2.com/code/ackermann_memo.py.

### Exercício 11.4

Se fez o Exercício 10.7, você já tem uma função chamada has\_duplicates, que recebe uma lista como parâmetro e retorna True se houver algum objeto que aparece mais de uma vez na lista.

Use um dicionário para escrever uma versão mais rápida e simples de has\_duplicates.

Solução: http://thinkpython2.com/code/has_duplicates.py.

### Exercício 11.5

Duas palavras são “pares rotacionados” se for possível rotacionar um deles e chegar ao outro (ver `rotate_word` no Exercício 8.5).

Escreva um programa que leia uma lista de palavras e encontre todos os pares rotacionados.

Solução: http://thinkpython2.com/code/rotate_pairs.py.

### Exercício 11.6

Aqui está outro quebra-cabeça do programa Car Talk (http://www.cartalk.com/content/puzzlers):

Ele foi enviado por Dan O’Leary. Dan descobriu uma palavra comum, com uma sílaba e cinco letras que tem a seguinte propriedade única. Ao removermos a primeira letra, as letras restantes formam um homófono da palavra original, que é uma palavra que soa exatamente da mesma forma. Substitua a primeira letra, isto é, coloque-a de volta, retire a segunda letra e o resultado é um outro homófono da palavra original. E a pergunta é, qual é a palavra?

Agora vou dar um exemplo que não funciona. Vamos usar a palavra de cinco letras, ‘wrack’ (mover, eliminar). W-R-A-C-K, como na expressão ‘wrack with pain’ (se contorcer de dor). Se eu retirar a primeira letra, sobra uma palavra de quatro letras, ‘R-A-C-K’ (galhada). Como na frase, ‘Holy cow, did you see the rack on that buck! It must have been a nine-pointer!’ (‘Minha nossa, você viu a galhada daquele cervo! Deve ter nove pontas!’). É um homófono perfeito. Se puser o ‘w’ de volta e retirar o ‘r’ em vez disso, sobra a palavra ‘wack’, que é uma palavra de verdade, mas não é um homófono das outras duas palavras.

Mas há pelo menos uma palavra que Dan e eu conhecemos, que produz dois homófonos se você retirar qualquer uma das duas primeiras letras, e duas novas palavras de quatro letras são formadas. A pergunta é, qual é a palavra?

Você pode usar o dicionário do Exercício 11.1 para verificar se uma string está na lista de palavras.

Para verificar se duas palavras são homófonas, você pode usar o Dicionário de pronúncia CMU. Ele pode ser baixado em http://www.speech.cs.cmu.edu/cgi-bin/cmudict ou em http://thinkpython2.com/code/c06d. Você também pode baixar http://thinkpy thon2.com/code/pronounce.py, que tem uma função chamada `read_dictionary`, que lê o dicionário de pronúncia e retorna um dicionário de Python que mapeia cada palavra a uma string que descreve sua pronúncia primária.

Escreva um programa que liste todas as palavras que resolvem o quebra-cabeça.

Solução: http://thinkpython2.com/code/homophone.py.
