def caesar_encode_ch(ch, shift):
    return chr(ord(ch) + shift)

def caesar_encode(text: str, shift: int = 3):
    full_text = []
    for ch in text:
        encode_ch = caesar_encode_ch(ch, shift)
        full_text.append(encode_ch)
    return "".join(full_text)

def caesar_decode(text: str, shift: int = 3):
    return caesar_encode(text, -shift)

def main():
    print(caesar_encode("Hello"))   # Khoor
    print(caesar_decode("Khoor"))   # Hello

if __name__ == "__main__":
    main()
