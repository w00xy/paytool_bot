def split_number(number):
    """Разбивает число на части, не превышающие 2.

    Args:
        number: Число, которое нужно разбить.

    Returns:
        Список частей числа.
    """
    parts = []
    while number > 0:
        if number >= 2:
            parts.append(2)
            number -= 2
        else:
            parts.append(number)
            number = 0
    return parts


def emoji_number(num):
    numbers = {
        1: '1️⃣',
        2: '2️⃣',
        3: '3️⃣',
        4: '4️⃣',
        5: '5️⃣',
        6: '6️⃣',
        7: '7️⃣',
        8: '8️⃣',
        9: '9️⃣',
        10: '🔟'
    }

    if num <= 10:
        return numbers.get(num, "")
    else:
        tens_digit = num // 10
        ones_digit = num % 10
        return numbers.get(tens_digit, "") + numbers.get(ones_digit, "")