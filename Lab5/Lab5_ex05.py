from circulo import area_circulo

def test_area_valida():
    assert area_circulo(5) == 78.5

def test_raio_negativo():
    assert area_circulo(-3) == "Invalido"