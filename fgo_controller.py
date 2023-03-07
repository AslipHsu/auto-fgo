from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget ,QMessageBox,QFileDialog
from fgo_ui import Ui_MainWindow
from set_support_class import Ui_set_support_class
from set_skill import Ui_set_skill
from set_attack import Ui_set_attack
from check_card import Ui_check_card
from fgo_click import Fgo_action
from screenshot import CaptureScreen
import time
from sys import settrace
import cv2
import numpy as np
#v1.25

ClassList=[]
Init_Url="./FGOPic/init.png"
NoAp_Url="./FGOPic/no_ap.png"
Yes_Url="./FGOPic/yes.png"
GoldApple_Url="./FGOPic/gold_apple.png"
SilverApple_Url="./FGOPic/silver_apple.png"
CopperApple_Url="./FGOPic/copper_apple.png"
EnterLevel_Url="./FGOPic/enter_level.png"
Support_Url="./FGOPic/support.png"
Support_CraftEssence_Url="./FGOPic/support_CraftEssence.png"
SupportScene_Url="./FGOPic/support_scene.png"
EnterBattleScen_Url="./FGOPic/enter_battle_scene.png"
AttackScene_url="./FGOPic/attack_scene.png"
CardPosition_url="./FGOPic/card_position.png"
EndPic1_url="./FGOPic/end_pic_1.png"
EndPic1_1_url="./FGOPic/end_pic_1_1.png"
EndPic2_url="./FGOPic/end_pic_2.png"
EndPic3_url="./FGOPic/end_pic_3.png"
EndPic4_url="./FGOPic/end_pic_4.png"
EndPic4_1_url="./FGOPic/end_pic_4_1.png"
#detec
Init_box=(642,365, 71,20)
NoAp_box=(314,21, 105, 34)

Support_class=None
SupportScene_box=(597, 2, 132, 46)

#好友支援職階 9種: 全 劍 弓 槍 騎 術 殺 狂 特
Class_click=[(56,75),(94,75),(132,75),(170,75),(208, 75),(246,75),(284,75),(322,75),(360,75)]
RandomSupport_click=(300, 165)

EnterBattleScene_box=(598, 4, 132, 32)
EnterBattle_click=(670, 384)

AttackScene_box=(610, 300, 80, 32)
Attack_click=(652, 318)

ServerSkill={"s11":(45,333),"s12":(95,333),"s13":(145,333),\
    "s21":(225, 333),"s22":(275,333),"s23":(325,333),\
    "s31":(409,333),"s32":(456,333),"s33":(507,333)}

CraftSkill_click=(680,183)
CraftSkill={"c1":(517,180),"c2":(571,180),"c3":(620,180)}
EnemySite={"e1":(26,25),"e2":(169,25),"e3":(313,25)}
ServerSite={"s1":(172,240),"s2":(359,240),"s3":(546,240)}

Card_click=[(68,315),(216,315),(364,315),(512,315),(660,315)]#5張卡的位置
Crad_boxs=[(20, 231,107,128),(174, 233, 98, 128),(319, 228, 102,131),(466,229, 99,130),(614,223,103,133)]

Server_area=[(18,214,160,93),(207,207,155,101),(385,209,156,97)]
Server_click=[(89,275),(273,268),(464,264)]
Server_img={}
SetCrad_roll=(363,213)
SetCrad_img={}
SetCardDetect_url="./FGOPic/set_card_detect.png"
SetCardQ_url="./FGOPic/set_card_Q.png"
SetCardA_url="./FGOPic/set_card_A.png"
SetCardB_url="./FGOPic/set_card_B.png" 
SetCardClose=(624,36)

DetectBattle1_url="./FGOPic/battle_1.png" 
DetectBattle2_url="./FGOPic/battle_2.png" 
DetectBattle3_url="./FGOPic/battle_3.png" 
DetectBattle_box=(507, 9, 8, 11)

NobleCrad={"s1":( 238,120),"s2":( 368,120),"s3":( 498,120)} 
ChangeStasr={"s1":(78,200),"s2":( 192 ,200),"s3":(307,200)}
ChangeSub={"s1":(422 ,200),"s2":(534,200),"s3":(654 ,200)}
ChangeOK_click=(367,357)

End_1_box=(35,90,141,32)
End_1_click=(104,108)
End_1_1_box=(376,258,131,20)
End_1_1_click=(104,108)
End_2_box=(365, 100, 97, 31)
End_2_click=(414, 116)
End_3_box=(570, 345,112,39)
End_3_click=( 628 ,367)
End_4_box=(205, 305,91, 37)
End_4_click=( 249 ,324)
End_4_1_box=(154,338,69, 27)
End_4_1_click=( 188 ,351)
#
CardSet_box=(302,172,62,20)

