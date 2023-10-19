import base64

Hex_String="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

Byte_String= bytes.fromhex(Hex_String)

B64_String= base64.b64encode(Byte_String)

print (B64_String)