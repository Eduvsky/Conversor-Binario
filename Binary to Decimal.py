def binary_to_decimal(binary):
    i,integer = 0,0
    size = len(binary)
    while i < len(binary):
        integer += int(binary[size - 1 - i])*pow(2,i)
        i+=1
    print(integer)

aux = input("Enter a binary valor (must contain only 0's and 1's  : ")
binary_to_decimal(aux)