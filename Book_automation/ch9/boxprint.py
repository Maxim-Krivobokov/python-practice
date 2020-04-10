def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol variable shold be single-symbol')
    if width <= 2:
        raise Exception('Value of width shoul be > 2')
    if height <= 2:
        raise Exception('Value of height shoul be > 2')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('!!!!!!!!!Exception Appeared: ' + str(err))