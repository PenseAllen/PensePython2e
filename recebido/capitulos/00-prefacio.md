# Prefácio

## A estranha história deste livro

Em janeiro de 1999 eu me preparava para dar aula a uma turma de programação introdutória em Java. Já tinha dado esse curso três vezes e estava ficando frustrado. O índice de aprovação era muito baixo e mesmo entre os alunos aprovados, o nível geral das notas era baixo demais.

Um dos problemas que eu via eram os livros. Eram muito grandes, com detalhes desnecessários sobre o Java, e não havia orientação de alto nível sobre como programar. E todos eles sofriam do efeito alçapão: no início era fácil, os alunos iam aprendendo aos poucos, e lá pelo Capítulo 5, perdiam o chão. Era muito material novo, muito rápido, e eles acabavam engatinhando no resto do semestre.

Duas semanas antes do primeiro dia de aula, eu decidi escrever meu próprio livro. Meus objetivos eram:

•        que o livro fosse curto. Era melhor os alunos lerem 10 páginas que não lerem 50.

•        abordar o vocabulário com cuidado. Tentei minimizar o jargão e definir cada termo no momento do primeiro uso.

•        construir o aprendizado passo a passo. Para evitar alçapões, dividi os tópicos mais difíceis e em uma série de etapas menores.

•        que o conteúdo fosse concentrado em programar mesmo, não na linguagem de programação. Selecionei um subconjunto mínimo útil do Java e omiti o resto.

Eu precisava de um título, então, por capricho, decidi chamá-lo de Pense como um cientista da computação.

A minha primeira versão era apenas um esboço, mas funcionou. Os alunos liam e entendiam o suficiente para podermos usar o tempo de aula para os tópicos difíceis, interessantes e (o mais importante) para permitir que os alunos praticassem.

Lancei o livro sob uma Licença de Documentação Livre GNU, que permite aos usuários copiar, modificar e distribuir o livro.

E o que aconteceu em seguida foi legal. Jeff Elkner, um professor de ensino médio na Virgínia adotou meu livro e o traduziu para Python. Ele me enviou uma cópia de sua tradução e tive a experiência excepcional de aprender Python lendo o meu próprio livro. Com a editora Green Tea, publiquei a primeira versão em Python em 2001.

Em 2003 comecei a trabalhar no Olin College e a ensinar Python pela primeira vez na vida. O contraste com o Java era notável. Os estudantes tinham menos dificuldades, aprendiam mais, trabalhavam em projetos mais interessantes e geralmente se divertiam muito mais.

Desde então continuei a desenvolver o livro, corrigindo erros, melhorando alguns exemplos e acrescentando material, especialmente exercícios.

O resultado está aqui, agora com o título menos grandioso de Pense em Python. Fiz algumas alterações:

•        Acrescentei uma seção sobre depuração (debugging) no fim de cada capítulo. Essas seções apresentam técnicas gerais para encontrar e evitar bugs (erros de programação) e avisos sobre armadilhas do Python.

•        Acrescentei exercícios, incluindo testes curtos de compreensão e alguns projetos substanciais. A maior parte dos exercícios tem um link para a minha solução.

•        Acrescentei uma série de estudos de caso – exemplos mais longos com exercícios, soluções e discussões.

•        Expandi a discussão sobre planos de desenvolvimento de programas e padrões de design básicos.

•        Acrescentei apêndices sobre depuração e análise de algoritmos.

Esta edição de Pense em Python tem as seguintes novidades:

•        O livro e todo o código de apoio foram atualizados para o Python 3.

•        Acrescentei algumas seções e mais detalhes sobre a web, para ajudar os principiantes a executar o Python em um navegador, e não ter que lidar com a instalação do programa até que seja necessário.

•        Para “Módulo turtle” na página 63 troquei meu próprio pacote gráfico turtle, chamado Swampy, para um módulo Python mais padronizado, turtle, que é mais fácil de instalar e mais eficiente.

•        Acrescentei um novo capítulo chamado “Extra”, que introduz alguns recursos adicionais do Python, não estritamente necessários, mas às vezes práticos.

Espero que goste de trabalhar com este livro, e que ele o ajude a aprender a programar e pensar, pelo menos um pouquinho, como um cientista da computação.

Allen B. Downey
Olin College

## Convenções usadas neste livro

