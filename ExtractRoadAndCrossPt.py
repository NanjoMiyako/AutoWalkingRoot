import cv2
import sys
import random
import math

#道と交差点が上書きされている画像から、道と交差点のピクセルのみ抽出する
def ExtractRoadAndCrossPt(img1):

    
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


#現在の交差点に接している道のピクセルを抽出
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
                if x1 < width and y1 < height:
                    if(CurrentCrossPtImg[y1, x1][0] == 0
                        and CurrentCrossPtImg[y1, x1][1] == 0
                        and CurrentCrossPtImg[y1, x1][2] == 0):
                        
                        out_img[y, x] = fillPixelValue


    return out_img

#画像中の黒ピクセルからExclusionImgに書かれていないものを候補ピクセルとして、
#ランダムに一つ抽出する
#候補黒ピクセルが0だったときは全黒ピクセルから一つ返す
def RandomPickUpPixel(img1, ExclusionImg):

        
        height, width, channel = img1.shape
        WholeBlackPixels = []
        CandidateBlackPixels = []
        
        for y in range(height):
            for x in range(width):
            
                if(img1[y, x][0] == 0 
                and img1[y, x][1] == 0
                and img1[y, x][2] == 0):
                
                    WholeBlackPixels.append([y, x])
                    
                    if(        ExclusionImg[y, x][0] != 0
                        or     ExclusionImg[y, x][1] != 0
                        or    ExclusionImg[y, x][2] != 0):
                        CandidateBlackPixels.append([y, x])
                    
        
        if(len(CandidateBlackPixels) >= 1):
            val1 = CandidateBlackPixels[random.randint(0, len(CandidateBlackPixels)-1)]
        else:
            val1 = WholeBlackPixels[random.randint(0, len(WholeBlackPixels)-1)]
        
        print(val1)
        return val1
        
def FillColor2(img, sx, sy, fColorB, fColorG, fColorR):
    height, width, channel = img.shape;

    out_img = cv2.imread("blank2.jpg")    
    
    out_img = cv2.resize(out_img, (width, height))
    
    prevColor = img[sy, sx]
    newColor = [fColorB, fColorG, fColorR]
    
    fillArray = []
    fillArray.append([sy, sx])
    
    while len(fillArray) >= 1:
        
        pixelPos = fillArray.pop(0)
        out_img[pixelPos[0], pixelPos[1]] = newColor
        x = pixelPos[1]
        y = pixelPos[0]
        
        x1 = x-1
        y1 = y-1
        if x1 >= 0 and y1 >= 0:
            if(   out_img[y1, x1][0] != newColor[0]
               or out_img[y1, x1][1] != newColor[1]
               or out_img[y1, x1][2] != newColor[2]):
               
               if(         img[y1, x1][0] == prevColor[0]
                       and img[y1, x1][1] == prevColor[1]
                       and img[y1, x1][2] == prevColor[2]
                       and [y1, x1] not in fillArray ):
                fillArray.append([y1, x1])
                
        x1 = x
        y1 = y-1
        if y1 >= 0:
            if(   out_img[y1, x1][0] != newColor[0]
               or out_img[y1, x1][1] != newColor[1]
               or out_img[y1, x1][2] != newColor[2]):
               
               if(         img[y1, x1][0] == prevColor[0]
                       and img[y1, x1][1] == prevColor[1]
                       and img[y1, x1][2] == prevColor[2]
                       and [y1, x1] not in fillArray ):
                fillArray.append([y1, x1])
                
        x1 = x+1
        y1 = y-1
        if x1 < width and y1 >= 0:
            if(   out_img[y1, x1][0] != newColor[0]
               or out_img[y1, x1][1] != newColor[1]
               or out_img[y1, x1][2] != newColor[2]):
               
               if(         img[y1, x1][0] == prevColor[0]
                       and img[y1, x1][1] == prevColor[1]
                       and img[y1, x1][2] == prevColor[2]
                       and [y1, x1] not in fillArray ):
                fillArray.append([y1, x1])
                

        x1 = x-1
        y1 = y
        if x1 >= 0:
            if(   out_img[y1, x1][0] != newColor[0]
               or out_img[y1, x1][1] != newColor[1]
               or out_img[y1, x1][2] != newColor[2]):
               
               if(         img[y1, x1][0] == prevColor[0]
                       and img[y1, x1][1] == prevColor[1]
                       and img[y1, x1][2] == prevColor[2]
                       and [y1, x1] not in fillArray ):
                fillArray.append([y1, x1])
                
        x1 = x+1
        y1 = y
        if x1 < width:
            if(   out_img[y1, x1][0] != newColor[0]
               or out_img[y1, x1][1] != newColor[1]
               or out_img[y1, x1][2] != newColor[2]):
               
               if(         img[y1, x1][0] == prevColor[0]
                       and img[y1, x1][1] == prevColor[1]
                       and img[y1, x1][2] == prevColor[2]
                       and [y1, x1] not in fillArray ):
                fillArray.append([y1, x1])
                
        x1 = x-1
        y1 = y+1
        if x1 >= 0 and y1 < height:
            if(   out_img[y1, x1][0] != newColor[0]
               or out_img[y1, x1][1] != newColor[1]
               or out_img[y1, x1][2] != newColor[2]):
               
               if(         img[y1, x1][0] == prevColor[0]
                       and img[y1, x1][1] == prevColor[1]
                       and img[y1, x1][2] == prevColor[2]
                       and [y1, x1] not in fillArray ):
                fillArray.append([y1, x1])
                
        x1 = x
        y1 = y+1
        if y1 < height:
            if(   out_img[y1, x1][0] != newColor[0]
               or out_img[y1, x1][1] != newColor[1]
               or out_img[y1, x1][2] != newColor[2]):
               
               if(         img[y1, x1][0] == prevColor[0]
                       and img[y1, x1][1] == prevColor[1]
                       and img[y1, x1][2] == prevColor[2]
                       and [y1, x1] not in fillArray ):
                fillArray.append([y1, x1])
                
        x1 = x+1
        y1 = y+1
        if x1 < width and y1 < height:
            if(   out_img[y1, x1][0] != newColor[0]
               or out_img[y1, x1][1] != newColor[1]
               or out_img[y1, x1][2] != newColor[2]):
               
               if(         img[y1, x1][0] == prevColor[0]
                       and img[y1, x1][1] == prevColor[1]
                       and img[y1, x1][2] == prevColor[2]
                       and [y1, x1] not in fillArray ):
                fillArray.append([y1, x1])
                
    return out_img
        
