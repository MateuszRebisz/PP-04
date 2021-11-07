tab = [15, 8, 31, 47, 2, 19]
even = 0
odd = 0
for x in tab:
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(odd)
print(even)