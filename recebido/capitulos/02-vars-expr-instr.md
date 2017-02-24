# Capítulo 2: Variáveis, expressões e instruções

Um dos recursos mais eficientes de uma linguagem de programação é a capacidade de manipular variáveis. Uma variável é um nome que se refere a um valor.

Instruções de atribuição

Uma instrução de atribuição cria uma nova variável e dá um valor a ela:

&gt;&gt;&gt; message = 'And now for something completely different'

&gt;&gt;&gt; n = 17

&gt;&gt;&gt; pi = 3.141592653589793

Esse exemplo faz três atribuições. A primeira atribui uma string a uma nova variável chamada message; a segunda dá o número inteiro 17 a n; a terceira atribui o valor (aproximado) de π a pi.

Uma forma comum de representar variáveis por escrito é colocar o nome com uma flecha apontando para o seu valor. Este tipo de número é chamado de diagrama de estado porque mostra o estado no qual cada uma das variáveis está (pense nele como o estado de espírito da variável). A Figura 2.1 mostra o resultado do exemplo anterior.

Figura 2.1 – Diagrama de estado.

Nomes de variáveis

Os programadores geralmente escolhem nomes significativos para as suas variáveis – eles documentam o uso da variável.

Nomes de variáveis podem ser tão longos quanto você queira. Podem conter tanto letras como números, mas não podem começar com um número. É legal usar letras maiúsculas, mas a convenção é usar apenas letras minúsculas para nomes de variáveis.

O caractere de sublinhar (\_) pode aparecer em um nome. Muitas vezes é usado em nomes com várias palavras, como your\_name ou airspeed\_of\_unladen\_swallow.

Se você der um nome ilegal a uma variável, recebe um erro de sintaxe:

&gt;&gt;&gt; 76trombones = 'big parade'

SyntaxError: invalid syntax

&gt;&gt;&gt; more@ = 1000000

SyntaxError: invalid syntax

&gt;&gt;&gt; class = 'Advanced Theoretical Zymurgy'

SyntaxError: invalid syntax

76trombones é ilegal porque começa com um número. more@ é ilegal porque contém um caractere ilegal, o @. Mas o que há de errado com class?

A questão é que class é uma das palavras-chave do Python. O interpretador usa palavras-chave para reconhecer a estrutura do programa e elas não podem ser usadas como nomes de variável.

O Python 3 tem estas palavras-chave:

False     class      finally    is         return

None      continue   for       lambda     try

True      def        from      nonlocal   while

and       del        global    not        with

as        elif       if        or         yield

assert    else       import    pass

break     except     in        raise

Você não precisa memorizar essa lista. Na maior parte dos ambientes de desenvolvimento, as palavras-chave são exibidas em uma cor diferente; se você tentar usar uma como nome de variável, vai perceber.

Expressões e instruções

Uma expressão é uma combinação de valores, variáveis e operadores. Um valor por si mesmo é considerado uma expressão, assim como uma variável, portanto as expressões seguintes são todas legais:

&gt;&gt;&gt; 42

42

&gt;&gt;&gt; n

17

&gt;&gt;&gt; n + 25

42

Quando você digita uma expressão no prompt, o interpretador a avalia, ou seja, ele encontra o valor da expressão. Neste exemplo, o n tem o valor 17 e n + 25 tem o valor 42.

Uma instrução é uma unidade de código que tem um efeito, como criar uma variável ou exibir um valor.

&gt;&gt;&gt; n = 17

&gt;&gt;&gt; print(n)

A primeira linha é uma instrução de atribuição que dá um valor a n. A segunda linha é uma instrução de exibição que exibe o valor de n.

Quando você digita uma instrução, o interpretador a executa, o que significa que ele faz o que a instrução diz. Em geral, instruções não têm valores.

Modo script

Até agora executamos o Python no modo interativo, no qual você interage diretamente com o interpretador. O modo interativo é uma boa forma de começar, mas se estiver trabalhando com mais do que algumas linhas do código, o processo pode ficar desorganizado.

A alternativa é salvar o código em um arquivo chamado script e então executar o interpretador no modo script para executá-lo. Por convenção, os scripts no Python têm nomes que terminam com .py.

Se souber como criar e executar um script no seu computador, você está pronto. Senão, recomendo usar o PythonAnywhere novamente. Inseri instruções sobre como executar programas no modo script em http://tinyurl.com/thinkpython2e.

Como o Python oferece os dois modos, você pode testar pedaços do código no modo interativo antes de colocá-los em um script. Mas há diferenças entre o modo interativo e o modo script que podem confundir as pessoas.

Por exemplo, se estiver usando o Python como uma calculadora, você poderia digitar:

