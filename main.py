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