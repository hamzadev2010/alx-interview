def validUTF8(data):
    numofbyte = 0
    # loop to return the number of bytes
    for num in data:
        bnr = format(num, "#010b")[-8:]
        if numofbyte == 0:
            for bit in bnr:
                if bit == '0':
                    break
                numofbyte += 1
            if numofbyte == 0:
                continue
            if numofbyte == 1 or numofbyte > 4:
                return False
        else:
            if bnr[0] != '1' or bnr[1] != '0':
                return False

        numofbyte -= 1

    return numofbyte == 0
