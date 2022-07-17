lst1 = "D9B4107B2BB854377CFF3E848F3C8CACD71F9D5F8A7A7977FC3C"
lst2 = "DAA51E762BB8423770FA2D988F229AE2D7509F169A657F6AFE3C"
lst3 = "CCA9057120FB546578F02390CE279AE2C14D9552D97E7575F73C"
lst4 = "DDBE157937B8493639F13F8F8F2D80ACC253D05591687E7AFE3C"
lst5 = "C7B007616EFA4F246DED6A9ADA2A9BA6834D9552D9606375FE3C"
lst6 = "CBB0037F2BF5412B39E92B8E8F2487A7835096168D617F6AFE3C"
lst7 = "C8A4026C3CF94C2C78F06A90CE3982A7D71F835A8C64607CFF3C"

list1 = [lst1, lst2, lst3, lst4, lst5, lst6, lst7]
list2 = []
list3 = []
buffer = ""
count = 0
for p in range(int(len(lst1) / 2)):
    for i in list1:
        for j in i:
            if count < 2:
                buffer += j
                count += 1
            else:
                list2.append(buffer)
                buffer = ""
                count = 0
                break
    list3.append(list2)
    list2 = []
    for x in range(len(list1)):
        list1[x] = list1[x][2:]


c = 26
l = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7
lis = []
x = ""

while len(l) != 0:
    x = l[:52]
    lis.append(x)
    x = ""
    l = l[52:]

count = 0
k = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
check = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
answerCheck = []
count = 0
output = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in check:
    answerCheck.append(hex(ord(i)))

for i in lis:
    for ii in range(0, len(i), 2):
        k[count].append(int(i[ii] + i[ii + 1], 16))
        count += 1
    count = 0

ke = ""
count2 = 0
count = 0

# for i in range(len(list3)):
#     print("{}: {}".format(i, list3[i]))

for i in k[12]:
    print(hex(i), chr(i ^ (0x8F ^ 0x20)))

x = 0x2D

print(chr(x ^ x ^ 0x20))


