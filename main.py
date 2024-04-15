import argparse

def remove_non_letters(text):
    letters_only = [char for char in text if char.isalpha()]
    return ''.join(letters_only)

def shift_cipher(text, shift_amount):
    cipher_text = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            cipher_text += shifted_char
    return cipher_text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shift', type=int, help='Shift amount for the cipher')
    args = parser.parse_args()

    if args.shift is None:
        print("Please provide a shift value using --shift")
        return

    try:
        with open('original.txt', 'r') as file:
            original_text = file.read().strip()  
    except FileNotFoundError:
        print("Error: original.txt file not found")
        return

    original_text = original_text

    cipher_text = shift_cipher(original_text, args.shift)

    decipher_text = shift_cipher(cipher_text, 26 - args.shift)

    print("Original text:", original_text)
    print("Cipher text:", cipher_text)
    print("Deciphered text:", decipher_text)

if __name__ == '__main__':
    main()