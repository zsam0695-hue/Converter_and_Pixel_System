from PIL import Image


# 1. Buld an ASCII-to-decimal converter.
s = input("Enter text: ")

for c in s:
    print(ord(c))


# 2. Build a number-base converter supporting binary, decimal, octal, and hexadecimal.
num = input("Enter a number: ")
base = int(input("Enter its base (2, 8, 10, 16): "))

decimal_val = int(num, base)
# [2:] takes away the first two numbers since it's a prefix
print("Binary Value: ", bin(decimal_val)[2:])
print("Octal Value: ", oct(decimal_val)[2:])
print("Decimal Value: ", decimal_val)
print("Hexadecimal Value: ", hex(decimal_val)[2:].upper()) #upper() for the A-F in hex context


# 3. Write a program that reads an image and prints its pixel values.
def toColor(color):
    if color == "(237, 28, 36)":
        return "R"
    elif color == "(0, 0, 0)":
        return "B"
    elif color == "(255, 242, 0)":
        return "Y"
    else: return color

output_file = open("input.txt", "w")

image_file = Image.open("./smiley.png")
image_file.load()

width, height = image_file.size

for y in range(height):
    for x in range(width):
        color = str(image_file.getpixel((x, y)))
        color = toColor(color)
        output_file.write(color)
        output_file.write(" ")
    output_file.write("\n")

output_file.close()

#for line in lines:
#    for pixel in line:
#        color = getColor(pixel)
#        print(color)
#    print(";\n")


# 4. Write a program that consumes pixel values and creates an image.
def toPixel(color):
    if color == "R":
        return (237, 28, 36)
    elif color == "B":
        return (0, 0, 0)
    elif color == "Y":
        return (255, 242, 0)
    else: return color

input_file = open("input.txt", "r")
lines = input_file.readlines()
width, height = lines[0].count(" "), len(lines)
output_image = Image.new("RGB", (width, height))

for y in range(height):
    line = lines[y].strip().split(" ")
    for x in range(width):
        color = toPixel(line[x])
        output_image.putpixel((x, y), color)

output_image.save("output.png")
input_file.close()

# 5. Test boundary cases, including zero, the largest supported unsigned value, and at least one negative two's-complement value.
print("\nBoundary Case Tests: ")

print("Zero: ", bin(0)[2:], oct(0)[2:], 0, hex(0)[2:].upper())
print("Largest Unsigned Value: ", bin(255)[2:], oct(255)[2:], 255, hex(255)[2:].upper())
print("Negative Two's Complement Value: ", format((-1) & 0xFF, "08b"), format((-1) & 0xFF, "03o"), -1, format((-1) & 0xFF, "02X"))
