# Especificação da Tarefa:

A tarefa de programação consiste em desenvolver uma Calculadora Matricial utilizando o Paradigma Orientado a Objetos. A Calculadora deve permitir a realização de operações com matrizes de m linhas e n colunas de números reais (ponto flutuante de precisão dupla), escolhidas de uma lista de matrizes armazenadas em memória principal. Este programa deverá implementar uma hierarquia de classes que permita operar de maneira diferenciada quando a matriz for “Quadrada”, ou “Triangular Inferior”, ou “Triangular Superior”, ou “Diagonal”.

As operações matriciais poderão ser aplicadas a quaisquer matrizes da lista, e deverão conter código para tratamento de exceções, como incompatibilidade entre matrizes em uma soma. Quando as matrizes operadas forem da mesma classe, o programa deverá utilizar uma operação especializada que execute o menor número de operações possível. Por exemplo, ao se somar duas matrizes diagonais 3x3, o programa deverá realizar apenas as 3 somas entre os elementos correspondentes das diagonais principais, e não entre os demais zeros.

O programa deverá, também, reconhecer a classe da matriz sendo armazenada e utilizar o “menor” espaço de memória possível para armazenar os seus elementos. Por exemplo, para uma matriz diagonal 3x3, deverá utilizar apenas 3 memórias de ponto flutuantes, uma para cada elemento da sua diagonal principal, pois são os únicos que podem ser diferentes de zero.

A fim de alcançar tais propriedades, as matrizes gerais m x n, e quadradas n x n, devem usar como estruturas de dados interna “array” de “arrays”. Quanto as matrizes triangulares e diagonais, para não ter que armazenar os zeros, as triangulares devem utilizar internamente uma estrutura de dados baseada em “array” de listas (pois as linhas possuem tamanho diferentes), e as diagonais um “array” simples (pois somente os elementos da diagonal principal podem ser não nulos).

A Calculadora deverá pelo menos oferecer as seguintes operações matriciais:
1. Soma e subtração matricial: C = A + B e C = A – B, onde A, B são matrizes da lista e C será uma nova matriz criada e inserida na lista.
2. Multiplicação por escalar: C = aA, onde a é um número real dado e A é uma matriz da lista e C será uma nova matriz criada e inserida na lista.
3. Multiplicação Matricial: C = A x B, onde A, B são matrizes da lista e C será uma nova matriz criada e inserida na lista.
4. Transposição.
5. Se a matriz for Quadrada, o TRAÇO da matriz (igual à soma dos elementos da sua diagonal principal)
6. Se a matriz for Triangular, o DETERMINANTE da matriz (igual ao produto dos elementos da sua diagonal principal)

As três primeiras operações deverão ser implementadas através de “sobrecarga” dos respectivos operadores, por exemplo, no caso da 1a opção, a sua programação deverá ser “Resultado = A + B”, onde A e B são as matrizes as serem somadas, selecionadas a partir da lista de matrizes.

Implemente métodos especializados para a Soma Matricial e a Multiplicação por um Escalar quando as matrizes operadas forem ambas do mesmo tipo especializado, por exemplo, se for a soma de duas matrizes Diagonais, a soma deverá apenas somar os elementos das diagonais principais (n operações de soma) e não utilizar um duplo FOR iterando sobre todos os elementos das respectivas matrizes (evitando assim as m x n operações de soma), e o resultado deverá ser do tipo especializado, ou seja, nesse exemplo, uma matriz do tipo Diagonal.

Quanto à manipulação com a Lista de Matrizes, o programa deverá permitir, via menu:
1. Imprimir uma, ou mais, matrizes da lista.
2. Inserir uma nova matriz lida do teclado ou de um arquivo que contenha somente uma matriz.
3. Inserir uma matriz identidade n x n.
4. Alterar ou remover uma, ou mais matrizes da lista.
5. Apresentar a lista de matrizes com a identificação das matrizes pelo seu TIPO, seu número de linhas e colunas, ou, alternativamente, por um nome dado pelo usuário quando de sua criação.
6. Gravar a lista com um nome diferente (backup).
7. Ler uma outra lista de matrizes, acrescentando à lista existente, ou a substituindo.
8. Zerar a lista de matrizes.

# Resultado a ser Entregue:

O resultado a ser entregue será na forma de:

1. Link para um repositório tipo Git (GitHub) com todos os arquivos do projeto.
2. Um pequeno arquivo de texto, em formato PDF, contendo comentários sobre o desenvolvimento (estruturas de dados utilizadas, divisão de módulos, descrição das rotinas e funções, complexidades de tempo e espaço, problemas e observações encontrados durante o desenvolvimento etc.) e uma conclusão a respeitos dos resultados obtidos. Este arquivo PDF também deverá estar no repositório tipo Git.
3. Se a tarefa for feita em grupo, o texto deverá ser postado, em formato PDF, por apenas um dos componentes do grupo. Os demais postam apenas uma folha de rosto contendo a lista completa dos componentes do grupo (nomes completos e DRE) e o link para o repositório do tipo Git (GitHub). O componente do grupo que não postar a folha de rosto ficará com nota ZERO na tarefa.