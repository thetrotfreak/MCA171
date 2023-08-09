def EncodeQR(product_name: str):
    if (
        len(product_name) < 1
        or len(product_name) > 5
        or not any(character.isalpha() for character in product_name)
    ):
        return None

    # format as a 8 bit wide binary
    # Read: https://docs.python.org/3/library/string.html#formatspec
    encode = lambda x: format(ord(x), "08b")

    # partially encode the letters in the argument
    encoded_letters = list(map(encode, product_name))

    # calculate padding and perform concatenation
    for i in range(len(product_name)):
        padding = list("".zfill(7))
        padding.insert(i, "1")
        padding = "".join(padding)
        encoded_letters[i] = padding + encoded_letters[i]
    return encoded_letters
