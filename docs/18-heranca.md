# Capítulo 18: Herança

O termo mais associado com a programação orientada a objeto é herança. A herança é a capacidade de definir uma nova classe que seja uma versão modificada de uma classe existente. Neste capítulo demonstrarei a herança usando classes que representam jogos de cartas, baralhos e mãos de pôquer.

Se você não joga pôquer, pode ler sobre ele em http://en.wikipedia.org/wiki/Poker, mas não é necessário; vou dizer tudo o que precisa saber para os exercícios.

Os exemplos de código deste capítulo estão disponíveis em https://github.com/AllenDowney/ThinkPython2/raw/master/code/Card.py.

## 18.1 - Objetos Card

Há 52 cartas em um baralho, e cada uma pertence a 1 dos 4 naipes e a 1 dos 13 valores. Os naipes são espadas, copas, ouros e paus (no bridge, em ordem descendente). A ordem dos valores é ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, valete, dama e rei. Dependendo do jogo que estiver jogando, um ás pode ser mais alto que o rei ou mais baixo que 2.

Se quiséssemos definir um novo objeto para representar uma carta de jogo, os atributos óbvios seriam rank (valor) e suit (naipe). Mas não é tão óbvio qual tipo de atributo deveriam ser. Uma possibilidade é usar strings com palavras como 'Spade' (Espadas) para naipes e 'Queen' (Dama) para valores. Um problema com esta implementação é que não seria fácil comparar cartas para ver qual valor ou naipe tem classificação mais alta em relação aos outros.

Uma alternativa é usar números inteiros para codificar os valores e os naipes. Neste contexto, “codificar” significa que vamos definir um mapeamento entre números e naipes, ou entre números e valores. Este tipo de codificação não tem nada a ver com criptografia.

Por exemplo, esta tabela mostra os naipes e os códigos de número inteiro correspondentes:


```
Spades (Espadas)     ↦ 3
Hearts (Copas)       ↦ 2
Diamonds (Ouros)     ↦ 1
Clubs (Paus)         ↦ 0
```

Este código facilita a comparação entre as cartas; como naipes mais altos mapeiam a números mais altos, podemos comparar naipes aos seus códigos.

O mapeamento de valores é até óbvio; cada um dos valores numéricos é mapeado ao número inteiro correspondente, e para cartas com figuras:


```
Jack (Valete)       ↦ 11
Queen (Dama)        ↦ 12
King (Rei)          ↦ 13
```

Estou usando o símbolo `↦` para deixar claro que esses mapeamentos não são parte do programa em Python. Eles são parte do projeto do programa, mas não aparecem explicitamente no código.

A definição de classe para Card (carta) é assim:

```python
class Card:
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
```

Como sempre, o método `__init__` recebe um parâmetro opcional de cada atributo. A carta padrão é 2 de paus.

Para criar um Card, você chama Card com o naipe e valor desejados:

```python
queen_of_diamonds = Card(1, 12)
```

## 18.2 - Atributos de classe

Para exibir objetos Card de uma forma que as pessoas possam ler com facilidade, precisamos de um mapeamento dos códigos de número inteiro aos naipes e valores correspondentes. Uma forma natural de fazer isso é com listas de strings. Atribuímos essas listas a atributos de classe:

```python
# dentro da classe Card:

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
```

Variáveis como `suit_names` e `rank_names`, que são definidas dentro de uma classe, mas fora de qualquer método, chamam-se atributos de classe porque são associadas com o objeto de classe Card.

Este termo as distingue de variáveis como `suit` e `rank`, chamadas de atributos de instância porque são associados com determinada instância.

Ambos os tipos de atributo são acessados usando a notação de ponto. Por exemplo, em `__str__`, `self` é um objeto `Card`, e `self.rank` é o seu valor. De forma semelhante, Card é um objeto de classe, e `Card.rank_names` é uma lista de strings associadas à essa classe.

Cada carta tem seu próprio suit e rank, mas há só uma cópia de suit_names e rank_names.

Juntando tudo, a expressão `Card.rank_names[self.rank]` significa “use o rank (valor) do atributo do objeto self como um índice na lista rank_names da classe Card e selecione a string adequada”.

O primeiro elemento de rank_names é None, porque não há nenhuma carta com valor zero. Incluindo None para ocupar uma variável, conseguimos fazer um belo mapeamento onde o índice 2 é associado à string '2', e assim por diante. Para evitar ter que usar esse truque, poderíamos usar um dicionário em vez de uma lista.

