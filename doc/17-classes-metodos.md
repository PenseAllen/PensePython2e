# Capítulo 17: Classes e métodos

Embora estejamos usando alguns recursos orientadas a objeto do Python, os programas dos dois últimos capítulos não são realmente orientados a objeto, porque não representam as relações entre os tipos definidos pelo programador e as funções que os produzem. O próximo passo é transformar essas funções em métodos que tornem as relações claras.

Os exemplos de código deste capítulo estão disponíveis em http://thinkpython2.com/code/Time2.py e as soluções para os exercícios estão em http://thinkpython2.com/code/Point2\_soln.py.

Recursos orientados a objeto

Python é uma linguagem de programação orientada a objeto, ou seja, ela oferece recursos de programação orientada a objeto que tem a seguintes características:

•        Os programas incluem definições de classes e métodos.

•        A maior parte dos cálculos é expressa em termos de operações em objetos.

•        Os objetos muitas vezes representam coisas no mundo real, e os métodos muitas vezes correspondem às formas em que as coisas no mundo real interagem.

Por exemplo, a classe Time definida no Capítulo 16 corresponde à forma em que as pessoas registram a hora do dia, e as funções que definimos correspondem aos tipos de coisas que as pessoas fazem com os horários. De forma similar, as classes Point e Rectangle no Capítulo 15 correspondem aos conceitos matemáticos de ponto e retângulo.

Por enquanto, não aproveitamos os recursos que o Python oferece para programação orientada a objeto. Esses recursos não são estritamente necessários; a maioria deles oferece uma sintaxe alternativa para coisas que já fizemos. No entanto, em muitos casos, a alternativa é mais concisa e representa de forma mais exata a estrutura do programa.

Por exemplo, em Time1.py não há nenhuma conexão óbvia entre a definição de classe e as definições de função que seguem. Com um pouco de atenção, é evidente que cada função recebe pelo menos um objeto Time como argumento.

Essa observação é a motivação para usar métodos; um método é uma função associada a determinada classe. Vimos métodos de string, listas, dicionários e tuplas. Neste capítulo definiremos métodos para tipos definidos pelo programador.

Métodos são semanticamente o mesmo que funções, mas há duas diferenças sintáticas:

•        Os métodos são definidos dentro de uma definição de classe para tornar clara a relação entre a classe e o método.

•        A sintaxe para invocar um método é diferente da sintaxe para chamar uma função.

Nas próximas seções tomaremos as funções dos dois capítulos anteriores e as transformaremos em métodos. Essa transformação é puramente mecânica; você pode fazê-la seguindo uma série de passos. Se estiver à vontade para fazer a conversão entre uma forma e outra, sempre poderá escolher a melhor forma para contemplar os seus objetivos.

Exibição de objetos

No Capítulo 16 definimos uma classe chamada Time em “Time”, na página 231, e você escreveu uma função denominada print\_time:

class Time:

    """Represents the time of day."""

def print\_time(time):

    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

Para chamar esta função, você precisa passar um objeto Time como argumento:

&gt;&gt;&gt; start = Time()

&gt;&gt;&gt; start.hour = 9

&gt;&gt;&gt; start.minute = 45

&gt;&gt;&gt; start.second = 00

&gt;&gt;&gt; print\_time(start)

09:45:00

Para fazer de print\_time um método, tudo o que precisamos fazer é mover a definição da função para dentro da definição da classe. Note a alteração na endentação:

class Time:

    def print\_time(time):

        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

Agora há duas formas de chamar print\_time. A primeira forma (e menos comum) é usar a sintaxe de função:

&gt;&gt;&gt; Time.print\_time(start)

09:45:00

Nesse uso da notação de ponto, Time é o nome da classe, e print\_time é o nome do método. start é passado como um parâmetro.

A segunda forma (e mais concisa) é usar a sintaxe de método:

&gt;&gt;&gt; start.print\_time()

09:45:00

Nesse uso da notação de ponto, print\_time é o nome do método (novamente), e start é o objeto no qual o método é invocado, que se chama de sujeito. Assim como em uma sentença, onde o sujeito é o foco da escrita, o sujeito de uma invocação de método é o foco do método.

