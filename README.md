# pip-encryption-module
Python pip package to encrypt and decrypt data in BW Cloud


**Needs to be public bc the other packages download this!**

## install

`pip3 install git+https://github.com/BuchingerWilhelmiApp/pip-encryption-module`
## usage

needs 2 environment variables:

- SALT
- ENCRYPTION_KEY

```
from bwcrypt.bwcrypt import encrypt,decrypt

encryptedString = encrypt("Peter Pan")
print(encryptedString)

normalString = decrypt(encryptedString)
print(normalString == "Peter Pan")

```




