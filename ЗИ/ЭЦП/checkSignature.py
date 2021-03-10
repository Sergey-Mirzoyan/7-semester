import hashlib
import rsa

def getHashFile(filename):
    _hash = hashlib.sha256()
    with open(filename, "rb") as f:
        data = f.read()
        _hash.update(data)
    return _hash.digest()


def checkSignature(fileToCheck, signatureFile, publicKey):
    _hash = getHashFile(fileToCheck)

    with open(signatureFile, "rb") as f:
        signature = f.read()
    try:
        _hashMessage = rsa.decrypt(signature, publicKey)
    except rsa.pkcs1.DecryptionError:
        return False
    return (_hash == _hashMessage)


if __name__ == "__main__":
    fileToCheck = 'hello.txt'
    signatureFile = 'signature'
    with open('private.pem', "rb") as k:
        keyData = k.read()
    publicKey = rsa.PrivateKey.load_pkcs1(keyData, format='PEM')

    with open('signature', "rb") as s:
        signature = s.read()

    isValid = checkSignature(fileToCheck, signatureFile, publicKey)

    if isValid:
        print("Электронная подпись корректна.")
    else:
        print("Электронная подпись некорректна.")

