"""
Modular calculations.
"""


def mod_pow(base, power, mod):
    """
    Solve x = a^b % c
    :param base: a
    :param power: b
    :param mod: c
    :return: x
    """
    if power < 0:
        return -1
    base %= mod
    result = 1

    while power > 0:
        if power & 1:
            result = (result * base) % mod
        power = power >> 1
        base = (base * base) % mod
    return result


if __name__ == "__main__":
    print(mod_pow(3, 8, 13))
