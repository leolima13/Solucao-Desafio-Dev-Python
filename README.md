# Desafio Dev Python Jr/Pl - 2022

Solução do desafio Dev Python 2022

Orientações gerais:

* Todos os problemas **devem** ser implementados em Python;
* Cada problema **deve** ser implementado em um arquivo separado;
* As implementações podem incluir casos de teste, utilizar POO, frameworks ou conter outros detalhes que você julgar necessários;
* Lembre-se de incluir instruções para instalação de dependências e execução das soluções.


Link do desafio: https://gitlab.com/priscilla.lopes/desafio-dev-python-2022

------------------------------------------------

## Problema 1 - Identificação de substrings

A solução está localizado no diretório Problema 1.

Em **identificacaodesubstrings.py** foi criada a classe **IdentificacaoDeSubstrings** com o método **contar_substring** que recebe duas strings como entrada, `s1` e `s2`, e retorna quantas vezes `s2`ocorre em `s1`.

Execute **test_identificacaodesubstrings** no pytest, para verificar o exemplo apresentado. 

Exemplo:

| `s1`         | `s2`    | Retorno |
|--------------|---------|---------|
| `'ABCDCDC'`  | `'CDC'` | 2       |


------------------------------------------------
## Problema 2 - Validação de sequência de caracteres

A solução está localizado no diretório Problema 2.

Em **validacaodesequenciadecaracteres** foi criada a classe **ValidacaoDeSequenciaDeCaracteres** com o método **check_brackets** que recebe uma string composta pelos caracteres `(`, `)`, `{`, `}`, `[` ou `]` e retorna `True` quando a string é válida e, caso contrário, retorna `False`. Obs: Uma sequência vazia também é considerada válida.

Execute **test_validacaodesequenciadecaracteres** no pytest, para verificar o exemplo apresentado. 


| Sequência      | Válida? | Obs.                                                    |
|----------------|---------|---------------------------------------------------------|
| `{[()]}`       | Sim     |                                                         |
| `()[]{}`       | Sim     | A concatenação de subsequências válidas também é válida |
| `([])`         | Sim     |                                                         |
| `{{[[(())]]}}` | Sim     |                                                         |
| `{[()([])]}`   | Sim     |                                                         |
| `([]`          | Não     | Não ocorre o fechamento de par com `(`                  |
| `[({)}]`       | Não     | A substring entre `[` e `]` não é válida                |
| `)(`           | Não     | Não é um par válido                                     |
| `(([{()}])))`  | Não     | Não existe um `(` para parear com o último caracter `)` |
| ` `            | Sim     | Sequência vazia é true                                  |


------------------------------------------------

## Problema 3 - Verificação de expressões em sentenças

A solução está localizado no diretório Problema 3.

Execute o programa **main.py** para que o arquivo `output.json` seja gerado no mesmo diretório. 


A saída para a solução inclui:
* O identificador do texto;
* Uma lista com cada sentença e a expressão cuja presença foi verificada (`null` se nenhuma das expressões está presente na sentença);
* `output.json` é o arquivo de saída.

Bibliotecas usadas:
* json;
* io;
* nltk;

**TO DO list**:
* Criar testes unitários;
* Simplificar o código, criando mais funções e elimnando os for loop;



