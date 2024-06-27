#!/usr/bin/python3
"""Check if a list of integers represents a valid UTF-8 encoding."""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the most significant bits in a byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Get the 8 least significant bits of the integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                # 1-byte character
                continue

            if num_bytes == 1 or num_bytes > 4:
                # Invalid scenarios:
                # 1. Continuation byte without a leading byte
                # 2. More than 4 bytes character
                return False
        else:
            # Continuation byte must be 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
