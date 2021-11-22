import numpy as np
import cv2
import os
from Filters import *
from SaveFile import *

def printMenu():
    print ("1. Bilateral Filter")
    print ("2. Blur")
    print ("3. Median Blur")
    print ("4. Dilate")
    print ("5. Erode")
    print ("6. Laplacian")
    print ("7. Cartoon")
    print ("8. Negative")
    print ("9. HSV")
    print ("10. Grayscale")
    
def savePrompt(finalImage):
    moveOn = False
    while(moveOn == False):
        save = input("Would you like to save the image?(Y/N): ")
        if(save == 'Y'):
            folderPath = input("What folder would you like to save your image in?\n")
            fileName = input("What would you like to name the image: ")
            saveImage(folderPath, fileName, finalImage)
            moveOn = True
        elif(save == 'N'):
            print("Moving On")
            moveOn = True
        else:
            print("Please enter a valid input")
        
def closePrompt():
    moveOn = False
    while(moveOn == False):
        closeImage = input("Would you like to close image and Photo Filter?(Y):  ")
        if(closeImage == 'Y'):
            cv2.destroyAllWindows()
            loop = False
            moveOn = True
        elif(closeImage != 'Y'):
            print("Please enter a valid input")
    return loop


def photoFilter():
    
    print (20 * "-", "PHOTO FILTER", 20 * "-")
    
    
    image = input("Enter the file path of target image: ")
    while(os.path.exists(image) == False):
        print("Please insert a valid image path")
        image = input("Enter the file path of target image: ")
    
    
    loop = True
    while loop:
            
        printMenu()
        selection = input("Enter the filter of your choice: ")
        
        if(selection == '1'):
            print (20 * "-", "Bilateral Filter", 20 * "-")
            strength = int(input("How strong do you want the filter strength: "))
            finalImage = bilateralFilter(image, strength)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
            
        elif(selection == '2'):
            print (20 * "-", "Blur Filter", 20 * "-")
            strength = int(input("How strong do you want the filter strength: "))
            finalImage = blurFilter(image, strength)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
        elif(selection == '3'):
            print (20 * "-", "Median Blur Filter", 20 * "-")
            strength = int(input("How strong do you want the filter strength: "))
            finalImage = medianBlurFilter(image, strength)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
        elif(selection == '4'):
            print (20 * "-", "Dilate Filter", 20 * "-")
            strength = int(input("How strong do you want the filter strength: "))
            finalImage = dilateFilter(image, strength)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
        elif(selection == '5'):
            print (20 * "-", "Erode Filter", 20 * "-")
            strength = int(input("How strong do you want the filter strength: "))
            finalImage = erodeFilter(image, strength)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
        elif(selection == '6'):
            print (20 * "-", "Laplacian Filter", 20 * "-")
            strength = int(input("How strong do you want the filter strength: "))
            finalImage = laplacianFilter(image, strength)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
        elif(selection == '7'):
            print (20 * "-", "Cartoon Filter", 20 * "-")
            finalImage = cartoonFilter(image)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
        elif(selection == '8'):
            print (20 * "-", "Negative Filter", 20 * "-")
            finalImage = negativeFilter(image)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
        elif(selection == '9'):
            print (20 * "-", "HSV Filter", 20 * "-")
            finalImage = HSVFilter(image)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
        elif(selection == '10'):
            print (20 * "-", "Grayscale Filter", 20 * "-")
            finalImage = grayscaleFilter(image)
            cv2.startWindowThread()
            savePrompt(finalImage)
            loop = closePrompt()
        else:
            print("Please do a valid number")

