# Capítulo 4: Estudo de caso: projeto de interface

Este capítulo apresenta um estudo de caso que demonstra o processo de criação de funções que operam simultaneamente.

Ele apresenta o módulo turtle, que permite criar imagens usando [_turtle graphics_][1]. O módulo turtle é incluído na maior parte das instalações do Python, mas se estiver executando a linguagem com o PythonAnywhere você não poderá executar os exemplos do turtle (pelo menos não era possível quando escrevi este livro).

Se já tiver instalado o Python no seu computador, você poderá executar os exemplos. Caso não, agora é uma boa hora para instalar. Publiquei instruções no site http://tinyurl.com/thinkpython2e.

Os exemplos de código deste capítulo estão disponíveis em https://github.com/AllenDowney/ThinkPython2/raw/master/code/polygon.py.

## 4.1 - Módulo turtle

Para conferir se você tem o módulo turtle, abra o interpretador do Python e digite:

```python
>>> import turtle
>>> bob = turtle.Turtle()
```

Ao executar este código o programa deve abrir uma nova janela com uma pequena flecha que representa o turtle. Feche a janela.

Crie um arquivo chamado mypolygon.py e digite o seguinte código:

```python
import turtle
bob = turtle.Turtle()
print(bob)
turtle.mainloop()
```

O módulo turtle (com t minúsculo) apresenta uma função chamada Turtle (com T maiúsculo), que cria um objeto Turtle, ao qual atribuímos uma variável chamada bob. Exibir bob faz algo assim:

```python
<turtle.Turtle object at 0xb7bfbf4c>
```

Isto significa que bob se refere a um objeto com o tipo Turtle definido no módulo turtle.

mainloop diz que a janela deve esperar que o usuário faça algo, embora neste caso não haja muito a fazer, exceto fechar a janela.

Uma vez que tenha criado o Turtle, você pode chamar um método para movê-lo pela janela. Método é semelhante a uma função, mas usa uma sintaxe ligeiramente diferente. Por exemplo, para mover o turtle para a frente:

```python
bob.fd(100)
```

O método fd é associado com o objeto turtle, que denominamos bob. Chamar de um método é como fazer um pedido: você está pedindo que bob avance.

O argumento de fd é uma distância em píxeis, então o tamanho real depende da sua tela.

Outros métodos que você pode chamar em um Turtle são bk para mover-se para trás, lt para virar à esquerda e rt para virar à direita. O argumento para lt e rt é um ângulo em graus.

Além disso, cada Turtle segura uma caneta, que está abaixada ou levantada; se a caneta estiver abaixada, o Turtle deixa um rastro quando se move. Os métodos pu e pd representam “caneta para cima” e “caneta para baixo”.

Para desenhar um ângulo reto, acrescente estas linhas ao programa (depois de criar bob e antes de chamar o mainloop):


```python
bob.fd(100)
bob.lt(90)
bob.fd(100)
```

Ao executar este programa, você deveria ver bob mover-se para o leste e depois para o norte, deixando dois segmentos de reta para trás.

Agora altere o programa para desenhar um quadrado. Só siga adiante neste capítulo se ele funcionar adequadamente!

## 4.2 - Repetição simples

Provavelmente você escreveu algo assim:

```python
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
```

Podemos fazer a mesma coisa de forma mais concisa com uma instrução for. Acrescente este exemplo a mypolygon.py e execute-o novamente:

```python
for i in range(4):
    print('Hello!')
```

Você deve ver algo assim:

```python
Hello!
Hello!
Hello!
Hello!
```

Este é o uso mais simples da instrução for; depois veremos mais sobre isso. Mas isso deve ser o suficiente para que você possa reescrever o seu programa de desenhar quadrados. Não continue a leitura até que dê certo.

Aqui está uma instrução for que desenha um quadrado:


```python
for i in range(4):
    bob.fd(100)
    bob.lt(90)
```

