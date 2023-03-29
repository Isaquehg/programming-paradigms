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