
def hexcolor(r, g, b):
    """ Given ints r, g and b (0-255) return a hex string describing a colour.
    """
    return '#' + ''.join([hex(c)[2:].zfill(2) for c in [r,g,b]])


def rgbcolor(hex_str):
    """ Given a color as a hex string return ints r, g, b. """
    r, g, b = [int(hex_str[i:i+2], 16) for i in range(1, 7, 2)]
    return r, g, b


def blend(colors):
    """ Given a list of hex string colors blend them and return a new hex string.
    """
    red = green = blue = 0
    for c in colors:
        r, g, b = rgbcolor(c)
        red += r
        green += g
        blue += b
    L = len(colors)
    return hexcolor(red//L, green//L, blue//L)


print(hexcolor(255,255,255))
print(blend(["#000000", "#778899"]))
