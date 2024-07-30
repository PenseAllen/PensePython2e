# Capítulo 15: Classes e objetos

A esta altura você já sabe como usar funções para organizar código e tipos integrados para organizar dados. O próximo passo é aprender “programação orientada a objeto”, que usa tipos definidos pelos programadores para organizar tanto o código quanto os dados. A programação orientada a objeto é um tópico abrangente; será preciso passar por alguns capítulos para abordar o tema.

Os exemplos de código deste capítulo estão disponíveis em https://github.com/AllenDowney/ThinkPython2/raw/master/code/Point1.py; as soluções para os exercícios estão disponíveis em https://github.com/AllenDowney/ThinkPython2/raw/master/code/Point1_soln.py.

## 15.1 - Tipos definidos pelos programadores

Já usamos muitos tipos integrados do Python; agora vamos definir um tipo próprio. Como exemplo, criaremos um tipo chamado `Point`, que representa um ponto no espaço bidimensional.

Na notação matemática, os pontos muitas vezes são escritos entre parênteses, com uma vírgula separando as coordenadas. Por exemplo, (0,0) representa a origem e (x, y) representa o ponto que está x unidades à direita e y unidades acima da origem.

Há várias formas para representar pontos no Python:

* Podemos armazenar as coordenadas separadamente em duas variáveis, x e y.

* Podemos armazenar as coordenadas como elementos em uma lista ou tupla.

* Podemos criar um tipo para representar pontos como objetos.

Criar um tipo é mais complicado que outras opções, mas tem vantagens que logo ficarão evidentes.

Um tipo definido pelo programador também é chamado de classe. Uma definição de classe pode ser assim:

```python
class Point:
    """Represents a point in 2-D space."""
```

O cabeçalho indica que a nova classe se chama `Point`. O corpo é uma docstring que explica para que a classe serve. Você pode definir variáveis e métodos dentro de uma definição de classe, mas voltaremos a isso depois.

Definir uma classe denominada `Point` cria um objeto de classe:

```python
>>> Point
<class '__main__.Point'>
```

Como `Point` é definido no nível superior, seu “nome completo” é `__main__.Point`.

O objeto de classe é como uma fábrica para criar objetos. Para criar um `Point`, você chama `Point` como se fosse uma função:


```python
>>> blank = Point()
>>> blank
<__main__.Point object at 0xb7e9d3ac>
```

O valor de retorno é uma referência a um objeto `Point`, ao qual atribuímos blank.

Criar um objeto chama-se instanciação, e o objeto é uma instância da classe.

Quando você exibe uma instância, o Python diz a que classe ela pertence e onde está armazenada na memória (o prefixo o 0x significa que o número seguinte está em formato hexadecimal).

Cada objeto é uma instância de alguma classe, então “objeto” e “instância” são intercambiáveis. Porém, neste capítulo uso “instância” para indicar que estou falando sobre um tipo definido pelo programador.

## 15.2 - Atributos

Você pode atribuir valores a uma instância usando a notação de ponto:

```python
>>> blank.x = 3.0
>>> blank.y = 4.0
```

Essa sintaxe é semelhante à usada para selecionar uma variável de um módulo, como math.pi ou string.whitespace. Nesse caso, entretanto, estamos atribuindo valores a elementos nomeados de um objeto. Esses elementos chamam-se atributos.

Em inglês, quando é um substantivo, a palavra “AT-trib-ute” é pronunciada com ênfase na primeira sílaba, ao contrário de “a-TRIB-ute”, que é um verbo.

O diagrama seguinte mostra o resultado dessas atribuições. Um diagrama de estado que mostra um objeto e seus atributos chama-se diagrama de objeto; veja a Figura 15.1.

![Figura 15.1 – Diagrama de um objeto Point.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1501.png)
<br>_Figura 15.1 – Diagrama de um objeto_ `Point`.

A variável blank refere-se a um objeto `Point`, que contém dois atributos. Cada atributo refere-se a um número de ponto flutuante.

