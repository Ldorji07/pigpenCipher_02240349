# pigpenCipher_02240349
### PIGPEN_KEY
A dictionary that maps letters (like 'H', 'E', 'L', 'P') to Pigpen cipher symbols (e.g., '┌ ┐').

### encrypt(text)
Takes a plain text string (like "HELP").

Replaces each letter with its symbol from PIGPEN_KEY.

Joins them with spaces to form the encrypted message.

### decrypt(symbols)
Reverses PIGPEN_KEY to map symbols back to letters.

Splits the encrypted symbols.

Converts them back into the original text.

### break_cipher(symbols)
Uses a predefined symbol-to-letter dictionary.

Also decrypts Pigpen symbols, just another way without reversing a dictionary.

