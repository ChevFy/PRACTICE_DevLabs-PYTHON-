
list = []

def input_data() :
    while True:
        entry = int(input())
        if entry == 0:
            break
        else:
            pass
        list.append(entry)
    return order()

def order() :
    mode = str(input().lower())
    if mode == "min":
        list.sort()
    elif mode == "max":
        list.sort(reverse=True)
    return list


input_data()
print(" ".join(map(str, list)))