#img中で(sx,sy)の周りでcolor_b,color_g,color_rの色のピクセルをfColorB,fColorG,fColorRで塗りつぶした画像を取得する
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
        print("b1")
        print(fillCount)
        print("b2")
        
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
                    if x1 < width and y1 < height:
                        if(out_img[y1, x1][0] == fColorB
                            and out_img[y1, x1][1] == fColorG
                            and out_img[y1, x1][2] == fColorR ):
                            
                            out_img[y, x] = fillPixelValue
                            fillCount = fillCount+1
                    
        
    return out_img

#地図上で道と交差点が上書きされた画像から道と交差点のみ抽出する
def main1():
    img1 = cv2.imread("base5.bmp")
    img1 = ExtractRoadAndCrossPt(img1)
    
    cv2.imwrite("RoadAndCrossPt.bmp", img1)
    

#表示した画像でクリックされた位置のx座標、y座標を表示する
def main2():

    out_img = cv2.imread("RoadAndCrossPt.bmp")

    cv2.imshow("img", out_img);    
    cv2.setMouseCallback("img", callback)

    
    while True:
        k = cv2.waitKey(1)
        #Escキーを押すと終了
        if k == 27 or k == ord("q") :
            print(">>> Exit")
            break


def main4():

    #道と交差点が書かれた画像読み込み
    img1 = cv2.imread("RoadAndCrossPt.bmp")
    height, width, channel = img1.shape
    
    out_img = cv2.resize(out_img, (width, height)) 

        
    #現在の交差点の部分を抽出
    img2 = FillColor2(img1, 0,0, 0, 0, 0)

def main5():
    img1 = cv2.imread("RoadAndCrossPt.bmp")
    
    img2 = cv2.imread("test2.bmp")
    
    img4 = cv2.imread("CurrentRoad.bmp")
    
    OtherCrossPtPixel= GetAnotherCrossPtPixel(img4, img2, img1)
    
    print(OtherCrossPtPixel)
    
    
