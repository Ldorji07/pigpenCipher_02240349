PIGPEN_KEY = {
    'A': 'symbol_A', 'B': 'symbol_B', 'C': 'symbol_C',
    'H': '┌ ┐', 'E': '┌─┐', 'L': '┐.', 'P': '└.',
    # Add remaining letters
}

def encrypt(text):
    return ' '.join(PIGPEN_KEY.get(char.upper(), '?') for char in text)

def decrypt(symbols):
    reverse_key = {v: k for k, v in PIGPEN_KEY.items()}
    return ''.join(reverse_key.get(sym, '?') for sym in symbols.split())

if __name__ == "__main__":
    message = "HELP"
    cipher = encrypt(message)
    print("Encrypted:", cipher)
    print("Decrypted:", decrypt(cipher))