args = input()

list_str = args.split(" ")

W = int(list_str[0])
H = int(list_str[1])
x = int(list_str[2])
y = int(list_str[3])
r = int(list_str[4])

flg1 = False
flg2 = False

if 0 <= (x - r) and (x + r) <= W:
    flg1 = True

    if 0 <= (y - r) and (y + r) <= H:
        flg2 = True

if flg1 and flg2:
    print('Yes')
else:
    print('No')
