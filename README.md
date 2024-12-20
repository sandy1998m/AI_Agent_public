# AI Agent
AI Agent應用於播放聲音、語音轉文字及鏡頭人數偵測功能。

# 使用方法
執行python main.py

輸入使用功能包含:<br>
1.播放聲音
2.語音轉文字
3.鏡頭人數偵測
4.輸入"停止"即結束

# AI Agent 應用說明
1.播放聲音 : 電腦播放預設好之音檔<br>
2.語音轉文字 : 連接筆電麥克風，並將文字輸出output.py<br>
3.鏡頭人數偵測 : 連接筆電鏡頭，使用OpenCV的Haar分類便是人臉<br>
4.AI Agent模型 : OpenAI gpt-3.5-turbo (程式中將Key隱藏)<br>

# 文件說明
AI_Agent/<br>
├── main.py            # 主程式<br>
├── tools.py           # 包含三個模組功能設定<br>
├── requirements.txt   # 套件<br>
├── README.md          # 說明文件<br>
├── sound.mp3          # 播放聲音檔案<br>
├── output.txt         # STT輸出文字檔案(執行STT時產生)<br>
└── recorded_audio.wav # STT輸出聲音檔案(執行STT時產生)<br>
