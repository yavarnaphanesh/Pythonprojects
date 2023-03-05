n = "14 41 12314 13124 161 116 611 7 989"
N = n.split()
N = sorted(N, key=len)
new_list = []
for i in N:
    sub_list = []
    for j in N[1:]:
        if len(i) == len(j):
            if sorted(i) == sorted(j):
                sub_list.append(j)
        else:
            sub_list.append(i)

    new_list.append(list(set(sub_list)))

result = []
for i in new_list:
    if i not in result:
        result.append(i)
for i in result:
    print(*i)
