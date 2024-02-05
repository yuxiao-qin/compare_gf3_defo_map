from compare_gf3_defo_map.main import read_geotiff

# generate a unittest with pytest for main.py read_geotiff() function.
def test_read_geotiff():

    fref = "tests/data/20181001_20181031_20181001_20181031_01_01_01_01.tif"
    ref = read_geotiff(fref)
