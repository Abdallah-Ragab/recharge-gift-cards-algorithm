from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad


class DESCipher:
    key = b"abdallah"

    @staticmethod
    def encrypt(message: bytes):

        cipher = DES.new(DESCipher.key, DES.MODE_ECB)
        padded_message = pad(message, DES.block_size)
        ciphertext = cipher.encrypt(padded_message)
        return ciphertext

    @staticmethod
    def decrypt(ciphertext: bytes):
        cipher = DES.new(DESCipher.key, DES.MODE_ECB)
        decoded_ciphertext = ciphertext
        decrypted_message = unpad(cipher.decrypt(decoded_ciphertext), DES.block_size)

        return decrypted_message
