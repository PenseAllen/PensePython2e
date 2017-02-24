# Capítulo 19: Extra

Uma das minhas metas com este livro é ensinar o mínimo possível de Python. Quando havia duas formas de fazer algo, escolhia uma e evitava mencionar a outra. Ou, às vezes, usava a segunda como exercício.

Agora quero voltar a algumas coisas boas que ficaram para trás. O Python oferece vários recursos que não são realmente necessários – você pode escrever um bom código sem eles – mas com eles é possível escrever um código mais conciso, legível ou eficiente e, às vezes, todos os três.

Expressões condicionais

Vimos instruções condicionais em “Execução condicional”, na página 78. As instruções condicionais muitas vezes são usadas para escolher um entre dois valores; por exemplo:

if x &gt; 0:

    y = math.log(x)

else:

    y = float('nan')

Esta instrução verifica se x é positivo. Nesse caso, ela calcula math.log. Do contrário, math.log causaria um ValueError. Para evitar interromper o programa, geramos um “NaN”, que é um valor de ponto flutuante especial que representa um “Não número”.

Podemos escrever essa instrução de forma mais concisa usando uma expressão condicional:

y = math.log(x) if x &gt; 0 else float('nan')

Você quase pode ler esta linha como se tivesse sido escrita em inglês: “y recebe log-x se x for maior que 0; do contrário, ele recebe NaN”.

As funções recursivas por vezes podem ser reescritas usando expressões condicionais. Por exemplo, aqui está uma versão recursiva de factorial:

def factorial(n):

    if n == 0:

        return 1

    else:

        return n \* factorial(n-1)

Podemos reescrevê-la assim:

def factorial(n):

    return 1 if n == 0 else n \* factorial(n-1)

Outro uso de expressões condicionais é lidar com argumentos opcionais. Por exemplo, aqui está o método init de GoodKangaroo (veja o Exercício 17.2):

def \_\_init\_\_(self, name, contents=None):

    self.name = name

    if contents == None:

        contents = \[\]

    self.pouch\_contents = contents

Podemos reescrevê-lo assim:

def \_\_init\_\_(self, name, contents=None):

    self.name = name

    self.pouch\_contents = \[\] if contents == None else contents

Em geral, é possível substituir uma instrução condicional por uma expressão condicional se ambos os ramos contiverem expressões simples que sejam retornadas ou atribuídas à mesma variável.

Abrangência de listas

Em “Mapeamento, filtragem e redução”, na página 147, vimos os padrões de filtragem e mapeamento. Por exemplo, esta função toma uma lista de strings, mapeia o método de string capitalize aos elementos, e retorna uma nova lista de strings:

def capitalize\_all(t):

    res = \[\]

    for s in t:

        res.append(s.capitalize())

    return res

Podemos escrever isso de forma mais concisa usando abrangência de listas (list comprehension):

def capitalize\_all(t):

    return \[s.capitalize() for s in t\]

Os operadores de colchete indicam que estamos construindo uma nova lista. A expressão dentro dos colchetes especifica os elementos da lista, e a cláusula for indica qual sequência estamos atravessando.

A sintaxe da abrangência de listas é um pouco esquisita porque a variável de loop, s nesse exemplo, aparece na expressão antes de chegarmos à definição.

Abrangências de listas também podem ser usadas para filtragem. Por exemplo, esta função só seleciona os elementos de t que são maiúsculos, e retorna uma nova lista:

def only\_upper(t):

    res = \[\]

    for s in t:

        if s.isupper():

            res.append(s)

    return res

Podemos reescrevê-la usando abrangência de listas:

def only\_upper(t):

    return \[s for s in t if s.isupper()\]

Abrangências de listas são concisas e fáceis de ler, pelo menos para expressões simples. E são normalmente mais rápidas que os loops for equivalentes, às vezes muito mais rápidas. Então, se você ficar irritado comigo por não ter mencionado isso antes, eu entendo.

Porém, em minha defesa, as abrangências de listas são mais difíceis de depurar porque não é possível ter instruções de exibição dentro do loop. Sugiro que você as use só se o cálculo for simples o suficiente para que acerte já de primeira. E para principiantes isso significa nunca.

Expressões geradoras

Expressões geradoras são semelhantes às abrangências de listas, mas com parênteses em vez de colchetes:

&gt;&gt;&gt; g = (x\*\*2 for x in range(5))

&gt;&gt;&gt; g

&lt;generator object &lt;genexpr&gt; at 0x7f4c45a786c0&gt;

O resultado é um objeto gerador que sabe como fazer iterações por uma sequência de valores. No entanto, ao contrário de uma abrangência de listas, ele não calcula todos os valores de uma vez; espera pelo pedido. A função integrada next recebe o próximo valor do gerador:

&gt;&gt;&gt; next(g)

0

