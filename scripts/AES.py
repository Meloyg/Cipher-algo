# https://cws.auckland.ac.nz/CWS/CourseWorkService.svc/cwt?cid=AES

key1 = "EF,86,16,76,7E,D2,C8,16,F4,67,5A,C2,E5,7F,3A,5D"
key2 = "91,4D,E5,D7,21,51,8E,8F,1F,F3,8C,93,47,E0,3F,64"
plainText = "nrFeuWNVYwQdYxrPKPUjBEHBHTLrKVdYWbmjtvNjPAfVRhdI"


def main():
    w1 = question1(plainText)
    print("Question 1: {}".format(w1))
    question4(w1)
    print()

    round0 = question2(w1, key1)
    print("Question 2: {}".format(round0))
    question4(round0)
    print()

    print("Question 3:\n Uses a lookup table called the S-Box (public) to substitute each cell value of the matrix, S obtained from previous AddRoundKey step\n Since each cell value is written in Hex e.g. XY, the cell value is replaced with the value in the xth row and yth column of the S-Box table")

    print("\nQuestion 4:\nNeed to shift manually")
    q4 = question4("0C,BF,53,7D,2B,97,44,09,95,CA,2B,24,65,C5,52,D7")


def question1(sentence):
    sentence = sentence[:16]
    hex1 = ""
    for i in sentence:
        word = hex(ord(i))
        word = word[2:]
        if len(word) == 1:
            word = "0" + word
        hex1 += word.upper() + ","
    return hex1[:-1]


def question2(w1, key1):
    lst1 = key1.split(",")
    lst2 = w1.split(",")
    w3 = ""
    for i in range(len(lst1)):
        result = (hex(int(lst1[i], 16) ^ int(lst2[i], 16)))[2:]
        if len(result) == 1:
            result = "0" + result
        w3 += result.upper() + ","
    return (w3[:-1])


def question4(q4):
    lst = q4.split(",")
    start = 0
    for i in range(4):
        lst1 = []
        for i in range(start, 16, 4):
            lst1.append(lst[i])
        start += 1
        print(lst1)
    return


main()
