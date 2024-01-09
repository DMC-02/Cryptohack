from binascii import unhexlify
import string

def Single_Byte_Xor(input, Key):
    if len(chr(Key)) != 1:
      raise "KEY LENGTH EXCEPTION: In Single_Byte_Xor Key must be 1 byte long!"

    output = b''
    for b in input:
        output += bytes([b ^ Key])

    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"

data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded = unhexlify(data)


result = {}
for i in range(256):
    result[i] = (Single_Byte_Xor(decoded, i))
    #print("[-] KEY: {}\nSTRING: {}".format(i,Single_Byte_Xor(decoded, i)))

print("{}".format([s for s in result.values() if "crypto" in s]))