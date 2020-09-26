import cv2
import sys
import random

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

def GetEdgeRoad(CurrentCrossPtImg, RoadAndCrossPtImg):

    fillPixelValue = [0, 0, 0]
    
    height, width, channel = RoadAndCrossPtImg.shape
    
    out_img = cv2.imread("blank2.jpg")    
    out_img = cv2.resize(out_img, (width, height))
    
    for y in range(height):
        for x in range(width):
                
            if (RoadAndCrossPtImg[y, x][0] == 0
               and RoadAndCrossPtImg[y, x][1] == 0
               and RoadAndCrossPtImg[y, x][2] == 0):
               
                x1 = x-1
                y1 = y-1
                if x1 >= 0 and y1 >= 0:
                    if(CurrentCrossPtImg[y1, x1][0] == 0
                        and CurrentCrossPtImg[y1, x1][1] == 0
                        and CurrentCrossPtImg[y1, x1][2] == 0):
                        
                        out_img[y, x] = fillPixelValue
                                            
                x1 = x
                y1 = y-1
                if y1 >= 0:
                    if(CurrentCrossPtImg[y1, x1][0] == 0
                        and CurrentCrossPtImg[y1, x1][1] == 0
                        and CurrentCrossPtImg[y1, x1][2] == 0):
                        
                        out_img[y, x] = fillPixelValue

                        
                x1 = x+1
                y1 = y-1
                if x1 < width and y1 >= 0:
                    if(CurrentCrossPtImg[y1, x1][0] == 0
                        and CurrentCrossPtImg[y1, x1][1] == 0
                        and CurrentCrossPtImg[y1, x1][2] == 0):
                        
                        out_img[y, x] = fillPixelValue

                        

                x1 = x-1
                y1 = y
                if x1 >= 0:
                    if(CurrentCrossPtImg[y1, x1][0] == 0
                        and CurrentCrossPtImg[y1, x1][1] == 0
                        and CurrentCrossPtImg[y1, x1][2] == 0):
                        
                        out_img[y, x] = fillPixelValue
                        
                x1 = x+1
                y1 = y
                if x1 < width:
                   if(CurrentCrossPtImg[y1, x1][0] == 0
                        and CurrentCrossPtImg[y1, x1][1] == 0
                        and CurrentCrossPtImg[y1, x1][2] == 0):
                        
                        out_img[y, x] = fillPixelValue

                        
                x1 = x-1
                y1 = y+1
                if x1 >= 0 and y1 < height:
                    if(CurrentCrossPtImg[y1, x1][0] == 0
                        and CurrentCrossPtImg[y1, x1][1] == 0
                        and CurrentCrossPtImg[y1, x1][2] == 0):
                        
                        out_img[y, x] = fillPixelValue

                        
                x1 = x
                y1 = y+1
                if y1 < height:
                    if(CurrentCrossPtImg[y1, x1][0] == 0
                        and CurrentCrossPtImg[y1, x1][1] == 0
                        and CurrentCrossPtImg[y1, x1][2] == 0):
                        
                        out_img[y, x] = fillPixelValue

                        
                x1 = x+1
                y1 = y+1
                if x < width and y1 < height:
                    if(CurrentCrossPtImg[y1, x1][0] == 0
                        and CurrentCrossPtImg[y1, x1][1] == 0
                        and CurrentCrossPtImg[y1, x1][2] == 0):
                        
                        out_img[y, x] = fillPixelValue


    return out_img

def RandomPickUpPixel(img1):

        height, width, channel = img1.shape
        
        BlackPixels = []
        for y in range(height):
            for x in range(width):
            
                if(img1[y, x][0] == 0 
                and img1[y, x][1] == 0
                and img1[y, x][2] == 0):
                    BlackPixels.append([y, x])
                    
                    
        val1 = BlackPixels[random.randint(0, len(BlackPixels)-1)]
        
        print(val1)
        return val1
        

