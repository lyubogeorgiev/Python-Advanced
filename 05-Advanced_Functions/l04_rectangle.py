def rectangle(length, width):
    if type(length) is not int or type(width) is not int:
        return f'Enter valid values!'

    def area():
        return length * width

    def perimeter():
        return length * 2 + width * 2

    return f'Rectangle area: {area()}\n' \
        f'Rectangle perimeter: {perimeter()}'


print(rectangle(2, 10))