&gt;&gt;&gt; next(g)

1

Quando você chega no fim da sequência, next cria uma exceção StopIteration. Também é possível usar um loop for para fazer a iteração pelos valores:

&gt;&gt;&gt; for val in g:

...     print(val)

4

9

16

O objeto gerador monitora a posição em que está na sequência, portanto o loop for continua de onde next parou. Uma vez que o gerador se esgotar, ele continua criando StopException:

&gt;&gt;&gt; next(g)

StopIteration

As expressões geradoras muitas vezes são usadas com funções como sum, max e min:

&gt;&gt;&gt; sum(x\*\*2 for x in range(5))

30

any e all

O Python tem uma função integrada, any, que recebe uma sequência de valores booleanos e retorna True se algum dos valores for True. Ela funciona em listas:

&gt;&gt;&gt; any(\[False, False, True\])

True

Entretanto, muitas vezes é usada com expressões geradoras:

&gt;&gt;&gt; any(letter == 't' for letter in 'monty')

True

Esse exemplo não é muito útil porque faz a mesma coisa que o operador in. Porém, podemos usar any para reescrever algumas das funções de pesquisa que escrevemos em “Busca”, na página 136. Por exemplo, poderíamos escrever avoids dessa forma:

def avoids(word, forbidden):

    return not any(letter in forbidden for letter in word)

A função quase pode ser lida como uma frase em inglês: “word evita forbidden se não houver nenhuma letra proibida em word”.

Usar any com uma expressão geradora é eficiente porque o programa é interrompido imediatamente se encontrar um valor True, então não é preciso avaliar a sequência inteira.

O Python oferece outra função integrada, all, que retorna True se todos os elementos da sequência forem True. Como exercício, use all para reescrever uses\_all de “Busca”, na página 136.

Conjuntos

Na seção “Subtração de dicionário”, da página 198, uso dicionários para encontrar as palavras que aparecem em um documento, mas não numa lista de palavras. A função que escrevi recebe d1, que contém as palavras do documento como chaves e d2, que contém a lista de palavras. Ela retorna um dicionário que contém as chaves de d1 que não estão em d2:

def subtract(d1, d2):

    res = dict()

    for key in d1:

        if key not in d2:

            res\[key\] = None

    return res

Em todos esses dicionários, os valores não são None porque nunca os usamos. O resultado é que desperdiçamos espaço de armazenamento.

O Python fornece outro tipo integrado, chamado set (conjunto), que se comporta como uma coleção de chaves de dicionário sem valores. Acrescentar elementos a um conjunto é rápido; assim como verificar a adesão. E os conjuntos fornecem métodos e operadores para calcular operações de conjuntos.

Por exemplo, a subtração de conjuntos está disponível como um método chamado difference ou como um operador, -. Portanto, podemos reescrever subtract desta forma:

def subtract(d1, d2):

    return set(d1) - set(d2)

O resultado é um conjunto em vez de um dicionário, mas, para operações como iteração, o comportamento é o mesmo.

Alguns exercícios neste livro podem ser feitos de forma concisa e eficiente com conjuntos. Por exemplo, aqui está uma solução para has\_duplicates, do Exercício 10.7, que usa um dicionário:

def has\_duplicates(t):

    d = {}

    for x in t:

        if x in d:

            return True

        d\[x\] = True

    return False

Quando um elemento aparece pela primeira vez, ele é acrescentado ao dicionário. Se o mesmo elemento aparece novamente, a função retorna True.

Usando conjuntos, podemos escrever a mesma função dessa forma:

def has\_duplicates(t):

    return len(set(t)) &lt; len(t)

Um elemento só pode aparecer em um conjunto uma vez, portanto, se um elemento em t aparecer mais de uma vez, o conjunto será menor que t. Se não houver duplicatas, o conjunto terá o mesmo tamanho que t.

Também podemos usar conjuntos para fazer alguns exercícios no Capítulo 9. Por exemplo, aqui está uma versão de uses\_only com um loop:

def uses\_only(word, available):

    for letter in word:

        if letter not in available:

            return False

    return True

uses\_only verifica se todas as cartas em word estão em available. Podemos reescrevê-la assim:

def uses\_only(word, available):

    return set(word) &lt;= set(available)

O operador &lt;= verifica se um conjunto é um subconjunto ou outro, incluindo a possibilidade de que sejam iguais, o que é verdade se todas as letras de word aparecerem em available.

Como exercício, reescreva avoids usando conjuntos.

Contadores

Um contador é como um conjunto, exceto que se um elemento aparecer mais de uma vez, o contador acompanha quantas vezes ele aparece. Se tiver familiaridade com a ideia matemática de um multiconjunto, um contador é uma forma natural de representar um multiconjunto.

Contadores são definidos em um módulo-padrão chamado collections, portanto é preciso importá-lo. Você pode inicializar um contador com uma string, lista ou alguma outra coisa que seja compatível com iteração:

