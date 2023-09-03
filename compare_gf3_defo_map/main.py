def read_geotiff():
    """Read in geotiff file and return as numpy array"""
    return

def imshow_geotiff():
    """Plot geotiff file with matplotlib."""
    return


def compare_geotiff():
    """This is a ploting function to compare two geotiff files pixel by pixel. """
    return


if __name__ == '__main__':
    reference = read_geotiff()
    imshow_geotiff(reference)

    comparee = read_geotiff()
    imshow_geotiff(comparee)

    compare_geotiff()
