import sys, string

def generateKey(plaintext, key):
   """
   Generate a key as long as the plaintext
   :param plaintext:
   :param key:
   """
   while len(key) < len(plaintext):
      key *= 2
   
   while len(key) > len(plaintext):
      key = key[:-1]
   
   return key

def rotateLeft(array, k):
   """
   Rotate a list to the left
   :param k:
   """
   return array[abs(k):] + array[:abs(k)]
   
def rotateRight(array, k):
   """
   Rotate a list to the right
   :param k:
   """
   return array[-abs(k):] + array[:-abs(k)]

def vigenereEncrypt(text, key):
   """
   Encrypt a string using the Vigenere cipher
   :param text:
   :param key:
   """
   alphabet = string.ascii_lowercase
   ciphertext = str()
   for i in range(0, len(text)):
      if text[i].lower() in alphabet:
         cipher_alphabet = rotateLeft(alphabet, alphabet.index(key[i].lower()))
         ciphertext += cipher_alphabet[alphabet.index(text[i].lower())] if text[i].islower() else cipher_alphabet[alphabet.index(text[i].lower())].upper()
      else: ciphertext += text[i]
   
   return ciphertext

def vigenereDecrypt(cipher_text, key):
   """
   Decrypt a string using the Vigenere cipher
   :param cipher_text:
   :param key:
   """
   alphabet = string.ascii_lowercase
   plaintext = str()
   for i in range(0, len(cipher_text)):
      if cipher_text[i].lower() in alphabet:
         decipher_alphabet = rotateRight(alphabet, alphabet.index(key[i].lower()))
         plaintext += decipher_alphabet[alphabet.index(cipher_text[i].lower())] if cipher_text[i].islower() else decipher_alphabet[alphabet.index(cipher_text[i].lower())].upper()
      else: plaintext += cipher_text[i]
   
   return plaintext