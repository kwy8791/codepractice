args = input()
ints = args.split(" ")

a = int(ints[0])
b = int(ints[1])
c = int(ints[2])

if a < b and b < c:
    print('Yes')
else:
    print('No')
