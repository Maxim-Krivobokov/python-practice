def search4vowels(phrase: str) -> set:
    """Searches vowels  in given word"""
    # returns True if any vowels were found in given word
    vowels = set('aeiou')

    return vowels.intersection(set(phrase))


def search4letters(phrase: str = 'galaxy', letters: str = 'auioe') -> set:
    """ returns set of chars from input arg "letters", found in given arg 'word' """
    return set(letters).intersection(set(phrase))


res1 = search4vowels('Azanulbizar')
print(res1)

res2 = search4letters('khazaddum', 'hzdnmtp')
print(res2)
