
auto-fgo  
=========
This is a FGO auto battle project based on win32gui and image recognition.  
to start: 
python fgo_start.py  
  
  
專案使用模擬器BlueStack5 : 
=========  
1.官網載點: https://www.bluestacks.com/download.html  
版本:Nougot 64 位元(支援hyper-v)  
<img src="https://github.com/AslipHsu/picture/blob/main/1.png" width="400">  
  
2.視窗設定  
保持右邊列表為展開狀態  
<img src="https://github.com/AslipHsu/picture/blob/main/2.png" width="400">  
  
3.參考設定  
<img src="https://github.com/AslipHsu/picture/blob/main/2.1.png" width="400">  
<img src="https://github.com/AslipHsu/picture/blob/main/2.2.png" width="400">  
遊戲內設置:  
<img src="https://github.com/AslipHsu/picture/blob/main/2.3.png" width="400">  
ps. 新版本bluestack5 好像有內建廣告 需要自己在設定關掉
  
auto-fgo功能:  
========= 
1.偵測並調整模擬器視窗大小 ,腳本運行時模擬器不要按縮小視窗 會點不到  
保持在 FGO running(768x447)狀態,不是的話 按一下detect按鈕  
<img src="https://github.com/AslipHsu/picture/blob/main/3.png" width="400">  
  
2.關卡設定(step1)  
take picture 截圖關卡,設定是否吃蘋果,按set寫入腳本  
<img src="https://github.com/AslipHsu/picture/blob/main/4.png" width="400">   
ps: 截圖關卡可保持在模擬器畫面最上方 防止誤判按到其他關 ,也不要截圖到AP(AP不夠時會變紅色導致誤判)  

3.支援選擇(step2)  
可選擇無指定(列表第一個) 或自訂截圖要找的從者 ,按set寫入腳本  
<img src="https://github.com/AslipHsu/picture/blob/main/5.png" width="400">   

4.戰鬥流程(step3)  
技能設定  
哪個battle 或是哪個turn發動,按add加入下方編輯區  
<img src="https://github.com/AslipHsu/picture/blob/main/6.png" width="400">  

腳本說明: skill-s12-s1  表示 使用server1的2技能, 並且這是指定技能 對象為從者1  
	    'B1':['skill-s12-s1','skill-s22'] 表示 在battle1時使用 s12,s22 技能  
<img src="https://github.com/AslipHsu/picture/blob/main/6.png" width="400">  

攻擊設定  
卡片可設定從者卡片優先度 發動寶具設定battle 或是哪個turn發動  
<img src="https://github.com/AslipHsu/picture/blob/main/7.png" width="400">  

4.腳本  
按start開始運行腳本 stop可隨時停止腳本 ,loop times可設定腳本次數  
undo返回腳本編輯的上一步  
clear完全清除  
save可儲存當下腳本內容  
load可讀取腳本  
ps.讀取腳本僅讀取text, 關卡和支援須重新重新截圖  
<img src="https://github.com/AslipHsu/picture/blob/main/8.png" width="400">  





      
      
      
      



