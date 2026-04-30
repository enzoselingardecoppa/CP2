# --- Ordenando ---

def ordenar_lados(a, b, c):
    """Garante que A seja o maior valor e C o menor."""
    lados = [a, b, c]
    lados.sort(reverse=True)
    return lados[0], lados[1], lados[2]

# --- Verificação de Tipos ---

def verificar_existencia(a, b, c):
    """Aplica a regra de desigualdade triangular (A >= B + C)."""
    if a >= (b + c):
        return False
    return True

def classificar_por_angulos(a, b, c):
    """Verifica se o triângulo é Retângulo, Obtusângulo ou Acutângulo."""
    quadrado_a = a**2
    soma_quadrados_bc = b**2 + c**2
    
    if quadrado_a == soma_quadrados_bc:
        print("TRIANGULO RETANGULO")
    elif quadrado_a > soma_quadrados_bc:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

def classificar_por_lados(a, b, c):
    """Verifica se o triângulo é Equilátero ou Isósceles."""
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")

# --- Execução Principal ---

def executar():
    lado1 = float(input("Digite o valor A: "))
    lado2 = float(input("Digite o valor B: "))
    lado3 = float(input("Digite o valor C: "))

    # Ordenação decrescente
    a, b, c = ordenar_lados(lado1, lado2, lado3)

    # Processamento dos resultados
    if not verificar_existencia(a, b, c):
        print("NAO FORMA TRIANGULO")
    else:
        classificar_por_angulos(a, b, c)
        classificar_por_lados(a, b, c)

executar()