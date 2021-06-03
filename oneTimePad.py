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

for i in range(65, 91):
    list4 = ""
    print(chr(i))
    for j in list2:
        value = i ^ int(j, 16)
        print(chr(value))

print(list2)
