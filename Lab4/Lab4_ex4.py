def analisar_qualidade_ar (indice):
    if indice<=25:
        return "Boa"
    elif indice<=50:
        return "Moderada"
    elif indice<=75:
        if indice >=80:
            return "Ruim!.Evitar atividades ao ar livre.(Acionando sistema de aspersão de água)"
        else:
            return"Ruim!.Evitar atividades ao ar livre"
    else:
        return "Ruim!.Evitar atividades ao ar livre.(Acionando sistema de aspersão de água)"
def principal():
    Indice=int(input("Insira o indice do qualidade do ar: "))
    print(analisar_qualidade_ar(Indice))
principal()
