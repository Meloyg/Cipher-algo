# https://cws.auckland.ac.nz/CWS/CourseWorkService.svc/cwt?cid=Hash
import hashlib

string2hash = "complexity:"

for i in range(1000):
    copy = string2hash
    string2hash += str(i)
    
    result = hashlib.md5(string2hash.encode())
    
    # if (result.hexdigest())[:2] == "00":
    #     print(string2hash)
    #     print(result.hexdigest())
    #     print()
    #     break
    # string2hash = copy

    if (result.hexdigest())[:5] == "00000":
        print(string2hash)
        print(result.hexdigest())
        print()
        break
    string2hash = copy
    


