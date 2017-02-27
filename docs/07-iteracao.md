# Capítulo 7: Iteração

Este capítulo é sobre a iteração, a capacidade de executar um bloco de instruções repetidamente. Vimos um tipo de iteração, usando a recursividade, em “Recursividade”, na página 81. Vimos outro tipo, usando um loop for, em “Repetição simples”, na página 65. Neste capítulo veremos ainda outro tipo, usando a instrução while. Porém, primeiro quero falar um pouco mais sobre a atribuição de variáveis.

## 7.1 - Reatribuição

Pode ser que você já tenha descoberto que é permitido fazer mais de uma atribuição para a mesma variável. Uma nova atribuição faz uma variável existente referir-se a um novo valor (e deixar de referir-se ao valor anterior).

```python
>>> x = 5
>>> x
5
>>> x = 7
>>> x
7
```

A primeira vez que exibimos x, seu valor é 5; na segunda vez, seu valor é 7.

A Figura 7.1 mostra que a reatribuição parece um diagrama de estado.

Neste ponto quero tratar de uma fonte comum de confusão. Como o Python usa o sinal de igual (=) para atribuição, é tentador interpretar uma afirmação como a = b como uma proposição matemática de igualdade; isto é, a declaração de que a e b são iguais. Mas esta é uma interpretação equivocada.

Em primeiro lugar, a igualdade é uma relação simétrica e a atribuição não é. Por exemplo, na matemática, se a=7 então 7=a. Mas no Python, a instrução a = 7 é legal e 7 = a não é.

Além disso, na matemática, uma proposição de igualdade é verdadeira ou falsa para sempre. Se a=b agora, então a sempre será igual a b. No Python, uma instrução de atribuição pode tornar duas variáveis iguais, mas elas não precisam se manter assim:

```python
>>> a = 5
>>> b = a    # a e b agora são iguais
>>> a = 3    # a e b não são mais iguais
>>> b
5
```

A terceira linha modifica o valor de a, mas não muda o valor de b, então elas já não são iguais.

A reatribuição de variáveis muitas vezes é útil, mas você deve usá-la com prudência. Se os valores das variáveis mudarem frequentemente, isso pode dificultar a leitura e depuração do código.

```python
Figura 7.1 – Diagrama de estado.
```

![Figura 7.1 – Diagrama de estado da variável x.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_0701.png)
<br>_Figura 7.1 – Diagrama de estado da variável x._

## 7.2 - Atualização de variáveis

Um tipo comum de reatribuição é uma atualização, onde o novo valor da variável depende do velho.

```python
>>> x = x + 1
```

Isso significa “pegue o valor atual de x, acrescente um, e então atualize x para o novo valor”.

Se você tentar atualizar uma variável que não existe, recebe um erro porque o Python avalia o lado direito antes de atribuir um valor a x:

```python
>>> x = x + 1
NameError: name 'x' is not defined
```

Antes de poder atualizar uma variável é preciso inicializá-la, normalmente com uma atribuição simples:

```python
>>> x = 0
>>> x = x + 1
```

Atualizar uma variável acrescentando 1 chama-se incremento; subtrair 1 chama-se decremento.

## 7.3 - Instrução while

Os computadores muitas vezes são usados para automatizar tarefas repetitivas. A repetição de tarefas idênticas ou semelhantes sem fazer erros é algo que os computadores fazem bem e as pessoas não. Em um programa de computador, a repetição também é chamada de iteração.

Já vimos duas funções, `countdown` e `print_n`, que se repetem usando recursividade. Como a iteração é bem comum, o Python fornece recursos de linguagem para facilitá-la. Um deles é a instrução `for` que vimos em “Repetição simples”, na página 65. Voltaremos a isso mais adiante.

Outra é a instrução `while`. Aqui está uma versão de countdown que usa a instrução `while`:

```python
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')
```

Você até pode ler a instrução `while` como se fosse uma tradução do inglês. Significa “Enquanto `n` for maior que 0, mostre o valor de `n` e então decremente `n`. Quando chegar a 0, mostre a palavra Blastoff!”

