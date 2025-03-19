nums = [1, 2, 3, 4]
# nums = list(range(1, 5))

even = []
for n in nums:
    if n % 2 == 0:
        even.append(n)
print(even)

even = [n for n in nums if n % 2 == 0]
print(even)

# asdad = [n * 2 for n in range(5)]
# print(asdad)

[print(x) for x in range(4)]

kek = {n: "even" if n % 2 == 0 else "odd" for n in nums}
print(kek)
