import hashlib
import rsa

def writeKeys(public, private):
    with open('public.pem', "wb") as pub:
        pub.write(public.save_pkcs1('PEM'))

    with open('private.pem', "wb") as pub:
        pub.write(private.save_pkcs1('PEM'))

def getHashFile(filename):
    _hash = hashlib.sha256()
    with open(filename, "rb") as f:
        data = f.read()
        _hash.update(data)
    return _hash.digest()


def createSignature(fileToSign, privateKey):
    _hash = getHashFile(fileToSign) # Считаем хэш файла
    signature = rsa.encrypt(_hash, privateKey)
    with open("signature", "wb") as f:
        f.write(signature)
    
    return signature

if __name__ == "__main__":
    print("Создание публичного и приватного ключей...")
    (publicKey, privateKey) = rsa.newkeys(1024)
    writeKeys(publicKey, privateKey)
    print("Ключи созданы и записаны в файл.")
    fileToSign = 'hello.txt'
    signature = createSignature(fileToSign, privateKey)

    with open('signature', "wb") as pub:
        pub.write(signature)
    
    print("Электронная подпись успешно создана.")