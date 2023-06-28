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
10. Equivalência de Tipos

## 1. Introdução
- Tipos de dados definidos pelo usuário
- Tipos abstratos de dados
    - Interface do tipo, ex.: POO
- Descritores de variável: : Útil para verificação de tipos e alocação/liberação
    - Atributos estáticos (nome, ...)
    - Atributos dinâmicos (endereco, tipo, ...)
- Objeto: Instâncias de abstrações.

## 2. Tipos Dados Primitivos
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

## 3. Tipos Ordinais Definidos pelo Usuário (Enum)
### Tipo Ordinal
- É uma classe de constantes enumeradas
- Utilizado para valores como dias, flags, etc
- Já é ordenada naturalmente
- Questões sobre verificações de tipos
    - Mesma constante em mais de um enum (Java sim, C não)
    - Valores de enumeração convertidos p inteiro (Java não, C sim)
    - Há outros tipos que podem ser convertidos para enum? (C apenas inteiros, como char)
- Controle sobre a faixa de valores
- Vantagem de melhorar Legibilidade e Confiabilidade(em Java)

## 4. Matrizes Associativas (Dict, HasMap)
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

## 5. Registros (Structs)
### Estruturas
- Armazenamento de structs são em locais diferentes de classes
- Structs em linguagens OOP são classes sem métodos, apenas atributos
- Formas de referenciar
    1. Full Qualified Name
    2. Referências Elípticas (COBOL) -> Mais gasto de processamento e podem ocorrer ambiguidades
- Operações
    - Atribuição
    - Comparação entre campos (COBOL) -> Move corresponding

## 6. Uniões - Variáveis com mais de um tipo, dependendo do momento da execução, unindo-os
### Questões
- A verificação de tipos deve ser obrigatória?
- As uniões devem ser structs?
- Tendência de sumirem, pois são perigosas quando sem discriminante
### Aplicação
- Fortran

        equivalence (a, b) -> são a mesma variável, com nomes diferentes

- C/C++

        union -> funcionam como structs, com "campos" sendo a mesma variável
- ADA

        Figure_1: Figure;
        Figure_2: FIgure(Form => Triangle)
        Deve prover todos campos, incluindo o discriminante, caso não teve seu discriminante declarado, como em Figure_1. 
### Famílias
- Discriminadas -> possui tag indicando qual o tipo da variável em dado momento (Algol 68 e ADA)
    - Quando seu discriminante não é declarado anteriormente, seus campos devem ser verificados dinamicamente.
    - Aloca-se memória para o maior variante quando não é fornecido discriminante
- Livres

## 7. Pointers
### Usos
1. Endereçamento indireto para linguagens de montagem (Assembly)
2. Gerenciar armazenamento dinâmico (heap/monte) -> aloc, maloc

### Definição
    - Não são dados estruturados, como matrizes e registros

### Questões
- Qual o escopo e tempo de vida de um ponteiro
- Qual o tempo de vida de uma var. dinâmica de monte? (Garbage collector ou usar uma função delete)
- Devem ter restrições sobre quais tipos os ponteiros podem apontar
- São utilizados para gerenciamento de armazenamento dinâmico, endereçamento indireto ou ambos? ()
- A linguagem deve suportar tipos ponteiro (*), tipos referência ou ambos? (Mais alto nível ou ambos ou só baixo nível)

### Operações
- Atribuição -> Atribui um valor útil ao ponteiro
- Desreferenciamento -> Obtêm o endereço do ponteiro

### Problemas
- Ponteiros soltos

        int * arrayPtr1;
        int * arrayPtr2 = new int[100];
        arrayPtr1 = arrayPtr2;
        delete [] arrayPtr2;
        // Agora, arrayPtrl é solto, porque o armazenamento no monte
        // para o qual ele estava apontando foi liberado.

- Variáveis dinâmicas de monte perdidas (Lixo e vazamento de memória) -> quando o ponteiro que continha o endereço passa a apontar para outro endereço e não desloca a antiga variável (memory leackage)

### Aplicação
- C/C++: 
    - Ponteiros void não correm problema de verificação de tipos, pois deve ocorrer um casting antes do desreferenciamento
    - Tipos de referência: 
        - Por valor/ponteiro: Passa uma cópia da variável, como é feito normalmente
        - Por referência/ponteiro: em C++ consegue-se passar tanto ponteiro quanto por referência. Em C podia apenas modificar por referência com & na chamada da função e * nos parâmetros. Em C++ pode-se usar & no parâmetro da função e depois fazer operações sem necessitar de utilizar *. Ex.: 
        
                func(int& a, int& b)

## 8. Verificação de Tipos
### Definição
Garantir que os operandos de um operador são tipos compatíveis
### Conversões
- Coerção: Conversão automática -> **Na coerção, sempre a conversão é feita para um tipo superior (maior, tipo de int para float ou float para double) na decisão dos tipos de dados que serão convertidos na operação!**

        float x = 1 + 5.0f

- Casting

        float x = (float)1 + 5.0f

### Momento de verificação
- Quando a verificação de tipos é feita em tempo de compilação, ocorre menos gasto computacional e ocorrem menos erros
- A vantagem de verificar em execução é poder executar sem grande tempo de planejamento
**Nem todos erros de tipo podem ser detectados em momento de compilação**

### Abordagens que podem resultar em complicações ao verificar tipos
Unions em C++, Equivalence em Fortran e registros variantes em Ada podem ocasionar problemas, pois uma mesma célula pode assumir mais de um tipo durante execução

## 9. Tipagem Forte
### Definição
A facilidade ou não da linguagem converter um tipo automaticamente

### Nonconverting cast (bypass de verificação de tipos)
Conversões que o desenvolvedor não deseja que sejam verificados explicitamente. O cast ocorre em nível binário

### Exemplos
- Fortemente tipadas: Java, C#, ML e Ada
- Fracamente tiapda: C/C++ (por conta das Unions), Javascript e PHP

### Regras de Coerção
- Podem ocorrer problemas de precisão
- A detecção de erros torna-se mais difícil

## 10. Equivalencia de Tipos
### Questões
- Definir regras de conversão para tipos escalares é casual
- Para tipos definidos pelo usuário, deve ser utilizado o termo **equivalente**, pois não haverá nenhum tipo de conversão

### Tipos de Equivalência
- Por nome -> A verificação é mais simples, porém mais restritivo
- por estrutura -> Vai verificar campo por campo e associá-los

### Por nome
- Todos os tipos devem possuir nome

### Por estrutura
- Equivalência por estrutura pode não ser suficiente. Caso das structs terem campos com mesmo tipo de dados mas com nomes diferentes, ex.: em duas structs pessoa. Uma com campo "peso" e outra "massa", ambos float
- Linguagens mais rigorosas utilizam equivalência por nome dentro da equivalência por estrutura
- Diferenciação
    1. Subtipo -> Uma versão igual ou reduzida ao tipo original. São equivalentes e não herdam as propriedades do tipo original.

            subtype Small_type is Integer range 0..99;

    2. Derivado -> Utilizam **new**. Não são equivalentes e herdam as propriedades do tipo original.
        > Exceção aos literais