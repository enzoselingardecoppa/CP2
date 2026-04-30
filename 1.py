Códigoestado = int(input("Digite um número de 1 a 5: "))
PesoT = float(input("Digite o peso em toneladas: "))
CódigoCarga = int(input("Digite um número de 1 a 40: "))
PrecoCarga = 0
Imposto = 0
PesoKG = PesoT * 1000
if 10 <= CódigoCarga <= 20:
   PrecoCarga = PesoKG * 100.00
elif 21 <= CódigoCarga <= 30:
    PrecoCarga = PesoKG * 250.00
elif 31 <= CódigoCarga <= 40:
    PrecoCarga = PesoKG * 340.00
else:
    print("Seu código é invalido")

if Códigoestado == 1:
    Imposto  = 0.35

elif  Códigoestado == 2:
        Imposto = 0.25
elif  Códigoestado == 3:
        Imposto = 0.15
elif  Códigoestado == 4:
        Imposto = 0.05
elif Códigoestado == 5:
        Imposto = 0

valor_imposto = PrecoCarga * Imposto
valor_Total = PrecoCarga + valor_imposto
print(valor_Total)