# Apêndice A: Depuração

Durante a depuração, você deve distinguir entre tipos diferentes de erros para rastreá-los mais rapidamente:

•        Erros de sintaxe são descobertos pelo interpretador quando ele está traduzindo o código-fonte para código de bytes. Eles indicam que há algo errado com a estrutura do programa. Exemplo: a omissão dos dois pontos no fim de uma instrução def gera a mensagem um tanto redundante SyntaxError: invalid syntax.

•        Erros de tempo de execução são produzidos pelo interpretador se algo der errado durante a execução do programa. A maior parte das mensagens de erro de tempo de execução inclui informações sobre onde o erro ocorreu e o que as funções estavam fazendo. Exemplo: a recursividade infinita eventualmente leva ao erro de tempo de execução maximum recursion depth exceeded.

•        Erros semânticos são problemas com um programa que é executado sem produzir mensagens de erro, mas que não faz a coisa certa. Exemplo: uma expressão que não pode ser avaliada na ordem esperada, produzindo um resultado incorreto.

O primeiro passo da depuração é compreender com que tipo de erro você está lidando. Embora as próximas seções sejam organizadas pelo tipo de erro, algumas técnicas são aplicáveis em mais de uma situação.

Erros de sintaxe

Os erros de sintaxe normalmente são fáceis de corrigir, uma vez que você descubra quais são. Infelizmente, as mensagens de erro muitas vezes não são úteis. As mensagens mais comuns são SyntaxError: invalid syntax e SyntaxError: invalid token, e nenhuma das duas é muito informativa.

Por outro lado, a mensagem diz onde no programa o problema ocorreu. E, na verdade, diz a você onde o Python notou um problema, que é não necessariamente onde o erro está. Às vezes, o erro está antes da posição da mensagem de erro, muitas vezes na linha precedente.

Se estiver construindo o programa incrementalmente, você terá uma boa ideia sobre onde encontrar o erro. Estará na última linha que acrescentou.

Se estiver copiando o código de um livro, comece comparando com atenção o seu código e o do livro. Verifique cada caractere. Ao mesmo tempo, lembre-se de que o livro pode estar errado, então, se vir algo que parece um erro de sintaxe, pode ser mesmo.

Aqui estão algumas formas de evitar os erros de sintaxe mais comuns:

1.        Confira se não está usando uma palavra-chave do Python para um nome de variável.

2.        Verifique se há dois pontos no fim do cabeçalho de cada instrução composta, incluindo instruções for, while, if e def.

3.        Confira se as strings no código têm as aspas correspondentes. Verifique se todas as aspas são retas, em vez de curvas.

4.        Se tiver strings com várias linhas com aspas triplas (simples ou duplas), confira se fechou a string adequadamente. Uma string não fechada pode causar um erro de invalid token no fim do seu programa, ou pode tratar a parte seguinte do programa como uma string até chegar à string seguinte. No segundo caso, o programa pode nem produzir uma mensagem de erro!

