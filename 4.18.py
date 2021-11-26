def suma(liczba):
    liczba=str(liczba)
    sum=0
    for x in range(0,len(liczba)):
        sum=sum+int(liczba[x])
    return sum

print(suma(7182))
    
    