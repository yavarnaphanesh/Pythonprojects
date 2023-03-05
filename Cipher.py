alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabets = [str(x) for x in alphabets]
encrypt_or_decrypt = input()
text = input()
shift = int(input())

if encrypt_or_decrypt == "encode":
    alphabets_encrpted = ""
    for i in text:
        res = alphabets.index(i) + shift
        alphabets_encrpted += alphabets[res]
    print(alphabets_encrpted)
elif encrypt_or_decrypt == "decode":
    alphabets_decode = ""
    for i in text:
        res = alphabets.index(i) - shift
        alphabets_decode += alphabets[res]
    print(alphabets_decode)
