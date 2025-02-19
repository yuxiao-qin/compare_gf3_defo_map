import rasterio
import numpy as np
import matplotlib.pyplot as plt


def read_geotiff(fgeotiff):
    """Read in geotiff file and return as numpy array"""

    with rasterio.open(fgeotiff) as src:
        w = src.read()

    return w

def imshow_geotiff(w, vlim=0.02):
    """Plot geotiff file with matplotlib."""

    # replace large numbers to NaN for plotting purpose
    w[w > 10000] = np.nan

    # invert colormap and set a specific dpi
    plt.rcParams['figure.dpi'] = 120
    plt.imshow(w[0], cmap="jet_r", vmin=-1*vlim, vmax=vlim)
    plt.colorbar()

def compare_geotiff(referece, comparate):
    """This is a ploting function to compare two geotiff files pixel by pixel. """
    flattened_ref = referece.flatten()
    flattened_comp = comparate.flatten()

    # remove large values
    flattened_ref[flattened_ref > 10000] = np.nan
    flattened_comp[flattened_comp > 10000] = np.nan

    # only compare pixels where both have a valid value
    flattened_ref[np.isnan(flattened_comp)] = np.nan
    flattened_comp[np.isnan(flattened_ref)] = np.nan

    # remove nans and save to a new array
    ref_mask = np.isnan(flattened_ref)
    ref_without_nans = flattened_ref[~ref_mask]
    comp_mask = np.isnan(flattened_comp)
    comp_without_nans = flattened_comp[~comp_mask]
    assert ref_without_nans.shape == comp_without_nans.shape

    return ref_without_nans, comp_without_nans

def plot_compare_geotiff(reference, comparate):

    # do a scatter plot for 2 numpy arrays: reference & comparate. reference is the x axis and comparate is the y axis.
    plt.rcParams['figure.dpi'] = 150
    plt.scatter(reference, comparate, s=0.1)

    return


if __name__ == '__main__':
    reference = read_geotiff()
    imshow_geotiff(reference)

    comparate = read_geotiff()
    imshow_geotiff(comparate)

    compare_geotiff()
