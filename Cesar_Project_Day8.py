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
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Função principal da cifra
def ceasar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Loop principal do programa
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye 👋")
