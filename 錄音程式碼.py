import speech_recognition as sr

# 錄音
recognizer = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

# 語音辨識    
# pip install SpeechRecognition
# pip install pyaudio
try:
    text=recognizer.recognize_google(audio, language='zh-tw')
    print(text)
except e:
    pass
