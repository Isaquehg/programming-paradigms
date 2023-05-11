# Tipos de Dados
## Tópicos abordados
1. Introdução
2. Tipos de Dados Primitivos
3. Tipos Ordinais Definidos pelo Usuário
4. Matrizes Associativas
5. Registros
6. Uniões
7. Pointers & Refs
8. Verificação de Tipos
9. Tipagem Forte
10. Verificação de Tipos

## Introdução
- Tipos de dados definidos pelo usuário
- Tipos abstratos de dados
    - Interface do tipo, ex.: POO
- Descritores de variável: : Útil para verificação de tipos e alocação/liberação
    - Atributos estáticos (nome, ...)
    - Atributos dinâmicos (endereco, tipo, ...)
- Objeto: Instâncias de abstrações.

## Tipos Dados Primitivos
- Tipos primitivos são, geralmente, mais próximos do hardware
### Float
- Representações são apenas aproximações para valores reais
- Perda de precisão por meio de operações aritméticas
- Valores:
    - Precisão
    - Faixa: Combinação
- Modelo IEEE:
    - 1 bit: sinal
    - 8 bits: Expoente
    - 23 bits: Fração (Mantissa)
### Complexo
- Valores são duplas de floats

### Decimal
- Ponto decimal tem posição fixa
- Maior precisão que float/double e maior gasto de memória

### Boolean
- Computadores não endereçam mais a nível de bit, apenas bytes
- Gastam, portanto, 8 bits
- Verdadeiro é qualquer valor diferente de 0!!!
- Flags passam a ser booleans para facilitar legibilidade

### Char
- ASCII
- ISO 88
- Unicode
    - UTF-8 -> 1 a 6 bytes
    - UTF-16 -> 2 a 4 bytes
    - UTF-32 -> fixado em 4 bytes

### Cadeias de Caracteres
- Tipo primitivo ou especial
    - Tipos primitivos são recomendados, visto sua praticidade
- Tamanho
    - Fixo: Maioria das linguagens (Descritor apenas em tempo de compilação)
    - Dinâmico Limitado: C/C++ (capacity e max_size)
    - Dinâmico Ilimitado: Limitado pela RAM apenas (Difícil implementação devida complexidade do descritor)

## Tipos Ordinais Definidos pelo Usuário (Enum)
### Tipo Ordinal
- É uma classe de constantes enumeradas
- Utilizado para valores como dias, flags, etc
- Já é ordenada naturalmente
- Questões sobre verificações de tipos
    - Mesma constante em mais de um enum (Java sim, C não)
    - Valores de enumeração convertidos p inteiro (Java não, C sim)
    - Há outros tipos que podem ser convertidos para enum? (C apenas inteiros, como char)
- Controle sobre a faixa de valores
- Vantagem de melhora de Legibilidade e Confiabilidade(em Java)

## Matrizes Associativas (Dict, HasMap)
### Estrutura e Operações
- Casos
    1. Perl
        - % Cria a disperção
        - $ Escalar
        - @ Referência
        - Estrutura Dinâmica
        - Chaves como string
    2. Python
        - Chaves como objetos
        - Métodos nativos mais seguros
    3. Ruby
        - Qualquer tipo de chave
    4. Lua
        - Tabelas que funcionam como matriz, matriz associativa e struct
- Eficiência de acesso entre O(1) a O(n), enquanto listas ficam em O(n), pois precisa percorrer todos elementos, já dicionário pode ser acessado diretamente com o valor da chave

## Registros (Structs)
### Estruturas
- Armazenamento de structs são em locais diferentes de classes
- Structs em linguagens OOP são classes sem métodos, apenas atributos
- Formas de referenciar
    1. Full Qualified Name
    2. Referências Elípticas (COBOL) -> Mais gasto de processamento e podem ocorrer ambiguidades
- Operações
    - Atribuição
    - Comparação entre campos (COBOL) -> Move corresponding
    - 