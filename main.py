import time
from datetime import datetime
import pyttsx3


def announce_hour():
    current_time = datetime.now()

    hour = current_time.strftime('%H')
    announcement = f"Agora são {hour} horas"
    print(announcement)

    engine = pyttsx3.init()
    volume = engine.getProperty('volume')
    print(volume)
    engine.say(announcement)
    engine.runAndWait()


if __name__ == "__main__":
    announce_hour()