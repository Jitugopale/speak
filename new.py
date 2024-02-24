import time
import random
import pyttsx3
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to generate a random time interval
def random_time_interval(hours):
    minutes = random.randint(1, hours / 60)
    return minutes * 60  # Convert to seconds

# Function to play a random music file
def play_random_music(music_folder):
    music_files = [file for file in os.listdir(music_folder) if file.endswith(('.mp3', '.wav'))]
    if music_files:
        random_music = random.choice(music_files)
        music_path = os.path.join(music_folder, random_music)
        os.system(f"start {music_path}")
    else:
        print("No music files found in the specified folder.")

# Specify the folder containing alert music files
music_folder = "sounds"

# Specify the number of seconds for random alerts
seconds = 60  # Change this to the desired number of seconds

try:
    while True:
        play_random_music(music_folder)
        time_interval = random_time_interval(seconds)
        time.sleep(time_interval)
except KeyboardInterrupt:
    pass