#載入圖片
Init_pic=cv2.imread(Init_Url) 
NoAp_pic=cv2.imread(NoAp_Url) 
Yes_pic=cv2.imread(Yes_Url) 
GoldApple_pic=cv2.imread(GoldApple_Url) 
SilverApple_pic=cv2.imread(SilverApple_Url) 
CopperApple_pic=cv2.imread(CopperApple_Url) 
SupportScene_pic=cv2.imread(SupportScene_Url) 
EnterBattle_pic=cv2.imread(EnterBattleScen_Url)
Attack_pic=cv2.imread(AttackScene_url)
SetCardDetect_pic=cv2.imread(SetCardDetect_url)
SetCardQ_pic=cv2.imread(SetCardQ_url)
SetCardA_pic=cv2.imread(SetCardA_url)
SetCardB_pic=cv2.imread(SetCardB_url)
End_pic_1=cv2.imread(EndPic1_url)
End_pic_1_1=cv2.imread(EndPic1_1_url)
End_pic_2=cv2.imread(EndPic2_url)
End_pic_3=cv2.imread(EndPic3_url)
End_pic_4=cv2.imread(EndPic4_url)
End_pic_4_1=cv2.imread(EndPic4_1_url)

def matToQpix(img):
    img2=cv2.resize(src=img,dsize=None,fx=1,fy=1)
    img3=QtGui.QImage(img2[:],img2.shape[1], img2.shape[0],img2.shape[1] * 3, QtGui.QImage.Format_RGB888)
    return QtGui.QPixmap.fromImage(img3)

class FindTargetErr(Exception):
    def __init__(self,e):
        self.e=e
    def __str__(self):
        return self.e

class StopThread(Exception):
    def __init__(self):
        pass

class TextBuff():
    def __init__(self):
        self.pointer=0
        self.data=[None]*3

    def reset(self):
        self.data=[None]*3

    def addData(self,n,data):
        try:
            self.pointer=n
            self.data[n]=data

        except Exception as e:
            print(e)  

    def previous(self):
        try:
            if self.pointer>0:
                self.pointer=self.pointer-1
                return self.data[self.pointer]
            return ""
        except Exception as e:
            print(e)

#subwindow(set_support_class)
class SubWindow_1(QWidget):
    def __init__(self,picurl=None,setLabel=None,setLabel_2=None):
        super().__init__()
        self.picurl=picurl
        self.setLabel=setLabel
        self.setLabel_2=setLabel_2
        self.ui = Ui_set_support_class()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.pushButton.clicked.connect(self.ok)
        self.ui.pushButton_2.clicked.connect(self.cancel)

    #subwindow (set_support_class)
    def ok(self):
        if self.picurl!=None:
            i=self.ui.comboBox.currentIndex()
            t=self.ui.comboBox.currentText()
            print(i,t)
            global Support_class
            Support_class=(i,t)
            self.screenshot_window = CaptureScreen(self.picurl,self.setLabel,self.setLabel_2,t)
            self.screenshot_window.show()
            self.close()
        else:
            # 改設定
            self.setLabel_2.setText(self.ui.comboBox.currentText())
    def cancel(self):
         self.close()

#subwindow(set_skill)
class SubWindow_2(QWidget):
    def __init__(self,main_textEdit):
        super().__init__()
        self.main_textEdit=main_textEdit
        self.ui = Ui_set_skill()
        self.ui.setupUi(self)
        self.setup_control()
        self.ui.textEdit.setText(main_textEdit.toPlainText())

    def setup_control(self):
        self.ui.buttonGroup.setId(self.ui.radioButton,1)
        self.ui.buttonGroup.setId(self.ui.radioButton_2,2)
        
        self.ui.pushButton.clicked.connect(self.addSetting)
        self.ui.pushButton_2.clicked.connect(self.ui.textEdit.clear)
        self.ui.pushButton_3.clicked.connect(self.ok)
        self.ui.pushButton_4.clicked.connect(self.cancel)

        self.ui.radioButton.click()
    def addSetting(self):
        if (not self.ui.checkBox.isChecked()) and (not self.ui.checkBox_2.isChecked()):
            QMessageBox.information(self,"標題","請勾選並設定Battle或TURN",QMessageBox.Yes)
            return
        msg = self.ui.textEdit.toPlainText() 
        print(msg)
        
        value=""
        if self.ui.buttonGroup.checkedId()==1:
            value="skill-"
            if self.ui.comboBox.currentIndex()<9:#從者技能1-1~3-3
                value=value+"s"+self.ui.comboBox.currentText()[-3]+self.ui.comboBox.currentText()[-1]
            else:#禮裝技能
                value=value+"c"+self.ui.comboBox.currentText()[-1]

            if self.ui.comboBox_2.currentIndex()!=0:
                value=value+"-s" if self.ui.comboBox_2.currentIndex()<4 else value+"-e"
                value=value+self.ui.comboBox_2.currentText()[-1]

        elif self.ui.buttonGroup.checkedId()==2:
            value="change-s"+self.ui.comboBox_3.currentText()[-1]+"-s"+self.ui.comboBox_4.currentText()[-1]
        print("v ",value)

        key=""
        if self.ui.checkBox.isChecked():
            key=key+"B"+str(self.ui.lineEdit.text())  
        if self.ui.checkBox_2.isChecked():
            key=key+"T"+str(self.ui.lineEdit_2.text())
        msg_map=dict()
        if msg!="":
            msg_map=eval(msg)
        print("k ",key)
        if key in msg_map:
            msg_map[key].append(value)
        else:
            msg_map[key]=[value]

        m=str(msg_map).replace("],","],\n",-1).replace(": ",":",-1)
        m=m.replace(", ",",",-1)
        self.ui.textEdit.setText(m)


    def ok(self):
        self.main_textEdit.setText(self.ui.textEdit.toPlainText())
        #msg設置全域變數?
        self.close()

    def cancel(self):
         self.close()