&gt;&gt;&gt; from collections import Counter

&gt;&gt;&gt; count = Counter('parrot')

&gt;&gt;&gt; count

Counter({'r': 2, 't': 1, 'o': 1, 'p': 1, 'a': 1})

Os contadores comportam-se como dicionários de muitas formas; eles mapeiam cada chave ao número de vezes que aparece. Como em dicionários, as chaves têm de ser hashable.

Ao contrário de dicionários, os contadores não causam uma exceção se você acessar um elemento que não aparece. Em vez disso, retornam 0:

&gt;&gt;&gt; count\['d'\]

0

Podemos usar contadores para reescrever is\_anagram do Exercício 10.6:

def is\_anagram(word1, word2):

    return Counter(word1) == Counter(word2)

Se duas palavras forem anagramas, elas contêm as mesmas letras com as mesmas contagens, então seus contadores são equivalentes.

Os contadores oferecem métodos e operadores para executar operações similares às dos conjuntos, incluindo adição, subtração, união e intersecção. E eles fornecem um método muitas vezes útil, most\_common, que retorna uma lista de pares frequência-valor, organizados do mais ao menos comum:

&gt;&gt;&gt; count = Counter('parrot')

&gt;&gt;&gt; for val, freq in count.most\_common(3):

...     print(val, freq)

r 2

p 1

a 1

defaultdict

O módulo collections também tem defaultdict, que se parece com um dicionário, exceto pelo fato de que se você acessar uma chave que não existe, um novo valor pode ser gerado automaticamente.

Quando você cria um defaultdict, fornece uma função usada para criar valores. Uma função usada para criar objetos às vezes é chamada de factory (fábrica). As funções integradas que criam listas, conjuntos e outros tipos podem ser usadas como fábricas:

&gt;&gt;&gt; from collections import defaultdict

&gt;&gt;&gt; d = defaultdict(list)

Note que o argumento é list, que é um objeto de classe, não list(), que é uma nova lista. A função que você fornece não é chamada a menos que você acesse uma chave que não existe:

&gt;&gt;&gt; t = d\['new key'\]

&gt;&gt;&gt; t

\[\]

A nova lista, que estamos chamando de t, também é adicionada ao dicionário. Então, se alterarmos t, a mudança aparece em d:

&gt;&gt;&gt; t.append('new value')

&gt;&gt;&gt; d

defaultdict(&lt;class 'list'&gt;, {'new key': \['new value'\]})

Se estiver fazendo um dicionário de listas, você pode escrever um código mais simples usando defaultdict. Na minha solução para o Exercício 12.2, que você pode ver em http://thinkpython2.com/code/anagram\_sets.py, faço um dicionário que mapeia uma string organizada de letras a uma lista de palavras que pode ser soletrada com essas letras. Por exemplo, 'opst' mapeia para a lista \['opts', 'post', 'pots', 'spot', 'stop', 'tops'\].

Aqui está o código original:

def all\_anagrams(filename):

    d = {}

    for line in open(filename):

        word = line.strip().lower()

        t = signature(word)

        if t not in d:

            d\[t\] = \[word\]

        else:

            d\[t\].append(word)

    return d

Isso pode ser simplificado usando setdefault, que você poderia ter usado no Exercício 11.2:

def all\_anagrams(filename):

    d = {}

    for line in open(filename):

        word = line.strip().lower()

        t = signature(word)

        d.setdefault(t, \[\]).append(word)

    return d

O problema dessa solução é que ela faz uma lista nova a cada vez, mesmo que não seja necessário. Para listas, isso não é grande coisa, mas se a função fábrica for complicada, poderia ser.

Podemos evitar este problema e simplificar o código usando um defaultdict:

def all\_anagrams(filename):

    d = defaultdict(list)

    for line in open(filename):

        word = line.strip().lower()

        t = signature(word)

        d\[t\].append(word)

    return d

A minha solução para o Exercício 18.3, que você pode baixar em http://thinkpython2.com/code/PokerHandSoln.py, usa setdefault na função has\_straightflush. O problema dessa solução é criar um objeto Hand cada vez que passa pelo loop, seja ele necessário ou não. Como exercício, reescreva-a usando um defaultdict.

Tuplas nomeadas

Muitos objetos simples são basicamente coleções de valores relacionados. Por exemplo, o objeto Point, definido no Capítulo 15, contém dois números, x e y. Ao definir uma classe como essa, normalmente você começa com um método init e um método str:

class Point:

    def \_\_init\_\_(self, x=0, y=0):

        self.x = x

        self.y = y

    def \_\_str\_\_(self):

        return '(%g, %g)' % (self.x, self.y)

É muito código para transmitir pouca informação. O Python tem uma forma mais concisa de dizer a mesma coisa:

from collections import namedtuple

Point = namedtuple('Point', \['x', 'y'\])

O primeiro argumento é o nome da classe que você quer criar. O segundo é uma lista dos atributos que o objeto Point deve ter, como strings. O valor de retorno de namedtuple é um objeto de classe:

&gt;&gt;&gt; Point

&lt;class '\_\_main\_\_.Point'&gt;

Point fornece automaticamente métodos como \_\_init\_\_ e \_\_str\_\_ então não é preciso escrevê-los.

Para criar um objeto Point, você usa a classe Point como uma função:

&gt;&gt;&gt; p = Point(1, 2)

&gt;&gt;&gt; p

Point(x=1, y=2)

O método init atribui os argumentos a atributos usando os nomes que você forneceu. O método str exibe uma representação do objeto Point e seus atributos.

Você pode acessar os elementos da tupla nomeada pelo nome:

&gt;&gt;&gt; p.x, p.y

(1, 2)

Mas também pode tratar uma tupla nomeada como uma tupla:

&gt;&gt;&gt; p\[0\], p\[1\]

(1, 2)

&gt;&gt;&gt; x, y = p

&gt;&gt;&gt; x, y

(1, 2)

Tuplas nomeadas fornecem uma forma rápida de definir classes simples. O problema é que classes simples não ficam sempre simples. Mais adiante você poderá decidir que quer acrescentar métodos a uma tupla nomeada. Nesse caso, você poderá definir uma nova classe que herde da tupla nomeada:

class Pointier(Point):

    \# adicionar mais métodos aqui

Ou poderá mudar para uma definição de classe convencional.

Reunindo argumentos de palavra-chave

Em “Tuplas com argumentos de comprimento variável”, na página 181, vimos como escrever uma função que reúne seus argumentos em uma tupla:

def printall(\*args):

    print(args)

Você pode chamar esta função com qualquer número de argumentos posicionais (isto é, argumentos que não têm palavras-chave):

&gt;&gt;&gt; printall(1, 2.0, '3')

(1, 2.0, '3')

Porém, o operador \* não reúne argumentos de palavra-chave:

&gt;&gt;&gt; printall(1, 2.0, third='3')

TypeError: printall() got an unexpected keyword argument 'third'

Para reunir argumentos de palavra-chave, você pode usar o operador \*\*:

def printall(\*args, \*\*kwargs):

    print(args, kwargs)

Você pode chamar o parâmetro de coleta de palavra-chave, como quiser, mas kwargs é uma escolha comum. O resultado é um dicionário que mapeia palavras-chave a valores:

&gt;&gt;&gt; printall(1, 2.0, third='3')

(1, 2.0) {'third': '3'}

Se tiver um dicionário de palavras-chave e valores, pode usar o operador de dispersão, \*\*, para chamar uma função:

&gt;&gt;&gt; d = dict(x=1, y=2)

&gt;&gt;&gt; Point(\*\*d)

Point(x=1, y=2)

Sem o operador de dispersão, a função trataria d como um único argumento posicional, e então atribuiria d a x e se queixaria porque não há nada para atribuir a y:

&gt;&gt;&gt; d = dict(x=1, y=2)

&gt;&gt;&gt; Point(d)

Traceback (most recent call last):

  File "&lt;stdin&gt;", line 1, in &lt;module&gt;

TypeError: \_\_new\_\_() missing 1 required positional argument: 'y'

Quando estiver trabalhando com funções com um grande número de parâmetros, muitas vezes é útil criar e usar dicionários que especifiquem as opções usadas frequentemente.

Glossário

expressão condicional:

Expressão que contém um de dois valores, dependendo de uma condição.

abrangência de listas:

Expressão com um loop for entre colchetes que produz uma nova lista.

expressão geradora:

Uma expressão com um loop for entre parênteses que produz um objeto gerador.

multiconjunto:

Entidade matemática que representa um mapeamento entre os elementos de um conjunto e o número de vezes que aparecem.

fábrica (factory):

Função normalmente passada como parâmetro, usada para criar objetos.

Exercícios

Exercício 19.1

Esta é uma função que calcula o coeficiente binominal recursivamente:

def binomial\_coeff(n, k):

    """Compute the binomial coefficient "n choose k".

    n: number of trials

    k: number of successes

    returns: int

    """

    if k == 0:

        return 1

    if n == 0:

        return 0

    res = binomial\_coeff(n-1, k) + binomial\_coeff(n-1, k-1)

    return res

Reescreva o corpo da função usando expressões condicionais aninhadas.

Uma observação: esta função não é muito eficiente porque acaba calculando os mesmos valores várias vezes. Você pode torná-lo mais eficiente com memos (veja “Memos”, na página 169). No entanto, vai ver que é mais difícil usar memos se escrevê-la usando expressões condicionais.

