# Hexadecimal to decimal
def hex_to_dec(hex_num):
    dec_num = 0
    for i, dig in enumerate(reversed(hex_num)):
        dec_num += int(dig, 16) * (16**i)
    return dec_num

# Decimal to hexadecimal
def dec_to_hex(dec_num):
    hex_num = ''
    while dec_num > 0:
        hex_dig = dec_num % 16
        if hex_dig<10:
            hex_num = str(hex_dig) + hex_num
        else:
            hex_num = chr(55 + hex_dig) + hex_num
        dec_num = dec_num // 16
    return hex_num

# Hexadecimal to binary
def hex_to_bin(hex_num):
    bin_num = ''
    for dig in hex_num:
        bin_dig = bin(int(dig,16))[2:].zfill(4)
        bin_num += bin_dig
    return bin_num

# Binary to hexadecimal
def bin_to_hex(bin_num):
    hex_num = ''
    for i in range(0, len(bin_num), 4):
        bin_dig = bin_num[i:i+4]
        hex_dig = str(int(bin_dig, 2))
        hex_num += hex_dig
    return hex_num

# Octal to decimal
def oct_to_dec(oct_num):
    dec_num = 0
    for i, dig in enumerate(reversed(oct_num)):
        dec_num += int(dig) * (8**i)
    return dec_num

# Decimal to octal
def dec_to_oct(dec_num):
    oct_num = ''
    while dec_num > 0:
        oct_dig = dec_num % 8
        oct_num = str(oct_dig) + oct_num
        dec_num = dec_num // 8
    return oct_num
