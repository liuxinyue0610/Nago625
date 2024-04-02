import re

def shift(text, shift_amount):
    shifted_alphabet = ''.join([chr((ord(char) - 65 + shift_amount) % 26 + 65) if char.isalpha() else char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
    mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', shifted_alphabet)
    return text.translate(mapping)

def encrypt(text, shift_amount):
    text = re.sub(r'[^a-zA-Z]', '', text.upper())
    encrypted_text = ''
    for i in range(0, len(text), 5):
        chunk = text[i:i+5]
        encrypted_chunk = shift(chunk, shift_amount)
        encrypted_text += encrypted_chunk + ' '
    return encrypted_text.strip()

def decrypt(text, shift_amount):
    return encrypt(text, -shift_amount)

def main():
    file_path = input("请输入文件路径：")
    shift_amount = int(input("请输入移位量："))
    
    with open(file_path, 'r') as file:
        plaintext = file.read()
    
    ciphertext = encrypt(plaintext, shift_amount)
    print("密文：", ciphertext)
    
    decrypted_text = decrypt(ciphertext, shift_amount)
    print("解密的文本：", decrypted_text)

if __name__ == "__main__":
    main()
