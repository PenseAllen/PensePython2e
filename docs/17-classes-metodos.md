# Capítulo 17: Classes e métodos

Embora estejamos usando alguns recursos de orientação a objeto do Python, os programas dos dois últimos capítulos não são realmente orientados a objeto, porque não representam as relações entre os tipos definidos pelo programador e as funções que os produzem. O próximo passo é transformar essas funções em métodos que tornem as relações claras.

Os exemplos de código deste capítulo estão disponíveis em http://thinkpython2.com/code/Time2.py e as soluções para os exercícios estão em http://thinkpython2.com/code/Point2_soln.py.

## 17.1 - Recursos de orientação a objeto

Python é uma linguagem de programação orientada a objeto, ou seja, ela oferece recursos de programação orientada a objeto que tem a seguintes características:

* Os programas incluem definições de classes e métodos.

* A maior parte dos cálculos é expressa em termos de operações em objetos.

* Os objetos muitas vezes representam coisas no mundo real, e os métodos muitas vezes correspondem às formas em que as coisas no mundo real interagem.

Por exemplo, a classe `Time` definida no Capítulo 16 corresponde à forma como as pessoas registram a hora do dia, e as funções que definimos correspondem aos tipos de coisas que as pessoas fazem com os horários. De forma similar, as classes `Point` e `Rectangle` no Capítulo 15 correspondem aos conceitos matemáticos de ponto e retângulo.

Por enquanto, não aproveitamos os recursos que o Python oferece para programação orientada a objeto. Esses recursos não são estritamente necessários; a maioria deles oferece uma sintaxe alternativa para coisas que já fizemos. No entanto, em muitos casos, a alternativa é mais concisa e representa de forma mais exata a estrutura do programa.

Por exemplo, em `Time1.py` não há nenhuma conexão óbvia entre a definição de classe e as definições de função que seguem. Com um pouco de atenção, é evidente que cada função recebe pelo menos um objeto Time como argumento.

Essa observação é a motivação para usar métodos; um método é uma função associada a determinada classe. Vimos métodos de string, listas, dicionários e tuplas. Neste capítulo definiremos métodos para tipos definidos pelo programador.

Métodos são semanticamente o mesmo que funções, mas há duas diferenças sintáticas:

* Os métodos são definidos dentro de uma definição de classe para tornar clara a relação entre a classe e o método.

* A sintaxe para invocar um método é diferente da sintaxe para chamar uma função.

Nas próximas seções tomaremos as funções dos dois capítulos anteriores e as transformaremos em métodos. Essa transformação é puramente mecânica; você pode fazê-la seguindo uma série de passos. Se estiver à vontade para fazer a conversão entre uma forma e outra, sempre poderá escolher a melhor forma para contemplar os seus objetivos.

## 17.2 - Exibição de objetos

No Capítulo 16 definimos uma classe chamada Time em “Time”, na página 231, e você escreveu uma função denominada `print_time`:

```python
class Time:
    """Represents the time of day."""

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
```

Para chamar esta função, você precisa passar um objeto Time como argumento:

```python
>>> start = Time()
>>> start.hour = 9
>>> start.minute = 45
>>> start.second = 00
>>> print_time(start)
09:45:00
```

Para fazer de `print_time` um método, tudo o que precisamos fazer é mover a definição da função para dentro da definição da classe. Note a alteração na endentação:

```python
class Time:
    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
```

Agora há duas formas de chamar `print_time`. A primeira forma (e menos comum) é usar a sintaxe de função:

```python
>>> Time.print_time(start)
09:45:00
```

Nesse uso da notação de ponto, Time é o nome da classe, e `print_time` é o nome do método. `start` é passado como um parâmetro.

A segunda forma (e mais concisa) é usar a sintaxe de método:

```python
>>> start.print_time()
09:45:00
```

Nesse uso da notação de ponto, `print_time` é o nome do método (novamente), e `start` é o objeto no qual o método é invocado, que se chama de sujeito. Assim como em uma sentença, onde o sujeito é o foco da escrita, o sujeito de uma invocação de método é o foco do método.

