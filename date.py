import time
import os

def display_time(elapsed_time):
    minutes, seconds = divmod(elapsed_time, 60)
    hours, minutes = divmod(minutes, 60)
    time_str = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
    print("Time Elapsed: {}".format(time_str))

def main():
    start_time = time.time()  # Record the current time when the system starts
    elapsed_time = 0

    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")  # Clear the console screen (for Windows and Unix)
            display_time(elapsed_time)
            time.sleep(1)
            elapsed_time = time.time() - start_time

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
