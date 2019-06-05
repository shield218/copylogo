import numpy as np
import os
import cv2

def viualize_segmentaion(segmentation,image=None):
    colors = np.array([[255, 0, 0],
                       [0, 255, 0],
                       [0, 0, 255],
                       [80, 128, 255],
                       [255, 230, 180],
                       [255, 0, 255],
                       [0, 255, 255],
                       [100, 0, 0],
                       [0, 100, 0],
                       [255, 255, 0],
                       [50, 150, 0],
                       [200, 255, 255],
                       [255, 200, 255],
                       [128, 128, 80],
                       [0, 255, 128],
                       [0, 128, 255],
                       [255, 0, 128],
                       [128, 0, 255],
                       [255, 128, 0],
                       [128, 255, 0],
                       [0, 0, 0]
                       ])
    h,w=segmentation.shape[:2]
    pred_seg=np.zeros([h,w,3],np.uint8)
    for i in np.unique(segmentation):
        if i==10:
            continue
        pred_seg[segmentation==i]=colors[i]
    if image is not None:
        pred_seg=pred_seg.astype(np.float32)*0.5+image.astype(np.float32)*0.5
        pred_seg=pred_seg.astype(np.uint8)

    return pred_seg


def visualize_depth(depth):
    depth=depth-depth.min()
    depth=depth/depth.max()*255
    depth=depth.astype(np.uint8)

    return depth