Dentro do método, o sujeito é atribuído ao primeiro parâmetro, portanto, neste caso, `start` é atribuído a `time`.

Por convenção, o primeiro parâmetro de um método chama-se `self`, então seria mais comum escrever `print_time` desta forma:

```python
class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
```

A razão dessa convenção é uma metáfora implícita:

* A sintaxe de uma chamada de função, `print_time(start)`, sugere que a função é o agente ativo. Ela diz algo como: “Ei, `print_time`! Aqui está um objeto para você exibir”.

* Na programação orientada a objeto, os objetos são os agentes ativos. Uma invocação de método `como start.print_time()` diz: “Ei, `start`! Por favor, exiba-se”.

Essa mudança de perspectiva pode ser mais polida, mas não é óbvio que seja útil. Nos exemplos que vimos até agora, pode não ser. Porém, às vezes, deslocar a responsabilidade das funções para os objetos permite escrever funções (ou métodos) mais versáteis e facilita a manutenção e reutilização do código.

Como exercício, reescreva `time_to_int` (de “Prototipação versus planejamento”, na página 234) como um método. Você pode ficar tentado a reescrever `int_to_time` como um método também, mas isso não faz muito sentido porque não haveria nenhum objeto sobre o qual invocá-lo.

## 17.3 - Outro exemplo

Aqui está uma versão de increment (de “Modificadores”, na página 233) reescrita como método:

```python
# dentro da classe Time:
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
```

Essa versão assume que `time_to_int` seja escrita como método. Além disso, observe que é uma função pura, não um modificador.

É assim que eu invocaria increment:

```python
>>> start.print_time()
09:45:00
>>> end = start.increment(1337)
>>> end.print_time()
10:07:17
```

O sujeito, start, é atribuído ao primeiro parâmetro, self. O argumento, 1337, é atribuído ao segundo parâmetro, seconds.

Esse mecanismo pode ser confuso, especialmente se você fizer um erro. Por exemplo, se invocar increment com dois argumentos, recebe:

```python
>>> end = start.increment(1337, 460)
TypeError: increment() takes 2 positional arguments but 3 were given
```

A mensagem de erro é inicialmente confusa, porque há só dois argumentos entre parênteses. No entanto, o sujeito também é considerado um argumento, então, somando tudo, são três.

A propósito, um argumento posicional é o que não tem um nome de parâmetro; isto é, não é um argumento de palavra-chave. Nesta chamada da função:

```python
sketch(parrot, cage, dead=True)
```

parrot e cage são posicionais, e dead é um argumento de palavra-chave.

## 17.4 - Um exemplo mais complicado

Reescrever `is_after` (de “Time”, na página 231) é ligeiramente mais complicado, porque ela recebe dois objetos Time como parâmetros. Nesse caso, a convenção é denominar o primeiro parâmetro self e o segundo parâmetro other:

```python
# dentro da classe Time:

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
```

Para usar este método, você deve invocá-lo para um objeto e passar outro como argumento:

```python
>>> end.is_after(start)
True
```

Uma vantagem desta sintaxe é que é quase literal em inglês: “o fim é depois da partida?”.

## 17.5 - Método init

O método `__init__` (abreviação da palavra em inglês para “inicialização”) é um método especial, invocado quando um objeto é instanciado. Seu nome completo é `__init__` (dois caracteres de sublinhado, seguidos de init, e mais dois sublinhados). Um método `__init__` da classe Time pode ser algo assim:

```python
# dentro da classe Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
```

É comum que os parâmetros de `__init__` tenham os mesmos nomes que os atributos. A instrução

```python
        self.hour = hour
```

guarda o valor do parâmetro `hour` como um atributo de `self`.

Os parâmetros são opcionais, então, se você chamar Time sem argumentos, recebe os valores padrão:

```python
>>> time = Time()
>>> time.print_time()
00:00:00
```

