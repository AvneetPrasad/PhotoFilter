import numpy as np
import cv2
import os
import matplotlib.image as img
from matplotlib import pyplot as plt

def bilateralFilter(image, strength):
    img1 = cv2.imread(image)
    size= 100
    w = int(img1.shape[1]*size/100)
    h = int(img1.shape[0]*size/100)
    dim = (w,h)
            
    #filtering
    for _ in  range(3):
        img1 = cv2.bilateralFilter(img1,15,strength,strength)
        
    finalImage = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Bilateral Filtered Image", finalImage)
    return finalImage
    
def blurFilter(image, strength):
    img1 = cv2.imread(image)
    size= 100
    w = int(img1.shape[1]*size/100)
    h = int(img1.shape[0]*size/100)
    dim = (w,h)
            
    #filtering
    img1 = cv2.blur(img1, (strength,strength))
        
    finalImage = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("BlurFiltered Image", finalImage)
    return finalImage

def medianBlurFilter(image, strength):
    img1 = cv2.imread(image)
    size= 100
    w = int(img1.shape[1]*size/100)
    h = int(img1.shape[0]*size/100)
    dim = (w,h)
            
    if ((strength%2)==0):
        strength = strength+1
        
        
    #filtering
    img1 = cv2.medianBlur(img1, strength)
        
    finalImage = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("BlurFiltered Image", finalImage)
    return finalImage

def dilateFilter(image, strength):
    img1 = cv2.imread(image)
    size= 100
    w = int(img1.shape[1]*size/100)
    h = int(img1.shape[0]*size/100)
    dim = (w,h)
            
    kernel = np.ones((strength, strength), np.uint8)
            
    #filtering
    img1 = cv2.dilate(img1,kernel, 1)
        
    finalImage = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Dilate Filtered Image", finalImage)
    return finalImage

def erodeFilter(image, strength):
    img1 = cv2.imread(image)
    size= 100
    w = int(img1.shape[1]*size/100)
    h = int(img1.shape[0]*size/100)
    dim = (w,h)
            
    kernel = np.ones((strength, strength), np.uint8)
            
    #filtering
    img1 = cv2.erode(img1,kernel, 1)
        
    finalImage = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Erode Filtered Image", finalImage)
    return finalImage

def laplacianFilter(image, strength):
    img1 = cv2.imread(image)
    size= 100
    w = int(img1.shape[1]*size/100)
    h = int(img1.shape[0]*size/100)
    dim = (w,h)
            
    if ((strength%2)==0):
        strength = strength+1
        
    blur = cv2.GaussianBlur(img1,(strength,strength),0)
    #filtering
    img1 = cv2.Laplacian(blur, cv2.CV_64F)
        
    finalImage = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("BlurFiltered Image", finalImage)
    return finalImage

def cartoonFilter(image):
    img = cv2.imread(image)
    
    size= 100
    w = int(img.shape[1]*size/100)
    h = int(img.shape[0]*size/100)
    dim = (w,h)
    
    line_size = 7
    blur_value = 9
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
    
    filename = 'edges.jpg'
    cv2.imwrite(filename, edges)
    
    strength = 25
    for _ in  range(3):
        img = cv2.bilateralFilter(img,15,strength,strength)

    cv2.imwrite('painted.jpg', img)

    cartoon = cv2.bitwise_and(img, img, mask=edges)
    
    finalImage = cv2.resize(cartoon, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow('Cartoon Filtered Image', cartoon)
    
    os.remove("painted.jpg")
    os.remove("edges.jpg")
    
    return finalImage

def negativeFilter(image):
    img = cv2.imread(image)
    size= 100
    w = int(img.shape[1]*size/100)
    h = int(img.shape[0]*size/100)
    dim = (w,h)
    
    inverted = cv2.bitwise_not(img)
    
    finalImage = cv2.resize(inverted, dim, interpolation = cv2.INTER_AREA)
    
    cv2.imshow("Invert Filtered Image", finalImage)
    return finalImage
    
def HSVFilter(image):
    img = cv2.imread(image)
    size= 100
    w = int(img.shape[1]*size/100)
    h = int(img.shape[0]*size/100)
    dim = (w,h)
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    finalImage = cv2.resize(hsv, dim, interpolation = cv2.INTER_AREA)
    
    cv2.imshow("HSV Filtered Image", finalImage)
    return finalImage

def grayscaleFilter(image):
    img = cv2.imread(image)
    size= 100
    w = int(img.shape[1]*size/100)
    h = int(img.shape[0]*size/100)
    dim = (w,h)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    finalImage = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
    
    cv2.imshow("Grayscale Filtered Image", finalImage)
    return finalImage