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
### Gramáticas de Atributos
Facilita o uso de regras como atribuição de variáveis em comparação com as BNFs
- Regra sintática (Define a regra geral BNF)
- Regra semântica (Verifica operações entre tipos)
- Predicado (verificação de valor esperado e valor recebido)


## Semântica Dinâmica