Se incluir um argumento, ele define hour.

```python
>>> time = Time (9)
>>> time.print_time()
09:00:00
```

Se fornecer dois argumentos, hour e minute serão definidos:

```python
>>> time = Time(9, 45)
>>> time.print_time()
09:45:00
```

E se você fornecer três argumentos, os três valores serão definidos.

Como exercício, escreva um método init da classe Point que receba x e y como parâmetros opcionais e os relacione aos atributos correspondentes.

## 17.6 - Método `__str__`

`__str__` é um método especial, como `__init__`, usado para retornar uma representação de string de um objeto.

Por exemplo, aqui está um método str para objetos Time:

```python
# dentro da classe Time:

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
```

Ao exibir um objeto com print, o Python invoca o método str:

```python
>>> time = Time(9, 45)
>>> print(time)
09:45:00
```

Quando escrevo uma nova classe, quase sempre começo escrevendo `__init__`, o que facilita a instanciação de objetos, e `__str__`, que é útil para a depuração.

Como exercício, escreva um método str da classe Point. Crie um objeto Point e exiba-o.

## 17.7 - Sobrecarga de operadores

Ao definir outros métodos especiais, você pode especificar o comportamento de operadores nos tipos definidos pelo programador. Por exemplo, se você definir um método chamado `__add__` para a classe Time de Time, pode usar o operador + em objetos Time.

A definição pode ser assim:

```python
# dentro da classe Time:

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
```


Você pode usá-lo assim:

```python
>>> start = Time(9, 45)
>>> duration = Time(1, 35)
>>> print(start + duration)
11:20:00
```

Ao aplicar o operador + a objetos Time, o Python invoca `__add__`. Ao exibir o resultado, o Python invoca `__str__`. Ou seja, há muita coisa acontecendo nos bastidores!

Alterar o comportamento de um operador para que funcione com tipos definidos pelo programador chama-se sobrecarga de operadores. Para cada operador no Python há um método especial correspondente, como `__add__`. Para obter mais informações, veja http://docs.python.org/3/reference/datamodel.html\#specialnames.

Como exercício, escreva um método add para a classe Point.

## 17.8 - Despacho por tipo

Na seção anterior, acrescentamos dois objetos Time, mas você também pode querer acrescentar um número inteiro a um objeto Time. A seguir, veja uma versão de `__add__`, que verifica o tipo de other e invoca `add_time` ou increment:

```python
# dentro da classe Time:
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
```

A função construída isinstance recebe um valor e um objeto de classe e retorna True se o valor for uma instância da classe.

Se other for um objeto Time, `__add__` invoca `add_time`. Do contrário, assume que o parâmetro seja um número e invoca increment. Essa operação chama-se despacho por tipo porque despacha a operação a métodos diferentes, baseados no tipo dos argumentos.

Veja exemplos que usam o operador `+` com tipos diferentes:

```python
>>> start = Time(9, 45)
>>> duration = Time(1, 35)
>>> print(start + duration)
11:20:00
>>> print(start + 1337)
10:07:17
```

Infelizmente, esta implementação da adição não é comutativa. Se o número inteiro for o primeiro operando, você recebe

```python
>>> print(1337 + start)
TypeError: unsupported operand type(s) for +: 'int' and 'instance'
```

O problema é que, em vez de pedir ao objeto Time que adicione um número inteiro, o Python está pedindo que um número inteiro adicione um objeto Time, e ele não sabe como fazer isso. Entretanto, há uma solução inteligente para este problema: o método especial `__radd__`, que significa “adição à direita”. Esse método é invocado quando um objeto Time aparece no lado direito do operador +. Aqui está a definição:

```python
# dentro da classe Time:
    def __radd__(self, other):
        return self.__add__(other)
```

E é assim que ele é usado:

```python
>>> print(1337 + start)
10:07:17
```

Como exercício, escreva um método add para Points que funcione com um objeto Point ou com uma tupla:

