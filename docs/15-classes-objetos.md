# Capítulo 15: Classes e objetos

A esta altura você já sabe como usar funções para organizar código e tipos integrados para organizar dados. O próximo passo é aprender “programação orientada a objeto”, que usa tipos definidos pelos programadores para organizar tanto o código quanto os dados. A programação orientada a objeto é um tópico abrangente; será preciso passar por alguns capítulos para abordar o tema.

Os exemplos de código deste capítulo estão disponíveis em http://thinkpython2.com/code/Point1.py; as soluções para os exercícios estão disponíveis em http://thinkpython2.com/code/Point1\_soln.py.

Tipos definidos pelos programadores

Já usamos muitos tipos integrados do Python; agora vamos definir um tipo próprio. Como exemplo, criaremos um tipo chamado Point, que representa um ponto no espaço bidimensional.

Na notação matemática, os pontos muitas vezes são escritos entre parênteses, com uma vírgula separando as coordenadas. Por exemplo, (0,0) representa a origem e (x, y) representa o ponto que está x unidades à direita e y unidades a partir da origem.

Há várias formas para representar pontos no Python:

•        Podemos armazenar as coordenadas separadamente em duas variáveis, x e y.

•        Podemos armazenar as coordenadas como elementos em uma lista ou tupla.

•        Podemos criar um tipo para representar pontos como objetos.

Criar um tipo é mais complicado que outras opções, mas tem vantagens que logo ficarão evidentes.

Um tipo definido pelo programador também é chamado de classe. Uma definição de classe pode ser assim:

class Point:

    """Represents a point in 2-D space."""

O cabeçalho indica que a nova classe se chama Point. O corpo é uma docstring que explica para que a classe serve. Você pode definir variáveis e métodos dentro de uma definição de classe, mas voltaremos a isso depois.

Definir uma classe denominada Point cria um objeto de classe:

&gt;&gt;&gt; Point

&lt;class '\_\_main\_\_.Point'&gt;

Como Point é definido no nível superior, seu “nome completo” é \_\_main\_\_.Point.

O objeto de classe é como uma fábrica para criar objetos. Para criar um Point, você chama Point como se fosse uma função:

&gt;&gt;&gt; blank = Point()

&gt;&gt;&gt; blank

&lt;\_\_main\_\_.Point object at 0xb7e9d3ac&gt;

O valor de retorno é uma referência a um objeto Point, ao qual atribuímos blank.

Criar um objeto chama-se instanciação, e o objeto é uma instância da classe.

Quando você exibe uma instância, o Python diz a que classe ela pertence e onde está armazenada na memória (o prefixo o 0x significa que o número seguinte está em formato hexadecimal).

Cada objeto é uma instância de alguma classe, então “objeto” e “instância” são intercambiáveis. Porém, neste capítulo uso “instância” para indicar que estou falando sobre um tipo definido pelo programador.

Atributos

Você pode atribuir valores a uma instância usando a notação de ponto:

&gt;&gt;&gt; blank.x = 3.0

&gt;&gt;&gt; blank.y = 4.0

Essa sintaxe é semelhante à usada para selecionar uma variável de um módulo, como math.pi ou string.whitespace. Nesse caso, entretanto, estamos atribuindo valores a elementos nomeados de um objeto. Esses elementos chamam-se atributos.

Em inglês, quando é um substantivo, a palavra “AT-trib-ute” é pronunciada com ênfase na primeira sílaba, ao contrário de “a-TRIB-ute”, que é um verbo.

O diagrama seguinte mostra o resultado dessas atribuições. Um diagrama de estado que mostra um objeto e seus atributos chama-se diagrama de objeto; veja a Figura 15.1.

Figura 15.1 – Diagrama de objeto.

A variável blank refere-se a um objeto Point, que contém dois atributos. Cada atributo refere-se a um número de ponto flutuante.

Você pode ler o valor de um atributo usando a mesma sintaxe:

&gt;&gt;&gt; blank.y

4.0

&gt;&gt;&gt; x = blank.x

&gt;&gt;&gt; x

3.0

A expressão blank.x significa “Ir ao objeto a que blank se refere e obter o valor de x”. No exemplo, atribuímos este valor a uma variável x. Não há nenhum conflito entre a variável x e o atributo x.

Você pode usar a notação de ponto como parte de qualquer expressão. Por exemplo:

&gt;&gt;&gt; '(%g, %g)' % (blank.x, blank.y)

'(3.0, 4.0)'

&gt;&gt;&gt; distance = math.sqrt(blank.x\*\*2 + blank.y\*\*2)

&gt;&gt;&gt; distance

5.0

Você pode passar uma instância como argumento da forma habitual. Por exemplo:

def print\_point(p):

    print('(%g, %g)' % (p.x, p.y))

print\_point toma um ponto como argumento e o exibe em notação matemática. Para invocá-lo, você pode passar blank como argumento:

&gt;&gt;&gt; print\_point(blank)

(3.0, 4.0)