A sintaxe de uma instrução for é semelhante à definição de uma função. Tem um cabeçalho que termina em dois pontos e um corpo endentado. O corpo pode conter qualquer número de instruções.

Uma instrução for também é chamada de loop porque o fluxo da execução passa pelo corpo e depois volta ao topo. Neste caso, ele passa pelo corpo quatro vezes.

Esta versão, na verdade, é um pouco diferente do código anterior que desenha quadrados porque faz outra volta depois de desenhar o último lado do quadrado. A volta extra leva mais tempo, mas simplifica o código se fizermos a mesma coisa a cada vez pelo loop. Esta versão também tem o efeito de trazer o turtle de volta à posição inicial, de frente para a mesma direção em que estava.

## 4.3 - Exercícios

A seguir, uma série de exercícios usando TurtleWorld. Eles servem para divertir, mas também têm outro objetivo. Enquanto trabalha neles, pense que objetivo pode ser.

As seções seguintes têm as soluções para os exercícios, mas não olhe até que tenha terminado (ou, pelo menos, tentado).

1. Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado.

        Escreva uma chamada de função que passe bob como um argumento para o square e então execute o programa novamente.

2. Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o comprimento dos lados seja length e então altere a chamada da função para fornecer um segundo argumento. Execute o programa novamente. Teste o seu programa com uma variedade de valores para length.

3. Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados.

        Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.

4. Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados. Teste a sua função com uma série de valores de r.

        Dica: descubra a circunferência do círculo e certifique-se de que length \* n = circumference.

5. Faça uma versão mais geral do circle chamada arc, que receba um parâmetro adicional de angle, para determinar qual fração do círculo deve ser desenhada. angle está em unidades de graus, então quando angle=360, o arc deve desenhar um círculo completo.

## 4.4 - Encapsulamento

O primeiro exercício pede que você ponha seu código para desenhar quadrados em uma definição de função e então chame a função, passando o turtle como parâmetro. Aqui está uma solução:

```python
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)
```

As instruções mais internas, fd e lt, são endentadas duas vezes para mostrar que estão dentro do loop for, que está dentro da definição da função. A linha seguinte, square(bob), está alinhada à margem esquerda, o que indica tanto o fim do loop for como da definição de função.

Dentro da função, o t indica o mesmo turtle bob, então t.lt (90) tem o mesmo efeito que bob.lt (90). Neste caso, por que não chamar o parâmetro bob? A ideia é que t pode ser qualquer turtle, não apenas bob, então você pode criar um segundo turtle e passá-lo como argumento ao square:

```python
alice = turtle.Turtle()
square(alice)
```

Incluir uma parte do código em uma função chama-se encapsulamento. Um dos benefícios do encapsulamento é que ele atribui um nome ao código, o que serve como uma espécie de documentação. Outra vantagem é que se você reutilizar o código, é mais conciso chamar uma função duas vezes que copiar e colar o corpo!

## 4.5 - Generalização

O próximo passo é acrescentar um parâmetro length ao square. Aqui está uma solução:

```python
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 100)
```

Acrescentar um parâmetro a uma função chama-se generalização porque ele torna a função mais geral: na versão anterior, o quadrado é sempre do mesmo tamanho; nesta versão, pode ser de qualquer tamanho.

O próximo passo também é uma generalização. Em vez de desenhar quadrados, polygon desenha polígonos regulares com qualquer número de lados. Aqui está uma solução:

```python
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob, 7, 70)
```

Este exemplo desenha um polígono de 7 lados, cada um de comprimento 70.

Se estiver usando Python 2, o valor do angle poderia estar errado por causa da divisão de número inteiro. Uma solução simples é calcular angle = 360.0 / n. Como o numerador é um número de ponto flutuante, o resultado é em ponto flutuante.

Quando uma função tem vários argumentos numéricos, é fácil esquecer o que eles são ou a ordem na qual eles devem estar. Neste caso, muitas vezes é uma boa ideia incluir os nomes dos parâmetros na lista de argumentos:

```python
polygon (bob, n=7, length=70)
```

