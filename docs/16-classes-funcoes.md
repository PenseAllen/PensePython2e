# Capítulo 16: Classes e funções

Agora que sabemos como criar tipos, o próximo passo deve ser escrever funções que recebam objetos definidos pelo programador como parâmetros e os retornem como resultados. Neste capítulo também vou apresentar o “estilo funcional de programação” e dois novos planos de desenvolvimento de programas.

Os exemplos de código deste capítulo estão disponíveis em https://github.com/AllenDowney/ThinkPython2/raw/master/code/Time1.py. As soluções para os exercícios estão em https://github.com/AllenDowney/ThinkPython2/raw/master/code/Time1\_soln.py.

## 16.1 - Time

Para ter mais um exemplo de tipo definido pelo programador, criaremos uma classe chamada `Time` (hora), que registra um horário no dia. A definição da classe é assim:


```python
class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
```

Podemos criar um objeto `Time` e ter atributos para horas, minutos e segundos:

```python
time = Time()
time.hour = 11
time.minute = 59
time.second = 30
```

O diagrama de estado do objeto Time está na Figura 16.1.

![Figura 16.1 – Diagrama de um objeto Time.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1601.png)
<br>_Figura 16.1 – Diagrama de um objeto_ `Time`.

Como exercício, escreva uma função chamada `print_time`, que receba um objeto Time e o exiba na forma hour:minute:second. Dica: a sequência de formatação `'%.2d'` exibe um número inteiro com, pelo menos, dois dígitos, incluindo um zero à esquerda, se for necessário.

Escreva uma função booleana chamada `is_after`, que receba dois objetos Time, `t1` e `t2`, e devolva `True` se `t1` for cronologicamente depois de `t2` e `False` se não for. Desafio: não use uma instrução `if`.

## 16.2 - Funções puras

Nas próximas seções, vamos escrever duas funções que adicionam valores de tempo. Elas demonstram dois tipos de funções: funções puras e modificadores. Também demonstram um plano de desenvolvimento que chamarei de protótipo e correção, que é uma forma de atacar um problema complexo começando com um protótipo simples e lidando com as complicações de forma incremental.

Aqui está um protótipo simples de `add_time`:

```python
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum
```

A função cria um novo objeto `Time`, inicializa seus atributos e retorna uma referência ao novo objeto. A função pura é chamada assim porque não altera nenhum dos objetos passados a ela como argumentos; além disso, ela não tem efeitos, como exibir um valor ou receber entradas de usuário, apenas retorna um valor.

Para testar esta função, criarei objetos `Time`: `start`, que contém o tempo de início de um filme, como _Monty Python e o cálice sagrado_, e `duration`, que contém o tempo de execução do filme, que é de 1 hora e 35 minutos.

`add_time` calcula quando o filme acaba:

```python
>>> start = Time()
>>> start.hour = 9
>>> start.minute = 45
>>> start.second = 0
>>> duration = Time()
>>> duration.hour = 1
>>> duration.minute = 35
>>> duration.second = 0
>>> done = add_time(start, duration)
>>> print_time(done)
10:80:00
```

O resultado, 10:80:00, pode não ser o que você esperava. O problema é que esta função não trata casos onde o número de segundos ou minutos é maior que 60. Quando isso acontece, precisamos transportar os segundos extras à coluna dos minutos ou os minutos extras à coluna das horas.

Aqui está uma versão melhorada:

```python
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum
```

Embora esta função esteja correta, é um pouco extensa. Veremos uma alternativa menor mais adiante.

## 16.3 - Modificadores

Às vezes é útil uma função alterar os objetos que recebe como parâmetros. Nesse caso, as mudanças são visíveis a quem chama a função. As funções que fazem isso chamam-se modificadores.

`increment`, que acrescenta um dado número de segundos a um objeto `Time`, pode ser escrita naturalmente como um modificador. Aqui está um primeiro esboço:

```python
def increment(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
```

A primeira linha executa a operação básica; o resto lida com os casos especiais que vimos antes.

Esta função está correta? O que acontece se `second` for muito mais que 60?