Com os métodos que temos por enquanto, podemos criar e exibir cartas:

```python
>>> card1 = Card(2, 11)
>>> print(card1)
Jack of Hearts
```

A Figura 18.1 é um diagrama do objeto de classe Card e uma instância de Card. Card é um objeto de classe; seu tipo é type. card1 é uma instância de Card, então seu tipo é Card. Para economizar espaço, não incluí o conteúdo de suit_names e rank_names.

![Figura 18.1 – Diagrama de objetos: classe Card e card1, uma instância de Card.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1801.png)
<br>_Figura 18.1 – Diagrama de objetos: classe_ `Card` _e_ `card1`, _uma instância de_ `Card`.

## 18.3 - Comparação de cartas

Para tipos integrados, há operadores relacionais (`<`, `>`, `==` etc.) que comparam valores e determinam quando um é maior, menor ou igual a outro. Para tipos definidos pelo programador, podemos ignorar o comportamento dos operadores integrados fornecendo um método denominado `__lt__`, que representa “menos que”.

`__lt__` recebe dois parâmetros, `self` e `other`, e `True` se self for estritamente menor que `other`.

A ordem correta das cartas não é óbvia. Por exemplo, qual é melhor, o 3 de paus ou o 2 de ouros? Uma tem o valor mais alto, mas a outra tem um naipe mais alto. Para comparar cartas, é preciso decidir o que é mais importante, o valor ou o naipe.

A resposta pode depender de que jogo você está jogando, mas, para manter a simplicidade, vamos fazer a escolha arbitrária de que o naipe é mais importante, então todas as cartas de espadas são mais importantes que as de ouros, e assim por diante.

Com isto decidido, podemos escrever `__lt__`:

```python
# dentro da classe Card:

    def __lt__(self, other):
        # conferir os naipes
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # os naipes são os mesmos... conferir valores
        return self.rank < other.rank
```

Você pode escrever isso de forma mais concisa usando uma comparação de tuplas:

```python
# dentro da classe Card:

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
```

Como exercício, escreva um método `__lt__` para objetos Time. Você pode usar uma comparação de tuplas, mas também pode usar a comparação de números inteiros.

## 18.4 - Baralhos

Agora que temos Card, o próximo passo é definir Deck (baralho). Como um baralho é composto de cartas, é natural que um baralho contenha uma lista de cartas como atributo.

Veja a seguir uma definição de classe para `Deck`. O método init cria o atributo cards e gera o conjunto padrão de 52 cartas:


```python
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
```

A forma mais fácil de preencher o baralho é com um loop aninhado. O loop exterior enumera os naipes de 0 a 3. O loop interior enumera os valores de 1 a 13. Cada iteração cria um novo Card com o naipe e valor atual, e a acrescenta a self.cards.

## 18.5 - Exibição do baralho

Aqui está um método __str__ para Deck:

```python
# dentro da classe Deck:

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
```

Este método demonstra uma forma eficiente de acumular uma string grande: a criação de uma lista de strings e a utilização do método de string join. A função integrada str invoca o método `__str__` em cada carta e retorna a representação da string.

Como invocamos join em um caractere newline, as cartas são separadas por quebras de linha. O resultado é esse:

```python
>>> deck = Deck()
>>> print(deck)
Ace of Clubs
2 of Clubs
3 of Clubs
...
10 of Spades
Jack of Spades
Queen of Spades
King of Spades
```

Embora o resultado apareça em 52 linhas, na verdade ele é uma string longa com quebras de linha.

## 18.6 - Adição, remoção, embaralhamento e classificação

Para lidar com as cartas, gostaríamos de ter um método que removesse uma carta do baralho e a devolvesse. O método de lista pop oferece uma forma conveniente de fazer isso:

```python
# dentro da classe Deck:

    def pop_card(self):
        return self.cards.pop()
```

Como pop retira a última carta na lista, estamos lidando com o fundo do baralho.

Para adicionar uma carta, podemos usar o método de lista append:

```python
# dentro da classe Deck:

    def add_card(self, card):
        self.cards.append(card)
```

Um método como esse, que usa outro método sem dar muito trabalho, às vezes é chamado de folheado. A metáfora vem do trabalho em madeira, onde o folheado é uma camada fina de madeira de boa qualidade colada à superfície de uma madeira mais barata para melhorar a aparência.

