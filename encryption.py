from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad


class DESCipher:
    key = b"abdallah"

    @staticmethod
    def encrypt(message: bytes):
        byte_representation = message.to_bytes((message.bit_length() + 7) // 8, byteorder='big')

        cipher = DES.new(DESCipher.key, DES.MODE_ECB)
        padded_message = pad(byte_representation, DES.block_size)
        ciphertext = cipher.encrypt(padded_message)
        return ciphertext

    @staticmethod
    def decrypt(ciphertext: bytes):
        cipher = DES.new(DESCipher.key, DES.MODE_ECB)
        decoded_ciphertext = ciphertext
        decrypted_message = unpad(cipher.decrypt(decoded_ciphertext), DES.block_size)

        return decrypted_message
