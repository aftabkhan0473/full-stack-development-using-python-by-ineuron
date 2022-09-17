# Let's make a function who can convert any binary number to decimal!
bin_number = input("Enter any binary number : ")
list_binary = list(bin_number)
list_binary.reverse()
decimal = 0;
for i in range(len(bin_number)):
    decimal = decimal + int(list_binary[i])*2**i;
print(decimal)