Nesse caso, `add_card` é um método “fino” que expressa uma operação de lista em termos adequados a baralhos. Ele melhora a aparência ou interface da implementação.

Em outro exemplo, podemos escrever um método Deck denominado shuffle, usando a função shuffle do módulo random:


```python
# dentro da classe Deck:

    def shuffle(self):
        random.shuffle(self.cards)
```

Não se esqueça de importar random.

Como exercício, escreva um método de Deck chamado sort, que use o método de lista sort para classificar as cartas em um Deck. sort usa o método `__lt__` que definimos para determinar a ordem.

## 18.7 - Herança

A herança é a capacidade de definir uma nova classe que seja uma versão modificada de uma classe existente. Como exemplo, digamos que queremos que uma classe represente uma “mão”, isto é, as cartas mantidas por um jogador. Uma mão é semelhante a um baralho: ambos são compostos por uma coleção de cartas, e ambos exigem operações como adicionar e remover cartas.

Uma mão também é diferente de um baralho; há operações que queremos para mãos que não fazem sentido para um baralho. Por exemplo, no pôquer poderíamos comparar duas mãos para ver qual ganha. No bridge, poderíamos calcular a pontuação de uma mão para fazer uma aposta.

Essa relação entre classes – semelhante, mas diferente – adequa-se à herança. Para definir uma nova classe que herda algo de uma classe existente, basta colocar o nome da classe existente entre parênteses:

```python
class Hand(Deck):
    """Represents a hand of playing cards."""
```

Esta definição indica que Hand herda de Deck; isso significa que podemos usar métodos como pop\_card e add\_card para Hand bem como para Deck.

Quando uma nova classe herda de uma existente, a existente chama-se pai e a nova classe chama-se filho.

Neste exemplo, Hand herda `__init__` de Deck, mas na verdade não faz o que queremos: em vez de preencher a mão com 52 cartas novas, o método init de Hand deve inicializar card com uma lista vazia.

Se fornecermos um método init na classe Hand, ele ignora o da classe Deck:

```python
# dentro da classe Hand:

    def __init__(self, label=''):
        self.cards = []
        self.label = label
```

Ao criar Hand, o Python invoca este método init, não o de Deck.

```python
>>> hand = Hand('new hand')
>>> hand.cards
[]
>>> hand.label
'new hand'
```

Outros métodos são herdados de Deck, portanto podemos usar `pop_card` e `add_card` para lidar com uma carta:

```python
>>> deck = Deck()
>>> card = deck.pop_card()
>>> hand.add_card(card)
>>> print(hand)
King of Spades
```

Um próximo passo natural seria encapsular este código em um método chamado `move_cards`:

```python
# dentro da classe Deck:

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
```

`move_cards` recebe dois argumentos, um objeto Hand e o número de cartas com que vai lidar. Ele altera tanto self como hand e retorna None.

Em alguns jogos, as cartas são movidas de uma mão a outra, ou de uma mão de volta ao baralho. É possível usar `move_cards` para algumas dessas operações: self pode ser um Deck ou Hand, e hand, apesar do nome, também pode ser um Deck.

A herança é um recurso útil. Alguns programas que poderiam ser repetitivos sem herança podem ser escritos de forma mais elegante com ela. A herança pode facilitar a reutilização de código, já que você pode personalizar o comportamento de classes pais sem ter que alterá-las. Em alguns casos, a estrutura de herança reflete a estrutura natural do problema, o que torna o projeto mais fácil de entender.

De outro lado, a herança pode tornar os programas difíceis de ler. Quando um método é invocado, às vezes não está claro onde encontrar sua definição. O código relevante pode ser espalhado por vários módulos. Além disso, muitas das coisas que podem ser feitas usando a herança podem ser feitas sem elas, às vezes, até de forma melhor.

## 18.8 - Diagramas de classe

Por enquanto vimos diagramas de pilha, que mostram o estado de um programa e diagramas de objeto, que mostram os atributos de um objeto e seus valores. Esses diagramas representam um retrato da execução de um programa, então eles mudam no decorrer da execução do programa.

Eles também são altamente detalhados; para alguns objetivos, detalhados demais. Um diagrama de classe é uma representação mais abstrata da estrutura de um programa. Em vez de mostrar objetos individuais, ele mostra classes e as relações entre elas.

Há vários tipos de relações entre as classes:

