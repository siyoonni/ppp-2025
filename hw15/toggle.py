def toggle_text(text: str) -> str:
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
    return result

def main():
    print(toggle_text("Hello"))

if __name__ == "__main__":
    main()