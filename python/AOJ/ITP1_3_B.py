def input_until_zero():
    rtn_list = []
    while True:
        in_value = int(input())
        if in_value == 0:
            break
        rtn_list.append(in_value)
        
    return rtn_list

rtn = input_until_zero()

for i in range(len(rtn)):
    print("Case " + str(i + 1) + ": " + str(rtn[i]))

