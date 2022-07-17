speed = 210/8 #mb/s /8
rrt_time = 90


file_b = 850 / 1000 # kb to mb
file_bb = 850/1000

compress1_b = 77 / 1000

compress2_b = 60 / 1000

image_size = 7
image_file_list = [1,2,2,2,1,1,1]


delete_image_position = [2,3,5]
delete_image_list = []
for i in range(len(image_file_list)):
    if i not in delete_image_position:
        delete_image_list.append(image_file_list[i])




file_b_l = [file_b]
result = 0
for i in range(len(file_b_l)):
    n = file_b_l[i]
    tem = n / speed * 1000 + 2 * rrt_time
    result += tem
print("11c1: " + str(round(result,2)))



print("11c2: " + str(round(result,2)))


compress1_file_b_l = [compress1_b]
result = 0
for i in range(len(compress1_file_b_l)):
    n = compress1_file_b_l[i]
    tem = n / speed * 1000 + 2 * rrt_time
    result += tem
print("11c3: " + str(round(result,2)))


file_b_2 = [file_bb]

total_list = file_b_2 + image_file_list
result = 0
for i in range(len(total_list)):
    n = total_list[i]
    tem = n / speed * 1000 + 2 * rrt_time
    result += tem
print("11c4: " + str(round(result,2)))




m1 = total_list
print(total_list)

result = 0
for i in range(len(m1)):
    n = m1[i]
    tem = n / speed * 1000
    result += tem
result += 3 * rrt_time
print("11c5: " + str(round(result,2)))


m2 = image_file_list
compress2_total_list = [compress2_b] + m2
print(compress2_total_list)
result = 0
for i in range(len(compress2_total_list)):
    n = compress2_total_list[i]
    tem = n / speed * 1000
    result += tem
result += 3 * rrt_time
print("11c6: " + str(round(result,2)))


delete_total_list = file_b_2 + delete_image_list
result = 0
for i in range(len(delete_total_list)):
    n = delete_total_list[i]
    tem = n / speed * 1000 + 2 * rrt_time
    result += tem
print("11c7: " + str(round(result,2)))



m3 = delete_total_list
print(m3)
result = 0
for i in range(len(m3)):
    n = m3[i]
    tem = n / speed * 1000
    result += tem
result += 3 * rrt_time
print("11c8: " + str(round(result,2)))

m4 = delete_image_list
compress2_delete_total_list = [compress2_b] + m4
print(compress2_delete_total_list)
result = 0
for i in range(len(compress2_delete_total_list)):
    n = compress2_delete_total_list[i]
    tem = n / speed * 1000 
    result += tem
result += 3 * rrt_time
print("11c9: " + str(round(result,2)))



