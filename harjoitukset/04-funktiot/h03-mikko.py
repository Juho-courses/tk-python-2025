# Kirjoita funktio, jolla on kaksi argumenttia 'numbers' (lista kokonaislukuja)
# ja 'divider' (kokonaisluku). Funktio suodattaa ja palauttaa listan niistä
# 'numbers':in arvoista, jotka ovat jaollisia 'divider':illä. 'divider':in
# oletusarvo on 2, joten funktiota voidaan kutsua myös yhdellä argumentilla.
#
#     filter_values([1,2,3,4,5,6]) -> [2, 4, 6]
#     filter_values([1,2,3,4,5,6], 3) -> [3, 6]

def filter_values(numbers: list[int], divisor: int = 2) -> list[int]:
    """ Filters values from a list based on the divisor.

    If the value modulo divisor is 0, it is considered a valid value and added 
    to the return value.
    
    Returns:
        list[int]: Filtered list
    """
    return [num for num in numbers if num % divisor == 0]


if __name__ == "__main__":
    nums = [1,2,3,4,5,6]

    print(filter_values(nums))
    print(filter_values(nums, 3))
