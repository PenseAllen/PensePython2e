# Capítulo 6: Funções com resultado

Muitas das funções do Python que usamos, como as matemáticas, produzem valores de retorno. Mas as funções que escrevemos até agora são todas nulas: têm um efeito, como exibir um valor ou mover uma tartaruga, mas não têm um valor de retorno. Neste capítulo você aprenderá a escrever funções com resultados.

## 6.1 - Valores de retorno

A chamada de função gera um valor de retorno, que normalmente atribuímos a uma variável ou usamos como parte de uma expressão.

```python
e = math.exp(1.0)
height = radius * math.sin(radians)
```

As funções que descrevemos, por enquanto, são todas nulas. Resumindo, elas não têm valores de retorno; mais precisamente, o seu valor de retorno é None.

Neste capítulo veremos (finalmente) como escrever funções com resultados. O primeiro exemplo é area, que devolve a área de um círculo com o raio dado:

```python
def area(radius):
    a = math.pi * radius**2
    return a
```

Já vimos a instrução return, mas em uma função com resultado ela inclui uma expressão. Esta instrução significa: “Volte imediatamente desta função e use a seguinte expressão como valor de retorno”. A expressão pode ser arbitrariamente complicada, então poderíamos ter escrito esta função de forma mais concisa:

```python
def area(radius):
    return math.pi * radius**2
```

Por outro lado, variáveis temporárias como a, tornam a depuração mais fácil.

Às vezes, é útil ter várias instruções de retorno, uma em cada ramo de uma condicional:

```python
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
```

Como essas instruções return estão em uma condicional alternativa, apenas uma é executada.

Logo que uma instrução de retorno seja executada, a função termina sem executar nenhuma instrução subsequente. Qualquer código que apareça depois de uma instrução return, ou em qualquer outro lugar que o fluxo da execução não atinja, é chamado de código morto.

Em uma função com resultado, é uma boa ideia garantir que cada caminho possível pelo programa atinja uma instrução return. Por exemplo:

```python
def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x
```

Essa função é incorreta porque se x for 0, nenhuma condição é verdade, e a função termina sem chegar a uma instrução return. Se o fluxo de execução chegar ao fim de uma função, o valor de retorno é None, que não é o valor absoluto de 0:

```python
>>> absolute_value(0)
None
```

A propósito, o Python oferece uma função integrada chamada abs, que calcula valores absolutos.

Como exercício, escreva uma função compare que receba dois valores, x e y, e retorne 1 se x &gt; y, 0 se x == y e -1 se x &lt; y.

## 6.2 - Desenvolvimento incremental

Conforme você escrever funções maiores, pode ser que passe mais tempo as depurando.

Para lidar com programas cada vez mais complexos, você pode querer tentar usar um processo chamado de desenvolvimento incremental. A meta do desenvolvimento incremental é evitar longas sessões de depuração, acrescentando e testando pequenas partes do código de cada vez.

Como um exemplo, vamos supor que você queira encontrar a distância entre dois pontos dados pelas coordenadas (x1, y1) e(x2, y2). Pelo teorema de Pitágoras, a distância é:

![Fórmula – Distância entre dois pontos.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/p63f1.png)

O primeiro passo é pensar como uma função distance deveria ser no Python. Em outras palavras, quais são as entradas (parâmetros) e qual é a saída (valor de retorno)?

Nesse caso, as entradas são dois pontos que você pode representar usando quatro números. O valor de retorno é a distância representada por um valor de ponto flutuante.

Imediatamente, é possível escrever um rascunho da função:

```python
def distance(x1, y1, x2, y2):
    return 0.0
```

Claro que esta versão não calcula distâncias; sempre retorna zero. Mas está sintaticamente correta, e pode ser executada, o que significa que você pode testá-la antes de torná-la mais complicada.

Para testar a nova função, chame-a com argumentos de amostra:

```python
>>> distance(1, 2, 4, 6)
0.0
```

Escolhi esses valores para que a distância horizontal seja 3 e a distância vertical, 4; assim, o resultado final é 5, a hipotenusa de um triângulo 3-4-5. Ao testar uma função, é útil saber a resposta certa.

Neste ponto confirmamos que a função está sintaticamente correta, e podemos começar a acrescentar código ao corpo. Um próximo passo razoável é encontrar as diferenças x2 − x1 e y2 − y1. A próxima versão guarda esses valores em variáveis temporárias e os exibe:

```python
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)
    print('dy is', dy)
    return 0.0
```

Se a função estiver funcionando, deve exibir dx is 3 e dy is 4. Nesse caso sabemos que a função está recebendo os argumentos corretos e executando o primeiro cálculo acertadamente. Se não, há poucas linhas para verificar.

Depois calculamos a soma dos quadrados de dx e dy:

```python
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    print('dsquared is: ', dsquared)
    return 0.0
```

Nesta etapa você executaria o programa mais uma vez e verificaria a saída (que deve ser 25). Finalmente, pode usar math.sqrt para calcular e devolver o resultado:

```python
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
```

Se funcionar corretamente, pronto. Senão, uma ideia é exibir o valor result antes da instrução de retorno.

A versão final da função não exibe nada ao ser executada; apenas retorna um valor. As instruções print que escrevemos são úteis para depuração, mas assim que conferir se a função está funcionando você deve retirá-las. Códigos desse tipo são chamados de scaffolding (andaime) porque são úteis para construir o programa, mas não são parte do produto final.

Ao começar, você deveria acrescentar apenas uma linha ou duas de código de cada vez. Conforme adquira mais experiência, poderá escrever e depurar parcelas maiores. De qualquer forma, o desenvolvimento incremental pode economizar muito tempo de depuração.

Os principais aspectos do processo são:

1. Comece com um programa que funcione e faça pequenas alterações incrementais. Se houver um erro em qualquer ponto, será bem mais fácil encontrá-lo.

2. Use variáveis para guardar valores intermediários, assim poderá exibi-los e verificá-los.

3. Uma vez que o programa esteja funcionando, você pode querer remover uma parte do scaffolding ou consolidar várias instruções em expressões compostas, mas apenas se isso não tornar o programa difícil de ler.

Como exercício, use o desenvolvimento incremental para escrever uma função chamada hypotenuse, que devolva o comprimento da hipotenusa de um triângulo retângulo dados os comprimentos dos outros dois lados como argumentos. Registre cada etapa do processo de desenvolvimento no decorrer do processo.

## 6.3 - Composição

Como você já deveria esperar a essa altura, é possível chamar uma função de dentro de outra. Como exemplo, escreveremos uma função que recebe dois pontos, o centro do círculo e um ponto no perímetro, para calcular a área do círculo.

Suponha que o ponto do centro seja guardado nas variáveis xc e yc e o ponto de perímetro está em xp e yp. O primeiro passo deve ser encontrar o raio do círculo, que é a distância entre os dois pontos. Acabamos de escrever uma função, distance, que faz isto:

```python
radius = distance(xc, yc, xp, yp)
```

O próximo passo deve ser encontrar a área de um círculo com aquele raio; acabamos de escrever isso também:

```python
result = area(radius)
```

Encapsulando esses passos em uma função, temos:

```python
def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result
```

As variáveis temporárias radius e result são úteis para desenvolvimento e depuração, e uma vez que o programa esteja funcionando podemos torná-lo mais conciso compondo chamadas de função:

```python
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))
```

## 6.4 - Funções booleanas

As funções podem retornar booleans, o que pode ser conveniente para esconder testes complicados dentro de funções. Por exemplo:

```python
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
```

É comum dar nomes de funções booleanas que pareçam perguntas de sim ou não; is\_divisible retorna True ou False para indicar se x é divisível por y.

Aqui está um exemplo:

```python
>>> is_divisible(6, 4)
False
>>> is_divisible(6, 3)
True
```

O resultado do operador == é um booleano, então podemos escrever a função de forma mais concisa, retornando-o diretamente:

```python
def is_divisible(x, y):
    return x % y == 0
```

As funções booleanas muitas vezes são usadas em instruções condicionais:

```python
if is_divisible(x, y):
    print('x is divisible by y')
```

Pode ser tentador escrever algo assim:

```python
if is_divisible(x, y) == True:
    print('x is divisible by y')
```

Mas a comparação extra é desnecessária.

Como um exercício, escreva uma função `is_between(x, y, z)` que retorne True, se x ≤ y ≤ z, ou False, se não for o caso.

## 6.5 - Mais recursividade

