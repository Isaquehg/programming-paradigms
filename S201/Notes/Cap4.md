# Nome, Vinculações e Escopo
## Programação Imperativa
- Baseiado na arquitetura Von Neumann
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