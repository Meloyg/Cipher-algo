# https://cws.auckland.ac.nz/CWS/CourseWorkService.svc/cwt?cid=DiffieHellman

# g = int("7", 16)
# p = int("D", 16)
g = 3
p = 251
# string = "8E246970"
string = "6D7CA839"

for i in range(1):
    a = i
    b = i
    if g ** a % p == 94:
        print("a {}".format(i))
    if g ** b % p == 101:
        print("b {}".format(i))

key = g ** (71 * 120) % p
print("Public key: {}".format(key))

new_result = ""
for i in string:
    letter = int(i, 16) ^ key

    new_result += str(hex(letter))[2:]
print(new_result.upper())

