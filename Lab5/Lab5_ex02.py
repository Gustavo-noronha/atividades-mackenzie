from media_vef import verificar_situacao

def test_aprovado():
    assert verificar_situacao(8) == "Aprovado"

def test_exame():
    assert verificar_situacao(5) == "Exame"

def test_reprovado():
    assert verificar_situacao(2) == "Reprovado"