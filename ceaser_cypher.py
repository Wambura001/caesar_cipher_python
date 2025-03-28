# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 09:18:07 2025

@author: USER
"""

class CaesarCipher: 
    '''
    class for doing encryption and decryption using a Caesar ciphrer
    '''
    def __init__(self, shift):
        '''
        Construct Caesar cipher using a given integer shift for rotation
        '''
        encoder = [None] * 26   #temp array for encryption 
        decoder = [None] * 26   #temp array for decryption
        
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)    #will store as string  
        self._backward = ''.join(decoder)    #since fixed
        
    def encrypt(self, message):
        '''
        Return string representing encrypted message
        '''
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        '''
        Return decrypted message given encrypted secret
        '''
        return self._transform(secret, self._forward)
    
    def _transform(self, original, code):
        '''
        Utility to perform transformation based on given code string
        '''
        msg = list(original)
        for k in range (len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')    #index from 0 to 25
                msg[k] = code[j]    #replace this character
        return ''.join(msg)
    
if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
    coded = cipher.encrypt(message)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print("Message: ", answer)
        