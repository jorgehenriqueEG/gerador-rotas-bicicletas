def planejar_rotas(enderecos):
    ordenados = sorted(enderecos, key=lambda x: x[1])
    bateria = 30
    rota = []
    energia_gasta = 0
    for nome, dist in ordenados:
        if energia_gasta + dist > bateria:
            break
        energia_gasta += dist
        rota.append(nome)
    return rota

enderecos = [
    ("Rua das Flores", 15),
    ("Av. Central", 8),
    ("Rua Verde", 25),
    ("Beco do Sol", 5)
]

resultado = planejar_rotas(enderecos)
print(f"Rotas: {resultado}")