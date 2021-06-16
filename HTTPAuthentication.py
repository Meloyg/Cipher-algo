import base64
import hashlib

sample_string = "yoshie:cefy"
sample_string_bytes = sample_string.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

# print(f"Encoded string: {base64_string}")
base64_string = "ZGFtaXI6bm90bm93"
base64_bytes = base64_string.encode("ascii")

sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("ascii")

# print(f"Decoded string: {sample_string}")
# print(f"Decoded string: {len(sample_string)}")

str2hash = "rizwan:compsci:letmein"
str2hash1 = "GET:/images/9.png"
result1 = hashlib.md5(str2hash.encode())
result2 = hashlib.md5(str2hash1.encode())
result1 = result1.hexdigest()
result2 = result2.hexdigest()

r1 = result1 + ":03e2abb8a924e696bee59d41cef32851:" + result2
result3 = hashlib.md5(r1.encode())
result3 = result3.hexdigest()
# print(result1)
# print(result2)
print(result3)
# print("==========================")

str2hash = "pearline:Mordor:crgv"
str2hash1 = "GET:/Public/CS/Home.png"
result1 = hashlib.md5(str2hash.encode())
result2 = hashlib.md5(str2hash1.encode())
result1 = result1.hexdigest()
result2 = result2.hexdigest()

r1 = result1 + ":03e2abb8a924e966bee59d41cef32851:" + result2
result3 = hashlib.md5(r1.encode())
result3 = result3.hexdigest()
# print(result1)
# print(result2)
# print(result3)


file = open("passwords.txt", "r")
cotent = file.read()
lst = cotent.split("\n")

for i in lst:
    str2hash = "sparkle:Mordor:"+(i.strip())
    str2hash1 = "GET:/Public/CS/Home.png"
    result1 = hashlib.md5(str2hash.encode())
    result2 = hashlib.md5(str2hash1.encode())
    result1 = result1.hexdigest()
    result2 = result2.hexdigest()

    r1 = result1 + ":03e2abb8a924e966bee59d41cef32851:"+result2
    result3 = hashlib.md5(r1.encode())
    result3 = result3.hexdigest()
    # print(result3)

    if result3 == "62b68b7b12ad5427a2eff21d9ac6dfb0":
        print(True)
        print(i)
        break