Dentro da função, p é um alias para blank, então, se a função altera p, blank também muda.

Como exercício, escreva uma função chamada distance\_between\_points, que toma dois pontos como argumentos e retorna a distância entre eles.

Retângulos

Às vezes, é óbvio quais deveriam ser os atributos de um objeto, mas outras é preciso decidir entre as possibilidades. Por exemplo, vamos supor que você esteja criando uma classe para representar retângulos. Que atributos usaria para especificar a posição e o tamanho de um retângulo? Você pode ignorar ângulo; para manter as coisas simples, suponha que o retângulo seja vertical ou horizontal.

Há duas possibilidades, no mínimo:

•        Você pode especificar um canto do retângulo (ou o centro), a largura e a altura.

•        Você pode especificar dois cantos opostos.

Nesse ponto é difícil dizer qual opção é melhor, então implementaremos a primeira, como exemplo.

Aqui está a definição de classe:

class Rectangle:

    """Represents a rectangle.

    attributes: width, height, corner.

    """

A docstring lista os atributos: width e height são números; corner é um objeto Point que especifica o canto inferior esquerdo.

Para representar um retângulo, você tem que instanciar um objeto Rectangle e atribuir valores aos atributos:

box = Rectangle()

box.width = 100.0

box.height = 200.0

box.corner = Point()

box.corner.x = 0.0

box.corner.y = 0.0

A expressão box.corner.x significa “Vá ao objeto ao qual box se refere e selecione o atributo denominado corner; então vá a este objeto e selecione o atributo denominado x”.

A Figura 15.2 mostra o estado deste objeto. Um objeto que é um atributo de outro objeto é integrado.

Figura 15.2 – Diagrama de objeto.

Instâncias como valores de retorno

As funções podem retornar instâncias. Por exemplo, find\_center recebe Rectangle como argumento e retorna Point, que contém as coordenadas do centro de Rectangle:

def find\_center(rect):

    p = Point()

    p.x = rect.corner.x + rect.width/2

    p.y = rect.corner.y + rect.height/2

    return p

Aqui está um exemplo que passa box como um argumento e atribui o ponto resultante a center:

&gt;&gt;&gt; center = find\_center(box)

&gt;&gt;&gt; print\_point(center)

(50, 100)

Objetos são mutáveis

Você pode alterar o estado de um objeto fazendo uma atribuição a um dos seus atributos. Por exemplo, para mudar o tamanho de um retângulo sem mudar sua posição, você pode alterar os valores de width e height:

box.width = box.width + 50

box.height = box.height + 100

Você também pode escrever funções que alteram objetos. Por exemplo, grow\_rectangle recebe um objeto Rectangle e dois números, dwidth e dheight, e adiciona os números à largura e altura do retângulo:

def grow\_rectangle(rect, dwidth, dheight):

    rect.width += dwidth

    rect.height += dheight

Aqui está um exemplo que demonstra o efeito:

&gt;&gt;&gt; box.width, box.height

(150.0, 300.0)

&gt;&gt;&gt; grow\_rectangle(box, 50, 100)

&gt;&gt;&gt; box.width, box.height

(200.0, 400.0)

Dentro da função, rect é um alias de box, então quando a função altera rect, box também muda.

Como exercício, escreva uma função chamada move\_rectangle que toma um Rectangle e dois números chamados dx e dy. Ela deve alterar a posição do retângulo, adicionando dx à coordenada x de corner e adicionando dy à coordenada y de corner.

Cópia

Alias podem tornar um programa difícil de ler porque as alterações em um lugar podem ter efeitos inesperados em outro lugar. É difícil monitorar todas as variáveis que podem referir-se a um dado objeto.

Em vez de usar alias, copiar o objeto pode ser uma alternativa. O módulo copy contém uma função chamada copy que pode duplicar qualquer objeto:

&gt;&gt;&gt; p1 = Point()

&gt;&gt;&gt; p1.x = 3.0

&gt;&gt;&gt; p1.y = 4.0

&gt;&gt;&gt; import copy

&gt;&gt;&gt; p2 = copy.copy(p1)

p1 e p2 contêm os mesmos dados, mas não são o mesmo Point:

&gt;&gt;&gt; print\_point(p1)

(3, 4)

&gt;&gt;&gt; print\_point(p2)

(3, 4)

&gt;&gt;&gt; p1 is p2

False

&gt;&gt;&gt; p1 == p2

False

O operador is indica que p1 e p2 não são o mesmo objeto, que é o que esperamos. Porém, você poderia ter esperado que == fosse apresentado como True, porque esses pontos contêm os mesmos dados. Nesse caso, pode ficar desapontado ao saber que, para instâncias, o comportamento-padrão do operador == é o mesmo que o do operador is; ele verifica a identidade dos objetos, não a sua equivalência. Isso acontece porque, para tipos definidos pelo programador, o Python não sabe o que deve ser considerado equivalente. Pelo menos, ainda não.