Mais formalmente, aqui está o fluxo de execução para uma instrução while:

1. Determine se a condição é verdadeira ou falsa.

2. Se for falsa, saia da instrução while e continue a execução da próxima instrução.

3. Se a condição for verdadeira, execute o corpo e então volte ao passo 1.

Este tipo de fluxo chama-se loop (laço), porque o terceiro passo faz um loop de volta ao topo.

O corpo do loop deve mudar o valor de uma ou mais variáveis para que, a certa altura, a condição fique falsa e o loop termine. Senão o loop vai se repetir para sempre, o que é chamado de loop infinito. Uma fonte infindável de divertimento para cientistas da computação é a observação das instruções no xampu, “Faça espuma, enxágue, repita”, que são parte de um loop infinito.

No caso de countdown, podemos provar que o loop termina: se `n` for zero ou negativo, o loop nunca é executado. Senão, `n` fica cada vez menor ao passar pelo loop, até eventualmente chegar a 0.

Para alguns outros loops, não é tão fácil perceber isso. Por exemplo:

```python
def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:        # n é par
            n = n / 2
        else:                 # n é ímpar
            n = n * 3 + 1
```

A condição deste loop é `n != 1`, então o loop continuará até que `n` seja 1, o que torna a condição falsa.

Cada vez que passa pelo loop, o programa produz o valor de `n` e então verifica se é par ou ímpar. Se for par, `n` é dividido por 2. Se for ímpar, o valor de `n` é substituído por `n * 3 + 1`. Por exemplo, se o argumento passado a sequence for 3, os valores resultantes de `n` são 3, 10, 5, 16, 8, 4, 2, 1.

Como `n` às vezes aumenta e às vezes diminui, não há nenhuma prova óbvia de que `n` chegará eventualmente a 1, ou que o programa terminará. Para alguns valores de `n`, podemos provar o término. Por exemplo, se o valor inicial for uma potência de dois, `n` será par cada vez que passar pelo loop até que chegue a 1. O exemplo anterior termina com uma sequência assim, que inicia com 16.