Esses são os argumentos de palavra-chave porque incluem os nomes dos parâmetros como “palavras-chave” (para não confundir com palavras-chave do Python, tais como while e def).

Esta sintaxe torna o programa mais legível. Também é uma lembrança sobre como os argumentos e os parâmetros funcionam: quando você chama uma função, os argumentos são atribuídos aos parâmetros.

## 4.6 - Projeto da interface

O próximo passo é escrever circle, que recebe um raio r, como parâmetro. Aqui está uma solução simples que usa o polygon para desenhar um polígono de 50 lados:

```python
import math
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
```

A primeira linha calcula a circunferência de um círculo com o raio r usando a fórmula 2πr. Já que usamos math.pi, temos que importar math. Por convenção, instruções import normalmente ficam no início do script.

n é o número de segmentos de reta na nossa aproximação de um círculo, então length é o comprimento de cada segmento. Assim, polygon desenha um polígono 50 lados que se aproxima de um círculo com o raio r.

Uma limitação desta solução é que n é uma constante. Para círculos muito grandes, os segmentos de reta são longos demais, e para círculos pequenos, perdemos tempo desenhando segmentos muito pequenos. Uma solução seria generalizar a função tomando n como parâmetro. Isso daria ao usuário (seja quem for que chame circle) mais controle, mas a interface seria menos limpa.

A interface de uma função é um resumo de como ela é usada: Quais são os parâmetros? O que a função faz? E qual é o valor de retorno? Uma interface é “limpa” se permitir à pessoa que a chama fazer o que quiser sem ter que lidar com detalhes desnecessários.

Neste exemplo, r pertence à interface porque especifica o círculo a ser desenhado. n é menos adequado porque pertence aos detalhes de como o círculo deve ser apresentado.

Em vez de poluir a interface, é melhor escolher um valor adequado para n, dependendo da circumference:

```python
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)
```

Neste ponto, o número de segmentos é um número inteiro próximo a circumference/3, então o comprimento de cada segmento é aproximadamente 3, pequeno o suficiente para que os círculos fiquem bons, mas grandes o suficiente para serem eficientes e aceitáveis para círculos de qualquer tamanho.

<a id="sec:4.7 - Refatoração"></a>
## 4.7 - Refatoração

Quando escrevi circle, pude reutilizar polygon porque um polígono de muitos lados é uma boa aproximação de um círculo. Mas o arc não é tão cooperativo; não podemos usar polygon ou circle para desenhar um arco.

Uma alternativa é começar com uma cópia de polygon e transformá-la em arc. O resultado poderia ser algo assim:

```python
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
```

A segunda metade desta função parece com a do polygon, mas não é possível reutilizar o polygon sem mudar a interface. Poderíamos generalizar polygon para receber um ângulo como um terceiro argumento, mas então polygon não seria mais um nome adequado! Em vez disso, vamos chamar a função mais geral de polyline:

```python
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
```

Agora podemos reescrever polygon e arc para usar polyline:

```python
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
```

Finalmente, podemos reescrever circle para usar arc:

```python
def circle(t, r):
    arc(t, r, 360)
```

Este processo – recompor um programa para melhorar interfaces e facilitar a reutilização do código – é chamado de refatoração. Neste caso, notamos que houve código semelhante em arc e polygon, então nós o “fatoramos” no polyline.

Se tivéssemos planejado, poderíamos ter escrito polyline primeiro e evitado a refatoração, mas muitas vezes não sabemos o suficiente já no início de um projeto para projetar todas as interfaces. Quando começarmos a escrever código, entenderemos melhor o problema. Às vezes, a refatoração é um sinal de que aprendemos algo.

## 4.8 - Um plano de desenvolvimento

Um plano de desenvolvimento é um processo para escrever programas. O processo que usamos neste estudo de caso é “encapsulamento e generalização”. Os passos deste processo são:

1. Comece escrevendo um pequeno programa sem definições de função.

