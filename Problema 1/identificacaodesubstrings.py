class IdentificacaoDeSubstrings:


    def contar_substring(self, s1, s2):
        '''
        Esta função recebe dois parametros strings
        para calcular quantas vezes uma string ocorre na outra
        :param s1: recebe uma string
        :param s2: recebe uma string
        :return: retorna quantas vezes s2 ocorre em s1
        '''

        countador_de_substring = 0
        for i in range(0, len(s1) - len(s2) + 1):
            if s1[i: i + len(s2)] == s2:
                countador_de_substring += 1
        return countador_de_substring


