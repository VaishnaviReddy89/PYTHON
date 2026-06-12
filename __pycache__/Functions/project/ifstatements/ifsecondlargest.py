a, b, c = 10, 20, 15

if (a > b and a < c) or (a > c and a < b):
    print("A is second largest")
elif (b > a and b < c) or (b > c and b < a):
    print("B is second largest")
else:
    print("C is second largest")