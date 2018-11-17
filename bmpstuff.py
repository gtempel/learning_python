'''
Module for dealing with BMP bitmap image files
'''


def dimensions(filename):
    '''
    Read the dimensions (in pixels) of a given BMP image.

    Args:
      filename: the filename of the BMP image to read.

    Returns:
      A tuple containing two integers, the width and
      the height, in pixels.

    Raises:
      ValueError: if the file wasn't a BMP file
      OSError: If there was a problem reading the file
    '''
    with open(filename, 'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))

        f.seek(18)  # jump to the dimension data
        width_bytes = f.read(4)
        height_bytes = f.read(4)

        return (_bytes_to_int32(width_bytes), _bytes_to_int32(height_bytes))


def write_grayscale(filename, pixels):
    '''
    Creates and writes a greyscale BMP file.

    Args:
      filename: the name of the BMP file to be created.

      pixels: a rectangular image stored as a sequence of
        rows. Each row must be an iterable series of integers
        in the range 0-255.

    Raises:
      OSError: if the file couldn't be written.
    '''
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, mode='wb') as bmp:
        # bmp header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()  # bookmark where we are in the file as a 32bit
        # little-endian int, zero placeholder for now
        bmp.write(b'\x00\x00\x00\x00')

        # unused 16 bit integers that should be zero
        bmp.write(b'\x00\x00')
        bmp.write(b'\x00\x00')

        pixel_offset_bookmark = bmp.tell()  # integer offset to the data; zero for now
        bmp.write(b'\x00\x00\x00\x00')

        # image header
        # image header size, in bytes (40 decimal)
        bmp.write(b'\x28\x00\x00\x00')
        bmp.write(_int32_to_bytes(width))
        bmp.write(_int32_to_bytes(height))
        bmp.write(b'\x01\x00')  # number of image planes
        bmp.write(b'\x08\x00')  # bits per pixel (8 for greyscale)
        bmp.write(b'\x00\x00\x00\x00')  # no compression
        bmp.write(b'\x00\x00\x00\x00')  # zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')  # unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # use whole color table
        bmp.write(b'\x00\x00\x00\x00')  # all colors are important

        # color palette -- a linear greyscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))  # blue green red zero

        # pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):  # bmp files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)
            # pad row to multiple of 4 bytes
            # Pad row to multiple of four bytes
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4)
            bmp.write(padding)

        # end of file
        eof_bookmark = bmp.tell()

        # fill in the placeholders from earlier
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # fill in the pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    '''Convert an integer to four bytes in little-endian format.'''
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


def _bytes_to_int32(b):
    '''Convert a group of 4 bytes (little-endian) to a 32bit int'''
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)
