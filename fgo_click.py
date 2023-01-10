
from PyQt5.QtWidgets import QApplication
from pyautogui import locate as pyautolocate
import time
import win32gui, win32con, win32api
from numpy import array ,int64 ,zeros,shape
import cv2 
import math
NowFGOImg="./FGOPic/now.png"

def convertQImageToMat(qt_img):
    qt_img = qt_img.convertToFormat(4)
    w = qt_img.width()
    h = qt_img.height()

    ptr = qt_img.bits()
    ptr.setsize(qt_img.byteCount())
    arr = array(ptr).reshape(h,w,4)
    return arr

class Fgo_action():
    def __init__(self):
        self.actionList=dict()

    def setup(self):
        self.hwndf = win32gui.FindWindow("Qt5154QWindowOwnDCIcon", None)
        if self.hwndf!=0:
            self.hwndc = win32gui.FindWindowEx(self.hwndf,0,"Qt5154QWindowIcon", None)
            main_rect=win32gui.GetWindowRect(self.hwndf)

            if (main_rect[2]-main_rect[0])!=768 or (main_rect[3]-main_rect[1])!=447:
                print("size err:",main_rect[2]-main_rect[0], main_rect[3]-main_rect[1])
                win32gui.MoveWindow(self.hwndf,0,0,768,447,True)
            return True
        else:
            return False

    def resize_window(self):
        win32gui.MoveWindow(self.hwndf,0,0,768,447,True)

    def getWindow_rect(self):
        main_rect=win32gui.GetWindowRect(self.hwndf)#左,上,右,下
        return main_rect[2]-main_rect[0], main_rect[3]-main_rect[1]
        

    def to_click(self,x,y):
        #要先點父視窗的標題 才點的到裡面.. 無解@@
        win32gui.PostMessage(self.hwndf, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,win32api.MAKELONG(590,15))
        win32gui.PostMessage(self.hwndf, win32con.WM_LBUTTONUP,0,win32api.MAKELONG(590,15))
        win32gui.PostMessage(self.hwndf, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,win32api.MAKELONG(590,15))
        win32gui.PostMessage(self.hwndf, win32con.WM_LBUTTONUP,0,win32api.MAKELONG(590,15))    

        time.sleep(0.5)
        win32gui.PostMessage(self.hwndc, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,win32api.MAKELONG(x,y))
        win32gui.PostMessage(self.hwndc, win32con.WM_LBUTTONUP,0,win32api.MAKELONG(x,y))
        time.sleep(0.5)
        print("click:",x,y)
    
    def to_roll(self,x,y,r=-240):
        main_rect=win32gui.GetWindowRect(self.hwndf)
        win32gui.PostMessage(self.hwndf, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,win32api.MAKELONG(590,15))
        win32gui.PostMessage(self.hwndf, win32con.WM_LBUTTONUP,0,win32api.MAKELONG(590,15))
        win32gui.PostMessage(self.hwndf, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,win32api.MAKELONG(590,15))
        win32gui.PostMessage(self.hwndf, win32con.WM_LBUTTONUP,0,win32api.MAKELONG(590,15))    
        
        time.sleep(0.5)
        #滾輪的xy座標是整個螢幕的座標 跟點擊事件不一樣@@ bug??
        #要參考當下視窗座標做修正
        win32gui.PostMessage(self.hwndc, win32con.WM_MOUSEWHEEL,win32api.MAKELONG(0,r),win32api.MAKELONG(main_rect[0]+x,main_rect[1]+y))#-120 #390 770
        time.sleep(0.5)
        print("roll:",x,y)

    def grabWindowImg(self):
        screen = QApplication.primaryScreen()
        qt_img = screen.grabWindow(self.hwndc).toImage()
        
        img=convertQImageToMat(qt_img)
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        return img2

    def locate_MT(self,needleImage,haystackImage,img_region=None):
        box=pyautolocate(needleImage,haystackImage,grayscale=True,confidence=0.8,region=img_region)  
        if box!=None:
            return (box[0]+(box[2]/2)).astype(int64),(box[1]+(box[3])/2).astype(int64)
        else:
            return None
    

    def find_target_MT(self,needleImage,img_region=None,conf=0.8):
        #模板匹配方法找點擊位置
        screen = QApplication.primaryScreen()
        qt_img = screen.grabWindow(self.hwndc).toImage()
        hImg=convertQImageToMat(qt_img)
        haystackImage=cv2.cvtColor(hImg,cv2.COLOR_BGR2RGB)      
        s = time.time()
        box=None
        if img_region!=None:
            box=pyautolocate(needleImage,haystackImage,grayscale=True,confidence=conf,region=img_region)  
        else:
            box=pyautolocate(needleImage,haystackImage,grayscale=True,confidence=conf)
        e = time.time()
        print("t",e-s)
        print("box ",box)
        if box!=None:
            return (box[0]+(box[2]/2)).astype(int64),(box[1]+(box[3])/2).astype(int64)
        else:
            return None
    def find_EP(self,needleImage,haystackImage):
        #特徵值匹配方法找點擊位置
        sift =  cv2.SIFT_create()
        _, des1 = sift.detectAndCompute(needleImage,None)
        _, des2 = sift.detectAndCompute(haystackImage,None)
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1,des2,k=2)
        good = 0
        for m,n in matches:
            if m.distance < 0.8*n.distance:#特徵距離越小越相近
                good=good+1
        return good


    def locate_EV(self,needleImage,haystackImage):
        #特徵值匹配方法找點擊位置`  `
        print("fff tev")
        sift =  cv2.SIFT_create()
        _, des1 = sift.detectAndCompute(needleImage,None)
        kp2, des2 = sift.detectAndCompute(haystackImage,None)
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1,des2,k=2)
        print(len(matches))
        good = []
        im2_kp=[]
        for m,n in matches:
            if m.distance < 0.8*n.distance:
                good.append((m,))
                im2_kp.append(list(kp2[m.trainIdx].pt))

        d=(needleImage.shape[0] if needleImage.shape[0]>needleImage.shape[1] else needleImage.shape[1])/2
        if len(good)<0.2*len(matches):
            print("not match",len(good),len(matches))
            return None
        
        print("match",len(good),len(matches))

        dict_num=zeros(len(im2_kp))
        for index,i in enumerate(im2_kp):
            for j in im2_kp:
                if not (i==j):
                    dist = math.dist(i,j)
                    if dist<=d:
                        dict_num[index]=dict_num[index]+1
        p=dict_num.argmax()
        print("p",int(im2_kp[p][0]),int(im2_kp[p][1]))

        return int(im2_kp[p][0]),int(im2_kp[p][1])
