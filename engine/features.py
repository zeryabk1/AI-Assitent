from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os
import time
import webbrowser

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


