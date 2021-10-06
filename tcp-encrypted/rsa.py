from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def newkeys(size):
    key = RSA.generate(size)

    public_key = key.publickey().exportKey('PEM')
    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)

    private_key = key.export_key('PEM')
    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)

    return (rsa_public_key, rsa_private_key)

def encrypt(message, rsa_public_key):
    return rsa_public_key.encrypt(message.encode())

def decrypt(encrypted_text, rsa_private_key):
    return rsa_private_key.decrypt(encrypted_text)
