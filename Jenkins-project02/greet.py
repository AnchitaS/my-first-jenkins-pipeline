# greet.py — Jenkins will run this file

import datetime

def greet():
    now = datetime.datetime.now()
    print(f"Hello from Jenkins!")
    print(f"This is second commit!")
    print(f"Script ran at: {now}")
    print("Python is working inside Jenkins!")

if __name__ == "__main__":
    greet()
