class ValidacaoDeSequenciaDeCaracteres:

    def check_brackets(self, string_to_check):
        '''
        Esta função confere se uma string é válida, ou seja, se todos
        os pares de caracters são válidos. Um par de caracteres é válido se
        os caracteres que este cerca também forem pares.
        :param string_to_check: string composta pelos caracteres (, ), {, }, [ ou ]
        :return: True quando a string é válida e, caso contrário, retorna False
        '''
        brackets = ['()', '{}', '[]']
        while any(x in string_to_check for x in brackets):
            for bracket in brackets:
                string_to_check = string_to_check.replace(bracket, '')

        return not string_to_check

