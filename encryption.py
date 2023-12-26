from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad


class DESCipher:
    """
    This class provides methods for encrypting and decrypting messages using the DES cipher.
    """

    key = b"abdallah"

    @staticmethod
    def encrypt(message: bytes):
        """
        Encrypts the given message using the DES cipher.

        Args:
            message (bytes): The message to be encrypted.

        Returns:
            bytes: The encrypted ciphertext.
        """

        cipher = DES.new(DESCipher.key, DES.MODE_ECB)
        padded_message = pad(message, DES.block_size)
        ciphertext = cipher.encrypt(padded_message)
        return ciphertext

    @staticmethod
    def decrypt(ciphertext: bytes):
        """
        Decrypts the given ciphertext using the DES cipher.

        Args:
            ciphertext (bytes): The ciphertext to be decrypted.

        Returns:
            bytes: The decrypted message.
        """

        cipher = DES.new(DESCipher.key, DES.MODE_ECB)
        decoded_ciphertext = ciphertext
        decrypted_message = unpad(cipher.decrypt(decoded_ciphertext), DES.block_size)

        return decrypted_message
