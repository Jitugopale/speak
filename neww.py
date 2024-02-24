import time
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to display elapsed time and speak a message
def display_and_speak_time(elapsed_time):
    minutes, seconds = divmod(elapsed_time, 60)
    time_str = "{:02}:{:02}".format(int(minutes), int(seconds))
    speak_message = f"You have traveled since {int(minutes)} minute{'s' if int(minutes) > 1 else ''} ago. Take some rest."
    print("Time Elapsed: {}".format(time_str))
    engine.say(speak_message)
    engine.runAndWait()

def main():
    start_time = time.time()  # Record the current time when the system starts

    # Specify the number of seconds for the interval (changed to 120 seconds for 2 minutes)
    alert_interval_seconds = 120  # Change this to the desired number of seconds (2 minutes)

    try:
        while True:
            elapsed_time = time.time() - start_time

            # Speak elapsed time every 2 minutes
            if elapsed_time >= alert_interval_seconds and elapsed_time % alert_interval_seconds < 1:
                display_and_speak_time(elapsed_time)

            time.sleep(1)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
