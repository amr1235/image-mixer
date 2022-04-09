from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore
from numpy.fft import fft2, ifft2, fftshift
from numpy import abs
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import logging

logger = logging.getLogger('Show Images Component') 

class DisplayImgComp():
    def __init__(self):
        #resize method 
        self.resizeMethod = None
        # path of img1
        path1 = os.path.realpath('images/test1.jpg')
        # path of img2
        path2 = os.path.realpath('images/test2.jpg')
        # path of img1 component
        path3 = os.path.realpath('images/img1comp.png')
        # path of img1 component
        path4 = os.path.realpath('images/img2comp.png')

        self.paths = [path1,path2,path3,path4] 
        image_arr1=mpimg.imread(path1)
        image_arr2=mpimg.imread(path2)
        self.img_arrays = [image_arr1,image_arr2]
    
#########################################
# After creating the omg component, you will pass the path of imgs to UI.py
# what you craete inside UI.py(create img1 and 2) will be global for all
# the other labels
# this file will be imported in UI.py


    def get_img_magnitude(self, img_number=1):
        # get arrays of images
        image_arr = self.img_arrays[img_number - 1]
        complex_arr = fft2(image_arr)
        #shift the signal to origin
        shifted_complex = fftshift(complex_arr)
        magnitude = np.abs(shifted_complex)
        plt.imshow(magnitude)
        plt.axis('off')
        plt.savefig(self.paths[img_number + 1],bbox_inches='tight')

    def get_img_reals(self, img_number=1):
        # get arrays of images
        image_arr = self.img_arrays[img_number - 1]
        complex_arr = fft2(image_arr)
        shifted_complex = fftshift(complex_arr)
        reals = np.real(shifted_complex)
        plt.imshow(reals)
        plt.axis('off')
        plt.savefig(self.paths[img_number + 1],bbox_inches='tight')

    def get_img_imgnary(self, img_number=1):
        # get arrays of images
        image_arr = self.img_arrays[img_number - 1]
        complex_arr = fft2(image_arr)
        shifted_complex = fftshift(complex_arr)
        shifted_complex = np.imag(shifted_complex)
        plt.imshow(shifted_complex)
        plt.axis('off')
        plt.savefig(self.paths[img_number + 1],bbox_inches='tight')

    def get_img_phase(self, img_number=1):
        # get an array of image
        image_arr = self.img_arrays[img_number - 1]
        complex_arr = fft2(image_arr)
        shifted_complex = fftshift(complex_arr)
        # get phase component
        phase_spectrumA = np.angle(shifted_complex)
        plt.imshow(phase_spectrumA)
        plt.axis('off')
        plt.savefig(self.paths[img_number + 1],bbox_inches='tight')