* Os objetos de uma classe podem conter referências a objetos em outra classe. Por exemplo, cada Rectangle contém uma referência a um Point, e cada Deck contém referências a muitos Cards. Esse tipo de relação chama-se composição. É uma relação do tipo HAS-A (tem um), com a ideia de “um Rectangle tem um Point”.

* Uma classe pode herdar de outra. Esta relação chama-se IS-A (é um), com a ideia de “um Hand é um tipo de Deck”.

* Uma classe pode depender de outra no sentido de que os objetos em uma classe possam receber objetos na segunda classe como parâmetros ou usar esses objetos como parte de um cálculo. Este tipo de relação chama-se dependência.

Um diagrama de classe é uma representação gráfica dessas relações. Por exemplo, a Figura 18.2 mostra as relações entre Card, Deck e Hand.

![Figura 18.2 – Diagrama de classes.](https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_1802.png)
<br>_Figura 18.2 – Diagrama de classes._

A flecha com um triângulo oco representa uma relação IS-A; nesse caso, indica que Hand herda de Deck.

A ponta de flecha padrão representa uma relação HAS-A; nesse caso, um Deck tem referências a objetos Card.

A estrela __*__  perto da ponta de flecha indica a multiplicidade; ela indica quantos Cards um Deck tem. Uma multiplicidade pode ser um número simples como 52, um intervalo como 5..7 ou uma estrela, que indica que um Deck pode ter qualquer número de Cards.

Não há nenhuma dependência neste diagrama. Elas normalmente apareceriam com uma flecha tracejada. Ou, se houver muitas dependências, às vezes elas são omitidas.

Um diagrama mais detalhado poderia mostrar que um Deck na verdade contém uma lista de Cards, mas os tipos integrados como lista e dict não são normalmente incluídos em diagramas de classe.

## 18.9 - Encapsulamento de dados

Os capítulos anteriores demonstram um plano de desenvolvimento que poderíamos chamar de “projeto orientado a objeto”. Identificamos os objetos de que precisamos – como Point, Rectangle e Time – e definimos classes para representá-los. Em cada caso há uma correspondência óbvia entre o objeto e alguma entidade no mundo real (ou, pelo menos, no mundo matemático).

Mas, às vezes, é menos óbvio quais objetos você precisa e como eles devem interagir. Nesse caso é necessário um plano de desenvolvimento diferente. Da mesma forma em que descobrimos interfaces de função por encapsulamento e generalização, podemos descobrir interfaces de classe por encapsulamento de dados.

A análise de Markov, de “Análise de Markov”, na página 200, apresenta um bom exemplo. Se baixar o meu código em https://github.com/AllenDowney/ThinkPython2/raw/master/code/markov.py, você vai ver que ele usa duas variáveis globais – suffix\_map e prefix – que são lidas e escritas a partir de várias funções.

```python
suffix_map = {}
prefix = ()
```

Como essas variáveis são globais, só podemos executar uma análise de cada vez. Se lermos dois textos, seus prefixos e sufixos seriam acrescentados às mesmas estruturas de dados (o que geraria textos interessantes).

Para executar análises múltiplas e guardá-las separadamente, podemos encapsular o estado de cada análise em um objeto. É assim que fica:

```python
class Markov:
    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()
```

Em seguida, transformamos as funções em métodos. Por exemplo, aqui está process_word:

```python
def process_word(self, word, order=2):
    if len(self.prefix) < order:
        self.prefix += (word,)
        return
    try:
        self.suffix_map[self.prefix].append(word)
    except KeyError:
        # se não houver entradas deste prefixo, crie uma.
        self.suffix_map[self.prefix] = [word]

    self.prefix = shift(self.prefix, word)
```

Transformar um programa como esse – alterando o projeto sem mudar o comportamento – é outro exemplo de refatoração (veja “Refatoração”, na página 70).

Este exemplo sugere um plano de desenvolvimento para projetar objetos e métodos:

1. Comece escrevendo funções que leiam e criem variáveis globais (quando necessário).

2. Uma vez que o programa esteja funcionando, procure associações entre variáveis globais e funções que as usem.

3. Encapsule variáveis relacionadas como atributos de objeto.

4. Transforme as funções associadas em métodos da nova classe.

Como exercício, baixe o meu código de Markov de https://github.com/AllenDowney/ThinkPython2/raw/master/code/markov.py e siga os passos descritos acima para encapsular as variáveis globais como atributos de uma nova classe chamada Markov.