Dentro do método, o sujeito é atribuído ao primeiro parâmetro, portanto, neste caso, start é atribuído a time.

Por convenção, o primeiro parâmetro de um método chama-se self, então seria mais comum escrever print\_time desta forma:

class Time:

    def print\_time(self):

        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

A razão dessa convenção é uma metáfora implícita:

•        A sintaxe de uma chamada de função, print\_time(start), sugere que a função é o agente ativo. Ela diz algo como: “Ei, print\_time! Aqui está um objeto para você exibir”.

•        Na programação orientada a objeto, os objetos são os agentes ativos. Uma invocação de método como start.print\_time() diz: “Ei, start! Por favor, exiba-se”.

Essa mudança de perspectiva pode ser mais polida, mas não é óbvio que seja útil. Nos exemplos que vimos até agora, pode não ser. Porém, às vezes, deslocar a responsabilidade das funções para os objetos permite escrever funções (ou métodos) mais versáteis e facilita a manutenção e reutilização do código.

Como exercício, reescreva time\_to\_int (de “Prototipação versus planejamento”, na página 234) como um método. Você pode ficar tentado a reescrever int\_to\_time como um método também, mas isso não faz muito sentido porque não haveria nenhum objeto sobre o qual invocá-lo.

Outro exemplo

Aqui está uma versão de increment (de “Modificadores”, na página 233) reescrita como método:

\# dentro da classe Time:

    def increment(self, seconds):

        seconds += self.time\_to\_int()

        return int\_to\_time(seconds)

Essa versão assume que time\_to\_int seja escrita como método. Além disso, observe que é uma função pura, não um modificador.

É assim que eu invocaria increment:

&gt;&gt;&gt; start.print\_time()

09:45:00

&gt;&gt;&gt; end = start.increment(1337)

&gt;&gt;&gt; end.print\_time()

10:07:17

O sujeito, start, é atribuído ao primeiro parâmetro, self. O argumento, 1337, é atribuído ao segundo parâmetro, seconds.

Esse mecanismo pode ser confuso, especialmente se você fizer um erro. Por exemplo, se invocar increment com dois argumentos, recebe:

&gt;&gt;&gt; end = start.increment(1337, 460)

TypeError: increment() takes 2 positional arguments but 3 were given

A mensagem de erro é inicialmente confusa, porque há só dois argumentos entre parênteses. No entanto, o sujeito também é considerado um argumento, então, somando tudo, são três.

A propósito, um argumento posicional é o que não tem um nome de parâmetro; isto é, não é um argumento de palavra-chave. Nesta chamada da função:

sketch(parrot, cage, dead=True)

parrot e cage são posicionais, e dead é um argumento de palavra-chave.

Um exemplo mais complicado

Reescrever is\_after (de “Time”, na página 231) é ligeiramente mais complicado, porque ela recebe dois objetos Time como parâmetros. Nesse caso, a convenção é denominar o primeiro parâmetro self e o segundo parâmetro other:

\# dentro da classe Time:

    def is\_after(self, other):

        return self.time\_to\_int() &gt; other.time\_to\_int()

Para usar este método, você deve invocá-lo para um objeto e passar outro como argumento:

&gt;&gt;&gt; end.is\_after(start)

True

Uma vantagem desta sintaxe é que é quase literal em inglês: “o fim é depois da partida?”.

Método init

O método init (abreviação da palavra em inglês para “inicialização”) é um método especial, invocado quando um objeto é instanciado. Seu nome completo é \_\_init\_\_ (dois caracteres de sublinhado, seguidos de init, e mais dois sublinhados). Um método init da classe Time pode ser algo assim:

\# dentro da classe Time:

    def \_\_init\_\_(self, hour=0, minute=0, second=0):

        self.hour = hour

        self.minute = minute

        self.second = second

É comum que os parâmetros de \_\_init\_\_ tenham os mesmos nomes que os atributos. A instrução

        self.hour = hour

guarda o valor do parâmetro hour como um atributo de self.

