from desconto import desconto

def test_sem_desconto():
    assert desconto(99.99) == 99.99

def test_limite_exato():
    assert desconto(100.00) == 90.0

def test_acima_do_limite():
    assert desconto(101.00) == 90.9