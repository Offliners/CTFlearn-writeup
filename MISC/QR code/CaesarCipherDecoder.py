def decrypt(key, message):
    message = message.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in message:
        if letter in alpha: 
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

text = input('Encrypt text : ')
for shift in range(0,26):
    output = decrypt(shift,text)
    print(f'#{shift} : ',output)
