def pode_aprovar(idade, renda, valor_empre):
    if idade >= 18 and valor_empre <= renda * 20:
        return True
    else:   
        return False    


def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10


def calcular_parcela(valor_empre, taxa, parcelas):
    i = taxa
    n = parcelas
    pmt = valor_empre * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    return pmt


def calcular_total(parcela, parcelas):
    return parcela * parcelas


def calcular_juros(total, valor):
    return total - valor


nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))
valor_empre = float(input("Digite o valor do empréstimo desejado (max: 20 vezes a sua renda mensal): "))
parcelas = int(input("Digite o número de parcelas (min:3 max:24): "))

if parcelas < 3 or parcelas > 24:
    print("Número de parcelas inválido!")
else:
    if pode_aprovar(idade, renda, valor_empre):
        taxa = definir_taxa(parcelas)
        parcela = calcular_parcela(valor_empre, taxa, parcelas)
        total = calcular_total(parcela, parcelas)
        juros = calcular_juros(total, valor_empre)

        print("Seu empréstimo foi APROVADO")
        print(f"Cliente: {nome}")
        print(f"Valor financiado: R$ {valor_empre:.2f}")
        print(f"Taxa de juros: {taxa*100:.0f}% ao mês")
        print(f"Valor da parcela: R$ {parcela:.2f}")
        print(f"Total pago: R$ {total:.2f}")
        print(f"Total de juros: R$ {juros:.2f}")
    else:
        print("Seu empréstimo foi NEGADO")
        if idade < 18: 
            print("Você não possui idade para fazer um financiamento")
        else:
            print("O valor do financiamento ultrapassou o limite permitido de 20 vezes a sua renda mensal")


    
       
   


            