Você pode ler o valor de um atributo usando a mesma sintaxe:

```python
>>> blank.y
4.0
>>> x = blank.x
>>> x
3.0
```

A expressão `blank.x` significa “Vá ao objeto a que blank se refere e pegue o valor de x”. No exemplo, atribuímos este valor a uma variável `x`. Não há nenhum conflito entre a variável `x` e o atributo `x`.

Você pode usar a notação de ponto como parte de qualquer expressão. Por exemplo:

```python
>>> '(%g, %g)' % (blank.x, blank.y)
'(3.0, 4.0)'
>>> distance = math.sqrt(blank.x ** 2 + blank.y ** 2)
>>> distance
5.0
```

Você pode passar uma instância como argumento da forma habitual. Por exemplo:

```python
def print_point(p):
    print('(%g, %g)' % (p.x, p.y))
```

`print_point` toma um ponto como argumento e o exibe em notação matemática. Para invocá-lo, você pode passar `blank` como argumento:

```python
>>> print_point(blank)
(3.0, 4.0)
```

Dentro da função, `p` é um alias para `blank`, então, se a função altera `p`, `blank` também muda.

Como exercício, escreva uma função chamada `distance_between_points`, que toma dois pontos como argumentos e retorna a distância entre eles.

## 15.3 - Retângulos

Às vezes, é óbvio quais deveriam ser os atributos de um objeto, mas outras é preciso decidir entre as possibilidades. Por exemplo, vamos supor que você esteja criando uma classe para representar retângulos. Que atributos usaria para especificar a posição e o tamanho de um retângulo? Você pode ignorar ângulo; para manter as coisas simples, suponha que o retângulo seja vertical ou horizontal.

Há duas possibilidades, no mínimo:

* Você pode especificar um canto do retângulo (ou o centro), a largura e a altura.

* Você pode especificar dois cantos opostos.

Nesse ponto é difícil dizer qual opção é melhor, então implementaremos a primeira, como exemplo.

Aqui está a definição de classe:

```python
class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """
```

A docstring lista os atributos: width e height são números; corner é um objeto `Point` que especifica o canto inferior esquerdo.

Para representar um retângulo, você tem que instanciar um objeto `Rectangle` e atribuir valores aos atributos:

```python
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
```

A expressão `box.corner.x` significa “Vá ao objeto ao qual `box` se refere e pegue o atributo denominado `corner`; então vá a este objeto e pegue o atributo denominado `x`”.

A Figura 15.2 mostra o estado deste objeto. Um objeto que é um atributo de outro objeto é integrado.

A Figura 10.1 mostra o diagrama de estado para cheeses, numbers e empty.

![Figura 15.2 – Diagrama de um objeto Rectangle.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1502.png)
<br>_Figura 15.2 – Diagrama de um objeto_ `Rectangle`.


## 15.4 - Instâncias como valores de retorno

As funções podem retornar instâncias. Por exemplo, `find_center` recebe um `Rectangle` como argumento e devolve um `Point`, que contém as coordenadas do centro do retângulo:

```python
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p
```

Aqui está um exemplo que passa `box` como um argumento para `find_center` e atribui o `ponto` resultante à variável `center`:

```python
>>> center = find_center(box)
>>> print_point(center)
(50, 100)
```

## 15.5 - Objetos são mutáveis

Você pode alterar o estado de um objeto fazendo uma atribuição a um dos seus atributos. Por exemplo, para mudar o tamanho de um retângulo sem mudar sua posição, você pode alterar os valores de width e height:

```python
box.width = box.width + 50
box.height = box.height + 100
```

Você também pode escrever funções que alteram objetos. Por exemplo, `grow_rectangle` recebe um objeto `Rectangle` e dois números, `dwidth` e `dheight`, e adiciona os números à largura e altura do retângulo:

```python
def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
```

Eis um exemplo que demonstra o efeito:

```python
>>> box.width, box.height
(150.0, 300.0)
>>> grow_rectangle(box, 50, 100)
>>> box.width, box.height
(200.0, 400.0)
```

Dentro da função, `rect` é um alias de `box`, então quando a função altera `rect`, `box` aponta para o objeto alterado.

Como exercício, escreva uma função chamada `move_rectangle` que toma um Rectangle e dois números chamados dx e dy. Ela deve alterar a posição do retângulo, adicionando dx à coordenada x de corner e adicionando dy à coordenada y de corner.

## 15.6 - Cópia

Alias podem tornar um programa difícil de ler porque as alterações em um lugar podem ter efeitos inesperados em outro lugar. É difícil monitorar todas as variáveis que podem referir-se a um dado objeto.

Em vez de usar alias, copiar o objeto pode ser uma alternativa. O módulo `copy` contém uma função chamada `copy` que pode duplicar qualquer objeto:

```python
>>> p1 = Point()
>>> p1.x = 3.0
>>> p1.y = 4.0
>>> import copy
>>> p2 = copy.copy(p1)
```

`p1` e `p2` contêm os mesmos dados, mas não são o mesmo `Point`:

```python
>>> print_point(p1)
(3, 4)
>>> print_point(p2)
(3, 4)
>>> p1 is p2
False
>>> p1 == p2
False
```

O operador `is` indica que `p1` e `p2` não são o mesmo objeto, que é o que esperamos. Porém, você poderia ter esperado que `==` fosse apresentado como `True`, porque esses pontos contêm os mesmos dados. Nesse caso, pode ficar desapontado ao saber que, para instâncias, o comportamento padrão do operador `==` é o mesmo que o do operador `is`; ele verifica a identidade dos objetos, não a sua equivalência. Isso acontece porque, para tipos definidos pelo programador, o Python não sabe o que deve ser considerado equivalente. Pelo menos, ainda não.

Se você usar `copy.copy` para duplicar um retângulo, descobrirá que ele copia o objeto `Rectangle`, mas não o `Point` embutido nele:

```python
>>> box2 = copy.copy(box)
>>> box2 is box
False
>>> box2.corner is box.corner
True
```

A Figura 15.3 mostra como fica o diagrama de objeto. Esta operação chama-se cópia superficial porque copia o objeto e qualquer referência que contenha, mas não os objetos integrados.

![Figura 15.3 – Diagrama: dois objetos Rectangle compartilhando o mesmo Point.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1503.png)
<br>_Figura 15.3 – Diagrama: dois objetos_ `Rectangle` _compartilhando o mesmo_ `Point`.

Para a maior parte das aplicações, não é isso que você quer. Nesse exemplo, invocar `grow_rectangle` em um dos Rectangles não afetaria o outro, mas invocar `move_rectangle` em qualquer um deles afetaria a ambos! Esse comportamento é confuso e propenso a erros.

Felizmente, o módulo `copy` oferece um método chamado `deepcopy` que copia não só o objeto, mas também os objetos aos quais ele se refere, e os objetos aos quais estes se referem, e assim por diante. Você não se surpreenderá ao descobrir que esta operação se chama cópia profunda.

```python
>>> box3 = copy.deepcopy(box)
>>> box3 is box
False
>>> box3.corner is box.corner
False
box3 e box são objetos completamente separados.
```

Como exercício, escreva uma versão de `move_rectangle` que cria e retorne um novo retângulo em vez de alterar o antigo.

## 15.7 - Depuração

Ao começar a trabalhar com objetos, provavelmente você encontrará algumas novas exceções. Se tentar acessar um atributo que não existe, recebe um `AttributeError`:

```python
>>> p = Point()
>>> p.x = 3
>>> p.y = 4
>>> p.z
AttributeError: Point instance has no attribute 'z'
```

Se não estiver certo sobre o tipo que um objeto é, pode perguntar:

```python
>>> type(p)
<class '__main__.Point'>
```

Você também pode usar `isinstance` para verificar se um objeto é uma instância de uma classe:

