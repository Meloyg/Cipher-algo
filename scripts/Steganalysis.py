from PIL import Image
list1 = []
hex2 = ""

file = open("../Code/Book1.txt", "r")
content = file.read().split("\n")
file.close()
for i in content:
    list1.append(i[1:])

for i in list1:
    hex2 += i + " "

num = 0
list1 = {}
buffer = ""

for i in hex2:
    if i != " ":
        buffer += i
    else:
        word = ""
        for i in range(len(buffer)):
            if i % 2 == 1:
                if buffer[i] == "F" or buffer[i] == "1":
                    word += "1"
                else:
                    word += "0"
        list1[num] = word
        num += 1

        buffer = ""

bitArray = []

for key, value in list1.items():
    bitArray.append(value)


width = 600
height = 77
#height1 = 77


def newImg(bitArray):
    img = Image.new('RGB', (width, height))
    counter = 0

    for j in range(height):
        for i in range(width):
            color1 = int(bitArray[counter][0]) * 255
            color2 = int(bitArray[counter][1]) * 255
            color3 = int(bitArray[counter][2]) * 255
            img.putpixel((i, j), (color1, color2, color3))
            counter += 1
    img.save('sqr.png')
    return img


wallpaper = newImg(bitArray)
wallpaper.show()

print(76.9/171)