Cobrimos apenas um pequeno subconjunto do Python, mas talvez seja bom você saber que este subconjunto é uma linguagem de programação completa, ou seja, qualquer coisa que possa ser calculada pode ser expressa nesta linguagem. Qualquer programa que já foi escrito pode ser reescrito apenas com os recursos da linguagem que você aprendeu até agora (na verdade, seria preciso alguns comandos para dispositivos de controle como mouse, discos etc., mas isso é tudo).

Comprovar esta declaração é um exercício nada trivial realizado pela primeira vez por Alan Turing, um dos primeiros cientistas da computação (alguns diriam que ele foi matemático, mas muitos dos primeiros cientistas da computação começaram como matemáticos). Assim, é conhecida como a Tese de Turing. Para uma exposição mais completa (e exata) da Tese de Turing, recomendo o livro de Michael Sipser, Introduction to the Theory of Computation (Introdução à teoria da computação, Course Technology, 2012).

Para dar uma ideia do que podemos fazer com as ferramentas que aprendeu até agora, avaliaremos algumas funções matemáticas definidas recursivamente. Uma definição recursiva é semelhante a uma definição circular, no sentido de que a definição contém uma referência à coisa que é definida. Uma definição realmente circular não é muito útil:

<dl>
<dt>vorpal</dt>
<dd>Adjetivo usado para descrever algo que é vorpal.</dd>
</dl>

Ver uma definição assim no dicionário pode ser irritante. Por outro lado, se procurar a definição da função de fatorial, denotada pelo símbolo !, você pode encontrar algo assim:

```
0! = 1
n! = n·(n − 1)!
```

Esta definição diz que o fatorial de 0 é 1, e o fatorial de qualquer outro valor, n, é n multiplicado pelo fatorial de n-1.

Então 3! é 3 vezes 2!, que é 2 vezes 1!, que é 1 vez 0!. Juntando tudo, 3! é igual a 3 vezes 2 vezes 1 vezes 1, que é 6.

Se puder escrever uma definição recursiva de algo, você poderá escrever um programa em Python que a avalie. O primeiro passo deve ser decidir quais parâmetros ela deve ter. Neste caso, deve estar claro que factorial recebe um número inteiro:

```python
def factorial(n):
```

Se o argumento for 0, tudo que temos de fazer é retornar 1:

```python
def factorial(n):
    if n == 0:
        return 1
```

Senão, e aí é que fica interessante, temos que fazer uma chamada recursiva para encontrar o fatorial de n-1 e então multiplicá-lo por n:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
```

O fluxo de execução deste programa é semelhante ao fluxo de countdown em “Recursividade”, na página 81. Se chamarmos factorial com o valor 3:

Como 3 não é 0, tomamos o segundo ramo e calculamos o fatorial de n-1...

&nbsp;&nbsp;&nbsp;&nbsp;Como 2 não é 0, tomamos o segundo ramo e calculamos o fatorial de n-1...

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Como 1 não é 0, tomamos o segundo ramo e calculamos o fatorial de n-1...

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Como 0 é igual a 0, tomamos o primeiro ramo e devolvemos 1 sem fazer mais chamadas recursivas.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O valor de retorno, 1, é multiplicado por n, que é 1, e o resultado é devolvido.

&nbsp;&nbsp;&nbsp;&nbsp;O valor de retorno, 1, é multiplicado por n, que é 2, e o resultado é devolvido.

O valor devolvido (2) é multiplicado por n, que é 3, e o resultado, 6, torna-se o valor devolvido pela chamada de função que começou o processo inteiro.

A Figura 6.1 mostra como é o diagrama da pilha para esta sequência de chamadas de função.

![Figura 6.1 – Diagrama da pilha para factorial.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_0601.png)
<br>_Figura 6.1 – Diagrama da pilha para factorial._


Os valores devolvidos são mostrados ao serem passados de volta até o alto da pilha. Em cada frame, o valor devolvido é o valor de `result`, que é o produto de `n` e `recurse`.

No último frame, as variáveis locais recurse e result não existem, porque o ramo que os cria não é executado.

## 6.6 - Salto de fé

Seguir o fluxo da execução é uma forma de ler programas, mas poderá ser trabalhoso demais. Uma alternativa é o que chamo de “salto de fé” (leap of faith). Ao chegar a uma chamada de função, em vez de seguir o fluxo de execução suponha que a função esteja funcionando corretamente e que está retornando o resultado certo.

Na verdade, você já está praticando este salto de fé quando usa funções integradas. Quando chama math.cos ou math.exp, você não examina o corpo dessas funções. Apenas supõe que funcionem porque as pessoas que as escreveram eram bons programadores.

O mesmo acontece ao chamar uma das suas próprias funções. Por exemplo, em “Funções booleanas”, na página 97, escrevemos uma função chamada is\_divisible que determina se um número é divisível por outro. Uma vez que estejamos convencidos de que esta função está correta – examinando o código e testando – podemos usar a função sem ver o corpo novamente.

O mesmo é verdade para programas recursivos. Quando chega à chamada recursiva, em vez de seguir o fluxo de execução, você deveria supor que a chamada recursiva funcione (devolva o resultado correto) e então perguntar-se: “Supondo que eu possa encontrar o fatorial de n-1, posso calcular o fatorial de n?”. É claro que pode, multiplicando por n.

Naturalmente, é um pouco estranho supor que a função funcione corretamente quando ainda não terminou de escrevê-la, mas é por isso que se chama um salto de fé!

## 6.7 - Mais um exemplo

Depois do factorial, o exemplo mais comum de uma função matemática definida recursivamente é fibonacci, que tem a seguinte definição (ver http://en.wikipedia.org/wiki/Fibonacci_number):

```
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(n) = fibonacci(n − 1) + fibonacci(n − 2)
```

Traduzida para Python, ela fica assim:

```python
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

