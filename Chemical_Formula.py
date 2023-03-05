n = "CHHHCOOH"
l = len(n)
output = ""
count = 1
sub_string = ""
for i in range(l-1):  # 0,1,2
    if n[i] == n[i+1]:
        count += 1
    else:
        if count > 1:
            sub_string += n[i] + str(count)
        else:
            sub_string += n[i]
        count = 1
    output += sub_string
    sub_string = ""

if count > 1:
    output += n[-1] + str(count)
else:
    output += n[-1]

print(output)
