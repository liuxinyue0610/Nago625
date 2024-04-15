import argparse

def remove_non_letters(text):
    # 주어진 텍스트에서 알파벳 문자만 제거하는 함수
    letters_only = [char for char in text if char.isalpha() or char.isspace()]  # 수정된 부분
    return ''.join(letters_only)

def shift_cipher(text, shift_amount):
    # Monoalphabetic Shift Cipher를 적용하는 함수
    cipher_text = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            cipher_text += shifted_char
        else:
            cipher_text += char
    return cipher_text

def main():
    # command-line argument 파싱
    parser = argparse.ArgumentParser()
    parser.add_argument('--shift', type=int, help='Shift amount for the cipher')
    args = parser.parse_args()

    # 사용자로부터 shift 양 입력 받기
    if args.shift is None:
        print("Please provide a shift value using --shift")
        return

    # original.txt 파일에서 original text 읽어오기
    with open('original.txt', 'r') as file:  # 수정된 부분
        original_text = file.readline().rstrip()

    # 알파벳 문자 이외의 문자 제거
    original_text = remove_non_letters(original_text)

    # 암호화 수행
    cipher_text = shift_cipher(original_text, args.shift)

    # 복호화 수행
    decipher_text = shift_cipher(cipher_text, 26 - args.shift)

    # 결과 출력
    print("Original text:", original_text)  # 추가된 부분
    print("Cipher text:", cipher_text)
    print("Deciphered text:", decipher_text)

if __name__ == '__main__':
    main()
