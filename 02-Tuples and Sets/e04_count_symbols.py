text = input()

symbol_dict = {}

for symbol in text:
    if symbol not in symbol_dict.keys():
        symbol_dict[symbol] = 0

    symbol_dict[symbol] += 1

[print(f'{key}: {value} time/s') for key, value in sorted(symbol_dict.items())]
