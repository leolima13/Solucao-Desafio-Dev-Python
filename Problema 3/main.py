from Texto import Expressao, Texto
import json
import io


def check_expression_index_in_sentence(sentence, expression):
    '''
    Esta função retorna o index da expressão dentro da sentença
    :param sentence: lista de strings da sentença
    :param expression: lista de strings da exmpressao
    :return: inteiro que corresponde ao index da primeira
    string da expressão encontrada na senteça.
        Caso a setença não contenha a expressão inserida, retorna -1
    '''

    index = -1
    for i in range(len(sentence)):
        if sentence[i:i + len(expression)] == expression:
            index = i
    return index


def check_expression_in_sentence(ObjExpressao, ObjTexto):
    '''

    :param ObjExpressao: Objeto Expressão
    :param ObjTexto: Objeto Texto
    :return: lista com listas de dicionários. O dicionário contém a setença do
    texto e a expressão encontrada.
    '''

    text_list = ObjTexto.get_all_texts()
    sentence_list = ObjTexto.get_senteces()
    token_list = ObjTexto.get_tokens()

    sentencas_dict_list = []
    for i in range(len(text_list)):
        text_list[i] = text_list[i].lower()

        result_list = [None for i in range(len(token_list[i]))]
        for j in range(len(token_list)):
            for k in range(len(ObjExpressao.sentence_string_list)):
                if(-1 < check_expression_index_in_sentence(token_list[i][j], ObjExpressao.sentence_string_list[k]) < 3):
                    result_list[j] = ObjExpressao.sentence_list[k]

        sentence_list_result =[]
        for j in range(len(sentence_list[i])):
            dict = {}
            dict['sentença'] = ObjTexto.get_senteces()[i][j]
            dict['expressão'] = result_list[j]
            sentence_list_result.append(dict)

        sentencas_dict_list.append(sentence_list_result)
    return sentencas_dict_list


Texto = Texto('textos.json')
Expressao = Expressao('expressoes.txt')

# Lista com as listas de dicionarios com a sentencae expressao
sentencas_dict_list = check_expression_in_sentence(Expressao, Texto)

# Cria uma nova lista incluindo a informacao de 'id' e 'sentencas' em sentencas_dict_list
final_json_list = []
for j in range(len(sentencas_dict_list)):
    dict_json = {}
    dict_json['id'] = Texto.json_text_data[j]['id']
    dict_json['sentenças'] = sentencas_dict_list[j]
    final_json_list.append(dict_json)

# Saida é escrita no arquivo output.json
with io.open('output.json', 'w', encoding='utf8') as jsonFile:
    json.dump(final_json_list, jsonFile, indent=4, ensure_ascii=False)
    jsonFile.close()
