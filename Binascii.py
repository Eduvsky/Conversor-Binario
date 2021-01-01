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
        Binary.append(' ')

def listToString(x):
    string = ''
    for i in x:
        string += i
    return string

Code_to_binary()
print(listToString(Binary))