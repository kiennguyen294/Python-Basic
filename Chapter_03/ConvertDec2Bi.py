from pythonds.basic import Stack

def divi_de_by_2(dec_number):
    remstack = Stack()
    while dec_number > 0:
        rem = dec_number % 2
        remstack.push(rem)
        dec_number = dec_number // 2
    bin_string = ""
    while not remstack.isEmpty():
        bin_string = bin_string + str(remstack.pop())

    return bin_string

print(divi_de_by_2(42))

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()
    while dec_number > 0:
        rem = dec_number % base
        remstack.push(rem)
        dec_number = dec_number // base
    new_string = ""
    while not remstack.isEmpty():
        new_string = new_string + digits[remstack.pop()]
    return new_string

