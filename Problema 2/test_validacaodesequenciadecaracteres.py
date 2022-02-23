from validacaodesequenciadecaracteres import ValidacaoDeSequenciaDeCaracteres
import pytest

Obj = ValidacaoDeSequenciaDeCaracteres()


@pytest.mark.parametrize(
    'input_string_valida',
    ['{[()]}', '{[()]}', '([])', '{{[[(())]]}}', '{[()([])]}', '{{[[(())]]}}', '']
)
def test_check_brackets_valido(input_string_valida):
    # Testa os casos onde todos os pares de caractres são válidos
    assert True == Obj.check_brackets(input_string_valida)


@pytest.mark.parametrize(
    'input_string_invalida',
    ['([]', '[({)}]', ')(', '(([{()}])))']
)
def test_check_brackets_invalido(input_string_invalida):
    # Testa os casos onde todos os pares de caractres são inválidos
    assert False == Obj.check_brackets(input_string_invalida)


