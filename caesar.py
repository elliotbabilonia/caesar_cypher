# Importing the sys module for handling command-line arguments
import sys  

# Defining a function to encrypt a message with a given key
def encrypt(message, k):
    # Initializing an empty string to store the encrypted message
    encrypted = ""  
    # Iterating through each character in the message
    for char in message:
        # Adding the character shifted by the key to the encrypted message
        encrypted += chr(ord(char) + k)  
    # Returning the final encrypted message
    return encrypted  

# Defining a function to decrypt a message with a given key
def decrypt(message, k):
    # Initializing an empty string to store the decrypted message
    decrypted = ""  
    # Iterating through each character in the message
    for char in message:
        # Subtracting the key from the character to decrypt and adding to the decrypted message
        decrypted += chr(ord(char) - k)  
    # Returning the final decrypted message
    return decrypted  

# Checking if this script is the main module
if __name__ == "__main__":
    # Setting the message and key manually to be encrypted
    message = "HelloWorld"
    key = 10

    # Encrypting the message
    encrypted = encrypt(message, key)

    # Decrypting the encrypted message
    decrypted = decrypt(encrypted, key)

    # Printing the results
    print("Your encrypted word is:", encrypted)
    print("Your decrypted word is:", decrypted)