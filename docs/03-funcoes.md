# Capítulo 3: Funções

No contexto da programação, uma função é uma sequência nomeada de instruções que executa uma operação de computação. Ao definir uma função, você especifica o nome e a sequência de instruções. Depois, pode “chamar” a função pelo nome.

Chamada de função

Já vimos um exemplo de chamada de função:

&gt;&gt;&gt; type(42)

&lt;class 'int'&gt;

O nome da função é type. A expressão entre parênteses é chamada de argumento da função. Para esta função, o resultado é o tipo do argumento.

É comum dizer que uma função “recebe” um argumento e “retorna” um resultado. O resultado também é chamado de valor de retorno.

O Python oferece funções que convertem valores de um tipo em outro. A função int recebe qualquer valor e o converte em um número inteiro, se for possível, ou declara que há um erro:

&gt;&gt;&gt; int('32')

32

&gt;&gt;&gt; int('Hello')

ValueError: invalid literal for int(): Hello

int pode converter valores de ponto flutuante em números inteiros, mas não faz arredondamentos; ela apenas corta a parte da fração:

&gt;&gt;&gt; int(3.99999)

3

&gt;&gt;&gt; int(-2.3)

-2

float converte números inteiros e strings em números de ponto flutuante:

&gt;&gt;&gt; float(32)

32.0

&gt;&gt;&gt; float('3.14159')

3.14159

Finalmente, str converte o argumento em uma string:

&gt;&gt;&gt; str(32)

'32'

&gt;&gt;&gt; str(3.14159)

'3.14159'

Funções matemáticas

O Python tem um módulo matemático que oferece a maioria das funções matemáticas comuns. Um módulo é um arquivo que contém uma coleção de funções relacionadas.

Antes que possamos usar as funções em um módulo, precisamos importá-lo com uma instrução de importação:

&gt;&gt;&gt; import math

Esta instrução cria um objeto de módulo chamado math (matemática). Ao se exibir o objeto de módulo, são apresentadas informações sobre ele:

&gt;&gt;&gt; math

&lt;module 'math' (built-in)&gt;

O objeto de módulo contém as funções e variáveis definidas no módulo. Para acessar uma das funções, é preciso especificar o nome do módulo e o nome da função, separados por um ponto. Este formato é chamado de notação de ponto.

&gt;&gt;&gt; ratio = signal\_power / noise\_power

&gt;&gt;&gt; decibels = 10 \* math.log10(ratio)

&gt;&gt;&gt; radians = 0.7

&gt;&gt;&gt; height = math.sin(radians)

O primeiro exemplo usa math.log10 para calcular a proporção de sinal e de ruído em decibéis (assumindo que signal\_power e noise\_power tenham sido definidos). O módulo matemático também oferece a função log, que calcula logaritmos de base e.

O segundo exemplo encontra o seno de radians. O nome da variável indica que sin e outras funções trigonométricas (cos, tan etc.) recebem argumentos em radianos. Para converter graus em radianos, divida por 180 e multiplique por π:

&gt;&gt;&gt; degrees = 45

&gt;&gt;&gt; radians = degrees / 180.0 \* math.pi

&gt;&gt;&gt; math.sin(radians)

0.707106781187

A expressão math.pi recebe a variável pi do módulo matemático. Seu valor é uma aproximação de ponto flutuante de π, com precisão aproximada de 15 dígitos.

Se souber trigonometria, você pode verificar o resultado anterior comparando-o com a raiz quadrada de 2 dividida por 2:

&gt;&gt;&gt; math.sqrt(2) / 2.0

0.707106781187

Composição

Por enquanto, falamos sobre os elementos de um programa – variáveis, expressões e instruções – de forma isolada, mas não sobre como combiná-los.

Uma das características mais úteis das linguagens de programação é a sua capacidade de usar pequenos blocos de montar para compor programas. Por exemplo, o argumento de uma função pode ser qualquer tipo de expressão, inclusive operadores aritméticos:

x = math.sin(degrees / 360.0 \* 2 \* math.pi)

E até chamadas de função:

x = math.exp(math.log(x+1))

É possível colocar um valor, uma expressão arbitrária, em quase qualquer lugar. Com uma exceção: o lado esquerdo de uma instrução de atribuição tem que ser um nome de variável. Qualquer outra expressão no lado esquerdo é um erro de sintaxe (veremos exceções a esta regra depois).

&gt;&gt;&gt; minutes = hours \* 60                \# correto

&gt;&gt;&gt; hours \* 60 = minutes                \# errado!

SyntaxError: can't assign to operator

Como acrescentar novas funções

