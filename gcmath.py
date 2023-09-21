def QS(number: int) -> int:
    """

    :param number:
    :return:
    """
    return sum([int(z) for z in str(number).replace('-', '')])


def BWW(word: str) -> int:
    """

    :param word:
    :return:
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzäöüß'
    sum = 0
    for let in word.lower():
        if let in alphabet:
            sum += (alphabet.index(let) + 1)
        elif let.isdigit():
            sum += int(let)
    return sum


def IQS(number: int) -> int:
    """

    :param number:
    :return:
    """
    while len(str(number)) > 1:
        number = QS(number)
    return number