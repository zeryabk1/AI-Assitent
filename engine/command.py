import pyttsx3
import speech_recognition as sr
import eel 
import time
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10,6)
    try:
        print('recognizing') 
        eel.DisplayMessage('recognizing....')
        query =  r.recognize_google(audio, language='en-pk')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
    except Exception as e:
        return ""
    return query.lower()



@eel.expose
def allCommand(message=1):
    if message == 1:
        query = takecommand()
        print("Voice query:", query)
        eel.senderText(query)
    else:
        query = message  
        print("Text query:", query)
        eel.senderText(query)


    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        else:
            from engine.features import chatBot
            chatBot(query)
    except Exception as e:
        print("Error:", str(e))
    
    eel.showHood()



