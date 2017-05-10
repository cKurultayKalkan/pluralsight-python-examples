""""A module for dealing with BMP bitmap image files"""

def write_grayscale(filename, pixels):
    """"Creates and writes a grayscale BMP file.

    Args:
        filename : The name of BMP file to be created

        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integers in the
            range 0-255.

    Raises:
        OSError: If the file couldn't be written
    """

    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        #BMP Header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()      # The next four btyes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for now

        bmp.write(b'\x00\x00')  # unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  # unused 16-bit integer - should be zero

        pixes_offset_bookmark = bmp.tell()      # The next four bytes hold the integer offset
        bmp.write(b'\x00\x00\x00\x00')          # to the pixel data. Zero placeholder for row.

        #Image Header
        bmp.write()

