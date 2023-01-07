
from PyQt5.QtWidgets import QApplication
from pyautogui import locate as pyautolocate
import time
import win32gui, win32con, win32api
from numpy import array ,int64 ,zeros,shape
import cv2 
import math
NowFGOImg="./FGOPic/now.png"

def convertQImageToMat(qt_img):
    # format_RGB32=4,存入格式為R,G,B,A 對應0,1,2,3
    # RGB32圖像每個像素用32bit表示,占4個字節
    #R,G,B分輛分別用8個bit表示,儲存順序為R,G,B 最後8個字節保留
    qt_img = qt_img.convertToFormat(4)
    w = qt_img.width()
    h = qt_img.height()

    ptr = qt_img.bits()
    ptr.setsize(qt_img.byteCount())
    arr = array(ptr).reshape(h,w,4)
    # arr為BGRA 4通道圖片
    return arr

class Fgo_action():
    def __init__(self):
        self.actionList=dict()
        # self.actionList["click"]=self.to_click

    def setup(self):
        self.hwndf = win32gui.FindWindow("Qt5154QWindowOwnDCIcon", None)#bluestack父視窗
        if self.hwndf!=0:
            self.hwndc = win32gui.FindWindowEx(self.hwndf,0,"Qt5154QWindowIcon", None)#bluestack子視窗
            #self.rect = win32gui.GetWindowRect(self.hwndc)
            main_rect=win32gui.GetWindowRect(self.hwndf)

            if (main_rect[2]-main_rect[0])!=768 or (main_rect[3]-main_rect[1])!=447:
                print("size err:",main_rect[2]-main_rect[0], main_rect[3]-main_rect[1])
                win32gui.MoveWindow(self.hwndf,0,0,768,447,True)
            return True
        else:
            return False

    def resize_window(self):
        win32gui.MoveWindow(self.hwndf,0,0,768,447,True)
        #print(self.main_rect) #(819, 530)794, 480 787, 512

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
        qt_img = screen.grabWindow(self.hwndc).toImage()#FGO視窗及時截圖(記憶體需釋放?) 
        
        img=convertQImageToMat(qt_img)
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        return img2

    def locate_MT(self,needleImage,haystackImage,img_region=None):
        box=pyautolocate(needleImage,haystackImage,grayscale=True,confidence=0.8,region=img_region)  
        if box!=None:
            return (box[0]+(box[2]/2)).astype(int64),(box[1]+(box[3])/2).astype(int64)
        else:
            return None
    

    #img_region is tuple of box
    def find_target_MT(self,needleImage,img_region=None,conf=0.8):
        #模板匹配方法找點擊位置
        screen = QApplication.primaryScreen()
        qt_img = screen.grabWindow(self.hwndc).toImage()#FGO視窗及時截圖(記憶體需釋放?)
        hImg=convertQImageToMat(qt_img)#qtimg 轉 cv2能讀取的格式 
        haystackImage=cv2.cvtColor(hImg,cv2.COLOR_BGR2RGB)      
        # nimg = cv2.imread(needleImage)
        #cv2.imshow("s1",haystackImage)
        # cv2.imshow("s2",nimg)
        # print("n shape:",shape(needleImage))
        # print("h shape:",shape(haystackImage))
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
        #print("find_EP")
        # Initiate SIFT detector
        sift =  cv2.SIFT_create()
        # find the keypoints and descriptors with SIFT
        _, des1 = sift.detectAndCompute(needleImage,None)
        _, des2 = sift.detectAndCompute(haystackImage,None)
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1,des2,k=2)
        #print(len(matches))
        good = 0
        # 如果圖片相近的話 理論上會是一個很近另一個很遠 也就是縮小n後還是大於m 這樣可以相信n是同個點
        for m,n in matches:
            if m.distance < 0.8*n.distance:#特徵距離越小越相近
                good=good+1
        return good


    def locate_EV(self,needleImage,haystackImage):
        #特徵值匹配方法找點擊位置`  `
        print("fff tev")
        # Initiate SIFT detector
        sift =  cv2.SIFT_create()
        # find the keypoints and descriptors with SIFT
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
        # 如果圖片相近的話 理論上會是一個很近另一個很遠 也就是縮小n後還是大於m 這樣可以相信n是同個點
        for m,n in matches:
            if m.distance < 0.8*n.distance:#特徵距離越小越相近
                good.append((m,))
                im2_kp.append(list(kp2[m.trainIdx].pt))

        d=(needleImage.shape[0] if needleImage.shape[0]>needleImage.shape[1] else needleImage.shape[1])/2
        if len(good)<0.2*len(matches):#過濾後
            print("not match",len(good),len(matches))
            return None
        
        print("match",len(good),len(matches))

        dict_num=zeros(len(im2_kp))
        #對每一個特徵點找半徑d內的neighber, neighber最多的特徵點當作點擊位置
        for index,i in enumerate(im2_kp):
            for j in im2_kp:
                if not (i==j):
                    dist = math.dist(i,j)
                    if dist<=d:
                        dict_num[index]=dict_num[index]+1
        p=dict_num.argmax()
        print("p",int(im2_kp[p][0]),int(im2_kp[p][1]))

        return int(im2_kp[p][0]),int(im2_kp[p][1])

def box_center(box):
    return ((box[0]+box[2])/2).astype(int64),((box[1]+box[3])/2).astype(int64)  

def measureTime(func, num):
    tStart = time.time() #計時開始
    for i in range(1000000):
        func(num)
    tEnd = time.time() #計時結束
    print(f"{func.__name__} 總共執行了{(tEnd - tStart):.4f}秒")


# box=pyautolocate("./03.png","./1.png",confidence=0.85)
# print(box)
# print(type(box))
# center_x,center_y=box_center(box)
# print(center_x,center_y)

# do=fgo_action()
# do.adjust_window()
# box=do.rect
# print(box)


# app = QApplication(sys.argv)
# screen = QApplication.primaryScreen()
# img = screen.grabWindow(do.hwndc).toImage()

# img.save("screenshot.jpg")

# def f1():
#     print("f1")

# def f2():
#     print("f2")

# do=fgo_action()
# a=[do.adjust_window,f2]  

# a[1]()


