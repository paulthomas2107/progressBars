import rsa

""" 
# Generate key pair
public_key, private_key = rsa.newkeys(1024)

with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))
"""

# Use key pair to encrypt / decrypt
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = 'Caitlin & Rory Thomas'
encryptedMessage = rsa.encrypt(message.encode(), public_key)

print(message)
print(encryptedMessage)

with open("encryptedMessage", "wb") as f:
    f.write(encryptedMessage)

encryptedMessage = open('encryptedMessage', 'rb').read()
print(encryptedMessage)

unencryptedMessage = rsa.decrypt(encryptedMessage, private_key)
print(unencryptedMessage.decode())

# Sign a message with private key
message = "This is an important message about MOD !!!"
signature = rsa.sign(message.encode(), private_key, "SHA-256")
# Write signature
""" 
with open("signature", "wb") as f:
    f.write(signature)
"""
# read signature and verify
with open("signature", "rb") as f:
    signature = f.read()
# Verified
print(rsa.verify(message.encode(), signature, public_key))
