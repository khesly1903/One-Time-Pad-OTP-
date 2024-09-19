# One-Time-Pad-OTP-
This repository contains a Python implementation of the One-Time Pad (OTP) encryption algorithm. OTP is a theoretically unbreakable encryption method, where the key is as long as the message and used only once.

Usage:
1) Generate a random key for your message.
2) Encrypt your message using the XOR operation.
3) Decrypt the encrypted message using the same key.

Notes:
Ensure the key is kept secure and only used once, as this is essential to the security of the OTP method.
The key length must match the length of the message.

Example:
Message: Cryptography
Binary message:  010000110111001001111001011100000111010001101111011001110111001001100001011100000110100001111001
Key:             110110110101101100111110110010100010010100101011001100110110110111101111001101000111101101100001
Encrypted:       100110000010100101000111101110100101000101000100010101000001111110001110010001000001001100011000
Decrypted:       Cryptography
