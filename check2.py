binary_input = input("Enter a binary number : ");
list_binary = list(binary_input)
list_binary.reverse() #can't store this in a variable!
decimal = 0;

for i in range(len(binary_input)):
    decimal = decimal + int(list_binary[i])*2**i;

print(decimal)