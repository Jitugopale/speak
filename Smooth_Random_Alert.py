import time
import random
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Adjust speech rate and volume
engine.setProperty('rate', 150)  # You can experiment with this value (words per minute)
engine.setProperty('volume', 0.5)  # Adjust the volume (0.0 to 1.0)

# Function to generate a random time interval
def random_time_interval(hours):
    minutes = random.randint(1, hours / 60)
    return minutes * 60  # Convert to seconds

# Function to alert and speak a random message
def alert_and_speak_random(messages):
    message = random.choice(messages)
    print("Alert:", message)
    engine.say(message)
    engine.runAndWait()

# List of alert messages
alert_messages = [
    "Time to take a break!",
    "Stay focused and productive!",
    "Stretch your legs and relax.",
    "Hydrate and refresh yourself.",
    "Remember to blink your eyes regularly.",
]

# Specify the number of seconds for random alerts
seconds = 60  # Change this to the desired number of seconds

try:
    while True:
        alert_and_speak_random(alert_messages)
        time_interval = random_time_interval(seconds)
        time.sleep(time_interval)
except KeyboardInterrupt:
    pass
