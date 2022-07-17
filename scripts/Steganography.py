hex1 = "FF0001 FF0000 FE0000 FE0000 FE0000 FE0000 FE0000 FE0000 FE0000 FE0000 FE00 "
hex2 = "00 FF0000 FF0101 FE0100 FF0000 FF0100 FF0100 FE0001 FF0001 FF0101 FE0101 FE0001 FF0100 FF0100 FF0100 "
hex3 = "FE0101 FF0001 FF0101 FE0101 FE0000 FF0100 FF0100 FF0000 FF0001 FF0000 FE0100 FE0101 FE0100 "
hex4 = "FE0000 FF0100 FE0001 FE0101 FF0001 FE0100 FE0101 FE0000 FF0000 FF0000 FF0000 FF0000 FF0000 "
hex2 = hex2 + hex3 + hex4
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

count = 104
"""
for key, value in list1.items():
    print("{} : {}".format(key, value))
"""

values = ""

for key, value in list1.items():
    values += value

values = values[:104][::-1]

for i in values:
    if count > 0:
        
        print(i, end="")
        count -= 1
