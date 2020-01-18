from pylab import *
import argparse
import time
import demosaic
import mosaic
import cv2
import numpy as np
import math

def psnr(img1, img2):
   mse = np.mean( (img1/255. - img2/255.) ** 2 )
   if mse < 1.0e-10:
      return 100
   PIXEL_MAX = 1
   return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default=r'./test.jpg', help='')
    parser.add_argument('--save_path', type=str, default=r'./mosaiced_image.jpg', help='')
    parser.add_argument('--result_path', type=str, default=r'./result.jpg', help='')
    parser.add_argument('--pattern', type=str, default='RGGB', help='')
    opt = parser.parse_args()
    time_start = time.time()
    bgr_image = cv2.imread(opt.input_path)
    mosaiced_image = mosaic.mosaicing(bgr_image,opt.pattern)
    cv2.imwrite(opt.save_path, mosaiced_image)
    result_image = demosaic.demosaicing_bilinear(mosaiced_image, opt.pattern)
    cv2.imwrite(opt.result_path, result_image)
    psnr = psnr(result_image, bgr_image)
    print("psnr:", psnr)
    time_end = time.time()
    print('totally cost', time_end - time_start)
    cv2.waitKey(0)