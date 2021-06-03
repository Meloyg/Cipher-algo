# https://cws.auckland.ac.nz/CWS/CourseWorkService.svc/cwt?cid=Feistel

keys = [0x4331, 0xD04A]
L0 = 0xD5B6
R0 = 0x9DA8
encryptionRound = 2
decryptionRound = 1

def main():
    encryptionL0, encryptionR0 = encryption()
    print("encryption: {} {}".format(hex(encryptionL0)[2:].upper(), hex(encryptionR0)[2:].upper()))
    decryptionL0, decryptionR0 = decryption(encryptionL0, encryptionR0)
    print("decryptionRound: {} {}".format(hex(decryptionL0)[2:].upper(), hex(decryptionR0)[2:].upper()))


def encryption():
    l0 = L0
    r0 = R0
    lst = list(keys)
    for i in range(encryptionRound):
        if i % 2 == 0:
            step1 = lst[0] + r0
            step2 = step1 ^ l0
            l0 = step2
        else:
            step1 = lst[1] + l0
            step2 = step1 ^ r0
            r0 = step2
    if encryptionRound % 2 == 0:

        return l0, r0
    else:
        return r0, l0

def decryption(encryptionL0, encryptionR0):
    l0 = encryptionR0
    r0 = (encryptionL0)
    lst = list(keys)
    for i in range(decryptionRound):
        if i % 2 == 0:
            step1 = lst[1] + r0
            step2 = step1 ^ l0
            l0 = step2
        else:
            step1 = lst[0] + l0
            step2 = step1 ^ r0
            r0 = step2
    if decryptionRound % 2 == 0:
        return r0, l0
    else:
        return l0, r0


main()