As seguintes convenções tipográficas são usadas neste livro:

Itálico

Indica novos termos, URLs, endereços de email, nomes de arquivo e extensões de arquivo.

Negrito

Indica termos definidos no glossário no final de capítulo.

Monoespaçado

Usada para código de programa, bem como dentro de parágrafos para referir-se a elementos do programa, como nomes de variáveis ou de funções, bancos de dados, tipos de dados, variáveis de ambiente, instruções e palavras-chave.

Monoespaçado negrito

Exibe comandos ou outros textos que devem ser digitados literalmente pelo usuário.

Monoespaçado itálico

Exibe textos que devem ser substituídos por valores fornecidos pelos usuários ou por valores determinados pelo contexto.

Exemplos de uso de código (de acordo com a política da O'Reilly)

Há material suplementar (exemplos de código, exercícios etc.) disponível para baixar em http://www.greenteapress.com/thinkpython2/code.

Este livro serve para ajudar você a fazer o que precisa. Em geral, se o livro oferece exemplos de código, você pode usá-los nos seus programas e documentação. Não é preciso entrar em contato conosco para pedir permissão, a menos que esteja reproduzindo uma porção significativa do código. Por exemplo, escrever um programa que use vários pedaços de código deste livro não exige permissão. Vender ou distribuir um CD-ROM de exemplos dos livros da O’Reilly exige permissão. Responder a uma pergunta citando este livro e reproduzindo exemplos de código não exige permissão. Incorporar uma quantidade significativa de exemplos de código deste livro na documentação do seu produto exige permissão.

Agradecemos, mas não exigimos, crédito. O crédito normalmente inclui o título, o autor, a editora e o ISBN. Por exemplo: “Pense em Python, 2ª edição, por Allen B. Downey (O’Reilly). Copyright 2016 Allen Downey, 978-1-4919-3936-9.”

Se acreditar que o seu uso dos exemplos de código não se ajusta à permissão dada anteriormente, fique à vontade para entrar em contato conosco pelo email permissions@oreilly.com.

Como entrar em contato conosco

Envie comentários e dúvidas sobre este livro à editora, escrevendo para: novatec@novatec.com.br.

Temos uma página web para este livro na qual incluímos erratas, exemplos e quaisquer outras informações adicionais.

•        Página da edição em português

        http://www.novatec.com.br/catalogo/7522508-pense-em-python

•        Página da edição original em inglês

        http://bit.ly/think-python\_2E

Para obter mais informações sobre os livros da Novatec, acesse nosso site em http://www.novatec.com.br.

Agradecimentos

Muito obrigado a Jeff Elkner, que traduziu meu livro de Java para o Python, o que deu início a este projeto e me apresentou ao que acabou sendo a minha linguagem favorita.

Agradeço também a Chris Meyers, que contribuiu em várias seções do Pense como um cientista da computação.

Obrigado à Fundação do Software Livre pelo desenvolvimento da Licença de Documentação Livre GNU, que me ajudou a tornar possível a colaboração com Jeff e Chris, e ao Creative Commons pela licença que estou usando agora.

Obrigado aos editores do Lulu, que trabalharam no Pense como um cientista da computação.

Obrigado aos editores da O’Reilly Media, que trabalharam no Pense em Python.

Obrigado a todos os estudantes que trabalharam com versões anteriores deste livro e a todos os contribuidores (listados a seguir) que enviaram correções e sugestões.

Lista de contribuidores

Mais de cem leitores perspicazes e atentos enviaram sugestões e correções nos últimos anos. Suas contribuições e entusiasmo por este projeto foram inestimáveis.

Se tiver alguma sugestão ou correção, por favor, envie um email a feedback@thinkpython.com. Se eu fizer alguma alteração baseada no seu comentário, acrescentarei seu nome à lista de contribuidores (a menos que você peça para eu omitir a informação).

Se você incluir pelo menos uma parte da frase onde o erro aparece, é mais fácil para eu procurá-lo. Também pode ser o número da página e seção, mas aí é um pouquinho mais difícil de encontrar o erro a ser corrigido. Obrigado!

•        Lloyd Hugh Allen enviou uma correção da Seção 8.4.

•        Yvon Boulianne enviou a correção de um erro semântico no Capítulo 5.

•        Fred Bremmer enviou uma correção da Seção 2.1.

•        Jonah Cohen escreveu os scripts em Perl para converter a fonte de LaTeX deste livro para o belo HTML.

•        Michael Conlon enviou uma correção gramatical do Capítulo 2 e uma melhoria no estilo do Capítulo 1, além de iniciar a discussão sobre os aspectos técnicos de interpretadores.

•        Benoit Girard enviou uma correção a um erro humorístico na Seção 5.6.

•        Courtney Gleason e Katherine Smith escreveram horsebet.py, que foi usado como um estudo de caso em uma versão anterior do livro. O programa agora pode ser encontrado no site.

•        Lee Harr enviou mais correções do que temos espaço para relacionar aqui, e na verdade ele deve ser apontado como um dos editores principais do texto.

•        James Kaylin é um estudante que usa o texto. Ele enviou várias correções.

•        David Kershaw corrigiu a função catTwice defeituosa na Seção 3.10.

•        Eddie Lam entregou diversas correções aos Capítulos 1, 2, e 3. Ele também corrigiu o Makefile para criar um índice na primeira vez que rodar e nos ajudou a estabelecer um esquema de versionamento.

•        Man-Yong Lee enviou uma correção do código de exemplo na Seção 2.4.

•        David Mayo indicou que a palavra “inconscientemente” no Capítulo 1 devia ser alterada para “subconscientemente”.

•        Chris McAloon enviou várias correções para as Seções 3.9 e 3.10.

•        Matthew J. Moelter tem contribuído já há um bom tempo e entregou diversas correções e sugestões para o livro.

•        Simon Dicon Montford informou que havia uma definição de função ausente e vários erros de ortografia no Capítulo 3. Ele também encontrou erros na função increment no Capítulo 13.

•        John Ouzts corrigiu a definição de “valor de retorno” no Capítulo 3.

•        Kevin Parks enviou comentários e sugestões valiosos para melhorar a distribuição do livro.

•        David Pool encontrou um erro de ortografia no glossário do Capítulo 1, e também enviou palavras gentis de encorajamento.

•        Michael Schmitt enviou uma correção ao capítulo sobre arquivos e exceções.

•        Robin Shaw indicou um erro na Seção 13.1, onde a função printTime foi usada em um exemplo sem ser definida.

•        Paul Sleigh encontrou um erro no Capítulo 7 e um bug no script em Perl de Jonah Cohen, que gera o HTML do LaTeX.

•        Craig T. Snydal está testando o texto em um curso na Drew University. Ele contribuiu com várias sugestões valiosas e correções.

•        Ian Thomas e seus alunos estão usando o texto em um curso de programação. Eles são os primeiros a testar os capítulos da segunda metade do livro e fizeram muitas correções e sugestões.

•        Keith Verheyden enviou uma correção no Capítulo 3.

•        Peter Winstanley nos avisou sobre um erro antigo no latim do Capítulo 3.

•        Chris Wrobel fez correções ao código no capítulo sobre arquivos E/S e exceções.

•        Moshe Zadka fez contribuições inestimáveis para este projeto. Além de escrever o primeiro rascunho do capítulo sobre Dicionários, ele forneceu orientação contínua nas primeiras etapas do livro.

•        Christoph Zwerschke enviou várias correções e sugestões pedagógicas, e explicou a diferença entre gleich e selbe.

•        James Mayer enviou-nos um monte de erros tipográficos e ortográficos, inclusive dois da lista de contribuidores.

•        Hayden McAfee percebeu uma inconsistência potencialmente confusa entre dois exemplos.

•        Angel Arnal faz parte de uma equipe internacional de tradutores que trabalhou na versão do texto para o espanhol. Ele também encontrou vários erros na versão em inglês.

•        Tauhidul Hoque e Lex Berezhny criaram as ilustrações do Capítulo 1 e melhoraram muitas das outras ilustrações.

•        O Dr. Michele Alzetta pegou um erro no Capítulo 8 e enviou alguns comentários pedagógicos interessantes e sugestões sobre Fibonacci e o jogo do Mico.

•        Andy Mitchell pegou um erro de ortografia no Capítulo 1 e um exemplo ruim no Capítulo 2.

•        Kalin Harvey sugeriu um esclarecimento no Capítulo 7 e achou alguns erros de ortografia.

•        Christopher P. Smith encontrou vários erros de ortografia e ajudou-nos a atualizar o livro para o Python 2.2.

•        David Hutchins encontrou um erro de ortografia no prefácio.

•        Gregor Lingl é professor de Python em uma escola de Ensino Médio em Viena, na Áustria. Ele está trabalhando em uma tradução do livro para o alemão e encontrou alguns erros feios no Capítulo 5.

•        Julie Peters achou um erro de ortografia no prefácio.

•        Florin Oprina enviou uma melhoria para o makeTime, uma correção no printTime e um belo erro de ortografia.

•        D. J. Webre sugeriu um esclarecimento no Capítulo 3.

•        Ken encontrou um punhado de erros nos Capítulos 8, 9 e 11.

•        Ivo Wever achou um erro de ortografia no Capítulo 5 e sugeriu um esclarecimento no Capítulo 3.

•        Curtis Yanko sugeriu um esclarecimento no Capítulo 2.

•        Ben Logan enviou vários erros de ortografia e problemas com a tradução do livro para HTML.

•        Jason Armstrong percebeu que faltava uma palavra no Capítulo 2.

•        Louis Cordier notou um ponto no Capítulo 16 onde o código não correspondia com o texto.

•        Brian Caim sugeriu vários esclarecimentos nos Capítulos 2 e 3.

•        Rob Black entregou um monte de correções, inclusive algumas alterações para Python 2.2.

•        Jean-Philippe Rey, da École Centrale Paris, enviou uma série de patches, inclusive algumas atualizações do Python 2.2 e outras melhorias bem pensadas.

•        Jason Mader, da George Washington University, fez uma série de sugestões e correções úteis.

•        Jan Gundtofte-Bruun nos lembrou de que “un erro” é um erro.

•        Abel David e Alexis Dinno nos lembraram de que o plural de “matriz” é “matrizes”, não “matrixes”. Este erro esteve no livro por anos, mas dois leitores com as mesmas iniciais informaram a respeito dele no mesmo dia. Bizarro.

•        Charles Thayer nos estimulou a sumir com os pontos e vírgulas que tínhamos posto no final de algumas instruções e a otimizar nosso uso de “argumento” e “parâmetro”.

•        Roger Sperberg indicou uma parte distorcida de lógica no Capítulo 3.

•        Sam Bull indicou um parágrafo confuso no Capítulo 2.

•        Andrew Cheung indicou duas ocorrências de “uso antes da definição”.

•        C. Corey Capel notou uma palavra ausente e um erro de ortografia no Capítulo 4.

•        Alessandra ajudou a eliminar algumas coisas confusas do Turtle.

•        Wim Champagne encontrou uma confusão de palavras em um exemplo de dicionário.

•        Douglas Wright indicou um problema com a divisão pelo piso em arc.

•        Jared Spindor encontrou uma confusão no fim de uma frase.

•        Lin Peiheng enviou várias sugestões muito úteis.

•        Ray Hagtvedt enviou dois erros e um quase erro.

•        Torsten Hübsch indicou uma inconsistência no Swampy.

•        Inga Petuhhov corrigiu um exemplo no Capítulo 14.

•        Arne Babenhauserheide enviou várias correções úteis.

•        Mark E. Casida é é bom em encontrar palavras repetidas.

•        Scott Tyler preencheu um que faltava. E em seguida enviou um monte de correções.

•        Gordon Shephard enviou várias correções, todas em emails separados.

•        Andrew Turner notou um erro no Capítulo 8.

•        Adam Hobart corrigiu um problema com a divisão pelo piso em arc.

•        Daryl Hammond e Sarah Zimmerman indicaram que eu trouxe o math.pi para a mesa cedo demais. E Zim achou um erro de ortografia.

•        George Sass encontrou um bug em uma seção de depuração.

•        Brian Bingham sugeriu o Exercício 11.5.

•        Leah Engelbert-Fenton indicou que usei tuple como um nome de variável, contrariando meu próprio conselho. E, em seguida, encontrou uma porção de erros de ortografia e um “uso antes da definição”.

•        Joe Funke achou um erro de ortografia.

•        Chao-chao Chen encontrou uma inconsistência no exemplo de Fibonacci.

•        Jeff Paine sabe a diferença entre espaço e spam.

•        Lubos Pintes enviou um erro de ortografia.

•        Gregg Lind e Abigail Heithoff sugeriram o Exercício 14.3.

•        Max Hailperin entregou uma série de correções e sugestões. Max é um dos autores das extraordinárias Abstrações Concretas (Tecnologia de curso, 1998), que você pode querer ler quando terminar este livro.

•        Chotipat Pornavalai encontrou um erro em uma mensagem de erro.

•        Stanislaw Antol enviou uma lista com várias sugestões úteis.

•        Eric Pashman enviou uma série de correções para os Capítulos 4-11.

•        Miguel Azevedo encontrou alguns erros de ortografia.

•        Jianhua Liu enviou uma longa lista de correções.

•        Nick King encontrou uma palavra que faltava.

•        Martin Zuther enviou uma longa lista de sugestões.

•        Adam Zimmerman encontrou uma inconsistência em uma ocorrência de “ocorrência” e vários outros erros.

•        Ratnakar Tiwari sugeriu uma nota de rodapé explicando triângulos degenerados.

•        Anurag Goel sugeriu outra solução para is\_abecedarian e enviou algumas correções adicionais. E ele sabe soletrar Jane Austen.

•        Kelli Kratzer notou um dos erros de ortografia.

•        Mark Griffiths indicou um exemplo confuso no Capítulo 3.

•        Roydan Ongie encontrou um erro no meu método de Newton.

•        Patryk Wolowiec me ajudou com um problema na versão do HTML.

•        Mark Chonofsky me falou de uma nova palavra-chave no Python 3.

•        Russell Coleman ajudou com a minha geometria.

•        Wei Huang notou vários erros tipográficos.

•        Karen Barber achou o erro de ortografia mais antigo no livro.

•        Nam Nguyen encontrou um erro de ortografia e indicou que usei o Decorator, mas não mencionei o nome.

•        Stéphane Morin enviou várias correções e sugestões.

•        Paul Stoop corrigiu um erro de ortografia em uses\_only.

•        Eric Bronner indicou uma confusão na discussão da ordem de operações.

•        Alexandros Gezerlis definiu um novo padrão para o número e a qualidade das sugestões que enviou. Estamos profundamente gratos!

•        Gray Thomas sabe diferenciar a direita da esquerda.

•        Giovanni Escobar Sosa enviou uma longa lista de correções e sugestões.

•        Alix Etienne corrigiu uma das URLs.

•        Kuang He encontrou um erro de ortografia.

•        Daniel Neilson corrigiu um erro sobre a ordem de operações.

•        Will McGinnis indicou que polyline foi definida de forma diferente em dois lugares.

•        Swarup Sahoo notou que faltava um ponto e vírgula.

•        Frank Hecker indicou que um exercício estava mal especificado e encontrou alguns links quebrados.

•        Animesh B me ajudou a esclarecer um exemplo confuso.

•        Martin Caspersen encontrou dois erros de arredondamento.

•        Gregor Ulm enviou várias correções e sugestões.

•        Dimitrios Tsirigkas sugeriu que eu esclarecesse um exercício.

•        Carlos Tafur enviou uma página de correções e sugestões.

•        Martin Nordsletten encontrou um bug na solução de um exercício.

•        Lars O.D. Christensen encontrou uma referência quebrada.

•        Vitor Simeone encontrou um erro de ortografia.

•        Sven Hoexter indicou que uma entrada de uma variável nomeada se sobrepõe a uma função integrada.

•        Viet Le encontrou um erro de ortografia.

•        Stephen Gregory indicou o problema com cmp no Python 3.

•        Matthew Shultz me avisou sobre um link quebrado.

•        Lokesh Kumar Makani me avisou sobre alguns links quebrados e algumas alterações em mensagens de erro.

•        Ishwar Bhat corrigiu minha declaração do último teorema de Fermat.

•        Brian McGhie sugeriu um esclarecimento.

•        Andrea Zanella traduziu o livro para o italiano e enviou uma série de correções ao longo do caminho.

•        Muito, muito obrigada a Melissa Lewis e Luciano Ramalho pelos comentários e sugestões excelentes na segunda edição.

•        Obrigado a Harry Percival do PythonAnywhere por ajudar as pessoas a começar a usar o Python em um navegador.

•        Xavier Van Aubel fez várias correções úteis na segunda edição.
