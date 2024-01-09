from binascii import unhexlify

def brute(Input, Key):
    if len(Input) != len(Key):
        return "Failed!"

    output = b''
    for b1, b2 in zip(Input, Key):
        output += bytes([b1 ^ b2])
    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"

data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
Cipher = unhexlify(data)
print("[-] CIPHER: {}".format(Cipher))


key_part = brute(Cipher[:7], "crypto{".encode())
print("[-] PARTIAL KEY FOUND: {}".format(key_part))


Key = (key_part + "y").encode()
Key += Key * int((len(Cipher) - len(Key))/len(Key))
Key += Key[:((len(Cipher) - len(Key))%len(Key))]
print("[-] Decoding using KEY: {}".format(Key))

plain = brute(Cipher, Key)
print("\n {}".format(plain))