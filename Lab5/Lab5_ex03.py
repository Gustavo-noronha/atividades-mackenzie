from triangulo import tipo_triangulo

def test_equilatero():
    assert tipo_triangulo(5, 5, 5) == "Equilátero"

def test_isosceles():
    assert tipo_triangulo(5, 5, 3) == "Isósceles"

def test_escaleno():
    assert tipo_triangulo(3, 4, 5) == "Escaleno"

def test_invalido():
    assert tipo_triangulo(1, 1, 10) == "Invalido"