&gt;&gt;&gt; miles = 26.2

&gt;&gt;&gt; miles \* 1.61

42.182

A primeira linha atribui um valor a miles, mas não tem efeito visível. A segunda linha é uma expressão, então o interpretador a avalia e exibe o resultado. No fim, chega-se ao resultado de que uma maratona tem aproximadamente 42 quilômetros.

Mas se você digitar o mesmo código em um script e executá-lo, não recebe nenhuma saída. Uma expressão, por conta própria, não tem efeito visível no modo script. O Python, na verdade, avalia a expressão, mas não exibe o valor a menos que você especifique:

miles = 26.2

print(miles \* 1.61)

Este comportamento pode confundir um pouco no início.

Um script normalmente contém uma sequência de instruções. Se houver mais de uma instrução, os resultados aparecem um após o outro, conforme as instruções sejam executadas.

Por exemplo, o script

print(1)

x = 2

print(x)

produz a saída

1

2

A instrução de atribuição não produz nenhuma saída.

Para verificar sua compreensão, digite as seguintes instruções no interpretador do Python e veja o que fazem:

5

x = 5

x + 1

Agora ponha as mesmas instruções em um script e o execute. Qual é a saída? Altere o script transformando cada expressão em uma instrução de exibição e então o execute novamente.

Ordem das operações

Quando uma expressão contém mais de um operador, a ordem da avaliação depende da ordem das operações. Para operadores matemáticos, o Python segue a convenção matemática. O acrônimo PEMDAS pode ser útil para lembrar das regras:

•        Os Parênteses têm a precedência mais alta e podem ser usados para forçar a avaliação de uma expressão na ordem que você quiser. Como as expressões em parênteses são avaliadas primeiro, 2 \* (3-1) é 4, e (1+1)\*\*(5-2) é 8. Também é possível usar parênteses para facilitar a leitura de uma expressão, como no caso de (minute \* 100) / 60, mesmo se o resultado não for alterado.

•        A Exponenciação tem a próxima precedência mais alta, então 1 + 2\*\*3 é 9, não 27, e 2 \* 3\*\*2 é 18, não 36.

•        A Multiplicação e a Divisão têm precedência mais alta que a Adição e a Subtração. Assim, 2\*3-1 é 5, não 4, e 6+4/2 é 8, não 5.

•        Os operadores com a mesma precedência são avaliados da esquerda para a direita (exceto na exponenciação). Assim, na expressão degrees/ 2 \* pi, a divisão acontece primeiro e o resultado é multiplicado por pi. Para dividir por 2π, você pode usar parênteses ou escrever degrees / 2 / pi.

Eu não fico sempre tentando lembrar da precedência de operadores. Se a expressão não estiver clara à primeira vista, uso parênteses para fazer isso.

Operações com strings

Em geral, não é possível executar operações matemáticas com strings, mesmo se elas parecerem números, então coisas assim são ilegais:

'2'-'1'    'eggs'/'easy'    'third'\*'a charm'

Mas há duas exceções, + e \*.

O operador + executa uma concatenação de strings, ou seja, une as strings pelas extremidades. Por exemplo:

&gt;&gt;&gt; first = 'throat'

&gt;&gt;&gt; second = 'warbler'

&gt;&gt;&gt; first + second

throatwarbler

O operador \* também funciona em strings; ele executa a repetição. Por exemplo, 'Spam'\*3 é 'SpamSpamSpam'. Se um dos valores for uma string, o outro tem de ser um número inteiro.

Este uso de + e \* faz sentido por analogia com a adição e a multiplicação. Tal como 4\*3 é equivalente a 4+4+4, esperamos que 'Spam'\*3 seja o mesmo que 'Spam'+'Spam'+'Spam', e assim é. Por outro lado, há uma diferença significativa entre a concatenação de strings e a repetição em relação à adição e à multiplicação de números inteiros. Você consegue pensar em uma propriedade que a adição tem, mas a concatenação de strings não tem?

Comentários

Conforme os programas ficam maiores e mais complicados, eles são mais difíceis de ler. As linguagens formais são densas e muitas vezes é difícil ver um pedaço de código e compreender o que ele faz ou por que faz isso.

Por essa razão, é uma boa ideia acrescentar notas aos seus programas para explicar em linguagem natural o que o programa está fazendo. Essas notas são chamadas de comentários, e começam com o símbolo \#:

\# computa a percentagem da hora que passou

percentage = (minute \* 100) / 60

Nesse caso, o comentário aparece sozinho em uma linha. Você também pode pôr comentários no fim das linhas:

percentage = (minute \* 100) / 60    \# percentagem de uma hora

Tudo do \# ao fim da linha é ignorado – não tem efeito na execução do programa.