A questão difícil é se podemos provar que este programa termina para todos os valores positivos de `n`. Por enquanto, ninguém foi capaz de comprovar ou refutar isso! (Veja http://en.wikipedia.org/wiki/Collatz\_conjecture.)

Como um exercício, reescreva a função print\_n de “Recursividade”, na página 81, usando a iteração em vez da recursividade.

## 7.4 - break

Às vezes você não sabe que está na hora de terminar um loop até que já esteja na metade do corpo. Neste caso pode usar a instrução break para sair do loop.

Por exemplo, suponha que você quer receber uma entrada do usuário até que este digite done. Você pode escrever:

```python
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
```

A condição do loop é True, que sempre é verdade, então o loop roda até que chegue à instrução de interrupção.

Cada vez que passa pelo loop, o programa apresenta ao usuário um colchete angular. Se o usuário digitar done, a instrução break sai do loop. Senão, o programa ecoa o que quer que o usuário digite e volta ao topo do loop. Aqui está uma amostra de execução:

```python
> not done
not done
> done
Done!
```

Esta forma de escrever loops while é comum porque podemos verificar a condição em qualquer lugar do loop (não somente no topo) e podemos exprimir a condição de parada afirmativamente (“pare quando isto acontecer”) em vez de negativamente (“continue a seguir até que isto aconteça”).

## 7.5 - Raízes quadradas

Loops muitas vezes são usados em programas que calculam resultados numéricos, começando com uma resposta aproximada e melhorando-a iterativamente.

Por exemplo, uma forma de calcular raízes quadradas é o método de Newton. Suponha que você queira saber a raiz quadrada de a. Se começar com quase qualquer estimativa, x, é possível calcular uma estimativa melhor com a seguinte fórmula:

![Fórmula – Raiz quadrada pelo método de Newton.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/p79f1.png)

```python
Por exemplo, se a for 4 e x for 3:
>>> a = 4
>>> x = 3
>>> y = (x + a/x) / 2
>>> y
2.16666666667
```
O resultado é mais próximo à resposta correta (![Fórmula – Raiz quadrada de 4.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/p79f2.png) = 2). Se repetirmos o processo com a nova estimativa, chegamos ainda mais perto:

```python
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.00641025641
```
Depois de algumas atualizações, a estimativa é quase exata:

```python
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.00001024003
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.00000000003
```

Em geral, não sabemos com antecedência quantos passos são necessários para chegar à resposta correta, mas sabemos quando chegamos lá porque a estimativa para de mudar:

```python
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.0
>>> x = y
>>> y = (x + a/x) / 2
>>> y
2.0
```
Quando y == x, podemos parar. Aqui está um loop que começa com uma estimativa inicial, x, e a melhora até que deixe de mudar:

```python
while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y
```

Para a maior parte de valores de `a` funciona bem, mas pode ser perigoso testar a igualdade de um float. Os valores de ponto flutuante são aproximadamente corretos: a maioria dos números racionais, como 1/3, e números irracionais, como ![Fórmula – Raiz quadrada de 2.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/p80f1.png), não podem ser representados exatamente com um float.

Em vez de verificar se `x` e `y` são exatamente iguais, é mais seguro usar a função integrada `abs` para calcular o valor absoluto ou magnitude da diferença entre eles:

```python
if abs(y-x) < epsilon:
    break
```

Onde `epsilon` tem um valor como 0.0000001, que determina a proximidade desejada entre `x` e `y`.

## 7.6 - Algoritmos

O método de Newton é um exemplo de um algoritmo: um processo mecânico para resolver uma categoria de problemas (neste caso, calcular raízes quadradas).

Para entender o que é um algoritmo, pode ser útil começar com algo que não é um algoritmo. Quando aprendeu a multiplicar números de um dígito, você provavelmente memorizou a tabuada. Ou seja, você memorizou 100 soluções específicas. Este tipo de conhecimento não é algorítmico.

No entanto, se você foi “preguiçoso”, poderia ter aprendido alguns truques. Por exemplo, para encontrar o produto de `n` e 9, pode escrever `n-1` como o primeiro dígito e `10-n` como o segundo dígito. Este truque é uma solução geral para multiplicar qualquer número de dígito único por 9. Isto é um algoritmo!

De forma semelhante, as técnicas que aprendeu, como o transporte na adição, o empréstimo na subtração e a divisão longa são todos algoritmos. Uma das características de algoritmos é que eles não exigem inteligência para serem executados. São processos mecânicos, nos quais cada passo segue a partir do último, de acordo com um conjunto de regras simples.

A execução de algoritmos é maçante, mas projetá-los é interessante, intelectualmente desafiador e uma parte central da Ciência da Computação.

Algumas coisas que as pessoas fazem naturalmente, sem dificuldade ou pensamento consciente, são as mais difíceis para exprimir algoritmicamente. A compreensão de linguagem natural é um bom exemplo. Todos nós o fazemos, mas por enquanto ninguém foi capaz de explicar como o fazemos, pelo menos não na forma de um algoritmo.

## 7.7 - Depuração

Ao começar a escrever programas maiores, pode ser que você passe mais tempo depurando. Mais código significa mais possibilidades fazer erros e mais lugares para esconder defeitos.

Uma forma de cortar o tempo de depuração é “depurar por bisseção”. Por exemplo, se há 100 linhas no seu programa e você as verifica uma a uma, seriam 100 passos a tomar.

Em vez disso, tente quebrar o problema pela metade. Olhe para o meio do programa, ou perto disso, para um valor intermediário que possa verificar. Acrescente uma instrução print (ou outra coisa que tenha um efeito verificável) e execute o programa.

Se a verificação do ponto central for incorreta, deve haver um problema na primeira metade do programa. Se for correta, o problema está na segunda metade.

Cada vez que executar uma verificação assim, divida ao meio o número de linhas a serem verificadas. Depois de seis passos (que é menos de 100), você teria menos de uma ou duas linhas do código para verificar, pelo menos em teoria.

Na prática, nem sempre é claro o que representa o “meio do programa” e nem sempre é possível verificá-lo. Não faz sentido contar linhas e encontrar o ponto central exato. Em vez disso, pense em lugares no programa onde poderia haver erros e lugares onde é fácil inserir um ponto de verificação. Então escolha um lugar onde as possibilidades são basicamente as mesmas de que o defeito esteja antes ou depois da verificação.

## 7.8 - Glossário

<dl>
<dt><a id="glos:reatribuição" href="#termo:reatribuição">reatribuição</a></dt>
<dd>Atribuir um novo valor a uma variável que já existe.</dd>

<dt><a id="glos:atualização" href="#termo:atualização">atualização</a></dt>
<dd>Uma atribuição onde o novo valor da variável dependa do velho.</dd>

<dt><a id="glos:inicialização" href="#termo:inicialização">inicialização</a></dt>
<dd>Uma atribuição que dá um valor inicial a uma variável que será atualizada.</dd>

<dt><a id="glos:incremento" href="#termo:incremento">incremento</a></dt>
<dd>Uma atualização que aumenta o valor de uma variável (normalmente por uma unidade).</dd>

<dt><a id="glos:decremento" href="#termo:decremento">decremento</a></dt>
<dd>Uma atualização que reduz o valor de uma variável.</dd>

<dt><a id="glos:iteração" href="#termo:iteração">iteração</a></dt>
<dd>Execução repetida de um grupo de instruções, usando uma chamada da função recursiva ou um loop.</dd>

<dt><a id="glos:loop infinito" href="#termo:loop infinito">loop infinito</a></dt>
<dd>Um loop no qual a condição de término nunca é satisfeita.</dd>

<dt><a id="glos:algoritmo" href="#termo:algoritmo">algoritmo</a></dt>
<dd>Um processo geral para resolver uma categoria de problemas.</dd>

</dl>

## 7.9 - Exercícios

### Exercício 7.1

Copie o loop de “Raízes quadradas”, na página 111, e encapsule-o em uma função chamada `mysqrt` que receba a como parâmetro, escolha um valor razoável de x e devolva uma estimativa da raiz quadrada de a.

Para testar, escreva uma função denominada `test_square_root`, que exibe uma tabela como esta:

```python
a   mysqrt(a)     math.sqrt(a)  diff
-   ---------     ------------  ----
1.0 1.0           1.0           0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0           2.0           0.0
5.0 2.2360679775  2.2360679775  0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0           3.0           0.0
```

A primeira coluna é um número, `a`; a segunda coluna é a raiz quadrada de a calculada com `mysqrt`; a terceira coluna é a raiz quadrada calculada por `math.sqrt`; a quarta coluna é o valor absoluto da diferença entre as duas estimativas.

### Exercício 7.2

A função integrada `eval` toma uma string e a avalia, usando o interpretador do Python. Por exemplo:

```python
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
```

Escreva uma função chamada `eval_loop` que iterativamente peça uma entrada ao usuário, a avalie usando `eval` e exiba o resultado.

Ela deve continuar até que o usuário digite `done`; então deverá exibir o valor da última expressão avaliada.

### Exercício 7.3

O matemático Srinivasa Ramanujan encontrou uma série infinita que pode ser usada para gerar uma aproximação numérica de 1/π:

![Fórmula – Aproximação de π pela série de Ramanujan.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/p83f1.png)

Escreva uma função chamada `estimate_pi` que use esta fórmula para computar e devolver uma estimativa de π. Você deve usar o loop `while` para calcular os termos da adição até que o último termo seja menor que 1e-15 (que é a notação do Python para `10 ** 15`). Você pode verificar o resultado comparando-o com `math.pi`.
