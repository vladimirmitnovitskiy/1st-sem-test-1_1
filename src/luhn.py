def luhnCheck(cardNumber):
    digits = [int(d) for d in str(cardNumber) if d.isdigit()]
    control = digits.pop()
    parity = (len(digits) + 1) % 2
    total = 0
    for i in range(len(digits)):
        if i % 2 == parity:
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digits[i]
    return (total + control) % 10 == 0

userInput = 0
try:
    userInput = int(input())
    if userInput == -1:
        pass

    else:
        print(luhnCheck(userInput))


except ValueError:
        print('Неверно введён номер карты')


