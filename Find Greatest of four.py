a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

if a >= b and a >= c and a >= d:
    print("a is greatest")
elif b >= a and b >= c and b >= d:
    print("b is greatest")
elif c >= a and c >= b and c >= d:
    print("c is greatest")
else:
    print("d is greatest")