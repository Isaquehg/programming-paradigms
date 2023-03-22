# Descrevendo Sintaxe & Semântica
## Terminologia
- Sentenças: conjunto de cadeias de caracteres de um alfabeto.
- Linguagem: conjunto de sentenças. 
- Lexemas: unidades sintáticas de mais baixo nívelde uma linguagem (exemplo: *, soma, início).
- Token:uma categoria de lexemas (exemplo: identificador).

## GLC, BNF & EBNF
Metaliguagem -> Gramática BNF
        
    <LHS> -> <RHS>

    (Simbolo)  (Terminal)   (Não Terminal)
    <digit> -> <integer> or <digit><integer>

### BNF Expressa
- Listas
- Ordem
- Estruturas Aninhadas
- Precedência de Operadores

Obs.: Gramática recursiva gera infinitas possibilidades

## Semântica Estática
Utilizada no momento de compilação
- Gramáticas de Atributos
- Facilita o uso de regras como atribuição de variáveis em comparação com as BNFs
- Implementação
    - Regra sintática (Define a regra geral BNF)
    - Regra semântica (Verifica operações entre tipos)
    - Predicado (verificação de valor esperado e valor recebido)

## Semântica Dinâmica
- Não possui uma gramática universal
- Atualmente possui apenas documentação para preencher a falta
- 3 Abordagens Semânticas
    - Operacional: Demonstra os estados fundamentais de um programa passo-a-passo, explicando variável por variável (descrição baixo nível)
    - Denotacional: Baseia-se em funções recursivas, divididos em objeto-função.
        - Domínio sintático: Entrada (Objeto sintático) passa pela Função Semântica
        - Domínio Semântico: Saída        
                
                Descrição da função para converter String binária em inteiro decimal
                Mbin('0') = 0
                Mbin('1') = 1
                Mbin(<bin_num> '0') = 2 * Mbin(<bin_num>)
                Mbin(<bin_num> '1') = 2 * Mbin(<bin_num>) + 1

    - Axiomática: Método para provar exatidão do código