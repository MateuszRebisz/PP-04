tab = [-15, 8, -31, 47, -2, 19]
min = tab[0]
max = tab[0]
for x in tab:
    if x < min:
        min = x
    if x > max:
        max = x
        
print(min)
print(max)