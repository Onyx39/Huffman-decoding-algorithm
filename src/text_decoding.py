import main

str=""
with open(main.compressed_file_path, 'rb') as f:
    contents = f.read()
    print(type(contents))
    print(contents[0])
    print(contents[1])
    print(bin(contents[0]))
    print(bin(contents[1]))
    print(bin(contents[2]))
    print(bin(contents[3]))
    print(type(contents[0]))

for i in contents :
    cand = (bin(i)[2:])
    while len(cand) < 8 :
        cand = '0' + cand
    str += cand

str2 = str[:25]

print(contents)
print(str)
print('00010111,00011011,01111010,10000000')
print(len(str))
print(len(str2))
print(str2)
'''
print(str[0:3])
print(str[3:5])
print(str[5:8])
print(str[8:11])
print(str[11:13])
print(str[13:16])
print(str[16:19])
print(str[19:22])
print(str[22:25])
'''
