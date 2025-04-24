import os

logo = r"""
  _____________________________
 |                             |
 |       CASA DE LEILÕES       |
 |_____________________________|

           _______
          |       |
          |       |
          |_______|
             ||   
             ||   
             ||   
             ||   
          ___||___
         |_______|
         |_______|
        /         \
       |___________|
        \_________/

"""

print(logo)
print("🔨 Bem-vindo ao Leilão! Que comecem os lances! 🔨\n")

# Dicionário para armazenar os lances
lances = {}

# Função para encontrar o maior lance e o vencedor
def encontrar_maior_lance(registro_de_lances):
    maior_lance = 0
    vencedor = ""
    for participante in registro_de_lances:
        valor_lance = registro_de_lances[participante]
        if valor_lance > maior_lance:
            maior_lance = valor_lance
            vencedor = participante
    print("\n🏆 Resultado Final 🏆")
    print(f"O vencedor é {vencedor} com um lance de R${maior_lance:.2f}")

# Controle do loop principal
leilao_finalizado = False

while not leilao_finalizado:
    nome = input("Qual é o seu nome?: ")
    try:
        valor = float(input("Qual é o valor do seu lance? R$"))
        lances[nome] = valor
    except ValueError:
        print("⚠️  Por favor, insira um valor numérico válido para o lance.")
        continue

    continuar = input("Há mais alguém que quer dar um lance? Digite 'sim' ou 'não': ").lower()
    if continuar == "não":
        leilao_finalizado = True
        encontrar_maior_lance(lances)
    else:
        os.system("cls" if os.name == "nt" else "clear")  # Compatível com Windows/Linux/Mac