Os parâmetros são opcionais, então, se você chamar Time sem argumentos, recebe os valores-padrão:

&gt;&gt;&gt; time = Time()

&gt;&gt;&gt; time.print\_time()

00:00:00

Se incluir um argumento, ele ignora hour.

&gt;&gt;&gt; time = Time (9)

&gt;&gt;&gt; time.print\_time()

09:00:00

Se fornecer dois argumentos, hour e minute serão ignorados:

&gt;&gt;&gt; time = Time(9, 45)

&gt;&gt;&gt; time.print\_time()

09:45:00

E se você fornecer três argumentos, os três valores-padrão serão ignorados.

Como exercício, escreva um método init da classe Point que receba x e y como parâmetros opcionais e os relacione aos atributos correspondentes.

Método \_\_str\_\_

\_\_str\_\_ é um método especial, como \_\_init\_\_, usado para retornar uma representação de string de um objeto.

Por exemplo, aqui está um método str para objetos Time:

\# dentro da classe Time:

    def \_\_str\_\_(self):

        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

Ao exibir um objeto com print, o Python invoca o método str:

&gt;&gt;&gt; time = Time(9, 45)

&gt;&gt;&gt; print(time)

09:45:00

Quando escrevo uma nova classe, quase sempre começo escrevendo \_\_init\_\_, o que facilita a instanciação de objetos, e \_\_str\_\_, que é útil para a depuração.

Como exercício, escreva um método str da classe Point. Crie um objeto Point e exiba-o.

Sobrecarga de operadores

Ao definir outros métodos especiais, você pode especificar o comportamento de operadores nos tipos definidos pelo programador. Por exemplo, se você definir um método chamado \_\_add\_\_ para a classe Time de Time, pode usar o operador + em objetos Time.

A definição pode ser assim:

\# dentro da classe Time:

    def \_\_add\_\_(self, other):

        seconds = self.time\_to\_int() + other.time\_to\_int()

        return int\_to\_time(seconds)

Você pode usá-lo assim:

&gt;&gt;&gt; start = Time(9, 45)

&gt;&gt;&gt; duration = Time(1, 35)

&gt;&gt;&gt; print(start + duration)

11:20:00

Ao aplicar o operador + a objetos Time, o Python invoca \_\_add\_\_. Ao exibir o resultado, o Python invoca \_\_str\_\_. Ou seja, há muita coisa acontecendo nos bastidores!

Alterar o comportamento de um operador para que funcione com tipos definidos pelo programador chama-se sobrecarga de operadores. Para cada operador no Python há um método especial correspondente, como \_\_add\_\_. Para obter mais informações, veja http://docs.python.org/3/reference/datamodel.html\#specialnames.

Como exercício, escreva um método add para a classe Point.

Despacho por tipo

Na seção anterior, acrescentamos dois objetos Time, mas você também pode querer acrescentar um número inteiro a um objeto Time. A seguir, veja uma versão de \_\_add\_\_, que verifica o tipo de other e invoca add\_time ou increment:

\# dentro da classe Time:

    def \_\_add\_\_(self, other):

        if isinstance(other, Time):

            return self.add\_time(other)

        else:

            return self.increment(other)

    def add\_time(self, other):

        seconds = self.time\_to\_int() + other.time\_to\_int()

        return int\_to\_time(seconds)

    def increment(self, seconds):

        seconds += self.time\_to\_int()

        return int\_to\_time(seconds)

A função construída isinstance recebe um valor e um objeto de classe e retorna True se o valor for uma instância da classe.

Se other for um objeto Time, \_\_add\_\_ invoca add\_time. Do contrário, assume que o parâmetro seja um número e invoca increment. Essa operação chama-se despacho por tipo porque despacha a operação a métodos diferentes, baseados no tipo dos argumentos.

Veja exemplos que usam o operador + com tipos diferentes:

&gt;&gt;&gt; start = Time(9, 45)

&gt;&gt;&gt; duration = Time(1, 35)

&gt;&gt;&gt; print(start + duration)

11:20:00

&gt;&gt;&gt; print(start + 1337)

10:07:17

