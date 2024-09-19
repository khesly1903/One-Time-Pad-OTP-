import random


def msg_to_binary(msg:str) -> str:
    bin_msg = ""
    
    for m in range(len(msg)):
        bin_m = format(ord(msg[m]), "08b")
        bin_msg += f"{bin_m}"
        
    return bin_msg


def binary_to_msg(bin_msg:str) -> str:
    msg = ""
    
    for m in range(0, len(bin_msg), 8):
            msg_part = bin_msg[m:m+8]
            msg_part = chr(int(msg_part,2))
            msg += f"{msg_part}"
    return msg

    
def xor(m:str, k:str) -> str:
    if len(m) != len(k):
        raise ValueError("Must be same length")
    
    result = ""
    
    for i in range(len(m)):
        if m[i] == k[i]:
            result += "0"
        else:
            result += "1"
        
    return result
    
    
def generate_key(length:int) -> str:
    key = ""
    
    for m in range(length):
        k = format(random.randint(0,255), "08b")
        key += f"{k}"
        
    return key


    
def encrypt(msg:str, key:str) -> str:
    bin_msg = msg_to_binary(msg)
    
    return xor(bin_msg, key)


def decrypt(enc_msg:str, key:str) -> str:
    dec_msg = xor(enc_msg,key)
    return binary_to_msg(dec_msg)




message = str(input("Message: "))
key = generate_key(len(message))
encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print(f"Binary message:  {msg_to_binary(message)}")
print(f"Key:             {key}")
print(f"Encrypted:       {encrypted}")
print(f"Decrypted:       {decrypted}")


