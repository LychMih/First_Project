#txt = input("Enter text... -> ")
txt = "jkhfga bkj jhvj kh vjk"

def make_list(text):
    my_list = []
    list_elem = ""
    for ch in text:
        if ch != " ":
            list_elem += ch
        else:
            my_list.append(list_elem)
            list_elem = ""
    else: my_list.append(list_elem)
    return my_list

x = txt.split("v ")
print(x)

result = []
for el in x:
    result.append(''.join(sorted(el)))

print(' '.join(result))
