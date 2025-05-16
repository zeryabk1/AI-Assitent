import struct
from playsound import playsound
import eel
import pyaudio
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os
import time
import webbrowser
import pvporcupine
from hugchat import hugchat


@eel.expose
def playAssistantSound():
    music_dir = "www\\assests\\vendore\\texllate\\audio\\start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower().strip()

    if not query:
        speak("Not found")
        return

    app_map = {
        "whatsapp": 'explorer shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App',
        "instagram": 'start https://www.instagram.com',
        "linkedin": 'start https://www.linkedin.com',
        "youtube": 'start chrome https://www.youtube.com', 
        "canva": 'start https://www.canva.com/' 
    }

    for app_name in app_map:
        if app_name in query:
            speak(f"Opening {app_name}")
            os.system(app_map[app_name])
            return

    speak("Opening " + query)
    os.system('start ' + query)


def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        print("Initializing hotword engine...", flush=True)

        porcupine = pvporcupine.create(keywords=['jarvis', 'alexa'])
        paud = pyaudio.PyAudio()

        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Listening for wake words...", flush=True)

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm_unpacked)

            if keyword_index >= 0:
                print(f"Hotword detected: {['jarvis', 'alexa'][keyword_index]}", flush=True)
                import pyautogui as autogui
                autogui.keyDown('win')
                autogui.press('j')
                time.sleep(0.1)
                autogui.keyUp('win')

    except Exception as e:
        print("Error in hotword():", e, flush=True)

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.stop_stream()
            audio_stream.close()
        if paud is not None:
            paud.terminate()


def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response