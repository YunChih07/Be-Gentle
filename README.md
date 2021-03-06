# LSA-Project

## 設備
| 設備 | 圖片 | 數量 | 來源   |
| ---- | ---- | ---- | ---- |
|Raspberry pi3|![](https://i.imgur.com/a4iazyc.png)|1|moli 
|麥克風|![](https://i.imgur.com/DB819Rv.png)|1|張董
|喇叭|![](https://i.imgur.com/3BVsP9W.png)|1|張董
|USB音效卡|![](https://i.imgur.com/wyW66tX.png)|1|PXhome|
|5v繼電器|![](https://i.imgur.com/k8xgynw.png)|1|moli|
|杜邦線|![](https://i.imgur.com/NJ5wOPj.png)|數條|moli|
|氣氛燈(含電池盒)|![](https://i.imgur.com/upxrLvP.png)|1|劉董|

## 安裝步驟
### 硬體設備
 - 先將USB音效卡街上樹莓派，再將喇叭與麥克風接上音效卡

### Python套件
 - 安裝 idle3 編譯器
    - ``` sudo apt install python3 idle3 ```
 
 - 安裝語音辨識套件
    - ``` pip install SpeechRecognition ```

 - 安裝Pyaudio
    - ``` sudo apt install python3-pyaudio```

 - 安裝flac
    - ``` sudo apt install flac```

 - 播放音樂套件pygame
    - ``` sudo pip3 install pygame```

### 連接繼電器與LED
 ![](https://i.imgur.com/JANjEYZ.png)
 - -(GND) 接到6號腳位
 - +(5V) 接到2號腳位
 - s(訊號) 接到40號腳位

 - 再把繼電器的NO跟COM用杜邦線接到(沒有去買電線只能用借來的公對公杜邦縣)LED與電池盒上，燈就會隨著繼電器開關亮了。
 - [手把手教學影片](https://www.youtube.com/watch?v=13T4u4ukdjY&ab_channel=YunChihChen)

## 工作分配
 - 語音辨識 : 陳畇至、劉律霆
 - 繼電器與燈具控制 : 張睿桓、王柏文

## Reference
 - [繼電器教學](https://www.google.com/amp/s/www.instructables.com/5V-Relay-Raspberry-Pi/%3famp_page=true)
 - [語音辨識](https://www.youtube.com/watch?v=R1SFP3t7Gwo&t=312s&ab_channel=Audas)
 - [Pygame套件](https://www.pygame.org/docs/ref/mixer.html)
 - [音樂來源](https://www.youtube.com/watch?v=TtQ9hwYoyWQ&ab_channel=%E5%8F%B0%E5%8D%97%E8%91%A1%E8%90%84%E5%9C%92%E6%95%99%E6%9C%83)

## Demo影片
 - https://www.youtube.com/watch?v=FnkCtDGOXew&t=4s&ab_channel=YunChihChen

## 特別感謝
 - Moli提供樹梅派、杜邦線、繼電器
 - 老師與助教們提供想法與建議