Os comentários tornam-se mais úteis quando documentam algo no código que não está óbvio. Podemos supor que o leitor compreenda o que o código faz; assim, é mais útil explicar porque faz o que faz.

Este comentário é redundante em relação ao código, além de inútil:

v = 5    \# atribui 5 a v

Este comentário contém informações úteis que não estão no código:

v = 5    \# velocidade em metros/segundo.

Bons nomes de variáveis podem reduzir a necessidade de comentários, mas nomes longos podem tornar expressões complexas difíceis de ler, então é preciso analisar o que vale mais a pena.

Depuração

Há três tipos de erros que podem ocorrer em um programa: erros de sintaxe, erros de tempo de execução e erros semânticos. É útil distinguir entre eles para rastreá-los mais rapidamente.

Erro de sintaxe:

A “sintaxe” refere-se à estrutura de um programa e suas respectivas regras. Por exemplo, os parênteses devem vir em pares correspondentes, então (1 + 2) é legal, mas 8) é um erro de sintaxe.

Se houver um erro de sintaxe em algum lugar no seu programa, o Python exibe uma mensagem de erro e para, e não será possível executar o programa. Nas primeiras poucas semanas da sua carreira em programação, você pode passar muito tempo rastreando erros de sintaxe. Ao adquirir experiência, você fará menos erros e os encontrará mais rápido.

Erro de tempo de execução:

O segundo tipo de erro é o erro de tempo de execução, assim chamado porque o erro não aparece até que o programa seja executado. Esses erros também se chamam de exceções porque normalmente indicam que algo excepcional (e ruim) aconteceu.

Os erros de tempo de execução são raros nos programas simples que veremos nos primeiros capítulos, então pode demorar um pouco até você encontrar algum.

Erro semântico:

O terceiro tipo do erro é “semântico”, ou seja, relacionado ao significado. Se houver um erro semântico no seu programa, ele será executado sem gerar mensagens de erro, mas não vai fazer a coisa certa. Vai fazer algo diferente. Especificamente, vai fazer o que você disser para fazer.

Identificar erros semânticos pode ser complicado, porque é preciso trabalhar de trás para a frente, vendo a saída do programa e tentando compreender o que ele está fazendo.

Glossário

variável:

Um nome que se refere a um valor.

atribuição:

Uma instrução que atribui um valor a uma variável.

diagrama de estado:

Uma representação gráfica de um grupo de variáveis e os valores a que se referem.

palavra-chave:

Uma palavra reservada, usada para analisar um programa; não é possível usar palavras-chave como if, def e while como nomes de variáveis.

operando:

Um dos valores que um operador produz.

expressão:

Uma combinação de variáveis, operadores e valores que representa um resultado único.

avaliar:

Simplificar uma expressão executando as operações para produzir um valor único.

instrução:

Uma seção do código que representa um comando ou ação. Por enquanto, as instruções que vimos são instruções de atribuições e de exibição.

executar:

Executar uma instrução para fazer o que ela diz.

modo interativo:

Um modo de usar o interpretador do Python, digitando o código no prompt.

modo script:

Um modo de usar o interpretador do Python para ler código em um script e executá-lo.

script:

Um programa armazenado em um arquivo.

ordem das operações:

As regras que governam a ordem na qual as expressões que envolvem vários operadores e operandos são avaliadas.

concatenar:

Juntar dois operandos pelas extremidades.

comentários:

Informações em um programa destinadas a outros programadores (ou qualquer pessoa que leia o texto fonte) que não têm efeito sobre a execução do programa.

erro de sintaxe:

Um erro em um programa que torna sua análise impossível (e por isso impossível de interpretar).

exceção:

Um erro que se descobre quando o programa é executado.

semântica:

O significado de um programa.

erro semântico:

Um erro que faz com que um programa faça algo diferente do que o programador pretendia.

Exercícios

Exercício 2.1

Repetindo o meu conselho do capítulo anterior, sempre que você aprender um recurso novo, você deve testá-lo no modo interativo e fazer erros de propósito para ver o que acontece.

•        Vimos que n = 42 é legal. E 42 = n?

•        Ou x = y = 1?

•        Em algumas linguagens, cada instrução termina em um ponto e vírgula ;. O que acontece se você puser um ponto e vírgula no fim de uma instrução no Python?

•        E se puser um ponto no fim de uma instrução?

•        Em notação matemática é possível multiplicar x e y desta forma: xy. O que acontece se você tentar fazer o mesmo no Python?

Exercício 2.2

Pratique o uso do interpretador do Python como uma calculadora:

1.        O volume de uma esfera com raio r é . Qual é o volume de uma esfera com raio 5?

2.        Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

3.        Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