Por enquanto, só usamos funções que vêm com o Python, mas também é possível acrescentar novas funções. Uma definição de função especifica o nome de uma nova função e a sequência de instruções que são executadas quando a função é chamada.

Aqui está um exemplo:

def print\_lyrics():

    print("I'm a lumberjack, and I'm okay.")

    print("I sleep all night and I work all day.")

def é uma palavra-chave que indica uma definição de função. O nome da função é print\_lyrics. As regras para nomes de função são as mesmas que as das variáveis: letras, números e sublinhado são legais, mas o primeiro caractere não pode ser um número. Não podemos usar uma palavra-chave como nome de uma função e devemos evitar ter uma variável e uma função com o mesmo nome.

Os parênteses vazios depois do nome indicam que esta função não usa argumentos.

A primeira linha da definição de função chama-se cabeçalho; o resto é chamado de corpo. O cabeçalho precisa terminar em dois pontos e o corpo precisa ser endentado. Por convenção, a endentação sempre é de quatro espaços. O corpo pode conter qualquer número de instruções.

As strings nas instruções de exibição são limitadas por aspas duplas. As aspas simples e as aspas duplas fazem a mesma coisa; a maior parte das pessoas usa aspas simples apenas nos casos em que aspas simples (que também são apóstrofes) aparecem na string.

Todas as aspas (simples e duplas) devem ser “aspas retas”, normalmente encontradas ao lado do Enter no teclado. “Aspas curvas”, como as desta oração, não são legais no Python.

Se digitar uma definição de função no modo interativo, o interpretador exibe pontos (...) para mostrar que a definição não está completa:

&gt;&gt;&gt; def print\_lyrics():

...     print("I'm a lumberjack, and I'm okay.")

...     print("I sleep all night and I work all day.")

...

Para terminar a função, é preciso inserir uma linha vazia.

A definição de uma função cria um objeto de função, que tem o tipo function:

&gt;&gt;&gt; print(print\_lyrics)

&lt;function print\_lyrics at 0xb7e99e9c&gt;

&gt;&gt;&gt; type(print\_lyrics)

&lt;class 'function'&gt;

A sintaxe para chamar a nova função é a mesma que a das funções integradas:

&gt;&gt;&gt; print\_lyrics()

I'm a lumberjack, and I'm okay.

I sleep all night and I work all day.

Uma vez que a função tenha sido definida, é possível usá-la dentro de outra função. Por exemplo, para repetir o refrão anterior, podemos escrever uma função chamada repeat\_lyrics:

def repeat\_lyrics():

    print\_lyrics()

    print\_lyrics()

E daí chamar repeat\_lyrics:

&gt;&gt;&gt; repeat\_lyrics()

I'm a lumberjack, and I'm okay.

I sleep all night and I work all day.

I'm a lumberjack, and I'm okay.

I sleep all night and I work all day.

Mas a canção não é bem assim.

Uso e definições

Juntando fragmentos de código da seção anterior, o programa inteiro fica assim:

def print\_lyrics():

    print("I'm a lumberjack, and I'm okay.")

    print("I sleep all night and I work all day.")

def repeat\_lyrics():

    print\_lyrics()

    print\_lyrics()

repeat\_lyrics()

Este programa contém duas definições de função: print\_lyrics e repeat\_lyrics. As definições de função são executadas como outras instruções, mas o efeito é criar objetos de função. As instruções dentro da função não são executadas até que a função seja chamada, e a definição de função não gera nenhuma saída.

Como poderíamos esperar, é preciso criar uma função antes de executá-la. Em outras palavras, a definição de função tem que ser executada antes que a função seja chamada.

Como exercício, mova a última linha deste programa para o topo, para que a chamada de função apareça antes das definições. Execute o programa e veja qual é a mensagem de erro que aparece.

Agora mova a chamada de função de volta para baixo e mova a definição de print\_lyrics para depois da definição de repeat\_lyrics. O que acontece quando este programa é executado?

Fluxo de execução

Para garantir que uma função seja definida antes do seu primeiro uso, é preciso saber a ordem na qual as instruções serão executadas. Isso é chamado de fluxo de execução.

A execução sempre começa na primeira instrução do programa. As instruções são executadas uma após a outra, de cima para baixo.

As definições de função não alteram o fluxo da execução do programa, mas lembre-se de que as instruções dentro da função não são executadas até a função ser chamada.

Uma chamada de função é como um desvio no fluxo de execução. Em vez de ir à próxima instrução, o fluxo salta para o corpo da função, executa as instruções lá, e então volta para continuar de onde parou.

