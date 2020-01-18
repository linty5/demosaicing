import numpy as np
import scipy.ndimage
import label

def demosaicing_bilinear(mosaiced_image, pattern='RGGB'):
    mosaiced_image = np.asarray(mosaiced_image, np.float_)
    B_label, G_label, R_label = label.channels_label(mosaiced_image.shape, pattern)
    H_G = ([[0, 1/4, 0],
           [1/4, 1, 1/4],
           [0, 1/4, 0]])
    H_BR = ([[1/4, 1/2, 1/4],
            [1/2, 1, 1/2],
            [1/4, 1/2, 1/4]])
    B = scipy.ndimage.convolve(mosaiced_image * B_label, H_BR)
    G = scipy.ndimage.convolve(mosaiced_image * G_label, H_G)
    R = scipy.ndimage.convolve(mosaiced_image * R_label, H_BR)
    return np.dstack([B, G, R])


