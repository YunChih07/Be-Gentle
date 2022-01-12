# Be-Gentle

## 設備
| 設備 | 數量 | 來源   |
| ---- | ---- | ---- |
|Raspberry pi3|1|moli 
|麥克風|1|張董
|喇叭|1|張董
|USB音效卡|1|PXhome|
|5v繼電器|1|moli|
|杜邦線|數條|moli|
|氣氛燈(含電池盒)|1|劉董|

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

### 連接繼電器
 - -(GND) 接到PIN6
 - +(5V) 接到PIN2
 - s(訊號) 接到PIN40

 - 再把繼電器的NO跟COM用杜邦線接到(沒有去買電線只能用借來的公對公杜邦縣)電池盒上，燈就會隨著繼電器開關亮了。

## 工作分配
 - 語音辨識 : 陳畇至、劉律霆
 - 繼電器與燈具控制 : 張睿桓、王柏文

## Reference
 - [繼電器教學](https://www.google.com/amp/s/www.instructables.com/5V-Relay-Raspberry-Pi/%3famp_page=true)
 - [語音辨識](https://www.youtube.com/watch?v=R1SFP3t7Gwo&t=312s&ab_channel=Audas)
 - [Pygame套件](https://www.pygame.org/docs/ref/mixer.html)