Parece bastante simples, até você lembrar que uma função pode chamar outra. Enquanto estiver no meio de uma função, o programa pode ter que executar as instruções em outra função. Então, enquanto estiver executando a nova função, o programa pode ter que executar mais uma função!

Felizmente, o Python é bom em não perder o fio da meada, então cada vez que uma função é concluída, o programa continua de onde parou na função que o chamou. Quando chega no fim do programa, ele é encerrado.

Resumindo, nem sempre se deve ler um programa de cima para baixo. Às vezes faz mais sentido seguir o fluxo de execução.

Parâmetros e argumentos

Algumas funções que vimos exigem argumentos. Por exemplo, ao chamar math.sin, você usa um número como argumento. Algumas funções exigem mais de um argumento: o math.pow exige dois, a base e o expoente.

Dentro da função, os argumentos são atribuídos a variáveis chamadas parâmetros. Aqui está a definição de uma função que precisa de um argumento:

def print\_twice(bruce):

    print(bruce)

    print(bruce)

Esta função atribui o argumento a um parâmetro chamado bruce. Quando a função é chamada, ela exibe o valor do parâmetro (seja qual for) duas vezes.

Esta função funciona com qualquer valor que possa ser exibido:

&gt;&gt;&gt; print\_twice('Spam')

Spam

Spam

&gt;&gt;&gt; print\_twice(42)

42

42

&gt;&gt;&gt; print\_twice(math.pi)

3.14159265359

3.14159265359

As mesmas regras de composição usadas para funções integradas também são aplicadas a funções definidas pelos programadores, então podemos usar qualquer tipo de expressão como argumento para print\_twice:

&gt;&gt;&gt; print\_twice('Spam '\*4)

Spam Spam Spam Spam

Spam Spam Spam Spam

&gt;&gt;&gt; print\_twice(math.cos(math.pi))

-1.0

-1.0

O argumento é avaliado antes de a função ser chamada. Então, nos exemplos, as expressões 'Spam '\*4 e math.cos (math.pi) só são avaliadas uma vez.

Você também pode usar uma variável como argumento:

&gt;&gt;&gt; michael = 'Eric, the half a bee.'

&gt;&gt;&gt; print\_twice(michael)

Eric, the half a bee.

Eric, the half a bee.

O nome da variável que passamos como argumento (michael) não tem nada a ver com o nome do parâmetro (bruce). Não importa que o valor tenha sido chamado de volta (em quem chama); aqui em print\_twice, chamamos todo mundo de bruce.

As variáveis e os parâmetros são locais

Quando você cria uma variável dentro de uma função, ela é local, ou seja, ela só existe dentro da função. Por exemplo:

def cat\_twice(part1, part2):

    cat = part1 + part2

    print\_twice(cat)

Esta função recebe dois argumentos, concatena-os e exibe o resultado duas vezes. Aqui está um exemplo que a usa:

&gt;&gt;&gt; line1 = 'Bing tiddle '

&gt;&gt;&gt; line2 = 'tiddle bang.'

&gt;&gt;&gt; cat\_twice(line1, line2)

Bing tiddle tiddle bang.

Bing tiddle tiddle bang.

Quando cat\_twice é encerrada, a variável cat é destruída. Se tentarmos exibi-la, recebemos uma exceção:

&gt;&gt;&gt; print(cat)

NameError: name 'cat' is not defined

Os parâmetros também são locais. Por exemplo, além de print\_twice, não existe o bruce.

Diagrama da pilha

Para monitorar quais variáveis podem ser usadas e onde, é uma boa ideia desenhar um diagrama da pilha. Assim como diagramas de estado, os diagramas da pilha mostram o valor de cada variável, mas também mostram a função à qual cada variável pertence.

Cada função é representada por um frame (quadro). Um frame é uma caixa com o nome de uma função junto a ele e os parâmetros e as variáveis da função dentro dele. O diagrama da pilha para o exemplo anterior é exibido na Figura 3.1.

Figura 3.1 – Diagrama da pilha.

Os frames são organizados em uma pilha que indica qual função que foi chamada por outra, e assim por diante. Neste exemplo, print\_twice foi chamada por cat\_twice e cat\_twice foi chamada por \_\_main\_\_, que é um nome especial para o frame na posição mais proeminente. Quando você cria uma variável fora de qualquer função, ela pertence a \_\_main\_\_.

Cada parâmetro refere-se ao mesmo valor como seu argumento correspondente. Desta forma, part1 tem o mesmo valor que line1, part2 tem o mesmo valor que line2 e bruce tem o mesmo valor que cat.

