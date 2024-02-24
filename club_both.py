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
    music_files = [file for file in os.listdir(music_folder) if file.endswith(('.mp4', '.wav'))]
    if music_files:
        random_music = random.choice(music_files)
        music_path = os.path.join(music_folder, random_music)
        os.system(f"start {music_path}")
    else:
        print("No music files found in the specified folder.")

# Function to display elapsed time and speak a message
def display_and_speak_time(elapsed_time):
    minutes, seconds = divmod(elapsed_time, 60)
    time_str = "{:02}:{:02}".format(int(minutes), int(seconds))
    speak_message = f"You have traveled since {int(minutes)} minute{'s' if int(minutes) > 1 else ''} ago. Take some rest."
    print("Time Elapsed: {}".format(time_str))
    engine.say(speak_message)
    engine.runAndWait()

# Function to display elapsed time
def display_time(elapsed_time):
    minutes, seconds = divmod(elapsed_time, 60)
    hours, minutes = divmod(minutes, 60)
    time_str = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
    print("Time Elapsed: {}".format(time_str))

def main():
    start_time_music = time.time()  # Record the current time when the system starts for music alerts
    start_time_speech = time.time()  # Record the current time when the system starts for speech alerts
    elapsed_time_music = 0
    elapsed_time_speech = 0

    # Specify the folder containing alert music files
    music_folder = "sounds"

    # Specify the number of seconds for random alerts (changed to 180 seconds for 3 minutes)
    alert_interval_music_seconds = 180  # Change this to the desired number of seconds for music alerts (3 minutes)

    # Specify the number of seconds for speech alerts (changed to 120 seconds for 2 minutes)
    alert_interval_speech_seconds = 120  # Change this to the desired number of seconds for speech alerts (2 minutes)

    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")  # Clear the console screen (for Windows and Unix)
            
            # Music Alerts
            display_time(elapsed_time_music)
            if elapsed_time_music >= alert_interval_music_seconds and elapsed_time_music % alert_interval_music_seconds < 1:
                play_random_music(music_folder)
            elapsed_time_music = time.time() - start_time_music

            # Speech Alerts
            if elapsed_time_speech >= alert_interval_speech_seconds and elapsed_time_speech % alert_interval_speech_seconds < 1:
                display_and_speak_time(elapsed_time_speech)
            elapsed_time_speech = time.time() - start_time_speech

            time.sleep(1)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
