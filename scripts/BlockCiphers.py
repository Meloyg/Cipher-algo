# https://cws.auckland.ac.nz/CWS/CourseWorkService.svc/cwt?cid=BlockCiphers

# plainText = [0xC13B, 0x981F, 0xD7A8]
# key = 0xABBA
# initVector = 0xD00D

# plainText = [0xEF51, 0x5B39, 0xE472]
# key = 0xABBA
# initVector = 0xBABE

# plainText = [0x6604, 0x8EFF, 0x7DA5]
# key = 0xABBA
# initVector = 0xBABE

plainText = [0xB823, 0x68EA, 0xAB77]
key = 0xABBA
initVector = 0xBABE


def main():
    # print(ecb())
    # print(cbc())
    print(pcbc())
    # print(cfb())


# ECB
def ecb():
    ecbStep1 = hex(key ^ plainText[2])
    return ecbStep1[2:].upper()

# CBC


def cbc():
    bufferHex = None
    cipherText = []
    for i in range(len(plainText)):
        if bufferHex is None:
            cbcStep1 = initVector ^ plainText[i]
        else:
            cbcStep1 = bufferHex ^ plainText[i]
        cbcStep2 = cbcStep1 ^ key
        bufferHex = cbcStep2
        cipherText.append(hex(bufferHex)[2:].upper())
    return cipherText

# PCBC


def pcbc():
    newInitVector = None
    buffer1 = None
    buffer2 = None
    cipherText = []
    for i in range(len(plainText)):

        if buffer2 is None:
            pcbcStep1 = plainText[i] ^ initVector
        else:
            newInitVector = buffer1 ^ buffer2
            pcbcStep1 = plainText[i] ^ newInitVector
        buffer1 = plainText[i]
        pcbcStep2 = pcbcStep1 ^ key
        buffer2 = pcbcStep2
        cipherText.append(hex(buffer2)[2:].upper())
    return cipherText

# CFB


def cfb():
    buffer1 = None
    cipherText = []
    for i in range(len(plainText)):
        if buffer1 is None:
            cfbStep1 = key ^ initVector
        else:
            cfbStep1 = buffer1 ^ key
        cfbStep3 = plainText[i] ^ cfbStep1
        buffer1 = cfbStep3
        cipherText.append(hex(cfbStep3)[2:].upper())
    return cipherText


main()
