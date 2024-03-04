import pyautogui
import time
import os

# Folder
folder = "frames"

# Create the frames folder if it doesn't exist
frames_dir = os.path.join(os.getcwd(), folder)
os.makedirs(frames_dir, exist_ok=True)

while True:
    # Capture the entire screen
    screenshot = pyautogui.screenshot()

    # Save the screenshot to the frames folder
    path = os.path.join(frames_dir, "frame.png")  # Using PNG to retain quality
    screenshot.save(path)
    print("🖥️ Screenshot saved.")

    # Wait for a bit before capturing the next frame
    time.sleep(2)