#subwindow(set_attack)
class SubWindow_3(QWidget):
    def __init__(self,main_textEdit):
        super().__init__()
        self.main_textEdit=main_textEdit
        self.ui = Ui_set_attack()
        self.ui.setupUi(self)
        self.setup_control()
        self.ui.textEdit.setText(main_textEdit.toPlainText())

    def setup_control(self):
        self.ui.pushButton_5.clicked.connect(self.addAttack)
        self.ui.pushButton.clicked.connect(self.addNoble)
        self.ui.pushButton_2.clicked.connect(self.ui.textEdit.clear)
        self.ui.pushButton_3.clicked.connect(self.ok)
        self.ui.pushButton_4.clicked.connect(self.cancel)

    def addNoble(self):
        if (not self.ui.checkBox.isChecked()) and (not self.ui.checkBox_2.isChecked()):
            QMessageBox.information(self,"標題","請勾選並設定Battle或TURN",QMessageBox.Yes)
            return
        msg = self.ui.textEdit.toPlainText() 
        print(msg)

        value=""
        if self.ui.checkBox.isChecked():
            value=value+"B"+str(self.ui.lineEdit.text())
        
        if self.ui.checkBox_2.isChecked():
            value=value+"T"+str(self.ui.lineEdit_2.text())
        value=value+"-"+"s"+self.ui.comboBox_7.currentText()[-1]
        if self.ui.comboBox_11.currentIndex()>0:
            value=value+"-"+"e"+self.ui.comboBox_11.currentText()[-1]
        msg_map=dict()
        if msg!="":
            msg_map=eval(msg)

        key="Noble"
        if key in msg_map:
            msg_map[key].append(value)
        else:
            msg_map[key]=[value]

        m=str(msg_map).replace("],","],\n",-1).replace(": ",":",-1)
        m=m.replace(", ",",",-1)
        self.ui.textEdit.setText(m)

    def addAttack(self):
        msg = self.ui.textEdit.toPlainText()
        print(msg)
        
        value=["s"+self.ui.comboBox.currentText()[-3]+self.ui.comboBox.currentText()[-1]]
        value.append("s"+self.ui.comboBox_2.currentText()[-3]+self.ui.comboBox_2.currentText()[-1])
        value.append("s"+self.ui.comboBox_3.currentText()[-3]+self.ui.comboBox_3.currentText()[-1])
        value.append("s"+self.ui.comboBox_4.currentText()[-3]+self.ui.comboBox_4.currentText()[-1])
        value.append("s"+self.ui.comboBox_5.currentText()[-3]+self.ui.comboBox_5.currentText()[-1])
        value.append("s"+self.ui.comboBox_6.currentText()[-3]+self.ui.comboBox_6.currentText()[-1])
        value.append("s"+self.ui.comboBox_9.currentText()[-3]+self.ui.comboBox_9.currentText()[-1])
        value.append("s"+self.ui.comboBox_8.currentText()[-3]+self.ui.comboBox_8.currentText()[-1])
        value.append("s"+self.ui.comboBox_10.currentText()[-3]+self.ui.comboBox_10.currentText()[-1])

        key="Attack"
        msg_map=dict()
        if msg!="":
            msg_map=eval(msg)
        msg_map[key]=value

        m=str(msg_map).replace("],","],\n",-1).replace(": ",":",-1)
        m=m.replace(", ",",",-1)
        self.ui.textEdit.setText(m)
    
    def ok(self):
        self.main_textEdit.setText(self.ui.textEdit.toPlainText())
        self.close()

    def cancel(self):
         self.close()

