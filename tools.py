from langchain_core.tools import tool
from playsound import playsound
import speech_recognition as SpRe
import cv2
import wave


# 1. 聲音
@tool
def tool_playsound():
    """
	輸入「播放嗽叭」、「播放聲音」、「讓喇叭發聲」等同語義詞
	"""
    return playsound("sound.mp3")


# 2. 語音轉文字
@tool
def tool_stt():
    """
    輸入「STT」、「語音轉文字」等同語義詞
    """
    recoginition = SpRe.Recognizer()
    with SpRe.Microphone() as source:
        print("請說話:")
        audio_Data = recoginition.listen(source) #麥克風    
        print("錄音完，處理中...")
    
    # 存錄音檔
    try:
        audio_name = "recorded_audio.wav"
        with wave.open(audio_name, "wb") as wf:
            wf.setnchannels(1)  # 單聲道
            wf.setsampwidth(2)  # 取樣寬度
            wf.setframerate(16000)  # 取樣率
            wf.writeframes(audio_Data.get_raw_data())
        # print(f"音檔已保存：{audio_name}")
    except:
        print("音檔保存Error")

    #轉文字
    try:
        content = recoginition.recognize_google(audio_Data, language = 'zh-tw') #存聲音於文字
        print(content)
        with open("output.txt", "w") as file:
            file.write(content)    
    except:
        print("轉文字Error")


# 3. 人數
@tool
def tool_persons():
    """
    輸入「現場人數」、「鏡頭中人數」等同意詞
    """
    cap = cv2.VideoCapture(0) # 電腦相機
    # cascade_path = cv2.data.haarcascades + "haarcascade_fullbody.xml" # 下載model路徑 全身
    # cascade_path = cv2.data.haarcascades + "haarcascade_upperbody.xml" # 下載model路徑 半身
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml" # 下載model路徑 人臉
    car = cv2.CascadeClassifier(cascade_path) # model

    ret, frame = cap.read() #bool, frame
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 轉灰階
        gray = cv2.medianBlur(gray, 5)  # 除雜訊 
        per = car.detectMultiScale(gray, scaleFactor = 1.12, minNeighbors = 5) # 偵測人,scaleFactor圖片縮放比例,minNeighbors目標偵測次數
        print(f"人數: {len(per)}")
        # cv2.imshow("Frame", frame) # 測試用:print出相機影像
    else:
        print("Error")

    # 關相機及視窗
    cap.release() 
    # cv2.waitKey(0)                      
    cv2.destroyAllWindows() 
