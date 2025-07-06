import pyautogui
import time

# ========== SETTINGS ==========
message = "I love you ❤️"
count = 10
delay = 2  # Change this to 2, 3, or 5 seconds
# ==============================

print("You have 10 seconds to focus the WhatsApp chat window...")
time.sleep(10)

for i in range(count):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    print(f" Send Message {i + 1}/{count}")
    time.sleep(delay)
