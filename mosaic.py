import numpy as np
import label

def mosaicing(BGR, pattern='RGGB'):
    B, G, R = np.array([BGR[..., x] for x in range(BGR.shape[-1])])
    B_label, G_label, R_label = label.channels_label(BGR.shape[0:2], pattern)
    mosaiced_image =  B * B_label + G * G_label + R * R_label
    return mosaiced_image
