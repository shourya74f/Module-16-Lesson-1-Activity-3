for n in [2, 3, 4, 5, 6, 7, 8, 9]:
    if n&1:
        print(" ", n, " - odd")
    else:
        print(" ", n, " - even")

n=int(input("Enter a number: "))
t=n
while t>0:
    print("Binary: ", bin(t)[2:], "last bit: ", t&1)
    t>>=1
print("Total 1s in ", n, "=", bin(n).count('1'))