Neste caso não basta transportar uma vez, temos que continuar fazendo isso até que time.second seja menos de 60. Uma solução é substituir a instrução `if` pela instrução `while`. Isso tornaria a função correta, mas não muito eficiente. Como exercício, escreva uma versão correta de `increment` que não contenha loops.

O que se faz com modificadores também pode ser feito com funções puras. Na verdade, algumas linguagens de programação só permitem funções puras. Há evidências de que os programas que usam funções puras são mais rápidos para serem desenvolvidos e menos propensos a erros que programas que usam modificadores. No entanto, modificadores são convenientes de vez em quando, e os programas funcionais tendem a ser menos eficientes.

De forma geral, recomendo que você escreva funções puras sempre que achar razoável e recorra a modificadores só se houver alguma vantagem clara. Esta abordagem pode ser chamada de __programação funcional__.

Como exercício, escreva uma versão “pura” de increment que cria e retorna um objeto `Time` em vez de alterar o parâmetro.

## 16.4 - Prototipação versus planejamento

O plano de desenvolvimento que estou demonstrando chama-se “protótipo e correção”. Para cada função, escrevi um protótipo que executa o cálculo básico e então testa a função, corrigindo erros no decorrer do caminho.

Esta abordagem pode ser eficaz, especialmente se você ainda não tem uma compreensão profunda do problema. Porém, as correções incrementais podem gerar código que se complica desnecessariamente (pois trata de muitos casos especiais) e pouco confiáveis (já que é difícil saber se todos os erros foram encontrados).

