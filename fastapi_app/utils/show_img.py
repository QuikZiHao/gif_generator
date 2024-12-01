from PIL import Image
import cv2
import numpy as np

def show_image(img : np.ndarray):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img =  Image.fromarray(img)
    img.show()