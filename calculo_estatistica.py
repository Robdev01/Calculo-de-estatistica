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

def calcular_variante(dados):
    media = calcular_media(dados)
    soma_quadrados = sum((x - media) ** 2 for x in dados)
    variancia = soma_quadrados / len(dados)
    return variancia

def calculo_intervalo(dados):
    dados_ordenados = sorted(dados)
    primeiro = (dados_ordenados[0])
    ultimo = (dados_ordenados[-1])

    intervalo = ultimo-primeiro
    return intervalo

def minimo_maximo(dados):
    dados_ordenados = sorted(dados)
    minimo = (dados_ordenados[0])
    maximo = (dados_ordenados[-1])
    return minimo, maximo

def valor_em_ordem(dados):
    dados_ordenados = sorted(dados)
    return dados_ordenados

# Obtendo os dados do usuário
dados = obter_dados_do_user()


# Exibindo os resultados
print("Os números informados são", dados)
print("Dados informado em ordem decrecente", valor_em_ordem(dados))
print("Média:", calcular_media(dados))
print("Mediana:", calcular_mediana(dados))
print("Moda:", calcular_moda(dados))
print("Desvio Padrão:", calcular_desvio_padrao(dados))
print("Variante", calcular_variante(dados))
print("Intervalo", calculo_intervalo(dados))
print("Valor minimo e maximo", minimo_maximo(dados))
