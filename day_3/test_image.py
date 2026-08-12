import astropy
from astropy.io import fits
import numpy as np
from astropy.wcs import WCS
import matplotlib.pyplot as plt
# Load the FITS file
fits_file = fits.open("hst_11137_01_wfpc2_total_wf_drz.fits")
print(fits_file.info())
# Extract the image data and header
image_data = fits_file[1].data
header = fits_file[1].header
print(fits_file[0].data)
# Create a figure with WCS projection
wcs = WCS(header)
print(header)
print(wcs)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection=wcs)
# Plot the image
ax.imshow(image_data,origin="lower",cmap="cividis",vmin=np.percentile(image_data, 1), vmax=np.percentile(image_data, 99))
ax.set_xlabel('Right Ascension')
ax.set_ylabel('Declination')
plt.title('Hubble Space Telescope Image')
plt.colorbar(ax.images[0], ax=ax, label='Intensity')
plt.savefig("hst_image.png", dpi=300,bbox_inches='tight')
fits_file.close()