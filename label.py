from pylab import *
import numpy as np

def channels_label(shape, pattern='RGGB'):
    channels = dict((channel, np.zeros(shape)) for channel in 'BGR')
    for channel, (y, x) in zip(pattern, [(0, 0), (0, 1), (1, 0), (1, 1)]):
        channels[channel][y::2, x::2] = 1
    return tuple(channels[c].astype(bool) for c in 'BGR' )