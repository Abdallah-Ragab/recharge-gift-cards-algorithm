import os
import struct


class BitStorage:
    file_path = "cards.bin"

    def create_file_if_not_exists():
        if not os.path.exists(BitStorage.file_path):
            with open(BitStorage.file_path, 'w'):
                pass
    @staticmethod
    def write_bit(bit_index, bit_value):
        BitStorage.create_file_if_not_exists()
        byte_index, offset = divmod(bit_index, 8)

        with open(BitStorage.file_path, 'rb+') as file:
            file.seek(byte_index)

            try:
                byte = struct.unpack('B', file.read(1))[0]
            except struct.error:
                byte = 0

            if bit_value == 1:
                byte |= (1 << offset)
            else:
                byte &= ~(1 << offset)

            file.seek(byte_index)
            file.write(struct.pack('B', byte))

    @staticmethod
    def read_bit(bit_index):
        BitStorage.create_file_if_not_exists()
        byte_index, offset = divmod(bit_index, 8)

        with open(BitStorage.file_path, 'rb') as file:
            file.seek(byte_index)

            try:
                byte = struct.unpack('B', file.read(1))[0]
            except struct.error:
                byte = 0

        return (byte >> offset) & 1
