
#刘馨月电脑的p老师
def remove_non_letters(text):
    return ''.join(char for char in text if char.isalpha())

def encrypt(text, shift):
    original_alphabet = 'ABCDEFGHIKLMNOPORSTUVWXYZ'
    shifted_alphabet = original_alphabet[shift:] + original_alphabet[:shift]
    encrypted_text = ''
    for char in text:
        if char.upper() in original_alphabet:
            index = original_alphabet.index(char.upper())
            if char.isupper():
                encrypted_text += shifted_alphabet[index].upper()
            else:
                encrypted_text += shifted_alphabet[index].lower()
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    original_alphabet = 'ABCDEFGHIKLMNOPORSTUVWXYZ'
    shifted_alphabet = original_alphabet[shift:] + original_alphabet[:shift]
    decrypted_text = ''
    for char in text:
        if char.upper() in shifted_alphabet:
            index = shifted_alphabet.index(char.upper())
            if char.isupper():
                decrypted_text += original_alphabet[index].upper()
            else:
                decrypted_text += original_alphabet[index].lower()
        else:
            decrypted_text += char
    return decrypted_text

def group_text(text, group_size):
    grouped_text = ''
    for i in range(0, len(text), group_size):
        grouped_text += text[i:i+group_size] + ' '
    return grouped_text.strip()

def main():
    file_path = 'input.txt'  # 替换为你的输入文件路径
    shift = 20  # 替换为你想要的移位量
    group_size = 5  # 分组大小
    with open(file_path, 'r') as file:
        input_text = file.read()
        cleaned_text = remove_non_letters(input_text)
        encrypted_text = encrypt(cleaned_text, shift)
        decrypted_text = decrypt(encrypted_text, shift)
        grouped_encrypted_text = group_text(encrypted_text, group_size)
        grouped_decrypted_text = group_text(decrypted_text, group_size)
        print("密文：")
        print(grouped_encrypted_text)
        print("解密文本：")
        print(grouped_decrypted_text)

if __name__ == '__main__':
    main()