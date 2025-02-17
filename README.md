
# PRODIGY_CS_01

The Caesar cipher is a type of substitution cipher in which each letter in the plaintext is shifted by a fixed number of places in the alphabet. It is one of the simplest and oldest encryption techniques, named after Julius Caesar, who reportedly used it to communicate secretly
How It Works
Each letter in the original message (plaintext) is replaced by a letter some fixed number of positions (shift value) down the alphabet. If the shift reaches the end of the alphabet, it wraps around to the beginning.

For example, with a shift of 3:

'A' → 'D'
'B' → 'E'
'X' → 'A'
'Y' → 'B'
'Z' → 'C'
Encryption Formula:
E(x)=(x+n)mod26

mod26 ensures wrapping around the alphabet
Decryption Formula
D(x)=(x−n)mod26
The decryption reverses the shift by subtracting the key.
