import requests
from pwn import xor

def Get_Ciphertext():
    r = requests.get("http://aes.cryptohack.org/flipping_cookie/get_cookie")
    return r.json()['cookie']

def Check_Admin(cookie,iv):
    r = requests.get(f"http://aes.cryptohack.org/flipping_cookie/Check_Admin/{cookie}/{iv}")
    return r.json()

ct = bytes.fromhex(Get_Ciphertext())
iv = ct[:16]
cookie = ct[16:].hex()

pt = b'admin=False;expiry='[:16]
pt_payload = b'admin=True;expiry='[:16]
iv_payload = xor(pt_payload, pt, iv).hex()
print(Check_Admin(cookie, iv_payload)['flag'])