Se ocorrer um erro durante uma chamada de função, o Python exibe o nome da função, o nome da função que a chamou e o nome da função que chamou esta função por sua vez, voltando até \_\_ main \_\_.

Por exemplo, se você tentar acessar cat de dentro de print\_twice, receberá uma mensagem de NameError:

Traceback (innermost last):

  File "test.py", line 13, in \_\_main\_\_

    cat\_twice(line1, line2)

  File "test.py", line 5, in cat\_twice

    print\_twice(cat)

  File "test.py", line 9, in print\_twice

    print(cat)

NameError: name 'cat' is not defined

Esta lista de funções é chamada de traceback. Ela mostra o arquivo do programa em que o erro ocorreu e em que linha, e quais funções estavam sendo executadas no momento. Ele também mostra a linha de código que causou o erro.

A ordem das funções no traceback é a mesma que a ordem dos frames no diagrama da pilha. A função que está sendo executada no momento está no final.

Funções com resultado e funções nulas

Algumas funções que usamos, como as funções matemáticas, devolvem resultados; por falta de um nome melhor, vou chamá-las de funções com resultados. Outras funções, como print\_twice, executam uma ação, mas não devolvem um valor. Elas são chamadas de funções nulas.

Quando você chama uma função com resultado, quase sempre quer fazer algo com o resultado; por exemplo, você pode atribui-lo a uma variável ou usá-la como parte de uma expressão:

x = math.cos(radians)

golden = (math.sqrt(5) + 1) / 2

Quando você chama uma função no modo interativo, o Python exibe o resultado:

&gt;&gt;&gt; math.sqrt(5)

2.2360679774997898

Mas em um script, se você chamar uma função com resultado e mais nada, o valor de retorno é perdido para sempre!

math.sqrt(5)

Este script calcula a raiz quadrada de 5, mas como não armazena ou exibe o resultado, não é muito útil.

As funções nulas podem exibir algo na tela ou ter algum outro efeito, mas não têm um valor de retorno. Se você atribuir o resultado a uma variável, recebe um valor especial chamado None:

&gt;&gt;&gt; result = print\_twice('Bing')

Bing

Bing

&gt;&gt;&gt; print(result)

None

O valor None não é o mesmo que a string 'None'. É um valor especial que tem seu próprio tipo:

&gt;&gt;&gt; print(type(None))

&lt;class 'NoneType'&gt;

As funções que apresentamos por enquanto são todas nulas. Vamos apresentar funções com resultado mais adiante.

Por que funções?

Caso o objetivo de dividir um programa em funções não esteja claro, saiba que na verdade há várias razões:

•        Criar uma nova função dá a oportunidade de nomear um grupo de instruções, o que deixa o seu programa mais fácil de ler e de depurar.

•        As funções podem tornar um programa menor, eliminando o código repetitivo. Depois, se fizer alguma alteração, basta fazê-la em um lugar só.

•        Dividir um programa longo em funções permite depurar as partes uma de cada vez e então reuni-las em um conjunto funcional.

•        As funções bem projetadas muitas vezes são úteis para muitos programas. Uma vez que escreva e depure uma, você pode reutilizá-la.

Depuração

Uma das habilidades mais importantes que você vai aprender é a depuração. Embora possa ser frustrante, a depuração é uma das partes mais intelectualmente ricas, desafiadoras e interessantes da programação.

De certa forma, depurar é similar ao trabalho de um detetive. Você tem pistas e precisa inferir os processos e eventos que levaram aos resultados exibidos.

A depuração também é como ciência experimental. Uma vez que você tenha uma ideia sobre o que está errado, basta alterar o programa e tentar novamente. Se a sua hipótese estava correta, você pode prever o resultado da alteração e chegar um passo mais perto de um programa funcional. Se a sua hipótese estava errada, é preciso criar outra. Como dizia Sherlock Holmes, “Quando se elimina o impossível, o que sobra, por mais incrível que pareça, só pode ser a verdade.” (A. Conan Doyle, O signo dos quatro).

Para algumas pessoas, programar e depurar são a mesma coisa. Isto é, a programação é o processo de depurar gradualmente um programa até que ele faça o que o programador quer. A ideia é que você comece com um programa funcional e faça pequenas alterações, depurando-as no decorrer do trabalho.

Por exemplo, o Linux é um sistema operacional que contém milhões de linhas de código, mas começou como um programa simples que Linus Torvalds usava para explorar o chip Intel 80386. Segundo Larry Greenfield, “Um dos primeiros projetos de Linus foi um programa que alternaria entre a exibição de AAAA e BBBB. Mais tarde isso se desenvolveu até virar o Linux.” (Guia do usuário de Linux versão beta 1).

Glossário

