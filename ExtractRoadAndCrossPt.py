import cv2
import sys

def ExtractRoadAndCrossPt():

    img1 = cv2.imread("test5b.bmp")
    
    out_img = cv2.imread("blank2.jpg")
    
    height, width, channel = img1.shape
    
    out_img = cv2.resize(out_img, (width, height))
    
    print(img1.shape)
    print(out_img.shape)
    
    for y in range(height):
        for x in range(width):
            pixelValue = img1[y, x]
            
            if (pixelValue[0] == 0
                and pixelValue[1] == 0
                and pixelValue[2] == 0):
                out_img[y, x] = pixelValue
            elif (pixelValue[0] == 0
                and pixelValue[1] == 0
                and pixelValue[2] == 255):
                out_img[y, x] = pixelValue
    
    return out_img
    
def main1():
    img1 = ExtractRoadAndCrossPt()
    
    cv2.imwrite("out5.bmp", img1)
    

main1()
    