import io
import json
import nltk


class Texto:
    '''
    A classe Texto retorna paramêtros do arquivo textos.json
    '''

    def __init__(self, input_json):
        self.input_json = input_json
        with io.open(self.input_json, 'r', encoding='utf8') as json_file:
            self.json_text_data = json.load(json_file)

    def get_all_texts(self):
        '''
        :return: lista com todos os textos do arquivo json
        '''

        self.all_texts_list = []
        for n in range(len(self.json_text_data)):
            self.all_texts_list.append(self.json_text_data[n]['texto'])

        return self.all_texts_list

    def get_all_ids(self):
        '''
        :return: ista com todos os ids do arquivo json
        '''

        self.all_ids_list = []
        for n in range(len(self.json_text_data)):
            self.all_ids_list.append(self.json_text_data[n]['id'])

        return self.all_ids_list

    def get_senteces(self):
        '''
        :return: lista com todas as sentenças do arquivo json
        '''

        self.all_sentences = []
        for n in range(len(self.get_all_texts())):
            self.all_sentences.append(nltk.tokenize.sent_tokenize(self.get_all_texts()[n]))

        return self.all_sentences


    def get_tokens(self):
        '''
        definição de token: uma string de caracteres contíguos, delimitada por espaços em branco e/ou pontuação;
        :return: lista com todas os tokens em minúsculo do arquivo json
        '''

        senteces = self.get_senteces()
        self.all_tokens = []
        for i in range(len(senteces)):
            self.token_list = []
            for j in range(len(senteces[i])):
                self.tokenize_senteces = (map(lambda x: x.lower(), nltk.word_tokenize(senteces[i][j])))
                self.token_list.append(list(self.tokenize_senteces))
                #elf.token_list.append(nltk.word_tokenize(senteces[i][j]))
            self.all_tokens.append(self.token_list)

        return self.all_tokens


class Expressao:
    '''
    A classe expressão retorna parêmtros do arquivo expressoes.txt
    '''

    def __init__(self, text_path):
        self.text_path = text_path
        self.sentence_list = self.make_list_line_from_txt(self.text_path)
        self.sentence_string_list = self.make_list_string_from_txt(self.text_path)

    def make_list_string_from_txt(self, txt_path):
        '''
        :param txt_path: diretório do arquivo expressoes.txt
        :return: lista com as strings de cada linha do arquivo .txt
        '''

        txt_file = io.open(txt_path, "r", encoding='utf8')
        string_list = []
        for line in txt_file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            string_list.append(line_list)
        txt_file.close()

        return string_list

    def make_list_line_from_txt(self, txt_path):
        '''
        :param txt_path: diretório do arquivo expressoes.txt
        :return: lista com uma string para cada linha do arquivo .txt
        '''

        txt_file = io.open(txt_path, "r", encoding='utf8')
        line_list = []
        for line in txt_file:
            stripped_line = line.strip()
            line_list.append(stripped_line)
        txt_file.close()

        return line_list
