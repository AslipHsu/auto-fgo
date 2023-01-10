
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt,qAbs,QRect
from PyQt5.QtGui import QPen,QPainter, QColor, QGuiApplication

#相當於開了一個子窗口做節圖動作
class CaptureScreen(QWidget):
    #初始化變量(改變時所有instance 都會跟著變)
    beginPosition = None
    endPosition =None
    fullScreenImage = None
    captureImage = None
    isMousePressLeft = None
    painter = QPainter()

    def __init__(self,pic_url,qlabel,qlabel_2=None,text=None):
        super().__init__()
        self.pic_url=pic_url
        self.qlabel=qlabel
        self.qlabel_2=qlabel_2
        self.text=text
        self.initWindow() #初始化窗口
        self.captureFullScreen() #獲取全屏

    def initWindow(self):
        self.setMouseTracking(True) #鼠標追蹤
        self.setCursor(Qt.CrossCursor)#設置光標
        self.setWindowFlag(Qt.FramelessWindowHint)#窗口無邊框
        self.setWindowState(Qt.WindowFullScreen)#窗口全屏

    def captureFullScreen(self):
        self.fullScreenImage = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId())

    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.beginPosition = event.pos()
            self.isMousePressLeft=True
        if event.button()==Qt.RightButton:
            #如果選取圖片 則按一次右鍵重新開始截圖
            if self.captureImage is not None:
                self.captureImage = None
                self.paintBackgroundImage()
                self.update()
            else:
                self.close()

    def mouseMoveEvent(self, event):
        if self.isMousePressLeft is True:
            self.endPosition = event.pos()
            self.update()

    def mouseReleaseEvent(self,event):
        self.endPosition= event.pos()
        self.isMousePressLeft =False
        if self.captureImage is not None:
            self.saveImage()
            pixmap=QtGui.QPixmap(self.pic_url)
            self.qlabel.setPixmap(pixmap)
            if self.qlabel_2!=None:
                self.qlabel_2.setText(self.text)
            self.close()
            
    def keyPressEvent(self,event):
        if event.key()==Qt.key_Escape:
            self.close()
        if event.key()==Qt.key_Enter or event.key()==Qt.key_Return:
            if self.captureImage():
                self.saveImage()
            # self.picLock.release()
            self.close()
           

    def paintBackgroundImage(self):
        shadowColor = QColor(0,0,0,100)
        self.painter.drawPixmap(0,0,self.fullScreenImage)
        self.painter.fillRect(self.fullScreenImage.rect(),shadowColor)

    def paintEvent(self,event):
        self.painter.begin(self) #開始繪圖
        self.paintBackgroundImage()
        penColor = QColor(30,144,245)#畫筆顏色
        self.painter.setPen(QPen(penColor,1,Qt.SolidLine,Qt.RoundCap))#設置畫筆 藍色1px大小,實線,圓形筆
        if self.isMousePressLeft is True:
            pickRect = self.getRectangle(self.beginPosition,self.endPosition)#獲取要截圖地矩形框
            self.captureImage = self.fullScreenImage.copy(pickRect)#抓截圖的圖片
            self.painter.drawPixmap(pickRect.topLeft(),self.captureImage)#填充截圖
            self.painter.drawRect(pickRect)#畫矩形邊框
        self.painter.end()

    def getRectangle(self,beginPoint,endPoint):
        pickRectWidth = int(qAbs(beginPoint.x()-endPoint.x()))
        pickRectHeight = int(qAbs(beginPoint.y()-endPoint.y()))
        pickRectTop=beginPoint.x() if beginPoint.x()<endPoint.x() else endPoint.x()
        pickRectLeft=beginPoint.y() if beginPoint.y()<endPoint.y() else endPoint.y()
        pickRect = QRect(pickRectTop, pickRectLeft, pickRectWidth, pickRectHeight) 
        #避免高寬為0時報錯
        if pickRectWidth==0:
            pickRect.setWidth(2)
        if pickRectHeight==0:
            pickRect.setHeight(2)
               
        return pickRect

    def saveImage(self):
        self.captureImage.save(self.pic_url,quality=95)