* Se o segundo operando for um Point, o método deve retornar um novo Point cuja coordenada x é a soma das coordenadas x dos operandos, e o mesmo se aplica às coordenadas de y.

* Se o segundo operando for uma tupla, o método deve adicionar o primeiro elemento da tupla à coordenada de x e o segundo elemento à coordenada de y, retornando um novo Point com o resultado.

## 17.9 - Polimorfismo

O despacho por tipo é útil, mas (felizmente) nem sempre é necessário. Muitas vezes, você pode evitá-lo escrevendo funções que funcionem corretamente para argumentos de tipos diferentes.

Muitas das funções que escrevemos para strings também funcionam para outros tipos de sequência. Por exemplo, em “Um dicionário como uma coleção de contadores”, na página 163, usamos histogram para contar o número de vezes que cada letra aparece numa palavra:

```python
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d
```

Essa função também funciona com listas, tuplas e até dicionários, desde que os elementos de s sejam hashable, então eles podem ser usados como chaves em d:

```python
>>> t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
>>> histogram(t)
{'bacon': 1, 'egg': 1, 'spam': 4}
```
As funções que funcionam com vários tipos chamam-se polimórficas. O polimorfismo pode facilitar a reutilização do código. Por exemplo, a função integrada sum, que adiciona os elementos de uma sequência, funciona só se os elementos da sequência forem compatíveis com adição.

Como os objetos Time oferecem o método add, eles funcionam com sum:

```python
>>> t1 = Time(7, 43)
>>> t2 = Time(7, 41)
>>> t3 = Time(7, 37)
>>> total = sum([t1, t2, t3])
>>> print(total)
23:01:00
```

Em geral, se todas as operações dentro de uma função forem compatíveis com um dado tipo, não haverá problemas.

O melhor tipo de polimorfismo é o não intencional, quando você descobre que uma função que já escreveu pode ser aplicada a um tipo para o qual ela não tinha planejada.

## 17.10 - Interface e implementação

Uma das metas do projeto orientado a objeto é facilitar a manutenção do programa, para que você possa mantê-lo funcionando quando outras partes do sistema forem alteradas, e também poder alterar o programa para satisfazer novas condições.

Um princípio de projeto que ajuda a atingir essa meta é manter as interfaces separadas das implementações. Para objetos, isso quer dizer que os métodos que uma classe oferece não devem depender de como os atributos são representados.

Por exemplo, neste capítulo desenvolvemos uma classe que representa uma hora do dia. Os métodos fornecidos por esta classe incluem time\_to\_int, is\_after e add\_time.

Podemos implementar esses métodos de várias formas. Os detalhes da implementação dependem de como representamos as horas. Neste capítulo, os atributos de um objeto Time são hour, minute e second.

Como alternativa, podemos substituir esses atributos por um número inteiro único que represente o número de segundos desde a meia-noite. Essa implementação faria com que alguns métodos, como is\_after, fossem mais fáceis de escrever, mas dificultaria o uso de outros métodos.

Pode acontecer que, depois de implementar uma nova classe, você descubra uma implementação melhor. Se outras partes do programa estiverem usando a sua classe, mudar a interface pode ser trabalhoso e induzir a erros.

No entanto, se projetou a interface cuidadosamente, pode alterar a implementação sem mudar a interface, e não será preciso mudar outras partes do programa.

## 17.11 - Depuração

É legal acrescentar atributos a objetos em qualquer ponto da execução de um programa, mas se você tiver objetos do mesmo tipo que não têm os mesmos atributos, é fácil cometer erros. É uma boa ideia inicializar todos os atributos de um objeto no método init.

Caso não tenha certeza se um objeto tem um determinado atributo, você pode usar a função integrada hasattr (ver “Depuração”, na página 236).

Outra forma de acessar atributos é com a função integrada vars, que recebe um objeto e retorna um dicionário que mapeia os nomes dos atributos (como strings) aos seus valores:

