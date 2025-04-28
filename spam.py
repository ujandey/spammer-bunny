import tkinter as tk
from tkinter import ttk
import pyautogui
import pyperclip
import time
import random
from PIL import Image, ImageTk
import os

# Constants
BACKGROUND_COLOR = "#FFC8DD"
BUTTON_COLOR = "#E0BBE4"
BUTTON_HOVER_COLOR = "#D19FE8"
TEXT_COLOR = "#333333"
FONT = ("Helvetica", 12)

# Bunny comments
BUNNY_COMMENTS = [
    "Hopping soon!",
    "Fasten your carrots!",
    "Get ready for some fun!",
    "Bunny is excited!",
]

class WhatsAppSpammerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Spammer")
        self.root.geometry("400x500")
        self.root.configure(bg=BACKGROUND_COLOR)

        # Print the current working directory
        print("Current Working Directory:", os.getcwd())

        self.create_widgets()
        self.update_bunny_comment()

    def create_widgets(self):
        # Load bunny image
        try:
            self.bunny_image = ImageTk.PhotoImage(Image.open(r"C:\Users\ANUSKA\Desktop\python\bunny.png").resize((100, 100)))
            print("Bunny image loaded successfully.")
        except FileNotFoundError:
            print("Error: bunny.png not found in the current directory.")
            self.bunny_image = None

        if self.bunny_image:
            self.bunny_label = tk.Label(self.root, image=self.bunny_image, bg=BACKGROUND_COLOR)
            self.bunny_label.pack(pady=10)

        # Bunny comment label
        self.bunny_comment_label = tk.Label(self.root, text="", font=FONT, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        self.bunny_comment_label.pack(pady=5)

        # Message input
        self.message_label = tk.Label(self.root, text="Message:", font=FONT, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        self.message_label.pack(pady=5)
        self.message_entry = tk.Entry(self.root, font=FONT, relief="flat", borderwidth=5)
        self.message_entry.pack(pady=5, padx=20, ipady=5, ipadx=5)

        # Number input
        self.number_label = tk.Label(self.root, text="Number of Messages:", font=FONT, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        self.number_label.pack(pady=5)
        self.number_entry = tk.Entry(self.root, font=FONT, relief="flat", borderwidth=5)
        self.number_entry.pack(pady=5, padx=20, ipady=5, ipadx=5)

        # Start button
        self.start_button = tk.Button(self.root, text="Start Spamming", font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                                      activebackground=BUTTON_HOVER_COLOR, relief="flat", command=self.start_spamming)
        self.start_button.pack(pady=20, ipadx=10, ipady=5)

        # Status label
        self.status_label = tk.Label(self.root, text="", font=FONT, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        self.status_label.pack(pady=5)

        print("Widgets created successfully.")

    def update_bunny_comment(self):
        comment = random.choice(BUNNY_COMMENTS)
        self.bunny_comment_label.config(text=comment)
        self.root.after(3000, self.update_bunny_comment)

    def start_spamming(self):
        message = self.message_entry.get()
        number = self.number_entry.get()

        if not message or not number.isdigit():
            self.status_label.config(text="Please enter a valid message and number.")
            return

        number = int(number)
        self.status_label.config(text=f"Open WhatsApp in 5 seconds...")
        self.root.update()
        time.sleep(5)

        self.status_label.config(text="Spamming started!")
        self.root.update()

        for i in range(number):
            pyperclip.copy(message)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            time.sleep(0.1)  # Adjust the delay as needed

        self.status_label.config(text="Spamming completed!")

if __name__ == "__main__":
    print("Starting the application...")
    root = tk.Tk()
    app = WhatsAppSpammerApp(root)
    print("Entering the main loop...")
    root.mainloop()
    print("Main loop exited.")