#subwindow4(check_card)
class SubWindow_4(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_check_card()
        self.ui.setupUi(self)
        
        # self.ui.label.setPixmap(matToQpix(T))
        self.ui.label.setPixmap(matToQpix(SetCrad_img["s1Q"]))
        self.ui.label_2.setPixmap(matToQpix(SetCrad_img["s1A"]))
        self.ui.label_3.setPixmap(matToQpix(SetCrad_img["s1B"]))
        self.ui.label_4.setPixmap(matToQpix(SetCrad_img["s2Q"]))
        self.ui.label_5.setPixmap(matToQpix(SetCrad_img["s2A"]))
        self.ui.label_6.setPixmap(matToQpix(SetCrad_img["s2B"]))
        self.ui.label_7.setPixmap(matToQpix(SetCrad_img["s3Q"]))
        self.ui.label_8.setPixmap(matToQpix(SetCrad_img["s3A"]))
        self.ui.label_9.setPixmap(matToQpix(SetCrad_img["s3B"]))


#main window
class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_control()
        self.do=Fgo_action()
        if self.do.setup()==False:
            self.ui.label_2.setStyleSheet("color:red")
            self.ui.label_2.setText("Can't find FGO !")
        else:
            rect=self.do.getWindow_rect()
            print("now size:",rect)
            self.ui.label_2.setStyleSheet("color:black")
            self.ui.label_2.setText("FGO running ("+str(rect[0])+"x"+str(rect[1])+")")
        self.schedulelist=[]
        self.Tbuff=TextBuff()
        #self.killed=False

    def setup_control(self):
        self.ui.buttonGroup.setId(self.ui.radioButton_3,1)
        self.ui.buttonGroup.setId(self.ui.radioButton_4,2)
        # self.ui.buttonGroup_2.setId(self.ui.radioButton,1)
        # self.ui.buttonGroup_2.setId(self.ui.radioButton_2,2)
        # self.ui.buttonGroup_3.setId(self.ui.radioButton_5,1)
        # self.ui.buttonGroup_3.setId(self.ui.radioButton_6,2)   
        self.ui.buttonGroup_4.setId(self.ui.radioButton_7,1)
        self.ui.buttonGroup_4.setId(self.ui.radioButton_8,2)   
        self.ui.buttonGroup_5.setId(self.ui.radioButton_9,1)
        self.ui.buttonGroup_5.setId(self.ui.radioButton_10,2)   

        self.ui.radioButton_3.click()
        # self.ui.radioButton.click()
        # self.ui.radioButton_5.click()
        self.ui.radioButton_7.click()
        self.ui.radioButton_9.click()

        self.ui.pushButton.clicked.connect(self.runScript)
        self.ui.pushButton_4.clicked.connect(self.doPrevious)
        self.ui.pushButton_6.clicked.connect(self.load)
        self.ui.pushButton_8.clicked.connect(self.save)
        self.ui.pushButton_7.clicked.connect(self.clear)
        self.ui.pushButton_5.clicked.connect(self.stop)

        self.ui.pushButton_2.clicked.connect(lambda: self.screenShot(self.ui.label_3,EnterLevel_Url))
        self.ui.pushButton_13.clicked.connect(lambda: self.screenShot(self.ui.label_16,Support_Url))
        # self.ui.pushButton_10.clicked.connect(lambda: self.screenShot(self.ui.label_10,Support_CraftEssence_Url))

        # self.ui.label_19.clicked.connect(self.resetClass)
        self.ui.radioButton_3.clicked.connect(self.ui.label_16.clear)
        self.ui.radioButton_3.clicked.connect(self.ui.label_19.clear)
        self.ui.radioButton_4.clicked.connect(lambda: self.setSelfDefine(Support_Url))
        # self.ui.radioButton.clicked.connect(self.ui.label_10.clear)
        # self.ui.radioButton_2.clicked.connect(lambda: self.setSelfDefine(Support_CraftEssence_Url))

        self.ui.pushButton_3.clicked.connect(lambda: self.addSchedule("enter_level"))
        self.ui.pushButton_11.clicked.connect(lambda: self.addSchedule("choose_support"))
        self.ui.pushButton_14.clicked.connect(lambda: self.addSchedule("battle"))
        self.ui.pushButton_15.clicked.connect(self.setSkill)
        self.ui.pushButton_16.clicked.connect(self.setAttack)
        self.ui.pushButton_17.clicked.connect(self.checkCard)

        self.ui.pushButton_9.clicked.connect(lambda: self.detectFGO())

    # 停止thread
    def stop(self):
        try:
            self.worker.kill()
        # self.ui.pushButton.setEnabled(True)
        except Exception as e:
            print(e)

    def doPrevious(self):
        self.ui.textEdit.setText(self.Tbuff.previous())

    def clear(self):
        self.Tbuff.reset()
        self.ui.textEdit.setText("")

    def load(self):
        try:
            filename, _ = QFileDialog.getOpenFileName(self, "Open folder", "./save",filter="TXT (*.txt)")
            #folder_path = QFileDialog.getExistingDirectory(self, "Open folder", "./")
            print("load:",filename)
            file = open(filename,'r')  
            text = file.read()  
            self.ui.textEdit.setText(text)
            file.close()   
        except Exception as e:
            print("load err:",e)

    def save(self):
        try:
            #存text
            print("save")
            text=self.ui.textEdit.toPlainText()
            filename, _ =QFileDialog.getSaveFileName(self, "save folder", "./save/output.txt",)
            f = open(filename, 'w')
            f.write(text)
            f.close()
            # 存圖片
        except Exception as e:
            print("save err:",e)

    # 截圖
    def screenShot(self,setLabel,picurl):
        #選擇自訂義才給截圖
        if (picurl==Support_Url and self.ui.buttonGroup.checkedId()==1) or \
            (picurl==Support_CraftEssence_Url and self.ui.buttonGroup_2.checkedId()==1):
                return
        
        # if picurl==Support_Url:#支援 設定職階
        #     self.subwindow=SubWindow_1(picurl,setLabel,self.ui.label_19)
        #     self.subwindow.show()
        # else:
        #     self.screenshot_window = CaptureScreen(picurl,setLabel)
        #     self.screenshot_window.show()

        self.screenshot_window = CaptureScreen(picurl,setLabel)
        self.screenshot_window.show()
        print("Your url is: ",picurl)

    #進階設置技能
    def setSkill(self):
        if self.ui.buttonGroup_4.checkedId()==2:
            self.subwindow=SubWindow_2(self.ui.textEdit_2)
            self.subwindow.show()

    #進階設置攻擊
    def setAttack(self):
        if self.ui.buttonGroup_5.checkedId()==2:
            self.subwindow=SubWindow_3(self.ui.textEdit_3)
            self.subwindow.show()

    #查看卡片
    def checkCard(self):
        if "s3B" in SetCrad_img:
            self.subwindow=SubWindow_4()
            self.subwindow.show()

    #支援職階重設(需要?)
    def resetClass(self):
        print(self.ui.label_19.text)
        if self.ui.label_19.text()!=None:
            self.subwindow=SubWindow_1(None,None,self.ui.label_19)
            self.subwindow.show()

    #自定義設置
    def setSelfDefine(self,pic_url):
        pixmap=QtGui.QPixmap(pic_url)
         #顯示截圖
        if pic_url==Support_Url:
            self.ui.label_16.setPixmap(pixmap)
            #顯示職階
            if Support_class!=None:
                self.ui.label_19.setText(Support_class[1])
        elif pic_url==Support_CraftEssence_Url:
            self.ui.label_10.setPixmap(pixmap)

    #加入動作排程
    def addSchedule(self,action):
        msg = self.ui.textEdit.toPlainText() 
        now_step=msg.count("\n")

        if action=="enter_level" and now_step==0:
            global EnterLevel_Url
            EnterLevel_Url="./FGOPic/enter_level.png"
            msg=msg+str(now_step+1)+". "+action
            id=self.ui.comboBox_7.currentIndex()
            if id>0 and id<4:#金銀銅蘋果 
                msg=msg+" "+str(id)
            msg=msg+"\n"
            pixmap=QtGui.QPixmap(EnterLevel_Url)
            self.ui.label_3.setPixmap(pixmap)
            self.Tbuff.addData(0,msg)

        elif action=="choose_support" and now_step==1:
            #讀取設定
            global Support_Url,Support_CraftEssence_Url
            Support_Url="./FGOPic/support.png"
            Support_CraftEssence_Url="./FGOPic/support_CraftEssence.png"
            set_a=self.ui.buttonGroup.checkedId()
            # set_b=self.ui.buttonGroup_2.checkedId()
            # set_c=self.ui.buttonGroup_3.checkedId()
            setup=[set_a]#[從者(1無 2自訂),禮裝(1無 2自訂),優先度(1從者 2禮裝)]
            msg = msg+str(now_step+1)+". "+action+" "+str(setup).replace(", ",",",-1)+"\n"
            self.Tbuff.addData(1,msg)

        elif action=="battle"and now_step==2:
            button_4=self.ui.buttonGroup_4.checkedId()
            button_5=self.ui.buttonGroup_5.checkedId()
            textedit_2=self.ui.textEdit_2.toPlainText()
            textedit_3=self.ui.textEdit_3.toPlainText()
            if (button_4==2 and len(textedit_2)==0) or (button_5==2 and len(textedit_3)==0):
                QMessageBox.information(self,"標題","自訂內容空白",QMessageBox.Yes)
                return
            msg=msg+str(now_step+1)+". "+action
            if button_4==1:
                msg=msg+" "+"NoSkillSetting"
            elif button_4==2:
                msg_t=textedit_2.replace("\n"," ",-1)
                msg_t=msg_t.replace(",  ",",",-1)
                msg=msg+" "+msg_t
            if button_5==1:
                msg=msg+" "+"AutoChooseCard"
            elif button_5==2:
                msg_t=textedit_3.replace("\n"," ",-1)
                msg_t=msg_t.replace(",  ",",",-1)
                msg_t=msg_t.replace("} ","}",-1)
                msg=msg+" "+msg_t
            msg=msg+"\n"
            self.Tbuff.addData(2,msg)

        self.ui.textEdit.setText(msg)

    def setBrowser(self,txt):
        if txt=="":
            self.ui.textBrowser.setText("")
        else:
            self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText()+txt)
    def runScript(self):
        self.ui.pushButton.setEnabled(False)
        msg = self.ui.textEdit.toPlainText() 
        schedulelist=msg.split("\n")[:-1]# 去掉最後一格為空['1. enter_level', '']
        print("sc list:",schedulelist)

        self.thread = QtCore.QThread()

        self.worker = DoSchedulel()

        self.worker.schedulelist=schedulelist
        self.worker.do=self.do
        self.worker.run_times=int(self.ui.lineEdit.text())
        self.worker.enterLevel_pic=cv2.imread(EnterLevel_Url)
        self.worker.support_pic=cv2.imread(Support_Url)
        self.worker.support_CraftEssence_pic=cv2.imread(Support_CraftEssence_Url)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.textBrowser.connect(self.setBrowser)
        self.worker.finished.connect(lambda: self.ui.pushButton.setEnabled(True))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread 
        self.thread.start()

    #調整視窗大小&偵測FGO
    def detectFGO(self):
        if self.do.setup()==False:
            self.ui.label_2.setStyleSheet("color:red")
            self.ui.label_2.setText("Can't find FGO !")
        else:
            rect=self.do.getWindow_rect()
            self.ui.label_2.setStyleSheet("color:black")
            self.ui.label_2.setText("FGO running ("+str(rect[0])+"x"+str(rect[1])+")")
            print("now size: ",rect)

