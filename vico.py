def convert_to_decimal(number, base):
    if not number:
        return 0
    last_digit = int(number[-1])
    remaining_number = number[:-1]
    return base * convert_to_decimal(remaining_number, base) + last_digit

number = "1011"
base = 2
result = convert_to_decimal(number, base)
print(result)