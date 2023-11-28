import os
import pygame
import random
from time import sleep

pygame.mixer.init()

while True:
    SongFolder = os.path.join("sounds")

    SongList = ["Sound_USB-Connected.mp3", "Sound-USB-Disconnected.mp3"]
    SleepTime = list(range(1, 21))

    RandomSleepTime = random.choice(SleepTime)
    RandomSongPlay = random.choice(SongList)

    try:
        pygame.mixer.music.load(os.path.join(SongFolder, RandomSongPlay))
        pygame.mixer.music.play()

        # Wait for the song to finish playing
        while pygame.mixer.music.get_busy():
            sleep(1)

        # Wait for a random amount of time before starting the loop again
        sleep(RandomSleepTime)

    except Exception as e:
        print(f"Error: {e}")
