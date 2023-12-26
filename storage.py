import os
import struct


class BitStorage:
    """
    A class that provides methods for reading and writing individual bits to files.

    Attributes:
        directory (str): The directory where the files are stored.
        num_files (int): The number of files to be used for storage.
        max_bit (int): The maximum bit value that can be stored.
        max_bits_per_file (int): The maximum number of bits that can be stored in each file.
    """

    directory = "storage"
    num_files = 100
    max_bit = 9_999_999_999
    max_bits_per_file = max_bit // num_files

    def get_file_name(bit_index):
        """
        Get the name of the file corresponding to the given bit index.

        Args:
            bit_index (int): The index of the bit.

        Returns:
            str: The name of the file.
        """
        file_index = bit_index // BitStorage.max_bits_per_file
        file_index_str = str(file_index).zfill(len(str(BitStorage.num_files)))
        return f"cards.{file_index_str}"

    def get_file_path(bit_index):
        """
        Get the file path corresponding to the given bit index.

        Args:
            bit_index (int): The index of the bit.

        Returns:
            str: The file path.
        """
        return os.path.join(BitStorage.directory, BitStorage.get_file_name(bit_index))

    def create_file_if_not_exists(file_path):
        """
        Create the file if it does not exist.

        Args:
            file_path (str): The path of the file.
        """
        if not os.path.exists(BitStorage.directory):
            os.makedirs(BitStorage.directory)

        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass

    def get_bit_index(bit_index):
        """
        Get the index of the bit within the file.

        Args:
            bit_index (int): The index of the bit.

        Returns:
            int: The index of the bit within the file.
        """
        return bit_index % BitStorage.max_bits_per_file

    def get_byte_and_offset(bit_index):
        """
        Get the byte index and bit offset within the byte for the given bit index.

        Args:
            bit_index (int): The index of the bit.

        Returns:
            tuple: A tuple containing the byte index and bit offset.
        """
        bit_index = BitStorage.get_bit_index(bit_index)
        return divmod(bit_index, 8)

    @staticmethod
    def write_bit(bit_index, bit_value):
        """
        Write the given bit value to the specified bit index.

        Args:
            bit_index (int): The index of the bit.
            bit_value (int): The value of the bit (0 or 1).
        """
        file_path = BitStorage.get_file_path(bit_index)
        BitStorage.create_file_if_not_exists(file_path)
        byte_index, offset = BitStorage.get_byte_and_offset(bit_index)

        with open(file_path, "rb+") as file:
            file.seek(byte_index)

            try:
                byte = struct.unpack("B", file.read(1))[0]
            except struct.error:
                byte = 0

            if bit_value == 1:
                byte |= 1 << offset
            else:
                byte &= ~(1 << offset)

            file.seek(byte_index)
            file.write(struct.pack("B", byte))

    @staticmethod
    def read_bit(bit_index):
        """
        Read the bit value at the specified bit index.

        Args:
            bit_index (int): The index of the bit.

        Returns:
            int: The value of the bit (0 or 1).
        """
        file_path = BitStorage.get_file_path(bit_index)
        BitStorage.create_file_if_not_exists(file_path)
        byte_index, offset = BitStorage.get_byte_and_offset(bit_index)

        with open(file_path, "rb") as file:
            file.seek(byte_index)

            try:
                byte = struct.unpack("B", file.read(1))[0]
            except struct.error:
                byte = 0

        return (byte >> offset) & 1

    def write_to_file(file_path, value):
        BitStorage.create_file_if_not_exists(file_path)
        file_path = os.path.join(BitStorage.directory, file_path)

        byte_value = bytes(value, "utf-8")
        with open(file_path, "wb") as file:
            file.write(byte_value)

    def read_from_file(file_path):
        BitStorage.create_file_if_not_exists(file_path)
        file_path = os.path.join(BitStorage.directory, file_path)

        with open(file_path, "rb") as file:
            try:
                byte_value = file.read()
                value = byte_value.decode("utf-8")
            except struct.error:
                value = None
        return value