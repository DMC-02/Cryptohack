from operator import xor

key1="a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1And2="37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2And3="c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
key1And2And3AndFlag="04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

Key1Byte=bytes.fromhex(key1)
key1And2Byte=bytes.fromhex(key1And2)

key2 = (Key1Byte ^ key1And2Byte)

key2And3Byte=bytes.fromhex(key2And3)

Key3= (key2 ^ key2And3Byte)

key1And2And3AndFlagByte= bytes.fromhex(key1And2And3AndFlag)

print(((key2^Key3)^(Key1Byte^key1And2And3AndFlagByte)))