def filter_values(numbers, divider=2):
    ret = []

    for n in numbers:
        if n % divider == 0:
            ret.append(n)

    return ret


def filter_values_comp(numbers, divider=2):
    return [n for n in numbers if n % divider == 0]


print(filter_values([1, 2, 3, 4, 5, 6]))
print(filter_values([1, 2, 3, 4, 5, 6], 3))

print(filter_values_comp([1, 2, 3, 4, 5, 6]))
print(filter_values_comp([1, 2, 3, 4, 5, 6], 3))
