# Nome, Vinculações e Escopo
## Programação Imperativa
- Baseado na arquitetura Von Neumann
- Paradigma mais antigo e popular
- Elementos base
    - Execução passo a passo
    - Controle de Fluxo
    - Variáveis
    - Intrução de atribuição
    
## Variáveis
- Abstração de células de memória
- Aspectos
    1. Nome/identificador
    2. Endereço
    3. Tipo
    4. Valor
    5. Tempo de Vida
    6. Escopo
### Questões - Nome
1. Comprimento máximo de variáveis
    - cammelCase
    - kebab-case
    - snake_case
2. Sensíveis à capitalização
    - Podem facilitar oudificultar a leitura: Contador, contador, CONTADOR
3. Palavras da LP são Palavras Reservadas ou Palavras-Chave
    - Palavras Reservadas: Significam a mesma coisa independente de onde estiverem no código (int, if, long, for, throw, etc..)
    - Palavras-Chave: São palavras reservadas dependendo do contexto
    Exemplo Fortran
            
            Integer Apple  //Criando variável Apple do tipo Integer
            Integer = 4    //atribuindo 4 à variável Integer

### Questões Endereço
1. Diferentes endereços durante execução
2. Diferentes endereços em diferentes locais do código (var. globais)
3. Pode haver dois nomes p mesmo endereço (ponteiros)

### Questões Tipo
1. Numeros
2. Números de precisão (float, double)
3. Strings
4. Booleans

### Questões Valor
- Conteúdos associados à célula de memória (lado direito)
- ID - OPERADOR - VALOR

### Questões Tempo de Vida & Escopo
- Intervalo entre criação e destruição
- Varia entre global e local
- static em C é uma variável local com tempo de vida global

## Manipulações de Memória
- Alocação
- Desalocação/liberação
- Realocação

## Tipos de Tempo de Vida (tempo alocação x tempo liberação)
- Estática
    - Vinculação de armazenamento ANTES da execução
    - Vantagens:
        - Suporte a subprogramas sensíveis a Historico (impede recursividade).
        - Eficiência (endereçamento aberto, acesso rápido)
    - Desvantagens:
    - Alocada no BSS Segment ou Data Segment
    - Exemplo: static int x;

- Dinâmica da Pilha (Stack dynamic)
    - Exemplo: Alocada quando o trecho é realmente chamado (dinâmico), mas o tipo já é vinculado antes da execução (estático) -> (híbrido)
    - Vantagens:
        - Permite compartilhamento de memória
        - Permite recursão
    - Desvantagens:
        - Sobrecarga de tempo de execução
        - Acessos mais lentos
        - Sem histórico de execução

- Dinâmica do Monte Explícitas (explicit heap dynamic)
    - Exempli: malloc, alloc, new, objetos Java, etc.
    - Exemplo C++

            int *intnode;
            intnode = new int;
            delete intnode;
        
    - Vantagens:
        - Estruturas dinâmicas
    - Desvantages
        - Dificuldade de usar ponteiros
        - Custo de referências
        - Complexidade de implementação do gerenciamento de memória

- Dinâmica do Monte Implícitas (implicit heap dynamic)
    - Só são vinculadas quando algum valor é atribuído à variável
    - Vantagens:
        - Flexibilidade
    - Desvantagens:
        - Ineficiente, pois atributos dependem do momento de execução
        - Perda de detecção de erros (sem type-checking)
    - Exemplos: 

## Escopo
### Tipos
- Visível
- Local: Declarada no bloco
- Não Local: Pode ser uma global utilizada em um bloco (não declarada no próprio bloco)

### Escopo Estático
- Maioria das linguagens
- Escopo definido no próprio código
- Processo de Busca
    - Ocorre de dentro p/ fora: Busca por aquela variável no bloco, depois em escopos maiores e assim por diante (Ancestrais estáticos)
    - Shadowing: Caso tenham duas declarações, uma dentro de outra, a declaração mais exterior nunca será referenciada pelos blocos mais interiores
- ex. C Acessar var global -> ::var (operador de escopo)
- Ordem de Declaração (Peculiaridade C#): Seu escopo é do bloco inteiro, mas a utilização é apenas da linha da declração p/ baixo
- Declaração não aloca memória, apenas na Definição
    - Declaração: extern int i
    - Declaração & Definição: int i
- Vantagens:
    Funciona bem, em geral
- Desvantagens:
    Conforme o programa cresce, torna-se excessivo

### Escopo Dinâmico
- A chamada pode referenciar até mesmo declarações irmãs, não apenas ancestrais; sendo definida pela ordem da função que chamou-a. Caso não a encontre, segue a mesma lógica...
- Ex.: Neste caso, se a ordem de chamada fosse A -> B -> C, a variável X seria 5. Caso fosse B -> A -> C, X resultaria em 20, pois A foi chamada antes de B.

        func A():
            var X = 20;
            func B():
                var x = 5;
            func C():
                print(x);

- Vantagens:
    - 
- Desvantagens:
    - 

## Ambientes de Referenciamento
- É a ideia oposta do Escopo
- Para Escopo Estático: Variáveis declaradas em seu escopo local + todas variáveis de escopos ancestrais
- Ex.: X de Sub3, A e B de Sub1

## Constantes Nomeadas
- Variáveis imutáveis
- Favorecem a legibilidade e confiabilidade(proteger de erros de digitar errado o mesmo número)
- Segurança e parametrização
- Ex.: const(JS, C#), final(C++), readonly(C#), etc.
- Casos Específicos:
    - Em Java, final pode ser utilizado em classes e funções também para prover recursos de bloqueio 
    - C# é possível escolher entre vinculação estática e dinâmica na declaração de constantes
        - const: estática
        - readonly: dinâmica
- Inicialização é alocar memória e salvar um valor nesse espaço, na declaração
