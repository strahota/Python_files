def get_symbol(first, second):
    collected_symbols = []
    for current_symbol in range(ord(first)+1, ord(second)+1):
        collected_symbols.append(chr(current_symbol))
    return collected_symbols

first_string = input()
second_string = input()
result = get_symbol(first_string, second_string)
print(" ".join(result))
