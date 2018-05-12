args = input()

list_str = args.split(" ")
list_int = [int(s) for s in list_str]

list_int.sort()

print(str(list_int[0]) + " " + str(list_int[1]) + " " + str(list_int[2]))