#指定した点から散歩ルートをランダムで作成していく
def main3():
    endDist = 250
    wholeDist = 0
    
    startX=137
    startY=152
    
    out_img = cv2.imread("blank3.bmp")
    
    #道と交差点が書かれた画像読み込み
    img1 = cv2.imread("RoadAndCrossPt.bmp")
    height, width, channel = img1.shape
    
    out_img = cv2.resize(out_img, (width, height)) 
    
    print("処理開始")
    while wholeDist < endDist:
    
        
        #現在の交差点の部分を抽出
        img2 = FillColor2(img1, startX, startY, 0, 0, 0)
        
        cv2.imwrite("test2.bmp", img2)
        
        #現在の交差点に接する道の部分のピクセル取得
        img3 = GetEdgeRoad(img2, img1)
        cv2.imwrite("test4.bmp", img3)
        
        #現在の交差点に接する道のピクセルのうちまだ通っていないものの中で一つを取得
        DirectionPixel = RandomPickUpPixel(img3, out_img)

        
        print(DirectionPixel)
        #上で取得した道の全体のピクセル取得
        img4 = FillColor2(img1, DirectionPixel[1], DirectionPixel[0], 0, 0, 0)
        OtherCrossPtPixel= GetAnotherCrossPtPixel(img4, img2, img1)
        
        if OtherCrossPtPixel[0] == -1:
            startX = startX
            startY = startY
        else:
            startX = OtherCrossPtPixel[1]
            startY = OtherCrossPtPixel[0]

        
        length1 = GetCircumferenceLengthOfRoadWithOutNearCrossPt(img4, img1)
        wholeDist = wholeDist + int(length1/2)
        
        
        out_img = DrawImage(out_img, img2)
        out_img = DrawImage(out_img, img4)
        
        
        print("--現在の距離--")
        print(wholeDist)
        print("--------")
            


    print("処理終了")
    cv2.imwrite("AutoWalkRoot1.jpg", out_img)



def DrawImage(img1, img2):
    out_img = cv2.imread("blank2.jpg")
    
    height, width, channel = img2.shape
    out_img = cv2.resize(out_img, (width,height))
    
    for y in range(height):
        for x in range(width):
            out_img[y, x] = img1[y, x]
            
    for y in range(height):
        for x in range(width):
            if(       img2[y, x][0] != 255
                or    img2[y, x][1] != 255
                or    img2[y, x][2] != 255):
                out_img[y, x] = img2[y,x]
           
    return out_img

def isExistNearColorPixel(img, x, y, ColorB, ColorG, ColorR):

    height, width, channel = img.shape
    resultLength = 0
    
    x1 = x-1
    y1 = y-1
    
    if x1 >= 0 and y1 >= 0:
        if(        img[y1, x1][0] == ColorB
            and img[y1, x1][1] == ColorG
            and img[y1, x1][2] == ColorR):
            return True
            

    x1 = x
    y1 = y-1
    if y1 >= 0:
        if(        img[y1, x1][0] == ColorB
            and img[y1, x1][1] == ColorG
            and img[y1, x1][2] == ColorR):
            return True
            
    x1 = x+1
    y1 = y-1
    if x1 < width and y1 >= 0:
        if(        img[y1, x1][0] == ColorB
            and img[y1, x1][1] == ColorG
            and img[y1, x1][2] == ColorR):
            return True
            

    x1 = x-1
    y1 = y
    if x1 >= 0:
        if(        img[y1, x1][0] == ColorB
            and img[y1, x1][1] == ColorG
            and img[y1, x1][2] == ColorR):
            return True
            
    x1 = x+1
    y1 = y
    if x1 < width:
        if(        img[y1, x1][0] == ColorB
            and img[y1, x1][1] == ColorG
            and img[y1, x1][2] == ColorR):
            return True
            
    x1 = x-1
    y1 = y+1
    if x1 >= 0 and y1 < height:
        if(        img[y1, x1][0] == ColorB
            and img[y1, x1][1] == ColorG
            and img[y1, x1][2] == ColorR):
            return True
            
    x1 = x
    y1 = y+1
    if y1 < height:
        if(        img[y1, x1][0] == ColorB
            and img[y1, x1][1] == ColorG
            and img[y1, x1][2] == ColorR):
            return True
            
    x1 = x+1
    y1 = y+1
    if x1 < width and y1 < height:
        if(        img[y1, x1][0] == ColorB
            and img[y1, x1][1] == ColorG
            and img[y1, x1][2] == ColorR):
            return True
            
    return False
    
