def decimalToBinary(num):
    # Convert decimal number to binary and pad to 4 bits
    binary_representation = bin(num)[2:].zfill(4)
    return binary_representation

def binaryToDecimal(binary_str):
    # Convert binary string to decimal
    decimal_representation = int(binary_str, 2)
    return decimal_representation

# Example calls
print("Decimal to Binary Conversion:")
print(decimalToBinary(9))   # Output: 1001
print(decimalToBinary(0))   # Output: 0000
print(decimalToBinary(15))  # Output: 1111

print("\nBinary to Decimal Conversion:")
print(binaryToDecimal("1001"))  # Output: 9
print(binaryToDecimal("0000"))  # Output: 0
print(binaryToDecimal("1111"))  # Output: 15
