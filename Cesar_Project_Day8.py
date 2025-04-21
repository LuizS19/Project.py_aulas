# Logo do programa
logo = '''
   _____                           _____  _       _               
  / ____|                         / ____|| |     (_)              
 | |      ___   __ _  ___  ___  | |     | |__    _   ___   _ __  
 | |     / _ \ / _` |/ __|/ _ \ | |     | '_ \  | | / _ \ | '_ \ 
 | |____|  __/| (_| |\__ \  __/ | |____ | | | | | || (_) || | | |
  \_____|\___| \__,_||___/\___|  \_____||_| |_| |_| \___/ |_| |_|
'''
print(logo)

# Alfabeto usado na cifra
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Função principal da cifra de César
def cifra_cesar(texto_original, deslocamento, direcao):
    texto_resultado = ""
    for letra in texto_original:
        if letra not in alfabeto:
            texto_resultado += letra
        else:
            if direcao == "decodificar":
                deslocamento *= -1
            posicao_alterada = alfabeto.index(letra) + deslocamento
            posicao_alterada %= len(alfabeto)
            texto_resultado += alfabeto[posicao_alterada]
    print(f"Resultado {direcao}do: {texto_resultado}")

# Loop principal do programa
continuar = True
while continuar:
    direcao = input("Digite 'codificar' para criptografar, ou 'decodificar' para descriptografar: ").lower()
    texto = input("Digite sua mensagem: ").lower()
    deslocamento = int(input("Digite o número do deslocamento: "))

    cifra_cesar(texto_original=texto, deslocamento=deslocamento, direcao=direcao)

    reiniciar = input("Deseja tentar novamente? Digite 'sim' para continuar ou 'nao' para sair: ").lower()
    if reiniciar == "nao":
        continuar = False
        print("Até logo 👋")
