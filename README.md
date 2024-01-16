# Caesar Cipher Encryption and Decryption

This Python script implements a simple Caesar cipher algorithm to encrypt and decrypt messages. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Script Details

### Encryption Function

The `encrypt` function takes a message and a key as parameters, shifting each character in the message by the key value to create an encrypted message.

### Decryption Function

The `decrypt` function reverses the encryption process. It takes an encrypted message and a key as parameters, shifting each character back by the key value to retrieve the original message.

### Usage

The script is pre-set with an example message ("HelloWorld") and a key (10). When run, it encrypts the message, then decrypts it, printing both the encrypted and decrypted versions.