def GetCircumferenceLengthOfRoadWithOutNearCrossPt(RoadImg, RoadAndCrossPtImg):

    height, width, channel = RoadImg.shape
    resultLength = 0
    
    for y in range(height):
        for x in range(width):
            
            if (    RoadImg[y, x][0] == 0
                and RoadImg[y, x][1] == 0
                and RoadImg[y, x][2] == 0
                and (not isExistNearColorPixel(RoadAndCrossPtImg, x, y, 0, 0, 255)) ):
        
                x1 = x-1
                y1 = y-1
                if x1 >= 0 and y1 >= 0:
                    if(     RoadImg[y1, x1][0] == 255
                        and RoadImg[y1, x1][1] == 255
                        and RoadImg[y1, x1][2] == 255):                        
                        resultLength = resultLength + 1
                        continue
                        

                x1 = x
                y1 = y-1
                if y1 >= 0:
                    if(     RoadImg[y1, x1][0] == 255
                        and RoadImg[y1, x1][1] == 255
                        and RoadImg[y1, x1][2] == 255):                        
                        resultLength = resultLength + 1
                        continue
                        
                x1 = x+1
                y1 = y-1
                if x1 < width and y1 >= 0:
                    if(     RoadImg[y1, x1][0] == 255
                        and RoadImg[y1, x1][1] == 255
                        and RoadImg[y1, x1][2] == 255):                        
                        resultLength = resultLength + 1
                        continue
                        

                x1 = x-1
                y1 = y
                if x1 >= 0:
                    if(     RoadImg[y1, x1][0] == 255
                        and RoadImg[y1, x1][1] == 255
                        and RoadImg[y1, x1][2] == 255):                        
                        resultLength = resultLength + 1
                        continue
                        
                x1 = x+1
                y1 = y
                if x1 < width:
                    if(     RoadImg[y1, x1][0] == 255
                        and RoadImg[y1, x1][1] == 255
                        and RoadImg[y1, x1][2] == 255):                        
                        resultLength = resultLength + 1
                        continue
                        
                x1 = x-1
                y1 = y+1
                if x1 >= 0 and y1 < height:
                    if(     RoadImg[y1, x1][0] == 255
                        and RoadImg[y1, x1][1] == 255
                        and RoadImg[y1, x1][2] == 255):                        
                        resultLength = resultLength + 1
                        continue
                        
                x1 = x
                y1 = y+1
                if y1 < height:
                    if(     RoadImg[y1, x1][0] == 255
                        and RoadImg[y1, x1][1] == 255
                        and RoadImg[y1, x1][2] == 255):                        
                        resultLength = resultLength + 1
                        continue
                        
                x1 = x+1
                y1 = y+1
                if x1 < width and y1 < height:
                    if(     RoadImg[y1, x1][0] == 255
                        and RoadImg[y1, x1][1] == 255
                        and RoadImg[y1, x1][2] == 255):                        
                        resultLength = resultLength + 1
                        continue
                            
   
    return resultLength
                                

def ChangeColor(img1, prevColorB, prevColorG, prevColorR, newColorB, newColorG, newColorR):

    height, width, channel = img1.shape
    
    out_img = cv2.imread("blank2.jpg")
    out_img = cv2.resize(out_img,(width, height))
    
    fillPixel = [newColorB, newColorG, newColorR]
    
    for y in range(height):
        for x in range(width):
            if(        img1[y, x][0] == prevColorB
                and    img1[y, x][1] == prevColorG
                and img1[y, x][2] == prevColorR):
                
                    out_img[y, x] = fillPixel
            else:
                out_img[y, x] = img1[y, x]
                
    return out_img

