import cv2
import numpy as np
import os

class dataloader():
    def __init__(self, root_dir='projection', src_name='IMG_0079', logo_name='Tencent', ext='.jpg'):
        self.root_dir = root_dir
        self.src_name = src_name
        self.logo_name = logo_name
        self.ext = ext

        self.get_path()
        self.load_images()
        self.load_params()

    def get_path(self):
        self.src_path = os.path.join(self.root_dir, self.src_name+self.ext)
        self.logo_path = os.path.join(self.root_dir, self.logo_name+self.ext)
        self.depth_path = os.path.join(self.root_dir, self.src_name+'depth.npy')
        self.seg_path = os.path.join(self.root_dir, self.src_name+'seg.npy')
        self.info_path = os.path.join(self.root_dir, self.src_name+'info.npy')
        self.para_path = os.path.join(self.root_dir, self.src_name+'params.npy')
        return 

    def load_images(self):
        self.src = cv2.imread(self.img_path)
        self.src = cv2.cvtColor(self.src,cv2.COLOR_BGR2GRAY)
        self.logo = cv2.imread(self.logo_path)
        self.logo = cv2.cvtColor(self.logo,cv2.COLOR_BGR2GRAY)
        self.depth = np.load(self.depth_path)
        self.seg = np.load(self.seg_path)

    def load_params(self):
        self.params = np.load(self.para_path)
        self.info = np.load(self.info_path)