2. Uma vez que o programa esteja funcionando, identifique uma parte coerente dele, encapsule essa parte em uma função e dê um nome a ela.

3. Generalize a função acrescentando os parâmetros adequados.

4. Repita os passos 1-3 até que tenha um conjunto de funções operantes. Copie e cole o código operante para evitar a redigitação (e redepuração).

5. Procure oportunidades de melhorar o programa pela refatoração. Por exemplo, se você tem um código semelhante em vários lugares, pode ser uma boa ideia fatorá-lo em uma função geral adequada.

Este processo tem algumas desvantagens – veremos alternativas mais tarde – mas pode ser útil se você não souber de antemão como dividir o programa em funções. Esta abordagem permite criar o projeto no decorrer do trabalho.

## 4.9 - docstring

Uma docstring é uma string no início de uma função que explica a interface (“doc” é uma abreviação para “documentação”). Aqui está um exemplo:

```python
def polyline(t, n, length, angle):
    """Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
```

Por convenção, todas as docstrings têm aspas triplas, também conhecidas como strings multilinha porque as aspas triplas permitem que a string se estenda por mais de uma linha.

É conciso, mas contém a informação essencial que alguém precisaria para usar esta função. Explica sucintamente o que a função faz (sem entrar nos detalhes de como o faz). Explica que efeito cada parâmetro tem sobre o comportamento da função e o tipo que cada parâmetro deve ser (se não for óbvio).

Escrever este tipo de documentação é uma parte importante do projeto da interface. Uma interface bem projetada deve ser simples de explicar; se não for assim, talvez a interface possa ser melhorada.

## 4.10 - Depuração

Uma interface é como um contrato entre uma função e quem a chama. Quem chama concorda em fornecer certos parâmetros e a função concorda em fazer certa ação.

Por exemplo, polyline precisa de quatro argumentos: t tem que ser um Turtle; n tem que ser um número inteiro; length deve ser um número positivo; e o angle tem que ser um número, que se espera estar em graus.

Essas exigências são chamadas de precondições porque se supõe que sejam verdade antes que a função seja executada. De forma inversa, as condições no fim da função são pós-condições. As pós-condições incluem o efeito desejado da função (como o desenho de segmentos de reta) e qualquer efeito colateral (como mover o Turtle ou fazer outras mudanças).

Precondições são responsabilidade de quem chama. Se quem chama violar uma precondição (adequadamente documentada!) e a função não funcionar corretamente, o problema está nesta pessoa, não na função.

Se as precondições forem satisfeitas e as pós-condições não forem, o problema está na função. Se as suas precondições e pós-condições forem claras, elas podem ajudar na depuração.

## 4.11 - Glossário

<dl>
<dt><a id="glos:método" href="#termo:método">método</a></dt>
<dd>Uma função associada a um objeto e chamada usando a notação de ponto.</dd>

<dt><a id="glos:loop" href="#termo:loop">loop</a></dt>
<dd>Parte de um programa que pode ser executada repetidamente.</dd>

<dt><a id="glos:encapsulamento" href="#termo:encapsulamento">encapsulamento</a></dt>
<dd>O processo de transformar uma sequência de instruções em uma definição de função.</dd>

<dt><a id="glos:generalização" href="#termo:generalização">generalização</a></dt>
<dd>O processo de substituir algo desnecessariamente específico (como um número) por algo adequadamente geral (como uma variável ou parâmetro).</dd>

<dt><a id="glos:argumento de palavra-chave" href="#termo:argumento de palavra-chave">argumento de palavra-chave</a></dt>
<dd>Um argumento que inclui o nome do parâmetro como uma “palavra-chave”.</dd>

<dt><a id="glos:interface" href="#termo:interface">interface</a></dt>
<dd>Uma descrição de como usar uma função, incluindo o nome e as descrições dos argumentos e do valor de retorno.</dd>

<dt><a id="glos:refatoração" href="#termo:refatoração">refatoração</a></dt>
<dd>O processo de alterar um programa funcional para melhorar a interface de funções e outras qualidades do código.</dd>