Infelizmente, esta implementação da adição não é comutativa. Se o número inteiro for o primeiro operando, você recebe

&gt;&gt;&gt; print(1337 + start)

TypeError: unsupported operand type(s) for +: 'int' and 'instance'

O problema é que, em vez de pedir ao objeto Time que adicione um número inteiro, o Python está pedindo que um número inteiro adicione um objeto Time, e ele não sabe como fazer isso. Entretanto, há uma solução inteligente para este problema: o método especial \_\_radd\_\_, que significa “adição à direita”. Esse método é invocado quando um objeto Time aparece no lado direito do operador +. Aqui está a definição:

\# dentro da classe Time:

    def \_\_radd\_\_(self, other):

        return self.\_\_add\_\_(other)

E é assim que ele é usado:

&gt;&gt;&gt; print(1337 + start)

10:07:17

Como exercício, escreva um método add para Points que funcione com um objeto Point ou com uma tupla:

•        Se o segundo operando for um Point, o método deve retornar um novo Point cuja coordenada x é a soma das coordenadas x dos operandos, e o mesmo se aplica às coordenadas de y.

•        Se o segundo operando for uma tupla, o método deve adicionar o primeiro elemento da tupla à coordenada de x e o segundo elemento à coordenada de y, retornando um novo Point com o resultado.

Polimorfismo

O despacho por tipo é útil, mas (felizmente) nem sempre é necessário. Muitas vezes, você pode evitá-lo escrevendo funções que funcionem corretamente para argumentos de tipos diferentes.

Muitas das funções que escrevemos para strings também funcionam para outros tipos de sequência. Por exemplo, em “Um dicionário como uma coleção de contadores”, na página 163, usamos histogram para contar o número de vezes que cada letra aparece numa palavra:

def histogram(s):

    d = dict()

    for c in s:

        if c not in d:

            d\[c\] = 1

        else:

            d\[c\] = d\[c\]+1

    return d

Essa função também funciona com listas, tuplas e até dicionários, desde que os elementos de s sejam hashable, então eles podem ser usados como chaves em d:

&gt;&gt;&gt; t = \['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'\]

&gt;&gt;&gt; histogram(t)

{'bacon': 1, 'egg': 1, 'spam': 4}

As funções que funcionam com vários tipos chamam-se polimórficas. O polimorfismo pode facilitar a reutilização do código. Por exemplo, a função integrada sum, que adiciona os elementos de uma sequência, funciona só se os elementos da sequência forem compatíveis com adição.

Como os objetos Time oferecem o método add, eles funcionam com sum:

&gt;&gt;&gt; t1 = Time(7, 43)

&gt;&gt;&gt; t2 = Time(7, 41)

&gt;&gt;&gt; t3 = Time(7, 37)

&gt;&gt;&gt; total = sum(\[t1, t2, t3\])

&gt;&gt;&gt; print(total)

23:01:00

Em geral, se todas as operações dentro de uma função forem compatíveis com um dado tipo, não haverá problemas.

O melhor tipo de polimorfismo é o não intencional, quando você descobre que uma função que já escreveu pode ser aplicada a um tipo para o qual ela não tinha planejada.

Interface e implementação

Uma das metas do projeto orientado a objeto é facilitar a manutenção do programa, para que você possa mantê-lo funcionando quando outras partes do sistema forem alteradas, e também poder alterar o programa para satisfazer novas condições.

Um princípio de projeto que ajuda a atingir essa meta é manter as interfaces separadas das implementações. Para objetos, isso quer dizer que os métodos que uma classe oferece não devem depender de como os atributos são representados.

Por exemplo, neste capítulo desenvolvemos uma classe que representa uma hora do dia. Os métodos fornecidos por esta classe incluem time\_to\_int, is\_after e add\_time.

Podemos implementar esses métodos de várias formas. Os detalhes da implementação dependem de como representamos as horas. Neste capítulo, os atributos de um objeto Time são hour, minute e second.

Como alternativa, podemos substituir esses atributos por um número inteiro único que represente o número de segundos desde a meia-noite. Essa implementação faria com que alguns métodos, como is\_after, fossem mais fáceis de escrever, mas dificultaria o uso de outros métodos.

