from random import randint

r1, r2 , r3, r4 = [randint(0, 255) for _ in range(4)]

print("Your random IP address is: {}.{}.{}.{}".format(r1, r2, r3, r4))

input("press enter to get the answer...")

print("{}.{}.{}.{}".format(str(bin(r1))[2:].zfill(8), str(bin(r2))[2:].zfill(8), str(bin(r3))[2:].zfill(8), str(bin(r4))[2:].zfill(8)))

