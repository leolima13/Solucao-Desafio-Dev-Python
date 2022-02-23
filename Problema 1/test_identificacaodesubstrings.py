from identificacaodesubstrings import IdentificacaoDeSubstrings

Obj = IdentificacaoDeSubstrings()


def test_contar_substring():
    # Testa um caso de sucesso, onde há duas ocorrências de substring na string
    assert 2 == Obj.contar_substring('ABCDCDC', 'CDC')




