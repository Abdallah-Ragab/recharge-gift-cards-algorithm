from storage import BitStorage
from encryption import DESCipher


class Card:
    """
    A class representing a recharge card.

    Attributes:
        max_value (int): The maximum value that a recharge card can have.

    Methods:
        generate_card_number(value: int, serial: int = None) -> int:
            Generates a unique card number based on the given serial and value.

        validate_card_number(card_number: int) -> None:
            Validates the format of a card number.

        validate_card_value(card_value: int) -> None:
            Validates the value of a card.

        retrieve_card_info(card_number: int) -> Tuple[int, int]:
            Retrieves the serial and value of a card based on the card number.

        check_redemption(card_number: int) -> bool:
            Checks if a card has been redeemed.

        check_value(card_number: int) -> int:
            Retrieves the value of a card.

        redeem_card(card_number: int) -> int:
            Redeems a card and updates its redemption status.
    """

    max_value = 999

    @staticmethod
    def generate_card_number(value: int, serial: int = None) -> int:
        """
        Generates a card number based on the given value and serial number.

        Args:
            value (int): The value of the card.
            serial (int, optional): The serial number of the card. If not provided, it will be automatically generated.

        Returns:
            int: The generated card number.

        Raises:
            ValueError: If the value is too large.

        """
        if value > Card.max_value:
            raise ValueError("Value is too large")

        if not serial:
            serial = Card.last_card_serial + 1
            Card.last_card_serial = serial

        card_value = value
        card_serial = serial

        card_serial_str = str(card_serial).zfill(10)
        card_value_str = str(card_value).zfill(3)

        card_int = int(card_serial_str + card_value_str)
        card_bytes = card_int.to_bytes(
            (card_int.bit_length() + 7) // 8, byteorder="big"
        )

        card_number_bytes = DESCipher.encrypt(card_bytes)
        card_number_int = int.from_bytes(card_number_bytes, byteorder="big")

        return card_number_int

    @staticmethod
    def validate_card_number(card_number: int) -> None:
        """
        Validates the format of a card number.

        Args:
            card_number (int): The card number to validate.

        Raises:
            ValueError: If the card number has an invalid number of digits.
        """
        num_of_digits = len(str(card_number))
        if num_of_digits not in [18, 19, 20]:
            raise ValueError("Invalid Card Number")

    @staticmethod
    def validate_card_value(card_value: int) -> None:
        """
        Validates the value of a card.

        Args:
            card_value (int): The card value to validate.

        Raises:
            ValueError: If the card value is invalid (greater than the maximum allowed value or less than 0).
        """
        if card_value > Card.max_value or card_value < 0:
            raise ValueError("Invalid Card Value: Card value must not be more than 999 and greater than 0")

    @staticmethod
    def retrieve_card_info(card_number: int):
        """
        Retrieves the serial and value of a card based on the card number.

        Args:
            card_number (int): The card number to retrieve information for.

        Returns:
            Tuple[int, int]: A tuple containing the serial and value of the card.
        """
        card_number_bytes = card_number.to_bytes(
            (card_number.bit_length() + 7) // 8, byteorder="big"
        )

        decrypted_bytes = DESCipher.decrypt(card_number_bytes)
        card_int = int.from_bytes(decrypted_bytes, byteorder="big")

        card_serial_str = str(card_int)[:-3]
        card_value_str = str(card_int)[-3:]

        card_serial = int(card_serial_str)
        card_value = int(card_value_str)

        return card_serial, card_value

    @staticmethod
    def check_redemption(card_number: int) -> bool:
        """
        Checks if a card has been redeemed.

        Args:
            card_number (int): The card number to check redemption for.

        Returns:
            bool: True if the card has been redeemed, False otherwise.
        """
        card_serial, card_value = Card.retrieve_card_info(card_number)
        bit_value = BitStorage.read_bit(card_serial)
        if bit_value == 1:
            return True
        else:
            return False

    @staticmethod
    def check_value(card_number: int) -> int:
        """
        Retrieves the value of a card.

        Args:
            card_number (int): The card number to retrieve the value for.

        Returns:
            int: The value of the card.
        """
        card_serial, card_value = Card.retrieve_card_info(card_number)
        return card_value

    @staticmethod
    def redeem_card(card_number: int) -> int:
        """
        Redeems a card and updates its redemption status.

        Args:
            card_number (int): The card number to redeem.

        Returns:
            int: The value of the redeemed card.
        """
        card_serial, card_value = Card.retrieve_card_info(card_number)
        BitStorage.write_bit(card_serial, 1)
        return card_value
    @staticmethod
    @property
    def last_card_serial():
        """
        Retrieves the last card serial number.

        Returns:
            int: The last card serial number.
        """
        return BitStorage.read_from_file('last.serial')

    @staticmethod
    @last_card_serial.setter
    def last_card_serial(value: int):
        """
        Sets the last card serial number.

        Args:
            value (int): The value to set the last card serial number to.
        """
        BitStorage.write_to_file('last.serial', value)

def test():
    card_number = Card.generate_card_number(1234567890, 100)
    print(card_number)
    card_serial, card_value = Card.retrieve_card_info(card_number)
    print(card_serial, card_value)
    print(Card.check_redemption(card_number))
    print(Card.redeem_card(card_number))
    print(Card.check_redemption(card_number))


if __name__ == "__main__":
    test()