Uma alternativa é o desenvolvimento planejado, no qual a compreensão de alto nível do problema pode facilitar muito a programação. Neste caso, descobre-se que um objeto Time é, na verdade, um número de três dígitos na base 60 (veja http://en.wikipedia.org/wiki/Sexagesimal)! O atributo second é a “coluna de unidades”, o atributo minute é a “coluna dos 60”, e o atributo hour é a “coluna do 3.600”.

Quando escrevemos `add_time` e `increment`, estávamos na verdade fazendo adições na base 60, e por isso transportávamos os resultados de uma coluna à seguinte.

Essa observação sugere outra abordagem para o problema inteiro – podemos converter objetos `Time` em números inteiros e aproveitar o fato de que o computador sabe trabalhar com aritmética de números inteiros.

Aqui está uma função que converte objetos `Time` em números inteiros:


```python
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
```

E aqui está uma função que converte um número inteiro em um `Time` (lembre-se de que `divmod` divide o primeiro argumento pelo segundo e devolve o quociente e o resto como uma tupla):

```python
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
```

Você pode ter que pensar um pouco e fazer alguns testes, para se convencer de que essas funções estão corretas. Um modo de testá-las é ver se `time_to_int(int_to_time(x)) == x` para muitos valores de `x`. Este é um exemplo de uma verificação de consistência.

Uma vez que esteja convencido de que estão corretas, você pode usá-las para reescrever `add_time`:

```python
def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
```

Esta versão é mais curta que a original, e mais fácil de verificar. Como exercício, reescreva `increment` usando `time_to_int` e `int_to_time`.

Em algumas situações, converter da base 60 para a base 10 e de volta é mais difícil que apenas lidar com as horas. A conversão de base é mais abstrata; nossa intuição para lidar com valores temporais é melhor.

No entanto, se tivermos discernimento para lidar com horas como números de base 60 e investirmos esforço em escrever as funções de conversão (`time_to_int` e `int_to_time`), chegamos a um programa que é mais curto, mais fácil de ler e depurar, e mais confiável.

Também é mais fácil acrescentar recursos depois. Por exemplo, imagine subtrair dois objetos `Time` para encontrar a duração entre eles. Uma abordagem ingênua seria implementar a subtração com transporte. Porém, usar funções de conversão seria mais fácil e, provavelmente, mais correto.

Ironicamente, tornar um problema mais difícil (ou mais geral) facilita (porque há menos casos especiais e menos oportunidades de erro).

## 16.5 - Depuração

Um objeto `Time` é bem formado se os valores de `minute` e `second` estiverem entre 0 e 60 (incluindo 0, mas não 60) e se `hour` for positivo. `hour` e `minute` devem ser valores inteiros, mas podemos permitir que `second` tenha uma parte fracionária.

Requisitos como esses chamam-se invariáveis porque sempre devem ser verdadeiros. Para dizer de outra forma, se não forem verdadeiros, algo deu errado.

Escrever código para verificar requisitos invariáveis pode ajudar a descobrir erros e encontrar suas causas. Por exemplo, você pode ter uma função como valid\_time, que receba um objeto Time e retorne False se ele violar um requisito invariável:

```python
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True
```

No início de cada função você pode verificar os argumentos para ter certeza de que são válidos:

```python
def add_time(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')

    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
```

Ou você pode usar uma instrução `assert`, que verifica determinado requisito invariável e cria uma exceção se ela falhar:

```python
def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
```

Instruções assert são úteis porque distinguem o código que lida com condições normais do código que verifica erros.

## 16.6 - Glossário

<dl>
<dt><a id="glos:protótipo e correção" href="#termo:protótipo e correção">protótipo e correção</a></dt>
<dd>Plano de desenvolvimento no qual a escrita do programa parte de um esboço inicial, e depois segue ao teste e correção de erros, conforme sejam encontrados.</dd>

<dt><a id="glos:desenvolvimento planejado" href="#termo:desenvolvimento planejado">desenvolvimento planejado</a></dt>
<dd>Plano de desenvolvimento que implica uma compreensão de alto nível do problema e mais planejamento que desenvolvimento incremental ou desenvolvimento prototipado.</dd>

<dt><a id="glos:função pura" href="#termo:função pura">função pura</a></dt>
<dd>Função que não altera nenhum dos objetos que recebe como argumento. A maior parte das funções puras gera resultado.</dd>

<dt><a id="glos:modificador" href="#termo:modificador">modificador</a></dt>
<dd>Função que modifica um ou vários dos objetos que recebe como argumento. A maior parte dos modificadores são nulos; isto é, retornam None.</dd>

<dt><a id="glos:programação funcional" href="#termo:programação funcional">programação funcional</a></dt>
<dd>Estilo de projeto de programa no qual a maioria das funções são puras.</dd>

<dt><a id="glos:invariável" href="#termo:invariável">invariável</a></dt>
<dd>Condição que sempre deve ser verdadeira durante a execução de um programa.</dd>

<dt><a id="glos:instrução assert" href="#termo:instrução assert">instrução assert</a></dt>
<dd>Instrução que verifica uma condição e levanta uma exceção se esta falhar.</dd>

</dl>

## 16.7 - Exercícios

Os exemplos de código deste capítulo estão disponíveis em https://github.com/AllenDowney/ThinkPython2/raw/master/code/Time1.py; as soluções para os exercícios estão disponíveis em https://github.com/AllenDowney/ThinkPython2/raw/master/code/Time1_soln.py.

### Exercício 16.1

Escreva uma função chamada `mul_time` que receba um objeto `Time` e um número e retorne um novo objeto `Time` que contenha o produto do `Time` original e do número.

Então use `mul_time` para escrever uma função que receba um objeto `Time` representando o tempo até o fim de uma corrida e um número que represente a distância, e retorne um objeto `Time` com o passo médio (tempo por milha).

### Exercício 16.2

O módulo `datetime` fornece objetos `time` que são semelhantes aos objetos `Time` deste capítulo, mas ele oferece um grande conjunto de métodos e operadores. Leia a documentação em http://docs.python.org/3/library/datetime.html.

1. Use o módulo `datetime` para escrever um programa que receba a data atual e exiba o dia da semana.

2. Escreva um programa que receba um aniversário como entrada e exiba a idade do usuário e o número de dias, horas, minutos e segundos até o seu próximo aniversário.

3. Para duas pessoas nascidas em dias diferentes, há um dia em que a idade de uma equivale a duas vezes a da outra. Este é o Dia Duplo delas. Escreva um programa que receba dois aniversários e calcule o Dia Duplo dos aniversariantes.

4. Para um desafio um pouco maior, escreva a versão mais geral que calcule o dia em que uma pessoa é N vezes mais velha que a outra.