5.        Um operador inicial aberto – (, { ou \[ – faz o Python continuar até a linha seguinte, como se esta fosse parte da instrução atual. Geralmente, um erro ocorre quase imediatamente na linha seguinte.

6.        Confira se há o clássico = em vez do == dentro de uma condicional.

7.        Verifique a endentação para ter certeza de que está alinhada como deveria. O Python pode lidar com espaços e tabulações, mas, se misturá-los, isso pode causar problemas. A melhor forma de evitar esse problema é usar um editor de texto que identifique o Python e gere endentação consistente.

8.        Se há caracteres não ASCII no código (incluindo strings e comentários), isso pode causar problemas, embora o Python 3 normalmente lide com caracteres não ASCII. Tenha cuidado se colar texto de uma página web ou outra fonte.

Se nada funcionar, vá para a próxima seção...

Continuo fazendo alterações e não faz nenhuma diferença

Se o interpretador disser que há um erro e você não o encontra, pode ser que você e o interpretador não estejam olhando para o mesmo código. Verifique o seu ambiente de programação para ter certeza de que o programa que está editando é o mesmo que o Python está tentando executar.

Se não estiver certo, tente pôr um erro de sintaxe óbvio e deliberado no início do programa. Agora execute-o novamente. Se o interpretador não encontrar o novo erro, você não está executando o novo código.

Há alguns culpados prováveis:

•        Você editou o arquivo e esqueceu de salvar as alterações antes de executá-lo novamente. Alguns ambientes de programação fazem isso para você, mas alguns não fazem.

•        Você mudou o nome do arquivo, mas ainda está executando o nome antigo.

•        Algo no seu ambiente de desenvolvimento está configurado incorretamente.

•        Se estiver escrevendo um módulo e usando import, confira se não usou o mesmo nome no seu módulo que os dos módulos padrão do Python.

•        Se você estiver usando import para ler um módulo, lembre-se de que é preciso reiniciar o interpretador ou usar reload para ler um arquivo alterado. Se importar o módulo novamente, ele não faz nada.

Se já esgotou as possibilidades e não conseguiu descobrir o que está acontecendo, uma abordagem é começar novamente com um programa como “Hello, World!”, para ter certeza de que consegue executar um programa conhecido. Então, gradualmente acrescente as partes do programa original ao novo.

Erros de tempo de execução

Uma vez que o seu programa esteja sintaticamente correto, o Python pode lê-lo e, pelo menos, começar a executá-lo. O que poderia dar errado?

Meu programa não faz nada

Este problema é mais comum quando o seu arquivo é composto de funções e classes, mas na verdade não invoca uma função para começar a execução. Isso pode ser intencional se você só planeja importar este módulo para fornecer classes e funções.

Se não for intencional, tenha certeza de que há uma chamada de função no programa, e que o fluxo de execução o alcança (veja “Fluxo da execução” a seguir).

Meu programa fica suspenso

Se um programa parar e parecer que não está fazendo nada, ele está “suspenso”. Muitas vezes isso significa que está preso em um loop ou recursividade infinita.

•        Se houver determinado loop que você suspeita ser o problema, acrescente uma instrução print imediatamente antes do loop que diga “entrando no loop”, e outra imediatamente depois que diga “saindo do loop”.

        Execute o programa. Se receber a primeira mensagem e a segunda não, você tem um loop infinito. Vá à seção “Loop infinito” mais adiante.

•        Na maior parte do tempo, a recursividade infinita fará com que o programa seja executado durante algum tempo e então gere um erro “RuntimeError: Maximum recursion depth exceeded”. Se isso acontecer, vá à seção “Recursividade infinita” mais adiante.

        Se não estiver recebendo este erro, mas suspeita que há um problema com um método ou função recursiva, você ainda pode usar as técnicas da seção “Recursividade infinita”.

•        Se nenhum desses passos funcionar, comece a testar outros loops e outras funções e métodos recursivos.

•        Se isso não funcionar, então é possível que você não entenda o fluxo de execução do seu programa. Vá à seção “Fluxo de execução” mais adiante.

Loop infinito

Se você acha que há um loop infinito e talvez saiba qual loop está causando o problema, acrescente uma instrução print no fim do loop que exiba os valores das variáveis na condição e o valor da condição.

Por exemplo:

while x &gt; 0 and y &lt; 0 :

    \# faz algo com x

    \# faz algo com y

    print('x: ', x)

    print('y: ', y)

    print("condition: ", (x &gt; 0 and y &lt; 0))

Agora, quando executar o programa, você verá três linhas de saída para cada vez que o programa passar pelo loop. Na última vez que passar pelo loop, a condição deve ser False. Se o loop continuar, você poderá ver os valores de x e y, e compreender porque não estão sendo atualizados corretamente.

Recursividade infinita

Na maioria das vezes, a recursividade infinita faz o programa rodar durante algum tempo e então produzir um erro de Maximum recursion depth exceeded.

Se suspeitar que uma função está causando recursividade infinita, confira se há um caso-base. Deve haver alguma condição que faz a função retornar sem fazer uma invocação recursiva. Do contrário, você terá que repensar o algoritmo e identificar um caso-base.

Se houver um caso-base, mas o programa não parece alcançá-lo, acrescente uma instrução print no início da função para exibir os parâmetros. Agora, quando executar o programa, você verá algumas linhas de saída cada vez que a função for invocada, e verá os valores dos parâmetros. Se os parâmetros não estiverem se movendo em direção ao caso-base, você terá algumas ideias sobre a razão disso.

Fluxo de execução

Se não tiver certeza de como o fluxo de execução está se movendo pelo seu programa, acrescente instruções print ao começo de cada função com uma mensagem como “entrada na função foo”, onde foo é o nome da função.

Agora, quando executar o programa, ele exibirá cada função que for invocada.

Quando executo o programa recebo uma exceção

Se algo der errado durante o tempo de execução, o Python exibe uma mensagem que inclui o nome da exceção, a linha do programa onde o problema ocorreu, e um traceback.

O traceback identifica a função que está rodando atualmente, e a função que a chamou, assim como a função que chamou esta, e assim por diante. Em outras palavras, ele traça a sequência de chamadas de função que fez com que você chegasse onde está, incluindo o número da linha no seu arquivo onde cada chamada ocorreu.

O primeiro passo é examinar o lugar no programa onde o erro ocorreu e ver se consegue compreender o que aconteceu. Esses são alguns dos erros de tempo de execução mais comuns:

NameError:

Você está tentando usar uma variável que não existe no ambiente atual. Confira se o nome está escrito corretamente e de forma consistente. E lembre-se de que as variáveis locais são locais; você não pode se referir a elas a partir do exterior da função onde são definidas.

TypeError:

Há várias causas possíveis:

•        Você está tentando usar um valor de forma inadequada. Exemplo: indexar uma string, lista ou tupla com algo diferente de um número inteiro.

•        Não há correspondência entre os itens em uma string de formatação e os itens passados para conversão. Isso pode acontecer se o número de itens não tiver correspondência ou uma conversão inválida for chamada.

•        Você está passando o número incorreto de argumentos a uma função. Para métodos, olhe para a definição do método e verifique se o primeiro parâmetro é self. Então olhe para a invocação do método; confira se está invocando o método a um objeto com o tipo correto e fornecendo os outros argumentos corretamente.

KeyError:

Você está tentando acessar um elemento de um dicionário usando uma chave que o dicionário não contém. Se as chaves forem strings, lembre-se de que letras maiúsculas são diferentes de minúsculas.

AttributeError:

Você está tentando acessar um atributo ou método que não existe. Verifique a ortografia! Você pode usar a função integrada vars para listar os atributos que existem mesmo.

Se um AttributeError indicar que um objeto é do tipo NoneType, fica subentendido que é None. Então o problema não é o nome do atributo, mas o objeto.

Pode ser que o objeto seja none porque você se esqueceu de retornar um valor de uma função; se chegar ao fim de uma função sem chegar a uma instrução return, ela retorna None. Outra causa comum é usar o resultado de um método de lista, como sort, que retorne None.

IndexError:

O índice que você está usando para acessar uma lista, string ou tupla é maior que o seu comprimento menos um. Imediatamente antes do local do erro, acrescente uma instrução print para exibir o valor do índice e o comprimento do array. O array é do tamanho certo? O índice tem o valor certo?

O depurador do Python (pdb) é útil para rastrear exceções porque permite examinar o estado do programa imediatamente antes do erro. Você pode ler sobre o pdb em https://docs.python.org/3/library/pdb.html.

Acrescentei tantas instruções print que fui inundado pelos resultados

Um dos problemas com a utilização de instruções print para a depuração é que você pode terminar enterrado pelos resultados. Há duas formas de prosseguir: simplifique a saída ou simplifique o programa.

Para simplificar a saída, você pode retirar ou transformar as instruções print que não estão ajudando em comentários, ou combiná-las, ou formatar a saída para que seja mais fácil de entender.

Para simplificar o programa, há várias coisas que você pode fazer. Em primeiro lugar, reduza o problema no qual o programa está trabalhando. Por exemplo, se está fazendo uma busca em uma lista, procure em uma lista pequena. Se o programa receber entradas do usuário, dê a entrada mais simples possível que cause o problema.

Em segundo lugar, limpe o programa. Retire o código morto e reorganize o programa para torná-lo o mais fácil possível de ler. Por exemplo, se você suspeitar que o problema está em uma parte profundamente aninhada do programa, tente reescrever aquela parte com uma estrutura mais simples. Se suspeitar de uma função grande, tente quebrá-la em funções menores para testá-las separadamente.

Muitas vezes, o próprio processo de encontrar o caso de teste mínimo leva você ao problema. Se descobrir que um programa funciona em uma situação, mas não em outra, isso dá uma pista sobre o que está acontecendo.

De forma similar, reescrever uma parte do código pode ajudar a encontrar erros sutis. Se fizer uma alteração que você ache que não vai afetar o programa, mas que acabe afetando, isso pode ajudá-lo.

Erros semânticos

De algumas formas, os erros semânticos são os mais difíceis de depurar, porque o interpretador não fornece nenhuma informação sobre qual é o problema. Só você sabe o que o programa deve fazer.

O primeiro passo é fazer uma conexão entre o texto do programa e o comportamento que está vendo. Você precisa de uma hipótese sobre o que o programa está fazendo de fato. Uma das coisas que torna isso difícil é que os computadores são rápidos.

Pode ser que você queira diminuir a velocidade do programa para ser equivalente à humana; com alguns depuradores é possível fazer isso. No entanto, o tempo que leva para inserir instruções print bem colocadas muitas vezes é curto em comparação ao da configuração do depurador, inserção e remoção de marcações e colocação do “compasso” do programa onde o erro está ocorrendo.

Meu programa não funciona

Você deve se perguntar o seguinte:

•        Há algo que o programa deveria fazer, mas que não parece acontecer? Encontre a seção do código que executa a função em questão e confira se está sendo executada quando você acha que deveria.

•        Algo está acontecendo, mas não o que deveria? Encontre o código no seu programa que executa a função em questão e veja se está sendo executada na hora errada.

•        Uma seção do código está produzindo um efeito que não é o esperado? Tenha certeza de que entende o código em questão, especialmente se envolver funções ou métodos de outros módulos do Python. Leia a documentação das funções que chama. Teste-as escrevendo casos de teste simples e verificando os resultados.

Para programar, é preciso ter um modelo mental de como os programas funcionam. Se escrever um programa que não faz o que espera, muitas vezes o problema não está no programa, está no seu modelo mental.

A melhor forma de corrigir o seu modelo mental é quebrar o programa nos seus componentes (normalmente as funções e métodos) e testar cada componente em separado. Uma vez que encontre a discrepância entre o seu modelo e a realidade, poderá resolver o problema.

Naturalmente, você deveria construir e testar componentes conforme desenvolva o programa. Assim, se encontrar um problema, deve haver só uma pequena quantidade de código novo que não sabe se está correto.

Tenho uma baita expressão cabeluda e ela não faz o que espero

Escrever expressões complexas é ótimo enquanto são legíveis, mas elas podem ser difíceis de depurar. Muitas vezes é uma boa ideia quebrar uma expressão complexa em uma série de atribuições a variáveis temporárias.

Por exemplo:

self.hands\[i\].addCard(self.hands\[self.findNeighbor(i)\].popCard())

A expressão pode ser reescrita assim:

neighbor = self.findNeighbor(i)

pickedCard = self.hands\[neighbor\].popCard()

self.hands\[i\].addCard(pickedCard)

A versão explícita é mais fácil de ler porque os nomes das variáveis oferecem documentação adicional, e é mais fácil de depurar porque você pode verificar os tipos das variáveis intermediárias e exibir seus valores.

Outro problema que pode ocorrer com grandes expressões é que a ordem da avaliação pode não ser o que você espera. Por exemplo, se estiver traduzindo a expressão  para o Python, poderia escrever:

y = x / 2 \* math.pi

Isso não está correto porque a multiplicação e a divisão têm a mesma precedência e são avaliadas da esquerda para a direita. Então, é assim que essa expressão é calculada: xπ/2.

Uma boa forma de depurar expressões é acrescentar parênteses para tornar a ordem da avaliação explícita:

y = x / (2 \* math.pi)

Sempre que não tiver certeza sobre a ordem da avaliação, use parênteses. Além de o programa ficar correto (quanto à execução do que era pretendido), ele também será mais legível para outras pessoas que não memorizaram a ordem de operações.

Tenho uma função que não retorna o que espero

Se tiver uma instrução return com uma expressão complexa, não há possibilidade de exibir o resultado antes do retorno. Novamente, você pode usar uma variável temporária. Por exemplo, em vez de:

return self.hands\[i\].removeMatches()

você poderia escrever:

count = self.hands\[i\].removeMatches()

return count

Agora você tem a oportunidade de exibir o valor de count antes do retorno.

Estou perdido e preciso de ajuda

Em primeiro lugar, afaste-se do computador por alguns minutos. Computadores emitem ondas que afetam o cérebro, causando estes sintomas:

•        frustração e raiva;

•        crenças supersticiosas (“o computador me odeia”) e pensamento mágico (“o programa só funciona quando uso o meu chapéu virado para trás”);

•        programação aleatória (a tentativa de programar escrevendo todos os programas possíveis e escolhendo aquele que faz a coisa certa).

Se estiver sofrendo algum desses sintomas, levante-se e dê uma volta. Quando se acalmar, pense no programa. O que ele está fazendo? Quais são algumas causas possíveis para esse comportamento? Quando foi a última vez que tinha um programa funcionando, e o que fez depois disso?

Às vezes leva tempo para encontrar um erro. Com frequência encontro erros quando estou longe do computador e deixo a minha mente vagar. Os melhores lugares para encontrar erros são os trens, o chuveiro e a cama, logo antes de adormecer.

Sério, preciso mesmo de ajuda

Acontece. Mesmo os melhores programadores ocasionalmente empacam. Pode ocorrer de você trabalhar tanto em um programa que não consegue enxergar o erro. Precisa de outro par de olhos.

Antes de trazer mais alguém, não se esqueça de se preparar. Seu programa deve ser o mais simples possível, e deve estar funcionando com a menor entrada possível que cause o erro. Deve ter instruções print nos lugares adequados (e a saída que produzem deve ser compreensível). Você deve entender o problema o suficiente para descrevê-lo de forma concisa.

Ao trazer alguém para ajudar, lembre-se de dar as informações de que a pessoa possa precisar:

•        Se houver uma mensagem de erro, qual é e que parte do programa indica?

•        Qual foi a última coisa que fez antes de este erro ocorrer? Quais foram as últimas linhas de código que escreveu, ou qual é o novo caso de teste que falhou?

•        O que tentou até agora e o que aprendeu?

Quando encontrar o erro, pense por um segundo no que poderia ter feito para encontrá-lo mais rápido. Na próxima vez em que vir algo similar, poderá encontrar o erro mais rapidamente.

Lembre-se, a meta não é só fazer o programa funcionar. A meta é aprender como fazer o programa funcionar.

