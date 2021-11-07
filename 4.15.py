import mymath

gra = True

while gra:
    if mymath.read_number() == mymath.generate_number():
        print("You've won")
        gra = False
    else:
        print("U've lost.")

