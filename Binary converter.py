word = input('Escreve uma palavra : ')

WordArray = list(word)
CodedArray = []
Binary = []
FinalCodedString = ''

for x in WordArray:
    CodedArray.append(ord(x))

def Code_to_binary():
    for x in CodedArray:
        Binary.append(bin(x)[2:])

Code_to_binary()
for x in Binary:
    print(x)