Se tentar seguir o fluxo de execução aqui, até para valores razoavelmente pequenos de n, sua cabeça explode. Porém, seguindo o salto de fé, supondo que as duas chamadas recursivas funcionem corretamente, então é claro que vai receber o resultado correto adicionando-as juntas.

## 6.8 - Verificação de tipos

O que acontece se chamarmos factorial e usarmos 1.5 como argumento?

```python
>>> factorial(1.5)
RuntimeError: Maximum recursion depth exceeded
```

Parece uma recursividade infinita. No entanto, por que isso acontece? A função tem um caso-base – quando n == 0. Mas se n não é um número inteiro, podemos perder o caso-base e recorrer para sempre.

Na primeira chamada recursiva, o valor de n é 0.5. No seguinte, é -0.5. Daí, torna-se menor (mais negativo), mas nunca será 0.

Temos duas escolhas. Podemos tentar generalizar a função factorial para trabalhar com números de ponto flutuante, ou podemos fazer factorial controlar o tipo de argumento que recebe. A primeira opção chama-se função gamma e está um pouco além do alcance deste livro. Então usaremos a segunda opção.

Podemos usar a função integrada isinstance para verificar o tipo de argumento. E vamos aproveitar para verificar também se o argumento é positivo:

```python
def factorial (n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

O primeiro caso-base lida com números não inteiros; o segundo, com números inteiros negativos. Em ambos os casos o programa exibe uma mensagem de erro e retorna None para indicar que algo deu errado:

```python
>>> factorial('fred')
Factorial is only defined for integers.
None
>>> factorial(-2)
Factorial is not defined for negative integers.
None
```

Se passarmos por ambas as verificações, sabemos que n é positivo ou zero, então podemos comprovar que a recursividade termina.

Esse programa demonstra um padrão às vezes chamado de guardião. As duas primeiras condicionais atuam como guardiãs, protegendo o código que segue de valores que poderiam causar um erro. As guardiãs permitem comprovar a correção do código.

Na “Busca reversa”, na página 165, veremos uma alternativa mais flexível para a exibição de uma mensagem de erro: o levantamento de exceções.

## 6.9 - Depuração

Quebrar um grande programa em funções menores cria controles naturais da depuração. Se uma função não estiver funcionando, há três possibilidades a considerar:

* Há algo errado com os argumentos que a função está recebendo; uma precondição está sendo violada.

* Há algo errado com a função; uma pós-condição foi violada.

* Há algo errado com o valor de retorno ou a forma na qual está sendo usado.

Para excluir a primeira possibilidade, você pode acrescentar uma instrução print no início da função e exibir os valores dos parâmetros (e talvez os seus tipos). Ou escrever código que verifique as precondições explicitamente.

Se os parâmetros parecerem bons, acrescente uma instrução print antes de cada instrução return e exiba o valor de retorno. Se possível, verifique o resultado à mão. Uma possibilidade é chamar a função com valores facilitem a verificação do resultado (como no “Desenvolvimento incremental”, da página 94).

Se a função parecer funcionar, veja a chamada da função para ter certeza de que o valor de retorno está sendo usado corretamente (ou se está sendo usado mesmo!).

Acrescentar instruções de exibição no começo e no fim de uma função pode ajudar a tornar o fluxo de execução mais visível. Por exemplo, aqui está uma versão de factorial com instruções de exibição:

```python
def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result
```

space é uma string de caracteres especiais que controla a endentação da saída. Aqui está o resultado de factorial(4):

```
                factorial 4
            factorial 3
        factorial 2
    factorial 1
