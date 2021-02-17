alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
s = input("Please Enter Yout Text:")
input = list(s)
mem = 0
counter = 0
for i in input:
    c = i
    c_asci = ord(c)
for j in range(8):
    this_bit = (c_asci & 128) >> 7
    mem = mem << 1
    mem = mem | this_bit
    counter = counter+1
    c_asci = c_asci << 1
    if counter == 6:
        print(str(alphabet[mem]), end="")
        mem = 0
        counter = 0
mem = mem << (6-counter)
if len(input) % 3 == 1:
    print(str(alphabet[mem])+"==")
if len(input) % 3 == 2:
    print(str(alphabet[mem])+"=")
