# Entrada de dados
def obter_dados_do_user():
    dados = []
    while True:
        entrada = input("Digite um número (ou 's' para sair):")
        if entrada.lower() == 's':
            break
        try:
            numero = float(entrada)
            dados.append(numero)
        except ValueError:
            print("Por favor, digite apenas números.")
    return dados
def calcular_media(dados):
    return sum(dados) / len(dados)

def calcular_mediana(dados):
    dados_ordenados = sorted(dados)
    tamanho = len(dados_ordenados)
    if tamanho % 2 == 0:
        return (dados_ordenados[tamanho//2 - 1] + dados_ordenados[tamanho//2]) / 2
    else:
        return dados_ordenados[tamanho//2]

def calcular_moda(dados):
    frequencias = {}
    for valor in dados:
        frequencias[valor] = frequencias.get(valor, 0) + 1
    moda = max(frequencias, key=frequencias.get)
    return moda

def calcular_desvio_padrao(dados):
    media = calcular_media(dados)
    soma_quadrados = sum((x - media) ** 2 for x in dados)
    variancia = soma_quadrados / len(dados)
    return variancia ** 0.5



# Obtendo os dados do usuário
dados = obter_dados_do_user()



# Exibindo os resultados
print("Os números informados são", dados)
print("Média:", calcular_media(dados))
print("Mediana:", calcular_mediana(dados))
print("Moda:", calcular_moda(dados))
print("Desvio Padrão:", calcular_desvio_padrao(dados))