def FillColor(img, sx, sy, color_b, color_g, color_r, fColorB, fColorG, fColorR):

    if color_b == fColorB and color_g == fColorG and color_r == fColorR:
        return

    height, width, channel = img.shape;

    out_img = cv2.imread("blank2.jpg")
    
    out_img = cv2.resize(out_img, (width, height))
    
    
    fillArray = []
    fillArray.append([sy, sx])
    fillPixelValue = [fColorB, fColorG, fColorR]
    
    out_img[sy, sx] = fillPixelValue
    print(out_img[sy, sx])
    fillCount = 1
    
    while fillCount >= 1:
        #print(fillCount)
        
        fillCount = 0
        
        for y in range(height):
            for x in range(width):
                if (img[y, x][0] == color_b
                    and img[y, x][1] == color_g
                    and img[y, x][2] == color_r
                    and out_img[y, x][0] == 255
                    and out_img[y, x][1] == 255
                    and out_img[y, x][2] == 255 ):
                    
                    
                    x1 = x-1
                    y1 = y-1
                    if x1 >= 0 and y1 >= 0:
                        if(out_img[y1, x1][0] == fColorB
                            and out_img[y1, x1][1] == fColorG
                            and out_img[y1, x1][2] == fColorR ):
                            
                            out_img[y, x] = fillPixelValue
                            fillCount = fillCount+1
                                                
                    x1 = x
                    y1 = y-1
                    if y1 >= 0:
                        if(out_img[y1, x1][0] == fColorB
                            and out_img[y1, x1][1] == fColorG
                            and out_img[y1, x1][2] == fColorR ):
                            
                            out_img[y, x] = fillPixelValue
                            fillCount = fillCount+1
                            
                    x1 = x+1
                    y1 = y-1
                    if x1 < width and y1 >= 0:
                        if(out_img[y1, x1][0] == fColorB
                            and out_img[y1, x1][1] == fColorG
                            and out_img[y1, x1][2] == fColorR ):
                            
                            out_img[y, x] = fillPixelValue
                            fillCount = fillCount+1
                            

                    x1 = x-1
                    y1 = y
                    if x1 >= 0:
                        if(out_img[y1, x1][0] == fColorB
                            and out_img[y1, x1][1] == fColorG
                            and out_img[y1, x1][2] == fColorR ):
                            
                            out_img[y, x] = fillPixelValue
                            fillCount = fillCount+1
                            
                    x1 = x+1
                    y1 = y
                    if x1 < width:
                        if(out_img[y1, x1][0] == fColorB
                            and out_img[y1, x1][1] == fColorG
                            and out_img[y1, x1][2] == fColorR ):
                            
                            out_img[y1, x1] = fillPixelValue
                            fillCount = fillCount+1
                            
                    x1 = x-1
                    y1 = y+1
                    if x1 >= 0 and y1 < height:
                        if(out_img[y1, x1][0] == fColorB
                            and out_img[y1, x1][1] == fColorG
                            and out_img[y1, x1][2] == fColorR ):
                            
                            out_img[y, x] = fillPixelValue
                            fillCount = fillCount+1
                            
                    x1 = x
                    y1 = y+1
                    if y1 < height:
                        if(out_img[y1, x1][0] == fColorB
                            and out_img[y1, x1][1] == fColorG
                            and out_img[y1, x1][2] == fColorR ):
                            
                            out_img[y, x] = fillPixelValue
                            fillCount = fillCount+1
                            
                    x1 = x+1
                    y1 = y+1
                    if x < width and y1 < height:
                        if(out_img[y1, x1][0] == fColorB
                            and out_img[y1, x1][1] == fColorG
                            and out_img[y1, x1][2] == fColorR ):
                            
                            out_img[y, x] = fillPixelValue
                            fillCount = fillCount+1
                    
        
    return out_img
    
def main1():
    img1 = ExtractRoadAndCrossPt()
    
    cv2.imwrite("out5.bmp", img1)
    

def main2():

    out_img = cv2.imread("out5.bmp")
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("img", callback)
    
    cv2.imshow("img", out_img);
    
    while True:
        k = cv2.waitKey(1)
        #Escキーを押すと終了
        if k == 27 or k == ord("q") :
            print(">>> Exit")
            break
        
def main3():

    img1 = cv2.imread("out5.bmp")
    
    img2 = FillColor(img1, 272, 174, 0, 0, 255, 0, 0, 0)
    cv2.imwrite("out7.bmp", img2)
    
    return


def main4():
    img1 = cv2.imread("out7.bmp")
    img2 = cv2.imread("out5.bmp")
    
    img3 = GetEdgeRoad(img1, img2)
    
    cv2.imwrite("out8.bmp", img3)
    
    return
    
def main5():
    img1 = cv2.imread("out8.bmp")
    StartRoadPixel = RandomPickUpPixel(img1)
    
    img2 = cv2.imread("out5.bmp")
    
    img3 = FillColor(img2, StartRoadPixel[1], StartRoadPixel[0], 0, 0, 0, 255, 0, 0)
    cv2.imwrite("out10.bmp", img3)
    
    return
    
mouse_x=0
mouse_y=0
def callback(event, x, y, flags, param):
    global mouse_x
    global mouse_y

    #マウスの左ボタンがクリックされたとき
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_x = x;
        mouse_y = y;
        

    #マウスの左ボタンが離されたとき
    if event == cv2.EVENT_LBUTTONUP:
    
        print("aaa")
        print(mouse_x)
        print(mouse_y)
        print("bbb")


    return 0

if __name__ == "__main__":
    main5()
    