```python
>>> isinstance(p, Point)
True
```

Caso não tenha certeza se um objeto tem determinado atributo, você pode usar a função integrada `hasattr`:

```python
>>> hasattr(p, 'x')
True
>>> hasattr(p, 'z')
False
```

O primeiro argumento pode ser qualquer objeto; o segundo argumento é uma `string` com o nome do atributo.

Você também pode usar uma instrução `try` para ver se o objeto tem os atributos de que precisa:


```python
try:
    x = p.x
except AttributeError:
    x = 0
```

Essa abordagem pode facilitar a escrita de funções que atuam com tipos diferentes; você verá mais informações sobre isso em “Polimorfismo”, na página 248.

## 15.8 - Glossário

<dl>
<dt><a id="glos:classe" href="#termo:classe">classe</a></dt>
<dd>Tipo definido pelo programador. Uma definição de classe cria um objeto de classe.</dd>

<dt><a id="glos:objeto de classe" href="#termo:objeto de classe">objeto de classe</a></dt>
<dd>Objeto que contém a informação sobre um tipo definido pelo programador. O objeto de classe pode ser usado para criar instâncias do tipo.</dd>

<dt><a id="glos:instância" href="#termo:instância">instância</a></dt>
<dd>Objeto que pertence a uma classe.</dd>

<dt><a id="glos:instanciar" href="#termo:instanciar">instanciar</a></dt>
<dd>Criar um objeto.</dd>

<dt><a id="glos:atributo" href="#termo:atributo">atributo</a></dt>
<dd>Um dos valores denominados associados a um objeto.</dd>

<dt><a id="glos:objeto integrado" href="#termo:objeto integrado">objeto integrado</a></dt>
<dd>Objeto que é armazenado como um atributo de outro objeto.</dd>

<dt><a id="glos:cópia superficial" href="#termo:cópia superficial">cópia superficial</a></dt>
<dd>Copiar o conteúdo de um objeto, inclusive qualquer referência a objetos integrados; implementada pela função copy no módulo copy.</dd>

<dt><a id="glos:cópia profunda" href="#termo:cópia profunda">cópia profunda</a></dt>
<dd>Copiar o conteúdo de um objeto, bem como qualquer objeto integrado, e qualquer objeto integrado a estes, e assim por diante; implementado pela função deepcopy no módulo copy.</dd>

<dt><a id="glos:diagrama de objeto" href="#termo:diagrama de objeto">diagrama de objeto</a></dt>
<dd>Diagrama que mostra objetos, seus atributos e os valores dos atributos.</dd>

</dl>

## 15.9 - Exercícios

### Exercício 15.1

1. Escreva uma definição para uma classe denominada `Circle`, com os atributos center e radius, onde center é um objeto `Point` e radius é um número.

2. Instancie um objeto `Circle`, que represente um círculo com o centro em 150, 100 e raio 75.

3. Escreva uma função denominada `point_in_circle`, que tome um `Circle` e um `Point` e retorne `True`, se o ponto estiver dentro ou no limite do círculo.

4. Escreva uma função chamada `rect_in_circle`, que tome um `Circle` e um Rectangle e retorne `True`, se o retângulo estiver totalmente dentro ou no limite do círculo.

5. Escreva uma função denominada `rect_circle_overlap`, que tome um `Circle` e um Rectangle e retorne `True`, se algum dos cantos do retângulo cair dentro do círculo. Ou, em uma versão mais desafiadora, retorne `True` se alguma parte do retângulo cair dentro do círculo.

Solução: https://github.com/AllenDowney/ThinkPython2/raw/master/code/Circle.py.

### Exercício 15.2

1. Escreva uma função chamada `draw_rect` que receba um objeto `Turtle` e um `Rectangle` e use o `Turtle` para desenhar o retângulo. Veja no Capítulo 4 os exemplos de uso de objetos `Turtle`.

2. Escreva uma função chamada `draw_circle`, que tome um Turtle e um `Circle` e desenhe o círculo.
