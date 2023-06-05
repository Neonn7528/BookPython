a = input("Enter A Number: ")  # 60
b = input("Now Enter Another Number: ")  # 5
sum = a + b
print("\nData Type sum:", sum, type(sum))
sum = int(a) + int(b)
print("Data Type sum:", sum, type(sum))
sum = float(sum)
print("Data Type sum:", sum, type(sum))
sum = chr(int(sum))
print("Data Type sum:", sum, type(sum))  # 65 - это ASCII-код символа А.
