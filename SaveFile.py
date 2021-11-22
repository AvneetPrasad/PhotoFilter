import cv2

def saveImage(location, fileName, image):
    if (location[-1] != "/"):
        location = location + "/"
    locationAndFileName = location + fileName + ".jpg"
    status = cv2.imwrite(locationAndFileName, image)
    print("Image "+fileName+" saved to "+location+": "+str(status))