Se você usar copy.copy para duplicar um retângulo, descobrirá que ele copia o objeto Rectangle, mas não o Point integrado:

&gt;&gt;&gt; box2 = copy.copy(box)

&gt;&gt;&gt; box2 is box

False

&gt;&gt;&gt; box2.corner is box.corner

True

A Figura 15.3 mostra como fica o diagrama de objeto. Esta operação chama-se cópia superficial porque copia o objeto e qualquer referência que contenha, mas não os objetos integrados.

Figura 15.3 – Diagrama de objeto.

Para a maior parte das aplicações, não é isso que você quer. Nesse exemplo, invocar grow\_rectangle em um dos Rectangles não afetaria o outro, mas invocar move\_rectangle em qualquer um deles afetaria a ambos! Esse comportamento é confuso e propenso a erros.

Felizmente, o módulo copy oferece um método chamado deepcopy que copia não só o objeto, mas também os objetos aos quais ele se refere, e os objetos aos quais estes se referem, e assim por diante. Você não se surpreenderá ao descobrir que esta operação se chama cópia profunda.

&gt;&gt;&gt; box3 = copy.deepcopy(box)

&gt;&gt;&gt; box3 is box

False

&gt;&gt;&gt; box3.corner is box.corner

False

box3 e box são objetos completamente separados.

Como exercício, escreva uma versão de move\_rectangle que cria e retorne um novo retângulo em vez de alterar o antigo.

Depuração

Ao começar a trabalhar com objetos, provavelmente você encontrará algumas novas exceções. Se tentar acessar um atributo que não existe, recebe um AttributeError:

&gt;&gt;&gt; p = Point()

&gt;&gt;&gt; p.x = 3

&gt;&gt;&gt; p.y = 4

&gt;&gt;&gt; p.z

AttributeError: Point instance has no attribute 'z'

Se não estiver certo sobre o tipo que um objeto é, pode perguntar:

&gt;&gt;&gt; type(p)

&lt;class '\_\_main\_\_.Point'&gt;

Você também pode usar isinstance para verificar se um objeto é uma instância de uma classe:

&gt;&gt;&gt; isinstance(p, Point)

True

Caso não tenha certeza se um objeto tem determinado atributo, você pode usar a função integrada hasattr:

&gt;&gt;&gt; hasattr(p, 'x')

True

&gt;&gt;&gt; hasattr(p, 'z')

False

O primeiro argumento pode ser qualquer objeto; o segundo argumento é uma string que contém o nome do atributo.

Você também pode usar uma instrução try para ver se o objeto tem os atributos de que precisa:

try:

    x = p.x

except AttributeError:

    x = 0

Essa abordagem pode facilitar a escrita de funções que atuam com tipos diferentes; você verá mais informações sobre isso em “Polimorfismo”, na página 248.

Glossário

classe:

Tipo definido pelo programador. Uma definição de classe cria um objeto de classe.

objeto de classe:

Objeto que contém a informação sobre um tipo definido pelo programador. O objeto de classe pode ser usado para criar instâncias do tipo.

instância:

Objeto que pertence a uma classe.

instanciar:

Criar um objeto.

atributo:

Um dos valores denominados associados a um objeto.

objeto integrado:

Objeto que é armazenado como um atributo de outro objeto.

cópia superficial:

Copiar o conteúdo de um objeto, inclusive qualquer referência a objetos integrados; implementada pela função copy no módulo copy.

cópia profunda:

Copiar o conteúdo de um objeto, bem como qualquer objeto integrado, e qualquer objeto integrado a estes, e assim por diante; implementado pela função deepcopy no módulo copy.

diagrama de objeto:

Diagrama que mostra objetos, seus atributos e os valores dos atributos.

Exercícios

Exercício 15.1

Escreva uma definição para uma classe denominada Circle, com os atributos center e radius, onde center é um objeto Point e radius é um número.

Instancie um objeto Circle, que represente um círculo com o centro em 150, 100 e raio 75.

Escreva uma função denominada point\_in\_circle, que tome um Circle e um Point e retorne True, se o ponto estiver dentro ou no limite do círculo.

Escreva uma função chamada rect\_in\_circle, que tome um Circle e um Rectangle e retorne True, se o retângulo estiver totalmente dentro ou no limite do círculo.

Escreva uma função denominada rect\_circle\_overlap, que tome um Circle e um Rectangle e retorne True, se algum dos cantos do retângulo cair dentro do círculo. Ou, em uma versão mais desafiadora, retorne True se alguma parte do retângulo cair dentro do círculo.

Solução: http://thinkpython2.com/code/Circle.py.

Exercício 15.2

Escreva uma função chamada draw\_rect que receba um objeto Turtle e um Rectangle e use o Turtle para desenhar o retângulo. Veja no Capítulo 4 os exemplos de uso de objetos Turtle.

Escreva uma função chamada draw\_circle, que tome um Turtle e um Circle e desenhe o círculo.

Solução: http://thinkpython2.com/code/draw.py.

