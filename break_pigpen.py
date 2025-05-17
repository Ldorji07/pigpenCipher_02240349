symbol_to_letter = {
    '┌ ┐': 'H', '┌─┐': 'E', '┐.': 'L', '└.': 'P',
    # Add rest of mappings
}

def break_cipher(symbols):
    return ''.join(symbol_to_letter.get(sym, '?') for sym in symbols.split())