factorial 0
returning 1
    returning 1
        returning 2
            returning 6
                returning 24
```

Se o fluxo de execução parecer confuso a você, este tipo de saída pode ser útil. Leva um tempo para desenvolver um scaffolding eficaz, mas um pouco dele pode economizar muita depuração.

## 6.10 - Glossário

<dl>
<dt><a id="glos:variável temporária" href="#termo:variável temporária">variável temporária</a></dt>
<dd>Uma variável usada para guardar um valor intermediário em um cálculo complexo.</dd>

<dt><a id="glos:código morto" href="#termo:código morto">código morto</a></dt>
<dd>A parte de um programa que nunca pode ser executada, muitas vezes porque aparece depois de uma instrução return.</dd>

<dt><a id="glos:desenvolvimento incremental" href="#termo:desenvolvimento incremental">desenvolvimento incremental</a></dt>
<dd>Um plano de desenvolvimento de programa para evitar a depuração, que acrescenta e testa poucas linhas de código de cada vez.</dd>

<dt><a id="glos:scaffolding (andaime)" href="#termo:scaffolding (andaime)">scaffolding (andaime)</a></dt>
<dd>O código que se usa durante o desenvolvimento de programa, mas que não faz parte da versão final.</dd>

<dt><a id="glos:guardião" href="#termo:guardião">guardião</a></dt>
<dd>Um padrão de programação que usa uma instrução condicional para verificar e lidar com circunstâncias que possam causar erros.</dd>

</dl>

## 6.11 - Exercícios

### Exercício 6.1

Desenhe um diagrama da pilha do seguinte programa. O que o programa exibe?

```python
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
```

### Exercício 6.2


A função de Ackermann, A(m, n), é definida assim:

![Fórmula – Função de Ackermann.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/p72f1.png)

Veja http://en.wikipedia.org/wiki/Ackermann_function. Escreva uma função denominada ack que avalie a função de Ackermann. Use a sua função para avaliar `ack(3, 4)`, cujo resultado deve ser 125. O que acontece para valores maiores de m e n?

Solução: http://thinkpython2.com/code/ackermann.py.

### Exercício 6.3

Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”. Recursivamente, uma palavra é um palíndromo se a primeira e última letras forem iguais e o meio for um palíndromo.

As funções seguintes recebem uma string como argumento e retornam as letras iniciais, finais e do meio das palavras:

```python
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
```

Veremos como funcionam no Capítulo 8.

1. Digite essas funções em um arquivo chamado palindrome.py e teste-as. O que acontece se chamar middle com uma string de duas letras? Uma letra? E se a string estiver vazia, escrita com `''` e não contiver nenhuma letra?

2. Escreva uma função chamada `is_palindrome` que receba uma string como argumento e retorne True se for um palíndromo e False se não for. Lembre-se de que você pode usar a função integrada len para verificar o comprimento de uma string.

Solução: http://thinkpython2.com/code/palindrome_soln.py.

### Exercício 6.4

Um número a é uma potência de b se for divisível por b e a/b for uma potência de b. Escreva uma função chamada is\_power que receba os parâmetros a e b e retorne True se a for uma potência de b. Dica: pense no caso-base.

### Exercício 6.5

O maior divisor comum (MDC, ou GCD em inglês) de a e b é o maior número que divide ambos sem sobrar resto.

Um modo de encontrar o MDC de dois números é observar qual é o resto r quando a é dividido por b, verificando que gcd(a, b) = gcd(b, r). Como caso-base, podemos usar gcd(a, 0) = a.

Escreva uma função chamada gcd que receba os parâmetros a e b e devolva o maior divisor comum.

Crédito: Este exercício é baseado em um exemplo do livro de Abelson e Sussman, Structure and Interpretation of Computer Programs (Estrutura e interpretação de programas de computador, MIT Press, 1996).
