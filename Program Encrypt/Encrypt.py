# import required module
from cryptography.fernet import Fernet

myFile1 = ['fileCipher']


def encrypt(file):
    # opening the key
    with open('../OUTS/' + file[0] + '.key', 'rb') as filekey:
        key = filekey.read()
        filekey.close()

    # using the generated key
    fernet = Fernet(key)

    # read the original file to encrypt
    with open('../' + file[1] + '.txt', 'rb') as file:
        original = file.read()
        file.close()

    # opening the file in write mode
    # fileCipher ########### ' + file[2] + ' - TypeError
    with open('../OUTS/fileCipher.txt', 'wb') as encrypted_file:
        try:
            # encrypting the file
            encrypted = fernet.encrypt(original)

            # writing the encrypted data
            encrypted_file.write(encrypted)
            encrypted_file.close()

        except Exception as err:
            print("Type error: {0}".format(err))