função:

Uma sequência nomeada de declarações que executa alguma operação útil. As funções podem receber argumentos ou não e podem ou não produzir algum resultado.

definição de função:

Uma instrução que cria uma função nova, especificando seu nome, parâmetros e as instruções que contém.

objeto da função:

Um valor é criado por uma definição de função. O nome da função é uma variável que se refere a um objeto de função.

cabeçalho:

A primeira linha de uma definição de função.

corpo:

A sequência de instruções dentro de uma definição de função.

parâmetro:

Um nome usado dentro de uma função para se referir ao valor passado como argumento.

chamada de função:

Uma instrução que executa uma função. É composta pelo nome da função seguido de uma lista de argumentos entre parênteses.

argumento:

Um valor apresentado a uma função quando a função é chamada. Este valor é atribuído ao parâmetro correspondente na função.

variável local:

Uma variável definida dentro de uma função. Uma variável local só pode ser usada dentro da sua função.

valor de retorno:

O resultado de uma função. Se uma chamada de função for usada como uma expressão, o valor de retorno é o valor da expressão.

função com resultado:

Uma função que devolve um valor.

função nula:

Uma função que sempre devolve None.

None:

Um valor especial apresentado por funções nulas.

módulo:

Um arquivo que contém uma coleção de funções relacionadas e outras definições.

instrução de importação:

Uma instrução que lê um arquivo de módulo e cria um objeto de módulo.

objeto de módulo:

Um valor criado por uma instrução import que oferece acesso aos valores definidos em um módulo.

notação de ponto:

A sintaxe para chamar uma função em outro módulo especificando o nome do módulo seguido de um ponto e o nome da função.

composição:

O uso de uma expressão como parte de uma expressão maior ou de uma instrução como parte de uma instrução maior.

fluxo de execução:

A ordem na qual as instruções são executadas.

diagrama da pilha:

Representação gráfica de uma pilha de funções, suas variáveis e os valores a que se referem.

frame:

Uma caixa em um diagrama da pilha que representa uma chamada de função. Contém as variáveis locais e os parâmetros da função.

traceback:

Lista das funções que estão sendo executadas, exibidas quando ocorre uma exceção.

Exercícios

Exercício 3.1

Escreva uma função chamada right\_justify, que receba uma string chamada s como parâmetro e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:

&gt;&gt;&gt; right\_justify('monty')

                                                                       monty

Dica: Use concatenação de strings e repetição. Além disso, o Python oferece uma função integrada chamada len, que apresenta o comprimento de uma string, então o valor de len('monty') é 5.

Exercício 3.2

Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como argumento. Por exemplo, do\_twice é uma função que toma um objeto de função como argumento e o chama duas vezes:

def do\_twice(f):

    f()

    f()

Aqui está um exemplo que usa do\_twice para chamar uma função chamada print\_spam duas vezes:

def print\_spam():

    print('spam')

do\_twice(print\_spam)

1.        Digite este exemplo em um script e teste-o.

2.        Altere do\_twice para que receba dois argumentos, um objeto de função e um valor, e chame a função duas vezes, passando o valor como um argumento.

3.        Copie a definição de print\_twice que aparece anteriormente neste capítulo no seu script.

4.        Use a versão alterada de do\_twice para chamar print\_twice duas vezes, passando 'spam' como um argumento.

5.        Defina uma função nova chamada do\_four que receba um objeto de função e um valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve haver só duas afirmações no corpo desta função, não quatro.

Solução: http://thinkpython2.com/code/do\_four.py.

Exercício 3.3

Nota: Este exercício deve ser feito usando-se apenas as instruções e os outros recursos que aprendemos até agora.

1.        Escreva uma função que desenhe uma grade como a seguinte:

        + - - - - + - - - - +

        |         |         |

        |         |         |

        |         |         |

        |         |         |

        + - - - - + - - - - +

        |         |         |

        |         |         |

        |         |         |

        |         |         |

        + - - - - + - - - - +

        Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência de valores separados por vírgula:

        print('+', '-')

        Por padrão, print avança para a linha seguinte, mas podemos ignorar esse comportamento e inserir um espaço no fim, desta forma:

        print('+', end=' ')

        print('-')

        A saída dessas instruções é '+ -'.

        Uma instrução print sem argumento termina a linha atual e vai para a próxima linha.

2.        Escreva uma função que desenhe uma grade semelhante com quatro linhas e quatro colunas.

Solução: http://thinkpython2.com/code/grid.py. Crédito: Este exercício é baseado em outro apresentado por Oualline, em Practical C Programming, Third Edition, O’Reilly Media, 1997.

