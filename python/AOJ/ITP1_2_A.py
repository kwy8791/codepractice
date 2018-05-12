args = input()
ints = args.split(" ")

a = int(ints[0])
b = int(ints[1])

if a < b:
    print('a < b')
elif a == b:
    print('a == b')
else:
    print('a > b')
