import cv2
import numpy as np
import os

def image_to_cam(img_size, depth, K):
    '''
    this function projects the pixels in the image frame to 3D points in the camera coordinates

    args:
        img_size: (height,widith)
        depth: H x W
        K: intrinsic matrix, 3 x 3

    return:

    '''

    H = img_size[0]
    W = img_size[1]

    x = np.linspace(0, 1, W)
    y = np.linspace(0, 1, H)
    xv, yv = np.meshgrid(x, y)
    
    Qc = 
    