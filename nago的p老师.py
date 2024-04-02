def encrypt(text, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            index = (alphabet.index(char.upper()) + shift) % 26
            encrypted_text += alphabet[index]
    return encrypted_text


def decrypt(encrypted_text, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            index = (alphabet.index(char.upper()) - shift) % 26
            decrypted_text += alphabet[index]
    return decrypted_text


def format_text(text):
    text = ''.join(char for char in text if char.isalpha())
    text = text.upper()
    text = ' '.join([text[i:i+5] for i in range(0, len(text), 5)])
    return text


def main():
    input_file = 'input.txt'
    with open(input_file, 'r') as file:
        text = file.read()

    # Remove non-letter characters and format the text
    text = format_text(text)

    # Prompt user for the shift amount
    shift = int(input("Enter the shift amount: "))

    # Encrypt the text
    encrypted_text = encrypt(text, shift)
    print('Encrypted text:', encrypted_text)

    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, shift)
    print('Decrypted text:', decrypted_text)


if __name__ == '__main__':
    main()