```python
>>> p = Point(3, 4)
>>> vars(p)
{'y': 4, 'x': 3}
```

Para facilitar a depuração, pode ser útil usar esta função:

```python
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))
```

`print_attributes` atravessa o dicionário e imprime cada nome de atributo e o seu valor correspondente.

A função integrada getattr recebe um objeto e um nome de atributo (como uma string) e devolve o valor do atributo.

## 17.12 - Glossário

<dl>
<dt><a id="glos:linguagem orientada a objeto" href="#termo:linguagem orientada a objeto">linguagem orientada a objeto</a></dt>
<dd>Linguagem que fornece recursos, como tipos definidos pelo programador e métodos, que facilitam a programação orientada a objeto.</dd>

<dt><a id="glos:programação orientada a objeto" href="#termo:programação orientada a objeto">programação orientada a objeto</a></dt>
<dd>Estilo de programação na qual os dados e as operações que os manipulam são organizadas em classes e métodos.</dd>

<dt><a id="glos:método" href="#termo:método">método</a></dt>
<dd>Função criada dentro de uma definição de classe e invocada em instâncias desta classe.</dd>

<dt><a id="glos:sujeito" href="#termo:sujeito">sujeito</a></dt>
<dd>Objeto sobre o qual um método é invocado.</dd>

<dt><a id="glos:argumento posicional" href="#termo:argumento posicional">argumento posicional</a></dt>
<dd>Argumento que não inclui um nome de parâmetro, portanto não é um argumento de palavra-chave.</dd>

<dt><a id="glos:sobrecarga de operador" href="#termo:sobrecarga de operador">sobrecarga de operador</a></dt>
<dd>Alteração do comportamento de um operador como + para que funcione com um tipo definido pelo programador.</dd>

<dt><a id="glos:despacho por tipo" href="#termo:despacho por tipo">despacho por tipo</a></dt>
<dd>Modelo de programação que invoca funções diferentes dependendo do tipo do operando.</dd>

<dt><a id="glos:polimórfico" href="#termo:polimórfico">polimórfico</a></dt>
<dd>Pertinente a uma função que pode funcionar com mais de um tipo.</dd>

<dt><a id="glos:ocultamento de informação" href="#termo:ocultamento de informação">ocultamento de informação</a></dt>
<dd>Princípio segundo o qual a interface fornecida por um objeto não deve depender da sua implementação, especialmente em relação à representação dos seus atributos.</dd>

</dl>

## 17.13 - Exercícios

### Exercício 17.1

Baixe o código deste capítulo em http://thinkpython2.com/code/Time2.py. Altere os atributos de Time para que um número inteiro único represente os segundos decorridos desde a meia-noite. Então altere os métodos (e a função int\_to\_time) para funcionar com a nova implementação. Você não deve modificar o código de teste em main. Ao terminar, a saída deve ser a mesma que antes.

Solução: http://thinkpython2.com/code/Time2_soln.py.

### Exercício 17.2

Este exercício é uma história com moral sobre um dos erros mais comuns e difíceis de encontrar no Python. Escreva uma definição de classe chamada Kangaroo com os seguintes métodos:

1. Um método `__init__` que inicialize um atributo chamado `pouch_contents`  em uma lista vazia.

2. Um método chamado `put_in_pouch` que receba um objeto de qualquer tipo e o acrescente a `pouch_contents`.

3. Um método `__str__` que retorne uma representação de string do objeto Kangaroo e os conteúdos de pouch (bolsa).

Teste o seu código criando dois objetos Kangaroo, atribuindo-os a variáveis chamadas kanga e roo, e então acrescentando roo ao conteúdo da bolsa de kanga.

Baixe http://thinkpython2.com/code/BadKangaroo.py. Ele contém uma solução para o problema anterior com um defeito bem grande e bem feio. Encontre e corrija o defeito.

Se não conseguir achar a solução, você pode baixar http://thinkpython2.com/code/GoodKangaroo.py, que explica o problema e demonstra uma solução.