<dt><a id="glos:plano de desenvolvimento" href="#termo:plano de desenvolvimento">plano de desenvolvimento</a></dt>
<dd>Um processo de escrever programas.</dd>

<dt><a id="glos:docstring" href="#termo:docstring">docstring</a></dt>
<dd>Uma string que aparece no início de uma definição de função para documentar a interface da função.</dd>

<dt><a id="glos:precondição" href="#termo:precondição">precondição</a></dt>
<dd>Uma exigência que deve ser satisfeita por quem chama a função, antes de executá-la.</dd>

<dt><a id="glos:pós-condição" href="#termo:pós-condição">pós-condição</a></dt>
<dd>Uma exigência que deve ser satisfeita pela função antes que ela seja encerrada.</dd>

</dl>

## 4.12 - Exercícios

### Exercício 4.1

Baixe o código deste capítulo no site https://github.com/AllenDowney/ThinkPython2/raw/master/code/polygon.py.

1. Desenhe um diagrama da pilha que mostre o estado do programa enquanto executa circle (bob, radius). Você pode fazer a aritmética à mão ou acrescentar instruções print ao código.

2. A versão de `arc` na seção <a href="#sec:4.7 - Refatoração">4.7 - Refatoração</a> não é muito precisa porque a aproximação linear do círculo está sempre do lado de fora do círculo verdadeiro. Consequentemente, o Turtle acaba ficando alguns píxeis de distância do destino correto. Minha solução mostra um modo de reduzir o efeito deste erro. Leia o código e veja se faz sentido para você. Se desenhar um diagrama, poderá ver como funciona.

### Exercício 4.2

Escreva um conjunto de funções adequadamente geral que possa desenhar flores como as da Figura 4.1.

![Figura 4.1 – Flores de tartaruga.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_0401.png)
<br>_Figura 4.1 – Flores de tartaruga._

Solução: https://github.com/AllenDowney/ThinkPython2/raw/master/code/flower.py, também exige https://github.com/AllenDowney/ThinkPython2/raw/master/code/polygon.py.

### Exercício 4.3

Escreva um conjunto de funções adequadamente geral que possa desenhar formas como as da Figura 4.2.

![Figura 4.2 – Tortas de tartaruga.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_0402.png)
<br>_Figura 4.2 – Tortas de tartaruga._

Solução: https://github.com/AllenDowney/ThinkPython2/raw/master/code/pie.py.


### Exercício 4.4

As letras do alfabeto podem ser construídas a partir de um número moderado de elementos básicos, como linhas verticais e horizontais e algumas curvas. Crie um alfabeto que possa ser desenhado com um número mínimo de elementos básicos e então escreva funções que desenhem as letras.

Você deve escrever uma função para cada letra, com os nomes draw\_a, draw\_b etc., e colocar suas funções em um arquivo chamado letters.py. Você pode baixar uma “máquina de escrever de turtle” no site https://github.com/AllenDowney/ThinkPython2/raw/master/code/typewriter.py para ajudar a testar o seu código.

Você pode ver uma solução no site https://github.com/AllenDowney/ThinkPython2/raw/master/code/letters.py; ela também exige https://github.com/AllenDowney/ThinkPython2/raw/master/code/polygon.py.

### Exercício 4.5

Leia sobre espirais em https://pt.wikipedia.org/wiki/Espiral; então escreva um programa que desenhe uma espiral de Arquimedes (ou um dos outros tipos).

[1] _turtle graphics_ ou gráficos de tartaruga é o sistema de desenho popularizado pela linguagem Logo, onde os comandos movimentam um cursor triangular pela tela, conhecido como _turtle_ ou tartaruga. A tartaruga deixa um rastro à medida que é movimentada, e é com esses rastros que se forma um desenho. Diferente dos sistemas usuais de desenho em computação gráfica, o sistema _turtle graphics_ não exige o uso de coordenadas cartesianas.
