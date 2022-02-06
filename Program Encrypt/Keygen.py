# import required module
from cryptography.fernet import Fernet


def keygen(file):
    # key generation
    key = Fernet.generate_key()

    # string the key in a file
    with open('../OUTS/' + file[0] + '.key', 'wb') as filekey:
        filekey.write(key)
        filekey.close()