#道の画像上から現在の交差点でない方の交差点のピクセルを一つ抽出する    
def GetAnotherCrossPtPixel(RoadImg, CurrentCrossPtImg, RoadAndCrossPtImg):
    
    out_img = cv2.imread("blank2.jpg")
    
    height, width, channel = RoadImg.shape
    

    
    out_img = cv2.resize(out_img, (width, height))
    otherCrossPtPixel = [-1, -1]
    
    for y in range(height):
    
        for x in range(width):
                
            if(     RoadImg[y, x][0] == 0
                and RoadImg[y, x][1] == 0
                and RoadImg[y, x][2] == 0):
                
                
                
                if not (isExistNearColorPixel(RoadAndCrossPtImg, x, y, 0, 0, 255)):
                    continue
                
                
                x1 = x-1
                y1 = y-1
                if x1 >= 0 and y1 >= 0:
                    if (    RoadAndCrossPtImg[y1, x1][0] == 0
                        and RoadAndCrossPtImg[y1, x1][1] == 0
                        and RoadAndCrossPtImg[y1, x1][2] == 255):
                        if (   CurrentCrossPtImg[y1, x1][0] != 0
                            or CurrentCrossPtImg[y1, x1][1] != 0
                            or CurrentCrossPtImg[y1, x1][2] != 0):
                            otherCrossPtPixel[0] = y1
                            otherCrossPtPixel[1] = x1
                            return otherCrossPtPixel
                        
                                            
                x1 = x
                y1 = y-1
                if y1 >= 0:
                    if (    RoadAndCrossPtImg[y1, x1][0] == 0
                        and RoadAndCrossPtImg[y1, x1][1] == 0
                        and RoadAndCrossPtImg[y1, x1][2] == 255):
                        if (   CurrentCrossPtImg[y1, x1][0] != 0
                            or CurrentCrossPtImg[y1, x1][1] != 0
                            or CurrentCrossPtImg[y1, x1][2] != 0):
                            otherCrossPtPixel[0] = y1
                            otherCrossPtPixel[1] = x1
                            return otherCrossPtPixel
                        
                x1 = x+1
                y1 = y-1
                if x1 < width and y1 >= 0:
                    if (    RoadAndCrossPtImg[y1, x1][0] == 0
                        and RoadAndCrossPtImg[y1, x1][1] == 0
                        and RoadAndCrossPtImg[y1, x1][2] == 255):
                        if (   CurrentCrossPtImg[y1, x1][0] != 0
                            or CurrentCrossPtImg[y1, x1][1] != 0
                            or CurrentCrossPtImg[y1, x1][2] != 0):
                            otherCrossPtPixel[0] = y1
                            otherCrossPtPixel[1] = x1
                            return otherCrossPtPixel
                        

                x1 = x-1
                y1 = y
                if x1 >= 0:
                    if (    RoadAndCrossPtImg[y1, x1][0] == 0
                        and RoadAndCrossPtImg[y1, x1][1] == 0
                        and RoadAndCrossPtImg[y1, x1][2] == 255):
                        if (   CurrentCrossPtImg[y1, x1][0] != 0
                            or CurrentCrossPtImg[y1, x1][1] != 0
                            or CurrentCrossPtImg[y1, x1][2] != 0):
                            otherCrossPtPixel[0] = y1
                            otherCrossPtPixel[1] = x1
                            return otherCrossPtPixel
                        
                x1 = x+1
                y1 = y
                if x1 < width:
                    if (    RoadAndCrossPtImg[y1, x1][0] == 0
                        and RoadAndCrossPtImg[y1, x1][1] == 0
                        and RoadAndCrossPtImg[y1, x1][2] == 255):
                        if (   CurrentCrossPtImg[y1, x1][0] != 0
                            or CurrentCrossPtImg[y1, x1][1] != 0
                            or CurrentCrossPtImg[y1, x1][2] != 0):
                            otherCrossPtPixel[0] = y1
                            otherCrossPtPixel[1] = x1
                            return otherCrossPtPixel
                        
                x1 = x-1
                y1 = y+1
                if x1 >= 0 and y1 < height:
                    if (    RoadAndCrossPtImg[y1, x1][0] == 0
                        and RoadAndCrossPtImg[y1, x1][1] == 0
                        and RoadAndCrossPtImg[y1, x1][2] == 255):
                        if (   CurrentCrossPtImg[y1, x1][0] != 0
                            or CurrentCrossPtImg[y1, x1][1] != 0
                            or CurrentCrossPtImg[y1, x1][2] != 0):
                            otherCrossPtPixel[0] = y1
                            otherCrossPtPixel[1] = x1
                            return otherCrossPtPixel
                        
                x1 = x
                y1 = y+1
                if y1 < height:
                    if (    RoadAndCrossPtImg[y1, x1][0] == 0
                        and RoadAndCrossPtImg[y1, x1][1] == 0
                        and RoadAndCrossPtImg[y1, x1][2] == 255):
                        if (   CurrentCrossPtImg[y1, x1][0] != 0
                            or CurrentCrossPtImg[y1, x1][1] != 0
                            or CurrentCrossPtImg[y1, x1][2] != 0):
                            otherCrossPtPixel[0] = y1
                            otherCrossPtPixel[1] = x1
                            return otherCrossPtPixel
                        
                x1 = x+1
                y1 = y+1
                if x1 < width and y1 < height:
                    if (    RoadAndCrossPtImg[y1, x1][0] == 0
                        and RoadAndCrossPtImg[y1, x1][1] == 0
                        and RoadAndCrossPtImg[y1, x1][2] == 255):
                        if (   CurrentCrossPtImg[y1, x1][0] != 0
                            or CurrentCrossPtImg[y1, x1][1] != 0
                            or CurrentCrossPtImg[y1, x1][2] != 0):
                            otherCrossPtPixel[0] = y1
                            otherCrossPtPixel[1] = x1
                            return otherCrossPtPixel

        
    return otherCrossPtPixel
        

def calcPixelDistance(sx, sy, ex, ey):

    dist = (ex - sx) * (ex - sx) + (ey - sy)*(ey - sy)
    dist = math.sqrt(dist)
    
    return dist
    
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
    main3()
    