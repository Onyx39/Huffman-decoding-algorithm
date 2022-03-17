import main

str=""
with open(main.compressed_file_path, 'rb') as f:
    contents = f.read()
    print(type(contents))
    print(contents[0])
    print(bin(contents[0]))
    print(type(contents[0]))


str += contents.decode('extend ascii')


print(contents)
print(str)
print(len(str))
print(str[0:3])
print(str[3:5])
print(str[5:8])
print(str[8:11])
print(str[11:13])
print(str[13:16])
print(str[16:19])
print(str[19:22])
print(str[22:25])
