# import required module
from cryptography.fernet import Fernet


def decrypt(file):
    # opening the key
    with open('../OUTS/' + file[0] + '.key', 'rb') as filekey:
        key = filekey.read()
        filekey.close()

    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open('../OUTS/' + file[1] + '.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
        enc_file.close()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    # ' + file[2] + '
    with open('../OUTS/' + file[2] + '.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
        dec_file.close()
