def fastPow(number, power):
    result = 1
    flag = 0
    if power < 0:
        power = -power
        flag = 1
    while power > 0:
        if power % 2 == 1:
            result *= number
        number *= number
        power = power // 2
    if flag == 1:
        return (f"1/{result}")
    return result

