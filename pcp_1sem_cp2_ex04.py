# --- Funções de Cálculo ---

def calcular_horas_extras(salario_base, horas):
    """Calcula o valor das horas extras: 1.5% do base por hora."""
    valor_por_hora = salario_base * 0.015
    return valor_por_hora * horas

def calcular_descontos_faltas(salario_base, faltas):
    """Calcula o desconto por faltas: 2% do base por falta."""
    valor_por_falta = salario_base * 0.02
    return valor_por_falta * faltas

def calcular_bonus(cargo, recebeu_bonus):
    """Define o bônus fixo baseado no cargo, se aplicável."""
    if recebeu_bonus.lower() != 's':
        return 0.0
    
    # 1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário
    if cargo == 1:
        return 1000.0
    elif cargo == 2:
        return 500.0
    elif cargo == 3:
        return 300.0
    elif cargo == 4:
        return 100.0
    else:
        return 0.0

# --- Processamento e Exibição ---

def gerar_folha_pagamento():
    # Entrada de dados
    nome = input("Nome do funcionário: ")
    print("Cargos: 1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário")
    cargo = int(input("Escolha o cargo (1-4): "))
    salario_base = float(input("Salário base: R$ "))
    h_extras = float(input("Total de horas extras: "))
    faltas = int(input("Total de faltas no mês: "))
    tem_bonus = input("Recebeu bônus por desempenho? (s/n): ")

    # Chamada das funções
    valor_extras = calcular_horas_extras(salario_base, h_extras)
    valor_bonus = calcular_bonus(cargo, tem_bonus)
    valor_faltas = calcular_descontos_faltas(salario_base, faltas)

    # Cálculos finais
    acrescimos = valor_extras + valor_bonus
    salario_bruto = salario_base + acrescimos
    salario_final = salario_bruto - valor_faltas

    # Saída
    print(f"\n--- Folha de Pagamento: {nome} ---")
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Total de Acréscimos (Extras + Bônus): R$ {acrescimos:.2f}")
    print(f"Total de Descontos (Faltas): R$ {valor_faltas:.2f}")
    print(f"Salário Final: R$ {salario_final:.2f}")

# Execução
gerar_folha_pagamento()