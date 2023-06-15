# Os 4 Principais Paradigmas
## Introdução
- Diferentes paradigma surgem com diferentes tipos de problema
- Sabendo fundamentos da Ciência da Computação possibilita a aprendizagem de qualquer paradigma

## Paradigma Imperativo (Procedural)
- Provêm da arquitetura de Von Neumann
- Estrutura
    1. Comandos explícitos e chamadas de procedimentos passo-a-passo
    2. Realizam operações de dados
    3. Modificam os valores das variáveis
    > Variáveis são consideradas containers nas células da memória do PC
- Resultado é o estado final da memória

## Paradigma Funcional
- O resultado de uma função depende da função interna
- Mais próximo da Matemática
- A execução é simplesmente a aplicação de todas as funções aos seus argumentos e cálculo de valores
- A execução é a evaluation de funções

## Paradigma Lógico
- Conjunto de fórmulas lógicas: Axiomas (fatos & regras / Predicados) que descrevem propriedades de objetos e um teorema a ser provado
- A execução é um processo de inferências (provas lógicas / regras) do teorema
- **Não há atribuição de variáveis**. São valores reais ou objetos obtidos na inferência
- Resulta em **falha** ou **sucesso** de prover a pesquisa

## Paradigma Orientado à Objetos
- Descreve estrutura e comportamento de classes e objetos
- Atributos e Métodos
- Relação entre classes com **hierarquias** customizadas
- A execução é uma troca de mensagens entre objetos

## Lingaugens e Técnicas de Programação
- Primeira linguagem que estruturou a ideia de POO: SmallTalk
    - OO + Imperativo: Java e C++
    - OO + Funcional: CLOS
    - OO + Lógico: Object Prolog e Logtalk

- Padrões e Característica do Paradigma Funcional e Lógico
    1. Recursão e Interpretação
    2. Estruturas de dado sflexíveis para representar dados complexos, como lista (Lisp) ou termo (Prolog)
    3. Recurso de correspondência de padrões (Refal, Prolog) e backtracking automático (Planner, Prolog)
    4. Funções de ordem superior (Lisp, Scheme)
    5. Mecanismo de avaliações parciais/Lazy Loading (Refal)
    Obs.:
        - Programação funcional é preferível para processamento simbólico, já lógico é melhor para dancos de dados dedutivos e sistemas especialistas. Ambos não são adequados para interação com usuário ou app de direcionamento de eventos
        - Linguagens Imperativas são mais convenientes para cálculos numéricos e simbólicos
        - OO é melhor para grandes aplicações

## Integração de Técnicas de Programação
- Marshalling
- Interoperabilidade

## Conclusão
### Os projetos de programação atuais dependem do uso de múltiplas linguagens de programação