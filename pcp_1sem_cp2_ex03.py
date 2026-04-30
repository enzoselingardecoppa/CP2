# --- Lógica de Seleção de Notas ---

def encontrar_menor_checkpoint(n1, n2, n3):
    """Identifica manualmente a menor nota entre os três checkpoints."""
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3

# --- Cálculos de Média ---

def calcular_media_semestre(cp1, cp2, cp3, sp1, sp2, gs):
    """Calcula a média sem peso e a média com peso 40%."""
    # Desconsidera a menor nota dos checkpoints
    menor = encontrar_menor_checkpoint(cp1, cp2, cp3)
    soma_maiores_cp = (cp1 + cp2 + cp3) - menor
    
    # Fórmula (Média CP e SP tem peso 40%, GS tem peso 60%)
    # (Soma dos 2 CPs + 2 SPs) / 4 * 0.4 + GS * 0.6
    media_total = ((soma_maiores_cp + sp1 + sp2) / 4) * 0.4 + (gs * 0.6)
    
    # Média com peso do 1º semestre (40%)
    media_peso = media_total * 0.4
    
    return media_total, media_peso

# --- Interface e Execução ---

def executar_sistema_notas():
    # Coleta de dados
    cp1 = float(input("Nota do Checkpoint 1: "))
    cp2 = float(input("Nota do Checkpoint 2: "))
    cp3 = float(input("Nota do Checkpoint 3: "))
    sp1 = float(input("Nota da Sprint 1: "))
    sp2 = float(input("Nota da Sprint 2: "))
    gs  = float(input("Nota da Global Solution: "))

    # Processamento
    media_semestre, media_com_peso = calcular_media_semestre(cp1, cp2, cp3, sp1, sp2, gs)

    # Exibição formatada com 1 casa decimal
    print(f"\nMédia do semestre (sem peso): {round(media_semestre, 1):.1f}")
    print(f"Média do semestre com peso (40%): {round(media_com_peso, 1):.1f}")

executar_sistema_notas()