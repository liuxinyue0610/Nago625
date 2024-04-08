def get_original_text():
    return "as df"

def get_shift_amounta():
    from argparse import ArgumentParser
    parser =ArgumentParser()
    parser.add_argument('--shift', type=int, default=3)
    args =parser.parse_args()
    print(args)
    return 1


def remove_nonletters(input_text):
    return"asdf"

def cipher(text,shift_amount):
    return"zxcv"

def decipher(text,shift_amount):
    return"asdf"

if __name__ == "__main__":
    original_text = get_original_text()

    shift_amount = get_shift_amounta()

    text_without_nonletters = remove_nonletters(original_text)
    print("Text without non-letters:", text_without_nonletters)

    encrypted_text = cipher(text_without_nonletters, shift_amount)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decipher(encrypted_text, shift_amount)
    print("Decrypted text:", decrypted_text)