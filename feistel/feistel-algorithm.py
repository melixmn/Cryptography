def F_function(part, key):
    return (part ^ key) % 256

def feistel_encrypt(plain_text, key, rounds=4):
    left = (plain_text >> 4) & 0x0F  
    right = plain_text & 0x0F        

   
    subkeys = [(key + i) & 0xFF for i in range(rounds)]

    for i in range(rounds):
        new_left = right
        right = left ^ F_function(right, subkeys[i])
        left = new_left

    
    cipher_text = (left << 4) | right
    return cipher_text

def feistel_decrypt(cipher_text, key, rounds=4):
    left = (cipher_text >> 4) & 0x0F
    right = cipher_text & 0x0F

    subkeys = [(key + i) & 0xFF for i in range(rounds)]

    for i in reversed(range(rounds)):
        new_right = left
        left = right ^ F_function(left, subkeys[i])
        right = new_right

    plain_text = (left << 4) | right
    return plain_text


key = 0x0F  
plain_text = 0xAB  

cipher = feistel_encrypt(plain_text, key, rounds=4)
print(f"Cipher Text: {hex(cipher)}")

decrypted = feistel_decrypt(cipher, key, rounds=4)
print(f"Decrypted Text: {hex(decrypted)}")
