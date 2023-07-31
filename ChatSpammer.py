import tkinter as Tk
import time
import keyboard
import pyautogui
import threading

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class font:
    header = ("Arial Bold", 15)
    entry = ("Arial", 10)
    standard = ("Arial", 12)

def start():
    root = Tk.Tk()
    root.title("RBLX CHAT SPAMMER")
    root.geometry('350x350')
    root.resizable(False,False)

    textInpText = Tk.Label(font=font.standard, text="Enter Chat Message")
    textInpText.pack()

    textInp = Tk.Entry(font=font.entry)
    textInp.pack()

    delayInpText = Tk.Label(font=font.standard, text="Enter Chat Delay")
    delayInpText.pack()

    DelayInp = Tk.Entry(font=font.entry)
    DelayInp.pack()

    start_keybindText = Tk.Label(font=font.standard, text="To start spamming press 'p'")
    start_keybindText.pack()

    stop_keybindText = Tk.Label(font=font.standard, text="To stop spamming press 'o'")
    stop_keybindText.pack()

    toggleText = Tk.Label(font=font.header, text="Not Running", fg="red")
    toggleText.pack()

    instructions = Tk.Label(font=font.standard, text="MOVE MOUSE TO CHAT BOX")
    instructions.pack()

    class AutoTyper:
        def __init__(self):
            self.running_flag = False

        def start(self):
            if not self.running_flag:
                self.running_flag = True
                toggleText.config(fg="green")
                toggleText.config(text="Running")
                thread = threading.Thread(target=self.run_loop)
                thread.start()

        def stop(self):
            if self.running_flag:
                self.running_flag = False
                toggleText.config(fg="red")
                toggleText.config(text="Not Running")

        def run_loop(self):
            while self.running_flag:
                copy_text = textInp.get()
                delay_time = DelayInp.get()
                time.sleep(int(float(delay_time)))
                pyautogui.click()
                pyautogui.typewrite(copy_text)
                time.sleep(0.1)
                keyboard.press("enter")

                
    auto_typer = AutoTyper()

    def on_key_event(event):
        if event.name == "p":
            auto_typer.start()
        elif event.name == "o":
            auto_typer.stop()

    keyboard.on_press(on_key_event)
    root.mainloop()
start()