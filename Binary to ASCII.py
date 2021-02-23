binary_valor = input("enter the binary valor : ")
binary_list = binary_valor.split(" ")
decimal_list = []
char_list = []
FinalCodedString = ''

def binary_to_decimal(binary):
    i,integer = 0,0
    size = len(binary)
    while i < len(binary):
        integer += int(binary[size - 1 - i])*pow(2,i)
        i+=1
    return integer

for x in binary_list:
   decimal_list.append(binary_to_decimal(x))

for x in decimal_list:
    char_list.append(chr(x))

for x in char_list:
    FinalCodedString += x

print(FinalCodedString)