Pode acontecer que, depois de implementar uma nova classe, você descubra uma implementação melhor. Se outras partes do programa estiverem usando a sua classe, mudar a interface pode ser trabalhoso e induzir a erros.

No entanto, se projetou a interface cuidadosamente, pode alterar a implementação sem mudar a interface, e não será preciso mudar outras partes do programa.

Depuração

É legal acrescentar atributos a objetos em qualquer ponto da execução de um programa, mas se você tiver objetos do mesmo tipo que não têm os mesmos atributos, é fácil cometer erros. É uma boa ideia inicializar todos os atributos de um objeto no método init.

Caso não tenha certeza se um objeto tem um determinado atributo, você pode usar a função integrada hasattr (ver “Depuração”, na página 236).

Outra forma de acessar atributos é com a função integrada vars, que recebe um objeto e retorna um dicionário que mapeia os nomes dos atributos (como strings) aos seus valores:

&gt;&gt;&gt; p = Point(3, 4)

&gt;&gt;&gt; vars(p)

{'y': 4, 'x': 3}

Para facilitar a depuração, pode ser útil usar esta função:

def print\_attributes(obj):

    for attr in vars(obj):

        print(attr, getattr(obj, attr))

print\_attributes atravessa o dicionário e imprime cada nome de atributo e o seu valor correspondente.

A função integrada getattr recebe um objeto e um nome de atributo (como uma string) e devolve o valor do atributo.

Glossário

linguagem orientada a objeto:

Linguagem que fornece recursos, como tipos definidos pelo programador e métodos, que facilitam a programação orientada a objeto.

programação orientada a objeto:

Estilo de programação na qual os dados e as operações que os manipulam são organizadas em classes e métodos.

método:

Função criada dentro de uma definição de classe e invocada em instâncias desta classe.

sujeito:

Objeto sobre o qual um método é invocado.

argumento posicional:

Argumento que não inclui um nome de parâmetro, portanto não é um argumento de palavra-chave.

sobrecarga de operador:

Alteração do comportamento de um operador como + para que funcione com um tipo definido pelo programador.

despacho por tipo:

Modelo de programação que invoca funções diferentes dependendo do tipo do operando.

polimórfico:

Pertinente a uma função que pode funcionar com mais de um tipo.

ocultamento de informação:

Princípio segundo o qual a interface fornecida por um objeto não deve depender da sua implementação, especialmente em relação à representação dos seus atributos.

Exercícios

Exercício 17.1

Baixe o código deste capítulo em http://thinkpython2.com/code/Time2.py. Altere os atributos de Time para que um número inteiro único represente os segundos decorridos desde a meia-noite. Então altere os métodos (e a função int\_to\_time) para funcionar com a nova implementação. Você não deve modificar o código de teste em main. Ao terminar, a saída deve ser a mesma que antes.

Solução: http://thinkpython2.com/code/Time2\_soln.py.

Exercício 17.2

Este exercício é uma história com moral sobre um dos erros mais comuns e difíceis de encontrar no Python. Escreva uma definição de classe chamada Kangaroo com os seguintes métodos:

1.        Um método \_\_init\_\_ que inicialize um atributo chamado pouch\_contents  em uma lista vazia.

2.        Um método chamado put\_in\_pouch que receba um objeto de qualquer tipo e o acrescente a pouch\_contents.

3.        Um método \_\_str\_\_ que retorne uma representação de string do objeto Kangaroo e os conteúdos de pouch (bolsa).

Teste o seu código criando dois objetos Kangaroo, atribuindo-os a variáveis chamadas kanga e roo, e então acrescentando roo ao conteúdo da bolsa de kanga.

Baixe http://thinkpython2.com/code/BadKangaroo.py. Ele contém uma solução para o problema anterior com um defeito bem grande e bem feio. Encontre e corrija o defeito.

Se não conseguir achar a solução, você pode baixar http://thinkpython2.com/code/GoodKangaroo.py, que explica o problema e demonstra uma solução.