#############################################################################

class DoSchedulel(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    runscrpt = QtCore.pyqtSignal()
    textBrowser=QtCore.pyqtSignal(str)

    # def __init__(self,schedulelist,do,run_times=1):
    def __init__(self):
        super().__init__()
        self.battle_img=None
        self.battle=0
        self.battle_flag={}#判斷是否battle的第一回合
        self.killed = False

    #避免stop按鈕無法立即停止線呈
    def time_wait(self,t):
        while t>=1:
            t-=1
            time.sleep(1)
        if t>0:
            time.sleep(t)

    def detectScene(self,pic,times,region,conf=0.8):
        i=0
        while i<times:
            if self.do.find_target_MT(pic,region,conf)!=None:
                return True
            i=i+1
            self.time_wait(1)
        return False

    def detectAttack(self,pic,times,region):
        i=0
        # ischeckBattle=True
        while i<times:
            img_w=self.do.grabWindowImg()
            if self.do.locate_MT(End_pic_1,img_w,End_1_box)!=None:
                return False
            if self.do.locate_MT(pic,img_w,region)!=None:
                return True
            i=i+1
            self.time_wait(1)
        return False
    
    #enterLevel
    def enterLevel(self,act): 
        #檢查進入關卡
        xy=self.do.find_target_MT(self.enterLevel_pic)
        if xy==None:
            raise FindTargetErr("can't find enterLevel_pic")
        self.do.to_click(xy[0],xy[1])
        #吃蘋果
        if self.detectScene(NoAp_pic,2,NoAp_box) and len(act)==3:
            eat_act=int(act[2])
            if eat_act==1:
                a=self.do.find_target_MT(GoldApple_pic)
                self.do.to_click(a[0],a[1])
            elif eat_act==2:
                a=self.do.find_target_MT(SilverApple_pic)
                self.do.to_click(a[0],a[1])
            elif eat_act==3:
                self.do.to_roll(377,257)
                self.time_wait(1)
                a=self.do.find_target_MT(CopperApple_pic)
                self.do.to_click(a[0],a[1])

            a=self.do.find_target_MT(Yes_pic)
            self.do.to_click(a[0],a[1])
            
            
    #chooseSupport
    def chooseSupport(self,act):
        set=eval(act)
        #確認進入支援選擇後 依序查看各職階是否有符合設定的支援?
        if not self.detectScene(SupportScene_pic,3,SupportScene_box):
            raise FindTargetErr("choose_support detectScene err")
        location=None
        #[從者] 
        if set[0]==2:
            for i in range(10):
                location=self.do.find_target_MT(self.support_pic)
                if location!=None:
                    break
                self.do.to_roll(363 ,287)
                self.time_wait(0.5)
            if location==None:
                location=(159,124)
        #[隨便選一個支援]
        else:
                #隨便選
                location=RandomSupport_click
        self.do.to_click(location[0],location[1])
        #檢查進入戰鬥確認
        if not self.detectScene(EnterBattle_pic,5,EnterBattleScene_box):
            raise FindTargetErr("enterBattle_pic detectScene err")
        #進入戰鬥
        self.do.to_click(EnterBattle_click[0],EnterBattle_click[1])
        while self.detectScene(Attack_pic,40,AttackScene_box):
                #轉場
                break

    #find card box from positionBox and coordinate-x 
    def findCard(self,pB,card_x):
        print("find card")
        #set_card_detect
        if 137<card_x<199:
            return (pB[0]-225,pB[1]+47,64,70)#137~199
        elif 234<card_x<294:
            return (pB[0]-130,pB[1]+47,64,70)#234~294
        elif 330<card_x<390:
            return (pB[0]-35,pB[1]+47,64,70)#330~390
        elif 426<card_x<485:
            return (pB[0]+60,pB[1]+47,64,70)#426 485
        elif 519<card_x<580:
            return (pB[0]+155,pB[1]+47,64,70)#519~580

    #set server Q A B card
    #s=0,1,2 (從者)
    def setCard(self,s):
        self.time_wait(1)
        print(self.detectScene(Attack_pic,1,AttackScene_box))
        self.do.to_click(Server_click[s][0],Server_click[s][1])
        self.time_wait(1)
        self.do.to_roll(SetCrad_roll[0],SetCrad_roll[1])
        self.time_wait(1)
        detect_box=self.do.find_target_MT(SetCardDetect_pic)
        w_img=self.do.grabWindowImg()
        cardQ_xy=self.do.locate_MT(SetCardQ_pic,w_img)
        # print(cardQ_xy)
        cardA_xy=self.do.locate_MT(SetCardA_pic,w_img)
        #print(cardA_xy)
        cardB_xy=self.do.locate_MT(SetCardB_pic,w_img)
        #print(cardB_xy)
        box_Q=self.findCard(detect_box,cardQ_xy[0])
        #print(box_Q)
        box_A=self.findCard(detect_box,cardA_xy[0])
        #print(box_A)
        box_B=self.findCard(detect_box,cardB_xy[0])
        #print(box_B)
        Qcard=w_img[box_Q[1]:box_Q[1]+box_Q[3],box_Q[0]:box_Q[0]+box_Q[2]]
        Acard=w_img[box_A[1]:box_A[1]+box_A[3],box_A[0]:box_A[0]+box_A[2]]
        Bcard=w_img[box_B[1]:box_B[1]+box_B[3],box_B[0]:box_B[0]+box_B[2]]
                
        SetCrad_img["s"+str(s+1)+"Q"]=Qcard
        SetCrad_img["s"+str(s+1)+"A"]=Acard
        SetCrad_img["s"+str(s+1)+"B"]=Bcard
        self.time_wait(1)
        self.do.to_click(SetCardClose[0],SetCardClose[1])

    def checkB(self):
        self.time_wait(0.5)
        img_w=self.do.grabWindowImg()
        box=DetectBattle_box
        img_box=img_w[box[1]:box[1]+box[3],box[0]:box[0]+box[2]]
        image_box = cv2.cvtColor(img_box, cv2.COLOR_RGB2GRAY)
        _, img_bin = cv2.threshold(image_box, 125, 1, cv2.THRESH_BINARY)
        if self.battle==0:
            self.battle=1
            self.battle_img=img_bin
        else:
            img_xor=cv2.bitwise_xor(img_bin,self.battle_img)
            print("bsum 1: ",np.sum(img_xor))
            bsum=np.sum(img_xor)
            print("bsum 2: ",bsum)
            if bsum>10:
                self.battle+=1
                self.battle_img=img_bin

    #doBattle
    def doBattle(self,act,t):
        #解析map
        skill_map,attack_map={},{}
        if act[2]!="NoSkillSetting":
            skill_map=eval(act[2])
            print(skill_map)
        if act[3]!="AutoChooseCard":
            attack_map=eval(act[3]) 
            print(attack_map)    
            if t==0 and "Attack" in attack_map:
                #辨識從者卡片的設置
                self.setCard(0)
                self.setCard(1)
                self.setCard(2)
            
        #進入戰鬥迴圈 回合結束檢查到attack代表 還在戰鬥階段
        self.battle_flag={}
        self.battle=0
        turn=1
        print("b1")
        while self.detectAttack(Attack_pic,45,AttackScene_box):
            #檢測battle
            self.checkB()
            
            #只勾選battle的話 默認為battle N 的第一回合
            # battle=0#(還沒加)
            b,t="B"+str(self.battle),"T"+str(turn)
            bt=""
            #判斷是否發動技能和卡片選擇方式
            if b in skill_map and b not in self.battle_flag:
                bt=b
            elif t in skill_map:
                bt=t
            elif b+t in skill_map:
                bt=b+t
            print("bt ",bt)
            #點選技能
            self.useSkill(skill_map,bt)

            #判斷寶具對象
            self.lockEnemy(attack_map,b,t)

            #點攻擊按鈕
            self.do.to_click(Attack_click[0],Attack_click[1])
            self.time_wait(1)

            #進行攻擊 點選卡片
            self.chooseCard(attack_map,b,t)

            self.battle_flag[b]=True#標記 之後同樣回合都不再執行
            turn+=1

    #battleEnd
    def battleEnd(self):
        # end detect 結束場景
        if self.detectScene(End_pic_1,5,End_1_box):
            print("battle end 1")
            self.time_wait(0.5)
            self.do.to_click(End_1_click[0],End_1_click[1])
        while self.detectScene(End_pic_1_1,2,End_1_1_box):#羈絆升級
            print("battle end 1_1")
            self.time_wait(0.5)
            self.do.to_click(End_1_1_click[0],End_1_1_click[1])
            self.time_wait(0.5)
        if self.detectScene(End_pic_2,3,End_2_box):
            print("battle end 2")
            self.time_wait(0.5)
            self.do.to_click(End_2_click[0],End_2_click[1])
        while self.detectScene(End_pic_3,3,End_3_box):
            print("battle end 3")
            self.time_wait(0.5)
            self.do.to_click(End_3_click[0],End_3_click[1])
            self.time_wait(0.5)
        if self.detectScene(End_pic_4_1,2,End_4_1_box):
            print("battle end 4_1")
            self.time_wait(0.5)
            self.do.to_click(End_4_1_click[0],End_4_1_click[1])         
        if self.detectScene(End_pic_4,3,End_4_box):
            print("battle end 4")
            self.time_wait(0.5)
            self.do.to_click(End_4_click[0],End_4_click[1])
        while self.detectScene(Init_pic,20,Init_box):
                #回到主畫面
                break

    #useSkill
    def useSkill(self,skill_map,bt):
        print("useSkill")
        if skill_map=={} or bt=="":
           return
        for s in skill_map[bt]:
            print("s: ",s)
            ss=s.split("-")
            if ss[0]=="skill":
                if len(ss)==3 and ss[2][0]=="e": #以敵人為對象
                    ss_xy2=EnemySite[ss[2]]
                    self.do.to_click(ss_xy2[0],ss_xy2[1]) 
                if ss[1][0]=="s":#從者技能
                    ss_xy1=ServerSkill[ss[1]]
                    self.do.to_click(ss_xy1[0],ss_xy1[1])
                elif ss[1][0]=="c":#禮裝技能
                    self.do.to_click(CraftSkill_click[0],CraftSkill_click[1])
                    self.time_wait(1)
                    ss_xy1=CraftSkill[ss[1]]
                    self.do.to_click(ss_xy1[0],ss_xy1[1])
                if len(ss)==3 and ss[2][0]=="s": #以從者為對象
                    ss_xy2=ServerSite[ss[2]]
                    self.do.to_click(ss_xy2[0],ss_xy2[1]) 
            elif ss[0]=="change":
                ss_xy1=CraftSkill[ss[1]]
                self.do.to_click(ss_xy1[0],ss_xy1[1])
                if len(ss)==3:
                    ss_xy2=CraftSkill[ss[2]]
                    self.do.to_click(ss_xy2[0],ss_xy2[1])
            while self.detectScene(Attack_pic,5,AttackScene_box):
                #發動技能動畫延遲?秒 
                break

    #lockEnemy    
    def lockEnemy(self,attack_map,b,t):
        if "Noble" not in attack_map:
            return
        for card_n in attack_map["Noble"]:
            card=card_n.split("-")
            if b+t!=card[0] and t!=card[0] and \
                (b!=card[0] or b in self.battle_flag):
                continue
            if len(card)==3:
                print("lockEnemy ",card[2])
                e=EnemySite[card[2]]
                self.do.to_click(e[0],e[1])
                self.time_wait(0.5)
                break
                    
    #chooseCard
    def chooseCard(self,attack_map,b,t):
        print("chooseCard")
        if attack_map=={}:
            #點前三張
            self.do.to_click(Card_click[0][0],Card_click[0][1])
            self.do.to_click(Card_click[1][0],Card_click[1][1])
            self.do.to_click(Card_click[2][0],Card_click[2][1])
        choose=0
        delay=0
        if "Noble" in attack_map:
            print(attack_map["Noble"])
            for card_n in attack_map["Noble"]:
                card=card_n.split("-")
                if b+t!=card[0] and t!=card[0] and \
                (b!=card[0] or b in self.battle_flag):
                    continue
                c=NobleCrad[card[1]]
                self.do.to_click(c[0],c[1])
                choose=choose+1
                delay+=4#發動寶具多等幾秒
                    
        if "Attack" in attack_map:
            print(attack_map["Attack"])
            img_w=self.do.grabWindowImg()
            img_w = cv2.cvtColor(img_w, cv2.COLOR_RGB2GRAY)###########################
            cardlist=["","","","",""]
            for i,box in enumerate(Crad_boxs):
                img_box=img_w[box[1]:box[1]+box[3],box[0]:box[0]+box[2]]
                max_cardEP=["",0]#["s1Q",13]

                for cimg in SetCrad_img.items():
                    ep=self.do.find_EP(cimg[1],img_box)
                    if ep>max_cardEP[1]:
                        max_cardEP[0]=cimg[0]#key
                        max_cardEP[1]=ep#value
                        #print("ep  ",max_cardEP[0],max_cardEP[1])
                cardlist[i]=max_cardEP[0]
            print("cardlist: ",cardlist)

            for card_a in attack_map["Attack"]:
                for i,card_c in enumerate(cardlist):
                    if card_a==card_c:
                        c=Card_click[i]
                        self.do.to_click(c[0],c[1])
                        choose=choose+1
                        print("choose card:",card_c)
                if choose>=5:
                    break
        self.time_wait(1+delay)#攻擊動畫延遲?秒 

    #run 
    def run(self): 
        """Long-running task.""" 
        settrace(self.globaltrace)#終止用 
        #fm42ul4 
        try: 
            self.textBrowser.emit("")
            print(self.schedulelist)
            t=0
            while t<self.run_times:
                self.textBrowser.emit("第"+str(t+1)+"輪\n")
                for action in self.schedulelist:
                    print(action)
                    act=action.split(" ")
                    print(act)
                    if act[1]=="enter_level":
                        self.enterLevel(act)
                    elif act[1]=="choose_support":
                        self.chooseSupport(act[2])
                        print("choose end")
                    if act[1]=="battle":
                        print("battle")
                        self.doBattle(act,t)
                        self.battleEnd()
                #end action
                t=t+1
            self.finished.emit()
            print("thread end")
        except FindTargetErr as e:
            self.finished.emit()
            # print(f"DoSchedulel thread end by FindTargetErr:\n{e}")
            self.textBrowser.emit(f"DoSchedulel thread end by FindTargetErr:\n{e}")
        except StopThread:
            self.finished.emit()
            # print(f"DoSchedulel thread end by stop")
            self.textBrowser.emit("DoSchedulel thread end by stop")
        except Exception as e:
            self.finished.emit()
            # print(f"DoSchedulel thread end by Exception:\n{e}")
            self.textBrowser.emit(f"DoSchedulel thread end by Exception:\n{e}")

    def globaltrace(self, frame, event, arg):         
        if event == 'call':             
            return self.localtrace         
        else:             
            return None       
    def localtrace(self, frame, event, arg):
        if self.killed:             
            if event == 'line':
                print(f"DoSchedulel thread end")    
                raise StopThread()

        return self.localtrace
    def kill(self):
        self.killed = True
###