Solução: https://github.com/AllenDowney/ThinkPython2/raw/master/code/markov2.py (observe o 2 no nome do arquivo).

## 18.10 - Depuração

A herança pode dificultar a depuração porque quando você invoca um método em um objeto, pode ser difícil compreender qual método será invocado.

Suponha que esteja escrevendo uma função que funcione com objetos Hand. Você gostaria que ela funcionasse com todos os tipos de Hand, como PokerHands, BridgeHands etc. Se invocar um método como shuffle, poderá receber o que foi definido em Deck, mas se alguma das subclasses ignorar este método, você receberá outra versão. Este comportamento pode ser bom, mas também confuso.

A qualquer momento em que não esteja seguro a respeito do fluxo de execução do seu programa, a solução mais simples é acrescentar instruções de exibição no início dos métodos em questão. Se Deck.shuffle exibir uma mensagem que diz algo como Running Deck.shuffle, então no decorrer da execução do programa ele monitora seu fluxo.

Uma alternativa é usar esta função, que recebe um objeto e um nome de método (como uma string) e retorna a classe que fornece a definição do método:

```python
def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty
```

Aqui está um exemplo:

```python
>>> hand = Hand()
>>> find_defining_class(hand, 'shuffle')
<class 'Card.Deck'>
```

Então o método shuffle deste Hand é o de Deck.

`find_defining_class` usa o método mro para obter a lista de objetos de classe (tipos) onde os métodos serão procurados. “MRO” significa “ordem de resolução do método”, que é a sequência de classes que o Python pesquisa para “descobrir” um nome de método.

Aqui está uma sugestão de projeto: quando você ignora um método, a interface do novo método deve ser a mesma que a do antigo. Ela deve receber os mesmos parâmetros, retornar o mesmo tipo e obedecer às mesmas precondições e pós-condições. Se seguir esta regra, você descobrirá que qualquer função projetada para funcionar com uma instância de uma classe pai, como Deck, também funcionará com instâncias de classes filho como Hand e PokerHand.

Se violar esta regra, o que se chama de “princípio de substituição de Liskov”, seu código cairá como (desculpe) um castelo de cartas.

## 18.11 - Glossário

<dl>
<dt><a id="glos:codificar" href="#termo:codificar">codificar</a></dt>
<dd>Representar um conjunto de valores usando outro conjunto de valores construindo um mapeamento entre eles.</dd>

<dt><a id="glos:atributo de classe" href="#termo:atributo de classe">atributo de classe</a></dt>
<dd>Atributo associado a um objeto de classe. Os atributos de classe são definidos dentro de uma definição de classe, mas fora de qualquer método.</dd>

<dt><a id="glos:atributo de instância" href="#termo:atributo de instância">atributo de instância</a></dt>
<dd>Atributo associado a uma instância de uma classe.</dd>

<dt><a id="glos:folheado" href="#termo:folheado">folheado</a></dt>
<dd>Método ou função que apresenta uma interface diferente para outra função sem fazer muitos cálculos.</dd>

<dt><a id="glos:herança" href="#termo:herança">herança</a></dt>
<dd>Capacidade de definir uma nova classe que seja uma versão modificada de uma classe definida anteriormente.</dd>

<dt><a id="glos:classe-pai" href="#termo:classe-pai">classe-pai</a></dt>
<dd>Classe da qual uma classe-filho herda.</dd>

<dt><a id="glos:classe-filho" href="#termo:classe-filho">classe-filho</a></dt>
<dd>Nova classe criada por herança de uma classe existente; também chamada de “subclasse”.</dd>

<dt><a id="glos:relação IS-A" href="#termo:relação IS-A">relação IS-A</a></dt>
<dd>Relação entre uma classe-filho e sua classe-pai. Também chamada de herança.</dd>

<dt><a id="glos:relação HAS-A" href="#termo:relação HAS-A">relação HAS-A</a></dt>
<dd>Relação entre duas classes onde as instâncias de uma classe contêm referências a instâncias da outra. Também chamada de composição.</dd>

<dt><a id="glos:dependência" href="#termo:dependência">dependência</a></dt>
<dd>Relação entre duas classes onde as instâncias de uma classe usam instâncias de outra classe, mas não as guardam como atributos.</dd>

<dt><a id="glos:diagrama de classe" href="#termo:diagrama de classe">diagrama de classe</a></dt>
<dd>Diagrama que mostra as classes em um programa e as relações entre elas.</dd>

