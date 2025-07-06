import pyautogui
import pyperclip
import time
from datetime import datetime
import pytz
import subprocess

# Set your message
message = '''
Happy New Year 2082, my love, Kritika! 💖
Budi, as we enter this beautiful new year, I just want to take a moment to thank you for being my everything. Your love, your kindness, and your support mean the world to me.
I love you, Kritika, more than words can describe, and I promise to always be with you, no matter what happens.

Budi, you are my strength, my happiness, and my reason to smile every single day. I want you to know that, no matter what the future holds, I will always stand by your side, loving you endlessly.

Here’s to another year of laughter, memories, and endless love. I love you so much, Kritika, and I’m so grateful to have you in my life.
Happy New Year, budi! ❤️
'''

# Define Nepali time zone
nepal_tz = pytz.timezone('Asia/Kathmandu')

# Set the exact time you want to send the message
send_hour = 0
send_minute = 5

def wait_until_target_time():
    print("Waiting for 12:00 PM Nepali time...")
    while True:
        now = datetime.now(nepal_tz)
        if now.hour == send_hour and now.minute == send_minute:
            print("It's time!")
            break
        time.sleep(10)

def open_chat(name):
    # Press ctrl+f to search
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)

def send_whatsapp_message(name, message):
    # Open chat
    open_chat(name)
    # Paste message
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # Send message
    pyautogui.press('enter')
    print("Message sent!")

# Make sure WhatsApp Desktop is running
subprocess.Popen("start whatsapp:", shell=True)

# Wait until 12:00 PM Nepali Time
wait_until_target_time()

# Send the message
send_whatsapp_message("Kritika", message)
