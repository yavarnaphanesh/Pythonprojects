n = [2,3,4,11,12,13,24,25,26]
N = sorted(n)
l = len(N)
Main_list = []
sub_list = []
for i in range(l-1):
    # 0,1,2,3,4,5,6,7,8,9,10
    if i+1 <= l:
        if N[i]+1 == N[i+1]:
            sub_list.extend([N[i], N[i+1]])
        else:
            sub_list.append(N[i])
            if sub_list not in Main_list:
                Main_list.append(list(set(sub_list)))
            sub_list = []

if sub_list not in Main_list:
    Main_list.append(list(set(sub_list)))
# print(Main_list)
# print(len(Main_list))
Main_list = sorted(Main_list, key=len)
max_len_Array = None
max_len = 0
for i in Main_list:
    if len(i) > max_len:
        max_len = len(i)
        max_len_Array = i
print(max_len_Array)