<dt><a id="glos:multiplicidade" href="#termo:multiplicidade">multiplicidade</a></dt>
<dd>Notação em um diagrama de classe que mostra, para uma relação HAS-A, quantas referências a instâncias da outra classe podem existir.</dd>

<dt><a id="glos:encapsulamento de dados" href="#termo:encapsulamento de dados">encapsulamento de dados</a></dt>
<dd>Plano de desenvolvimento de programa que envolve um protótipo usando variáveis globais e uma versão final que transforma as variáveis globais em atributos de instância.</dd>

</dl>

## 18.12 - Exercícios

### Exercício 18.1

Para o seguinte programa, desenhe um diagrama de classe UML que mostre estas classes e as relações entre elas.

```python
class PingPongParent:
    pass

class Ping(PingPongParent):
    def __init__(self, pong):
        self.pong = pong

class Pong(PingPongParent):
    def __init__(self, pings=None):
        if pings is None:
            self.pings = []
        else:
            self.pings = pings
    def add_ping(self, ping):
        self.pings.append(ping)

pong = Pong()
ping = Ping(pong)
pong.add_ping(ping)
```

### Exercício 18.2

Escreva um método Deck chamado `deal_hands` que receba dois parâmetros: o número de mãos e o número de cartas por mão. Ele deve criar o número adequado de objetos Hand, lidar com o número adequado de cartas por mão e retornar uma lista de Hands.

### Exercício 18.3

A seguir, as mãos possíveis no pôquer, em ordem crescente de valor e ordem decrescente de probabilidade:

<dl>
<dt>par</dt>
<dd>Duas cartas com o mesmo valor.</dd>

<dt>dois pares</dt>
<dd>Dois pares de cartas com o mesmo valor.</dd>

<dt>trinca</dt>
<dd>Três cartas com o mesmo valor.</dd>

<dt>sequência</dt>
<dd>Cinco cartas com valores em sequência (os ases podem ser altos ou baixos, então Ace-2-3-4-5 é uma sequência, assim como 10-Jack-Queen-King-Ace, mas Queen-King-Ace-2-3 não é.)</dd>

<dt>flush</dt>
<dd>Cinco cartas com o mesmo naipe.</dd>

<dt>full house</dt>
<dd>Três cartas com um valor, duas cartas com outro.</dd>

<dt>quadra</dt>
<dd>Quatro cartas com o mesmo valor.</dd>

<dt>straight flush</dt>
<dd>Cinco cartas em sequência (como definido acima) e com o mesmo naipe.</dd>

</dl>

A meta desses exercícios é estimar a probabilidade de ter estas várias mãos.

1. Baixe os seguintes arquivos:

 * [`Card.py`](https://github.com/AllenDowney/ThinkPython2/raw/master/code/Card.py): Versão completa das classes Card, Deck e Hand deste capítulo.

 * [`PokerHand.py`](https://github.com/AllenDowney/ThinkPython2/raw/master/code/PokerHand.py): Uma implementação incompleta de uma classe que representa uma mão de pôquer e código para testá-la.

2. Se executar PokerHand.py, você verá que o programa cria mãos de pôquer com 7 cartas e verifica se alguma delas contém um flush. Leia este código com atenção antes de continuar.

3. Acrescente métodos a PokerHand.py chamados `has_pair`, `has_twopair`, etc. que retornem True ou False conforme a mão cumpra os critérios em questão. Seu código deve funcionar corretamente para “mãos” que contenham qualquer número de cartas (embora 5 e 7 sejam as quantidades mais comuns).

4. Escreva um método chamado classify que descubra a classificação do valor mais alto para uma mão e estabeleça o atributo label em questão. Por exemplo, uma mão de 7 cartas poderia conter um flush e um par; ela deve ser marcada como “flush”.

5. Quando se convencer de que os seus métodos de classificação estão funcionando, o próximo passo deve ser estimar as probabilidades de várias mãos. Escreva uma função em PokerHand.py que embaralhe cartas, divida-as em mãos, classifique as mãos e conte o número de vezes em que várias classificações aparecem.

6. Exiba uma tabela das classificações e suas probabilidades. Execute seu programa com números cada vez maiores de mãos até que os valores de saída convirjam a um grau razoável de exatidão. Compare seus resultados com os valores em http://en.wikipedia.org/wiki/Hand_rankings.

Solução: https://github.com/AllenDowney/ThinkPython2/raw/master/code/PokerHandSoln.py.
